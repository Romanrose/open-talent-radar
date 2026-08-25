const jobs = [
  { score: 96, name: "AI Infra 研发实习生", org: "Baidu", city: "深圳", track: "AI Infrastructure", skills: "Go · Python · Linux · K8s · GPU/RDMA", url: "https://talent.baidu.com/jobs/detail/INTERN/520472fa-81c9-462f-b603-b1e7ec4763e7" },
  { score: 95, name: "大模型算法实习生", org: "Baidu", city: "深圳", track: "LLM Engineering", skills: "Python · PyTorch · LLM · 评测 · RL", url: "https://talent.baidu.com/jobs/detail/INTERN/a6067048-13d7-4949-ae47-edef93b80b19" },
  { score: 94, name: "文心前沿算法实习生", org: "Baidu", city: "深圳 / 上海 / 北京", track: "Multimodal Learning", skills: "PyTorch · 多模态 · C++ · 模型评测", url: "https://talent.baidu.com/jobs/detail/INTERN/ca1e873a-f3e5-4227-befd-5b408965a610" },
  { score: 92, name: "大模型智能体实习生", org: "Baidu", city: "上海 / 北京", track: "Agent Engineering", skills: "Agent · Coding Agent · RAG · 评测", url: "https://talent.baidu.com/jobs/detail/INTERN/320200cd-893d-4076-b39d-1f77f7a79948" },
  { score: 90, name: "大模型后端研发实习生", org: "Baidu", city: "上海", track: "LLM Engineering", skills: "Go · Python · Linux · 分布式系统", url: "https://talent.baidu.com/jobs/detail/INTERN/15f123ac-2755-4324-b5ba-25682d0f9b40" },
  { score: 88, name: "大模型智能体策略实习生", org: "Baidu", city: "北京", track: "Agent Engineering", skills: "Python · LLM · 多模态 · RL · 评测", url: "https://talent.baidu.com/jobs/detail/INTERN/a1db2391-2c99-4fc5-bbeb-f2c048f45998" },
];

const programs = [
  ["腾讯犀牛鸟开源人才计划", "主线 · Agent Memory / CubeSandbox", "https://opensource.tencent.com/summer-of-code"],
  ["MindSpore 开源实习", "导师制 · AI 框架与系统", "https://www.mindspore.cn/internship"],
  ["Casbin Talent 2026", "导师制 · 权限与工程贡献", "https://github.com/apache/casbin-Talent2026"],
  ["开源之夏", "真实社区课题与导师", "https://summer-ospp.ac.cn/"],
  ["PaddlePaddle 社区", "深度学习框架与模型算法", "https://www.paddlepaddle.org.cn/"],
  ["openEuler 社区", "系统、云原生与基础设施", "https://www.openeuler.org/zh/"],
];

const sources = ["16 个求职官方入口", "13 个开源官方入口", "每日 09:00（UTC）巡检", "仅人工核验后入库"];

export default function Home() {
  return <main>
    <header className="topbar"><a className="brand" href="#top">Open Talent Radar <small>Romanrose</small></a><nav><a href="#jobs">岗位</a><a href="#opensource">开源</a><a href="#insight">分析</a></nav><span className="verified">● 已核验 2026.08.25</span></header>
    <section id="top" className="wrap intro"><p className="kicker">PERSONAL CAREER INTELLIGENCE</p><h1>用真实机会，<em>组织学习与行动。</em></h1><p>开发、AI Infra、模型算法、智能体方向的双雷达。所有展示岗位均保留官方详情页与技能证据。</p><div className="stats"><div><b>16</b><span>已核验岗位</span></div><div><b>16</b><span>开源机会</span></div><div><b>29</b><span>官方来源</span></div><div><b>5</b><span>优先城市</span></div></div></section>
    <section id="jobs" className="wrap section"><div className="section-title"><div><p className="kicker">01 / JOB RADAR</p><h2>优先投递</h2></div><p>城市排序：深圳 → 广州 → 上海 → 北京 → 厦门；新加坡仅作补充观察。</p></div><div className="job-list">{jobs.map((job) => <article className="job" key={job.url}><b className="score">{job.score}</b><div><h3>{job.name}</h3><p>{job.org} · {job.city} · {job.track}</p><span>{job.skills}</span></div><a href={job.url} target="_blank" rel="noreferrer" aria-label={`打开 ${job.name} 官方岗位详情`}>官方详情 ↗</a></article>)}</div><p className="hint">广州、厦门目前以官方入口持续监测为主；不把未核验或泛搜索链接伪装成可投岗位。</p></section>
    <section id="opensource" className="muted"><div className="wrap section"><div className="section-title"><div><p className="kicker">02 / OPEN SOURCE RADAR</p><h2>开源主线</h2></div><p>优先选择有导师、能形成真实 commit 和可讲述工程证据的计划。</p></div><div className="programs">{programs.map(([name, detail, url]) => <a href={url} target="_blank" rel="noreferrer" key={name}><h3>{name}</h3><p>{detail}</p><span>查看官方入口 ↗</span></a>)}</div></div></section>
    <section id="insight" className="wrap section"><div className="section-title"><div><p className="kicker">03 / WHAT TO BUILD</p><h2>学习取舍</h2></div><p>岗位频次和个人缺口共同决定，而不是追逐泛化关键词。</p></div><div className="insights"><article><b>01</b><h3>AI Infra</h3><p>Linux、Docker、Kubernetes、分布式系统、GPU 基础；将其落在一个可跑的 Agent 服务中。</p></article><article><b>02</b><h3>Agent 工程</h3><p>工具调用、RAG、记忆管理、评测与回归；与腾讯 Agent Memory issue 形成同一条证据线。</p></article><article><b>03</b><h3>模型算法</h3><p>PyTorch、多模态、模型评估和 RL 基础；用实验记录而非只列论文证明掌握程度。</p></article></div><div className="source-strip">{sources.map((source) => <span key={source}>✓ {source}</span>)}</div></section>
    <footer className="wrap">OPEN TALENT RADAR <span>daily monitored · human reviewed</span></footer>
  </main>;
}
