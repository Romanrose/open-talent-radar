const jobs = [
  { score: 96, name: "AI Infra 研发实习生", org: "Baidu", city: "深圳", track: "AI Infrastructure", skills: "Go · Python · Linux · K8s · GPU/RDMA", url: "https://talent.baidu.com/jobs/detail/INTERN/520472fa-81c9-462f-b603-b1e7ec4763e7" },
  { score: 95, name: "大模型算法实习生", org: "Baidu", city: "深圳", track: "LLM Engineering", skills: "Python · PyTorch · LLM · 评测 · RL", url: "https://talent.baidu.com/jobs/detail/INTERN/a6067048-13d7-4949-ae47-edef93b80b19" },
  { score: 94, name: "文心前沿算法实习生", org: "Baidu", city: "深圳 / 上海 / 北京", track: "Multimodal Learning", skills: "PyTorch · 多模态 · C++ · 模型评测", url: "https://talent.baidu.com/jobs/detail/INTERN/ca1e873a-f3e5-4227-befd-5b408965a610" },
  { score: 92, name: "大模型智能体实习生", org: "Baidu", city: "上海 / 北京", track: "Agent Engineering", skills: "Agent · Coding Agent · RAG · 评测", url: "https://talent.baidu.com/jobs/detail/INTERN/320200cd-893d-4076-b39d-1f77f7a79948" },
  { score: 90, name: "大模型后端研发实习生", org: "Baidu", city: "上海", track: "LLM Engineering", skills: "Go · Python · Linux · 分布式系统", url: "https://talent.baidu.com/jobs/detail/INTERN/15f123ac-2755-4324-b5ba-25682d0f9b40" },
  { score: 88, name: "大模型智能体策略实习生", org: "Baidu", city: "北京", track: "Agent Engineering", skills: "Python · LLM · 多模态 · RL · 评测", url: "https://talent.baidu.com/jobs/detail/INTERN/a1db2391-2c99-4fc5-bbeb-f2c048f45998" },
  { score: 92, name: "AI 应用算法工程师（实习）", org: "Alibaba", city: "广州 / 上海 / 北京", track: "Agent & LLM", skills: "Agent · RAG · Memory · SFT/RL · PyTorch", url: "https://campus-talent.alibaba.com/campus/position/199903540003?deptCodes=AT1LW3%2C9SQM5Z" },
  { score: 82, name: "算法工程师（实习）", org: "Xiaomi", city: "北京", track: "Model Algorithm", skills: "Python · 深度学习 · CV/NLP", url: "https://hr.xiaomi.com/campus/view/872" },
  { score: 79, name: "Python 工程师（实习）", org: "Xiaomi", city: "北京", track: "Software Engineering", skills: "Python · Go/Java · Redis · Linux", url: "https://hr.xiaomi.com/campus/view/897" },
  { score: 78, name: "服务端工程师（实习）", org: "Xiaomi", city: "北京", track: "Backend & Infra", skills: "Java/C++ · Linux · Distributed Systems", url: "https://hr.xiaomi.com/campus/view/867" },
  { score: 77, name: "大数据开发工程师（实习）", org: "Xiaomi", city: "北京", track: "Data & ML Systems", skills: "Python · C++ · Hadoop · Data Mining", url: "https://hr.xiaomi.com/campus/view/879" },
  { score: 75, name: "AI 实习生专项", org: "Huawei", city: "深圳 / 上海 / 北京", track: "AI Infrastructure", skills: "AI · 云计算 · Agent · 系统工程", url: "https://career.huawei.com/cn/campus-recruitment" },
  { score: 93, name: "C/C++ 研发工程师（性能优化）", org: "Meitu MT Lab", city: "厦门 / 深圳", track: "AI Infrastructure", skills: "C++ · GPU · CUDA · 性能优化 · Linux", url: "https://mtlab.meitu.com/aboutUs" },
  { score: 91, name: "3D 图形与渲染研发工程师", org: "Meitu MT Lab", city: "厦门 / 深圳", track: "Graphics Engineering", skills: "C++ · OpenGL · GLSL · 渲染 · GPU", url: "https://mtlab.meitu.com/aboutUs" },
  { score: 89, name: "用户画像算法工程师", org: "Meitu", city: "厦门", track: "Model Algorithm", skills: "Python · Machine Learning · 模型评测", url: "https://hr.meitu.com/en" },
  { score: 84, name: "AI 算法实习生", org: "Aifly", city: "厦门", track: "Model Algorithm", skills: "Python · 深度学习 · CV · 模型评测", url: "https://www.aifly.cn/join" },
  { score: 74, name: "嵌入式软件实习生", org: "Aifly", city: "厦门", track: "Software Engineering", skills: "C++ · Embedded · Linux · 算法", url: "https://www.aifly.cn/join" },
];

