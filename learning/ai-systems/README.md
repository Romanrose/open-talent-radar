# AI 系统与开源贡献学习路线

> 目标：用一条“复习—实现—复盘—贡献”的路线，同时准备 AI 沙盒、内存/性能工程、LLM 技术服务、MindSpore 实习任务，以及 Casbin/Casibase 贡献。

这不是一份需要从零学完的课程清单。它假定你已有 Python、C++、深度学习和 LLM/RAG 项目经验，但编码手感、工程细节和系统基础需要重新建立。每一周都应留下可运行代码、测试、文档或 PR，而不是只看教程。

## 1. 技术定位与取舍

建议将个人技术主线定义为：

> **AI Systems / LLM Infrastructure Engineer**：以 Python 为主、Go 为第二语言，结合 Linux 系统、服务工程、模型评测和权限/隔离能力，构建安全、可观测、可复现的大模型服务。

### 语言策略

| 技术 | 学习深度 | 原因 |
|---|---:|---|
| Python | 主力 | 已有基础；用于模型、数据、评测、自动化和 MindSpore。 |
| Go | 第二主力 | 适合并发服务、Casbin/Casibase、工具与基础设施。 |
| C++ | 复习与阅读 | 重点恢复内存、并发、性能分析能力；不额外开启大型 C++ 项目。 |
| TypeScript / React | 能读能改 | 用于 Casibase 前端联调；不作为近期主攻方向。 |

### 一套能力如何覆盖不同目标

| 目标 | 关键能力 | 在本路线的对应模块 |
|---|---|---|
| AI 沙盒 | 容器、进程隔离、资源限制、日志审计 | 第 3 周 |
| Memory 管理 | 并发、缓存、内存模型、profiling、压测 | 第 4 周 |
| 大模型技术服务 | API、流式推理、队列、评测、可观测性 | 第 5–6 周 |
| MindSpore | Python、模型推理、评测、复现、PR 协作 | 第 7 周 |
| Casbin / Casibase | Go、鉴权、LLM 服务、Docker、数据库 | 第 8 周 |

## 2. 每周学习节奏

建议每周投入 10–15 小时，采用 4 天循环；时间不足时，优先保留“实现”和“复盘”。

1. **复习（30–45 分钟）**：只复习本周任务会用到的旧知识，例如 Python 并发、C++ RAII、Git rebase。
2. **实现（90–120 分钟）**：完成一个可运行的小模块，不追求全功能产品。
3. **验证（30–45 分钟）**：补单元测试、压测、日志或最小复现实验。
4. **沉淀（15–30 分钟）**：更新 README，写下“问题、原因、解决方式、下一步”。

每周最后安排一次 60 分钟复盘：删掉没有转化为代码或贡献的学习项，并将下一周任务拆成 3–5 个 GitHub Issue。

## 3. 八周路线

### 第 0 周（1–2 天）：恢复工作环境和工程习惯

**复习**：Git 分支、commit、PR、虚拟环境、Docker 基本命令、Linux 文件与进程命令。

**实现**：创建一个 `ai-systems-lab` 仓库；使用 Python + Go 放置两个最小服务，并配置 Docker Compose、`.env.example`、`Makefile` 和 GitHub Actions 测试。

**验收**：新机器按 README 能在 10 分钟内启动；每次 push 自动跑测试。

### 第 1 周：Python 工程复习

**复习**：类型标注、包管理、异常处理、`pytest`、`asyncio`、HTTP 客户端、配置管理。

**实现**：用 FastAPI 写一个带健康检查、配置读取、结构化日志和单测的 API 服务。

**验收**：至少覆盖成功、参数错误和上游超时三类测试；README 说明如何运行与测试。

### 第 2 周：Go 与服务并发

**复习**：module、interface、error、context、goroutine、channel、table-driven test。

**实现**：用 Go 写一个并发任务 API：支持提交任务、查询状态、超时取消；Python 服务作为调用方或测试客户端。

**验收**：解释并实现 `context` 取消、并发上限与 race 检查；不要只写“Hello World”。

### 第 3 周：Linux、容器与沙盒基础

**复习**：进程/线程、信号、文件描述符、namespace、cgroup、capability、seccomp 的用途与边界。

**实现**：做一个**仅本地使用**的容器任务执行器：执行预设命令，限制运行时间、CPU、内存和进程数，并保存 stdout/stderr 与退出码。

**验收**：能展示一次正常执行、一次超时、一次内存/资源限制失败。不要将其暴露为可供公网执行任意命令的服务。

