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

const programs = [
  { score: 97, name: "MindSpore 开源实习", org: "华为 MindSpore", state: "持续关注", detail: "导师制 · AI 框架 / 系统方向", tone: "blue" },
  { score: 92, name: "腾讯犀牛鸟开源人才计划", org: "Tencent Open Source", state: "已提交申请", detail: "已选 Agent Memory / CubeSandbox 等方向", tone: "violet" },
  { score: 86, name: "Casbin Talent 2026", org: "Apache Casbin", state: "持续关注", detail: "社区导师 · 权限系统与工程贡献", tone: "orange" },
  { score: 73, name: "开源之夏", org: "Open Source Promotion Plan", state: "等待下一期", detail: "导师制 · 真实社区贡献", tone: "pink" },
];

export default function Home() {
  return (
    <main>
      <nav className="topbar">
        <a className="brand" href="#top"><span>OR</span> Open Talent Radar</a>
        <div className="navlinks"><a href="#jobs">求职雷达</a><a href="#opensource">开源雷达</a><a href="#sources">官方来源</a><a href="#growth">能力路线</a></div>
        <button className="sync">● 已核验 · 08.25</button>
      </nav>
      <section id="top" className="hero wrap">
        <div>
          <p className="eyebrow">JINYUAN LI · PERSONAL CAREER INTELLIGENCE</p>
          <h1>把岗位情报，<br /><em>变成行动优先级。</em></h1>
          <p className="hero-copy">面向 AI Agent、LLM Infra、多模态与软件工程的双雷达：一边追踪岗位，一边持续投入有导师的开源社区。</p>
          <div className="hero-actions"><a className="primary" href="#jobs">查看高匹配岗位 <b>↓</b></a><a className="quiet" href="#growth">查看补强路线</a></div>
        </div>
        <aside className="hero-stat"><div className="stat-label">CURRENT FOCUS</div><strong>Agent<br />Systems</strong><div className="stat-bottom"><span>24</span><small>jobs + OSS programs<br />in radar</small></div></aside>
      </section>
      <section className="wrap metrics" aria-label="Radar overview"><div><b>08</b><span>已核验岗位</span></div><div><b>16</b><span>开源培养计划</span></div><div><b>20</b><span>官方来源监测</span></div><div><b>2028</b><span>硕士毕业年份</span></div></section>
      <section id="jobs" className="wrap section">
        <div className="section-heading"><div><p className="eyebrow">01 / JOB RADAR</p><h2>高匹配机会</h2></div><p>按技术栈、研究兴趣、岗位方向与地点偏好进行解释型匹配。</p></div>
        <div className="job-list">{jobs.map((job, index) => <article className="job-card" key={job.code}><div className="rank">0{index + 1}</div><div className={`score ${job.tone}`}>{job.score}<small>/100</small></div><div className="job-main"><div className="job-title"><h3>{job.name}</h3><span>{job.code}</span></div><p>{job.org} <i>·</i> 北京 / 线下实习</p><div className="chips"><span>{job.track}</span><span>{job.skills}</span></div></div><a className="arrow" href="https://talent.baidu.com/jobs/list?recruitType=INTERN" aria-label={`View ${job.name}`}>↗</a></article>)}</div>
      </section>
      <section id="opensource" className="oss-section"><div className="wrap section"><div className="section-heading"><div><p className="eyebrow">02 / OPEN SOURCE RADAR</p><h2>开源不只是“加分项”</h2></div><p>优先关注有导师、可提交真实贡献，并能与你的 Agent / AI Infra 学习路线形成闭环的计划。</p></div><div className="program-grid">{programs.map((program) => <article className="program-card" key={program.name}><div className={`score ${program.tone}`}>{program.score}<small>/100</small></div><div><p className="program-org">{program.org}</p><h3>{program.name}</h3><p className="program-detail">{program.detail}</p></div><span className="program-state">{program.state}</span></article>)}</div><p className="oss-note">腾讯犀牛鸟当前作为你的主线：项目申请与已认领 issue 会被单独保留为后续贡献证据。</p></div></section>
      <section id="growth" className="growth-section"><div className="wrap growth-grid"><div><p className="eyebrow light">02 / GROWTH ROUTE</p><h2>不是“缺什么学什么”，<br />而是为目标岗位补齐证据。</h2><p className="growth-copy">把学习路径绑定到真实岗位：每一项能力都要最终落在一个项目、一次贡献或一段可讲述的工程经历上。</p><a className="text-link" href="#sources">查看官方来源与核验机制 →</a></div><div className="gap-list">{gaps.map(([name, detail], index) => <div className="gap" key={name}><span>0{index + 1}</span><div><h3>{name}</h3><p>{detail}</p></div><b>→</b></div>)}</div></div></section>
      <section id="sources" className="wrap section sources"><div className="section-heading"><div><p className="eyebrow">03 / TRUST LAYER</p><h2>双雷达来源监测</h2></div><p>11 个求职入口与 9 个开源入口均只保留官方页面；变化只会生成待复核提醒。</p></div><div className="source-grid">{["求职 · 腾讯招聘", "求职 · 百度校园招聘", "求职 · 字节 Seed", "求职 · 华为校招", "求职 · Microsoft", "开源 · 腾讯犀牛鸟", "开源 · MindSpore", "开源 · Casbin Talent", "开源 · GSoC", "开源 · CNCF Mentorship", "开源 · Outreachy", "开源 · LFX Mentorship"].map((name) => <div className="source" key={name}><span className="dot" /><div><h3>{name}</h3><p>Official source · monitored</p></div><span>↗</span></div>)}</div></section>
      <footer className="wrap"><span>OPEN TALENT RADAR</span><p>Built for deliberate learning &amp; meaningful work.</p><span>2026</span></footer>
    </main>
  );
}