const officialPipelines = [
  ["Tencent", "深圳 / 广州", "大模型与 Agent · 云原生研发", "https://jobs.tencent.com/"],
  ["Alibaba", "广州 / 上海", "通义模型 · AI 应用与平台工程", "https://campus-talent.alibaba.com/campus/gov"],
  ["Huawei", "深圳 / 上海", "昇腾 / MindSpore · AI Infra", "https://career.huawei.com/cn/campus-recruitment"],
  ["ByteDance", "深圳 / 上海", "Seed 模型 · 推荐 / Agent", "https://seed.bytedance.com/zh/seedearlycareer"],
  ["Xiaomi", "北京 / 深圳", "算法 · 服务端 · 大数据", "https://hr.xiaomi.com/"],
  ["Ant Group", "杭州 / 上海", "大模型应用 · 分布式系统", "https://talent.antgroup.com/"],
  ["Meituan", "北京 / 上海", "AI 平台 · 后端与数据工程", "https://career.meituan.com/"],
  ["JD Technology", "北京 / 上海", "智能体 · 搜索推荐 · 云平台", "https://zhaopin.jd.com/"],
  ["Bilibili", "上海", "推荐算法 · AIGC · 平台研发", "https://jobs.bilibili.com/"],
  ["Kuaishou", "北京 / 深圳", "多模态 · 推荐 · AI 基础设施", "https://zhaopin.kuaishou.cn/"],
  ["Baidu", "深圳 / 上海", "文心 · Agent · AI Infra", "https://talent.baidu.com/jobs/campus"],
  ["DiDi", "北京 / 上海", "自动驾驶 · ML Systems", "https://talent.didiglobal.com/"],
  ["Shopee", "新加坡", "后端 · 机器学习平台", "https://careers.shopee.sg/"],
  ["PingCAP", "北京 / 上海", "数据库 · 云原生 · AI 工程", "https://www.pingcap.com/careers/"],
  ["vivo", "深圳 / 东莞", "算法 · 系统软件 · 智能终端", "https://hr.vivo.com/"],
  ["OPPO", "深圳 / 东莞", "AI 算法 · ColorOS · 平台研发", "https://careers.oppo.com/"],
  ["NetEase", "广州 / 杭州", "AI 应用 · 游戏技术 · 后端工程", "https://campus.163.com/"],
  ["Meitu", "厦门 / 深圳", "多模态 · Agent · 图形与性能工程", "https://hr.meitu.com/en"],
  ["Aifly", "厦门", "AI 算法 · 嵌入式软件 · 飞控系统", "https://www.aifly.cn/join"],
  ["CHIXM", "厦门", "Java / C++ 研发 · Web 前端", "https://www.chixm.com/job/?sort=0&type=1"],
  ["Veewo Games", "厦门", "C++ / C# · Unity 开发", "https://www.veewo.com/careers-intern?lang=zh"],
];

const programs = [
  ["腾讯犀牛鸟开源人才计划", "Tencent Open Source · Agent Memory / CubeSandbox", "开放", "https://opensource.tencent.com/summer-of-code"],
  ["MindSpore 开源实习", "MindSpore · AI 框架与系统", "开放", "https://www.mindspore.cn/internship"],
  ["Casbin Talent 2026", "Casbin Community · 权限与工程贡献", "开放", "https://github.com/apache/casbin-Talent2026"],
  ["OpenAtom 开源大赛", "OpenAtom Foundation · AI 与开源实践", "开放", "https://competition.openatom.tech/"],
  ["ByteDance Seed 实习", "ByteDance Seed · 基础模型与研究工程", "开放", "https://seed.bytedance.com/zh/seedearlycareer"],
  ["开源之夏", "中科院软件所 · 社区导师制课题", "下一期观察", "https://summer-ospp.ac.cn/"],
  ["PaddlePaddle Hackathon", "PaddlePaddle · 深度学习框架", "下一期观察", "https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/10_contribution/hackathon_cn.html"],
  ["openEuler & openGauss", "华为计算社区 · 系统与基础设施", "待核验", "https://edu.hicomputing.huawei.com/openeuler-opengauss-talent"],
  ["OceanBase AI 生态实习", "OceanBase · 数据库与 AI 工程", "待核验", "https://ask.oceanbase.com/t/topic/35645128"],
  ["NebulaGraph 社区实践", "NebulaGraph · 图数据库与图智能", "待核验", "https://www.nebula-graph.com.cn/university"],
  ["Linux Foundation LFX", "Linux Foundation · 云原生与系统", "待核验", "https://lfx.linuxfoundation.org/tools/mentorship/"],
  ["Google Summer of Code", "Google Open Source · 全球社区导师制", "下一期观察", "https://developers.google.com/open-source/gsoc"],
  ["Outreachy Internship", "Outreachy · 远程开源实习", "下一期观察", "https://www.outreachy.org/"],
  ["KDE Season of KDE", "KDE Community · 社区项目", "下一期观察", "https://mentorship.kde.org/sok/"],
  ["PingCAP TiDB Talent Plan", "PingCAP · 分布式数据库", "下一期观察", "https://tidb.net/talent-plan"],
  ["韩国开源贡献学院", "Open UP / NIPA · 国际开源实践", "下一期观察", "https://www.contribution.ac/2026ossca"],
];

