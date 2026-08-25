const jobs = [
  { score: 95, name: "Agent开发工程师", code: "J104755", org: "Baidu ACG", track: "Agent Engineering", skills: "AI Agents · Coding Agents · RAG", tone: "violet" },
  { score: 89, name: "大模型算法实习生", code: "J99230", org: "Baidu Foundation Model R&D", track: "LLM Engineering", skills: "LLM · Deep Learning · Multimodal", tone: "blue" },
  { score: 87, name: "Seed Foundation Model Internship", code: "2026", org: "ByteDance Seed", track: "LLM Engineering", skills: "LLM Infra · Model Evaluation · C++", tone: "orange" },
  { score: 84, name: "视频生成大模型算法实习生", code: "J96241", org: "Baidu Applied Model R&D", track: "Multimodal Learning", skills: "Multimodal · PyTorch · C++", tone: "pink" },
];

const gaps = [
  ["Kubernetes / Linux", "LLM Infra 岗位的首要补强项"],
  ["Reinforcement Learning", "Agent 算法与科研实习的加分项"],
  ["Simulation & Optimization", "具身评测与 AI4S 方向的延展项"],
];

export default function Home() {
  return (
    <main>
      <nav className="topbar">
        <a className="brand" href="#top"><span>OR</span> Open Talent Radar</a>
        <div className="navlinks"><a href="#jobs">求职雷达</a><a href="#sources">官方来源</a><a href="#growth">能力路线</a></div>
        <button className="sync">● 已核验 · 08.25</button>
      </nav>
      <section id="top" className="hero wrap">
        <div>
          <p className="eyebrow">JINYUAN LI · PERSONAL CAREER INTELLIGENCE</p>
          <h1>把岗位情报，<br /><em>变成行动优先级。</em></h1>
          <p className="hero-copy">面向 AI Agent、LLM Infra、多模态与软件工程的个人求职雷达。只跟踪官方来源，只保留经核验、值得投入的机会。</p>
          <div className="hero-actions"><a className="primary" href="#jobs">查看高匹配岗位 <b>↓</b></a><a className="quiet" href="#growth">查看补强路线</a></div>
        </div>
        <aside className="hero-stat"><div className="stat-label">CURRENT FOCUS</div><strong>Agent<br />Systems</strong><div className="stat-bottom"><span>08</span><small>verified roles<br />in radar</small></div></aside>
      </section>
      <section className="wrap metrics" aria-label="Radar overview"><div><b>08</b><span>已核验岗位</span></div><div><b>04</b><span>优先投递机会</span></div><div><b>06</b><span>官方来源监测</span></div><div><b>2028</b><span>硕士毕业年份</span></div></section>
      <section id="jobs" className="wrap section">
        <div className="section-heading"><div><p className="eyebrow">01 / JOB RADAR</p><h2>高匹配机会</h2></div><p>按技术栈、研究兴趣、岗位方向与地点偏好进行解释型匹配。</p></div>
        <div className="job-list">{jobs.map((job, index) => <article className="job-card" key={job.code}><div className="rank">0{index + 1}</div><div className={`score ${job.tone}`}>{job.score}<small>/100</small></div><div className="job-main"><div className="job-title"><h3>{job.name}</h3><span>{job.code}</span></div><p>{job.org} <i>·</i> 北京 / 线下实习</p><div className="chips"><span>{job.track}</span><span>{job.skills}</span></div></div><a className="arrow" href="https://talent.baidu.com/jobs/list?recruitType=INTERN" aria-label={`View ${job.name}`}>↗</a></article>)}</div>
      </section>
      <section id="growth" className="growth-section"><div className="wrap growth-grid"><div><p className="eyebrow light">02 / GROWTH ROUTE</p><h2>不是“缺什么学什么”，<br />而是为目标岗位补齐证据。</h2><p className="growth-copy">把学习路径绑定到真实岗位：每一项能力都要最终落在一个项目、一次贡献或一段可讲述的工程经历上。</p><a className="text-link" href="#sources">查看官方来源与核验机制 →</a></div><div className="gap-list">{gaps.map(([name, detail], index) => <div className="gap" key={name}><span>0{index + 1}</span><div><h3>{name}</h3><p>{detail}</p></div><b>→</b></div>)}</div></div></section>
      <section id="sources" className="wrap section sources"><div className="section-heading"><div><p className="eyebrow">03 / TRUST LAYER</p><h2>官方来源监测</h2></div><p>页面变化只会生成待复核提醒；不会自动抓取、杜撰岗位或自动投递。</p></div><div className="source-grid">{["腾讯招聘", "阿里巴巴校招", "百度校园招聘", "字节 Seed", "华为校招", "美团招聘"].map((name) => <div className="source" key={name}><span className="dot" /><div><h3>{name}</h3><p>Official source · checked today</p></div><span>↗</span></div>)}</div></section>
      <footer className="wrap"><span>OPEN TALENT RADAR</span><p>Built for deliberate learning &amp; meaningful work.</p><span>2026</span></footer>
    </main>
  );
}