### 第 4 周：Memory、缓存与性能分析

**复习**：栈/堆、GC、RAII、数据竞争、缓存局部性、连接池、LRU/TTL。

**实现**：为第 2 周服务加入带 TTL 的缓存和并发保护；用 Go `pprof` 或 Python profiling 找到一个真实瓶颈并记录优化前后对比。

**验收**：提交一份简短性能报告：压测条件、吞吐、P95 延迟、内存占用和结论。

### 第 5 周：LLM 技术服务

**复习**：OpenAI 兼容接口、流式响应、token/上下文、重试、限流、Embedding、RAG 基础。

**实现**：为服务增加模型适配层：可连接本地/远端 OpenAI-compatible API，并提供流式聊天、请求超时和会话记录。

**验收**：同一接口可切换模拟模型与真实模型；错误不会泄露密钥；请求都有唯一 Trace ID。

### 第 6 周：评测与可观测性

**复习**：日志、指标、Trace、Prometheus、OpenTelemetry；正确性、延迟、吞吐、成本、失败率的评测维度。

**实现**：增加最小评测集和指标：记录请求延迟、成功率、模型输出摘要；为一个 RAG/问答任务输出可复现评测报告。

**验收**：README 中有一次完整评测命令和结果解释；能定位一次模拟故障的原因。

### 第 7 周：MindSpore 定向准备与贡献

**复习**：MindSpore/MindFormers 的基本推理流程、模型配置、测试与 PR 规范。

**实现**：完成官方测试任务或一个可复现的示例修复；优先选择推理服务、模型评测、文档复现或测试稳定性任务。

**验收**：形成一个小而完整的 PR：问题描述、复现方式、测试依据、改动范围。申请与认领以官方页面的实时任务状态为准。

### 第 8 周：Casbin / Casibase 定向准备与贡献

**复习**：RBAC、ABAC、OAuth/OIDC、JWT、租户隔离；Go HTTP、React API 联调、PostgreSQL/Redis 基础。

**实现**：优先在 Casibase 找模型接入、文档处理、评测、测试或文档类小 Issue；若需要快速产出首个贡献，可改选 PyCasbin 的 Python 测试、集成或文档任务。

**验收**：先提交一个范围明确的 Issue 讨论或 PR；不要在未与导师确认前承诺大规模功能重构。

## 4. 贯穿式作品：AI Systems Lab

不要同时做五个分散项目。用一个可持续演进的作品串联路线：

```text
Client
  → API gateway (Go / FastAPI)
  → Authentication + rate limit + Trace ID
  → LLM adapter (OpenAI-compatible)
  → Redis cache / PostgreSQL audit
  → Evaluation runner + metrics

Local task runner (Docker)
  → time / CPU / memory / process limits
  → execution logs and result records
```

它可以针对不同方向重新表述，而无需重写项目：

- **AI 沙盒**：隔离、资源限制、执行审计。
- **Memory 管理**：缓存、并发、性能压测与 profiling。
- **大模型技术服务**：模型网关、流式响应、评测与可观测性。
- **MindSpore**：推理复现、评测脚本、服务性能基准。
- **Casbin/Casibase**：鉴权、多租户、审计与模型/知识库集成。

## 5. 申请并行策略

- 已提交的项目：每周花 1–2 小时整理项目材料和技术问答，不因等待结果停下学习。
- MindSpore：第 1 周就开始阅读实时任务并完成测试任务；不必等到第 7 周。
- Casbin：第 2 周开始阅读 Casibase/PyCasbin Issue；先完成一个 easy task 或小 PR，再与导师讨论三个月项目计划。

## 6. 每次贡献前的检查清单

- [ ] Issue 仍开放，范围、导师与认领规则已实时确认。
- [ ] 本地已复现问题或跑通基线。
- [ ] 改动可拆为一个小 PR，而不是大规模重构。
- [ ] 有测试、复现步骤或截图/日志作为验证。
- [ ] README/PR 说明了影响范围、验证方式与后续工作。
- [ ] 未提交密钥、个人数据或不应公开的申请材料。

## 7. 路线完成标准

八周结束时，应具备以下可见成果：

1. 一个可运行、可测试、可部署的 `ai-systems-lab`；
2. 一份包含压测与 profiling 结果的性能报告；
3. 一套可复现的 LLM 服务与评测脚本；
4. 至少一个 MindSpore 或 Casbin 相关的高质量 Issue/PR；
5. 能在 3 分钟内清楚说明沙盒、内存/性能、LLM 服务、评测与权限控制之间的关系。