const sources = ["16 个求职官方入口", "13 个开源官方入口", "每日 09:00（UTC）巡检", "仅人工核验后入库"];

export default function Home() {
  return <main>
    <header className="topbar"><a className="brand" href="#top">Open Talent Radar <small>Romanrose</small></a><nav><a href="#jobs">岗位</a><a href="#opensource">开源</a><a href="#insight">分析</a></nav><span className="verified">● 已核验 2026.08.25</span></header>
    <section id="top" className="wrap intro"><p className="kicker">PERSONAL CAREER INTELLIGENCE</p><h1>用真实机会，<em>组织学习与行动。</em></h1><p>开发、AI Infra、模型算法、智能体方向的双雷达。岗位池由可直达职位与官方招聘方向组成，避免把搜索结果伪装为职位。</p><div className="stats"><div><b>55+</b><span>可行动岗位池</span></div><div><b>16</b><span>开源机会</span></div><div><b>33</b><span>官方来源</span></div><div><b>5</b><span>优先城市</span></div></div></section>
    <section id="jobs" className="wrap section"><div className="section-title"><div><p className="kicker">01 / JOB RADAR</p><h2>优先投递</h2></div><p>城市排序：深圳 → 广州 → 上海 → 北京 → 厦门；新加坡仅作补充观察。</p></div><div className="job-list">{jobs.map((job) => <article className="job" key={job.url + job.name}><b className="score">{job.score}</b><div><h3>{job.name}</h3><p>{job.org} · {job.city} · {job.track}</p><span>{job.skills}</span></div><a href={job.url} target="_blank" rel="noreferrer" aria-label={`打开 ${job.name} 官方岗位详情`}>官方详情 ↗</a></article>)}</div><p className="hint">以上为 17 个已核验职位；厦门优先展示美图与艾飞方向，其余已核验记录保留在数据报告中。</p><h3 className="pool-title">官方岗位方向池 · 42 条</h3><p className="hint">每家保留两个与你匹配的投递方向，链接均为公司官方招聘入口；进入后按城市与关键词筛选再投递。</p><div className="pipeline-grid">{officialPipelines.map(([company, city, focus, url]) => <a href={url} target="_blank" rel="noreferrer" key={company}><b>{company}</b><span>{city}</span><p>{focus}</p><small>2 个候选方向 · 官方入口 ↗</small></a>)}</div></section>
    <section id="opensource" className="muted"><div className="wrap section"><div className="section-title"><div><p className="kicker">02 / OPEN SOURCE RADAR</p><h2>全部开源机会 · {programs.length}</h2></div><p>覆盖国内优先的社区计划与少量国际观察项；状态区分“可行动”和“等待下一期”。</p></div><div className="programs">{programs.map(([name, detail, state, url]) => <a href={url} target="_blank" rel="noreferrer" key={name}><div className="program-top"><h3>{name}</h3><b className={state === "开放" ? "open" : "watch"}>{state}</b></div><p>{detail}</p><span>查看官方入口 ↗</span></a>)}</div></div></section>
    <section id="insight" className="wrap section"><div className="section-title"><div><p className="kicker">03 / WHAT TO BUILD</p><h2>学习取舍</h2></div><p>岗位频次和个人缺口共同决定，而不是追逐泛化关键词。</p></div><div className="insights"><article><b>01</b><h3>AI Infra</h3><p>Linux、Docker、Kubernetes、分布式系统、GPU 基础；将其落在一个可跑的 Agent 服务中。</p></article><article><b>02</b><h3>Agent 工程</h3><p>工具调用、RAG、记忆管理、评测与回归；与腾讯 Agent Memory issue 形成同一条证据线。</p></article><article><b>03</b><h3>模型算法</h3><p>PyTorch、多模态、模型评估和 RL 基础；用实验记录而非只列论文证明掌握程度。</p></article></div><div className="source-strip">{sources.map((source) => <span key={source}>✓ {source}</span>)}</div></section>
    <footer className="wrap">OPEN TALENT RADAR <span>daily monitored · human reviewed</span></footer>
  </main>;
}
