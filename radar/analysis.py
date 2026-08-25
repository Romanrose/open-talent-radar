from __future__ import annotations

from collections import Counter
from datetime import date

from .matcher import rank
from .models import Opportunity, Profile


def _count_by(items: list[Opportunity], field: str) -> Counter[str]:
    return Counter(getattr(item, field) or "Unspecified" for item in items)


def render_analysis(profile: Profile, jobs: list[Opportunity], programs: list[Opportunity]) -> str:
    """Create a small, auditable portfolio-level radar summary."""
    matches = rank(profile, jobs)
    career = profile.preferences.get("career", {})
    locations = career.get("locations", [])
    job_locations = _count_by(jobs, "location")
    roles = _count_by(jobs, "role_family")
    skills = Counter(skill for job in jobs for skill in job.skills)
    status = _count_by(jobs, "status")
    lines = [
        "# Open Talent Radar — 综合分析",
        "",
        f"生成日期：{date.today().isoformat()}。本报告只统计仓库内已人工核验、可追溯至官方页面的记录。",
        "",
        "## 覆盖概览",
        "",
        f"- **求职岗位：{len(jobs)}** 个；其中开放 {status['open']} 个、需复核 {status['verify']} 个、观察 {status['watch']} 个。",
        f"- **开源机会：{len(programs)}** 个；导师制机会 {sum(item.mentorship for item in programs)} 个。",
        f"- **职业目标**：开发、AI Infra、模型算法、智能体；城市优先级为 {' → '.join(locations)}。",
        "",
        "## 城市覆盖与下一步",
        "",
        "| 优先级 | 城市 | 当前已核验岗位 | 行动建议 |",
        "| ---: | --- | ---: | --- |",
    ]
    for index, city in enumerate(locations, start=1):
        count = sum(count for place, count in job_locations.items() if city.lower() in place.lower())
        action = "持续补充直达岗位页" if count else "保持官方入口监测，发现合适岗位后人工入库"
        lines.append(f"| {index} | {city} | {count} | {action} |")

    lines += ["", "## 岗位方向分布", "", "| 方向 | 数量 |", "| --- | ---: |"]
    for role, count in roles.most_common():
        lines.append(f"| {role} | {count} |")

    lines += ["", "## 高频技术栈（用于学习取舍）", "", "| 技术 | 出现次数 |", "| --- | ---: |"]
    for skill, count in skills.most_common(12):
        lines.append(f"| {skill} | {count} |")

    lines += ["", "## 当前优先行动", ""]
    for item in matches[:5]:
        job = item.opportunity
        lines.append(f"- **{item.score}/100 · [{job.name}]({job.url})**：{job.location} · {job.role_family}；补强 {', '.join(item.gaps[:3]) or '无关键缺口'}。")
    lines += [
        "",
        "## 数据治理说明",
        "",
        "- GitHub Actions 每日巡检官方来源并更新变更报告；不会把未验证页面自动写成岗位。",
        "- 每条岗位保留官方直达链接、核验日期、地点、岗位族与技能要求，便于复查与更新。",
    ]
    return "\n".join(lines) + "\n"
