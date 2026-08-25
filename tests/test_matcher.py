import unittest
from datetime import date

from radar.matcher import match, rank
from radar.models import Opportunity, Profile


class MatcherTests(unittest.TestCase):
    def setUp(self):
        self.profile = Profile.from_dict(
            {
                "name": "Ada",
                "education": {"graduation_year": 2028},
                "skills": {"strong": ["Python", "Git"], "familiar": ["RAG"]},
                "interests": ["AI Agents", "Open Source"],
                "preferences": {"mentorship": True, "remote": True},
            }
        )

    def test_mentor_and_skill_match_raise_score(self):
        opportunity = Opportunity.from_dict(
            {
                "slug": "demo",
                "name": "Demo",
                "organization": "Demo Org",
                "kind": "mentorship",
                "url": "https://example.com",
                "status": "open",
                "mentorship": True,
                "remote": True,
                "skills": ["Python", "Git", "RAG"],
                "interests": ["AI Agents"],
            }
        )
        result = match(self.profile, opportunity, today=date(2026, 7, 28))
        self.assertGreaterEqual(result.score, 70)
        self.assertEqual(result.gaps, [])

    def test_expired_deadline_is_penalized(self):
        opportunity = Opportunity.from_dict(
            {
                "slug": "expired",
                "name": "Expired",
                "organization": "Demo Org",
                "kind": "mentorship",
                "url": "https://example.com",
                "status": "open",
                "deadline": "2026-01-01",
                "skills": ["Python"],
            }
        )
        result = match(self.profile, opportunity, today=date(2026, 7, 28))
        self.assertIn("Deadline has passed", result.fit_notes)

    def test_rank_is_descending(self):
        strong = Opportunity.from_dict({"slug": "strong", "name": "Strong", "organization": "O", "kind": "x", "url": "https://x", "status": "open", "mentorship": True, "skills": ["Python", "Git"]})
        weak = Opportunity.from_dict({"slug": "weak", "name": "Weak", "organization": "O", "kind": "x", "url": "https://x", "status": "watch", "skills": ["Rust", "Kubernetes"]})
        results = rank(self.profile, [weak, strong])
        self.assertEqual(results[0].opportunity.slug, "strong")

    def test_ineligible_graduation_year_is_explained(self):
        opportunity = Opportunity.from_dict({"slug": "graduate", "name": "Graduate", "organization": "O", "kind": "x", "url": "https://x", "status": "open", "graduation_years": [2027], "skills": ["Python"]})
        result = match(self.profile, opportunity, today=date(2026, 7, 28))
        self.assertIn("Expected graduation year 2028 is not listed as eligible", result.fit_notes)

    def test_job_preferences_raise_score(self):
        profile = Profile.from_dict({
            "name": "Ada",
            "education": {"graduation_year": 2028},
            "skills": {"strong": ["Python"]},
            "interests": ["AI Agents"],
            "preferences": {"career": {"employment_types": ["internship"], "role_families": ["Agent Engineering"], "locations": ["Beijing"]}},
        })
        job = Opportunity.from_dict({"slug": "job", "name": "Job", "organization": "O", "kind": "internship", "url": "https://x", "status": "open", "track": "job", "employment_type": "internship", "role_family": "Agent Engineering", "location": "Beijing", "skills": ["Python"]})
        result = match(profile, job)
        self.assertIn("Preferred role family: Agent Engineering", result.fit_notes)
        self.assertGreaterEqual(result.score, 60)

    def test_location_order_prefers_first_matching_city(self):
        profile = Profile.from_dict({
            "name": "Ada",
            "skills": {"strong": ["Python"]},
            "preferences": {"career": {"locations": ["Shenzhen", "Shanghai", "Beijing"]}},
        })
        shenzhen = Opportunity.from_dict({"slug": "sz", "name": "SZ", "organization": "O", "kind": "internship", "url": "https://x", "status": "open", "track": "job", "location": "Shenzhen / Beijing", "skills": ["Python"]})
        beijing = Opportunity.from_dict({"slug": "bj", "name": "BJ", "organization": "O", "kind": "internship", "url": "https://x", "status": "open", "track": "job", "location": "Beijing", "skills": ["Python"]})
        self.assertGreater(match(profile, shenzhen).score, match(profile, beijing).score)


if __name__ == "__main__":
    unittest.main()
