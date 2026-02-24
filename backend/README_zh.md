# ULTRON AI — 后端服务

ULTRON AI 的后端服务，基于 **FastAPI** 和 **Python 3.12** 构建，采用领域驱动设计（DDD）架构。

## 架构

```
app/
├── domain/            # 核心业务逻辑
│   ├── models/        # 领域实体和值对象
│   └── services/
│       ├── agents/    # AI 智能体（基础、执行）
│       ├── flows/     # 编排（PlanAct 流程）
│       └── tools/     # 工具实现（浏览器、终端、文件、搜索）
│
├── infrastructure/    # 外部服务集成
│   └── external/
│       ├── llm/       # LLM 客户端（OpenAI 兼容）
│       ├── search/    # 搜索引擎（Bing、Google、百度）
│       └── storage/   # 文件存储适配器
│
├── interfaces/        # API 层
│   ├── api/           # REST 路由
│   └── ws/            # WebSocket 处理
│
├── application/       # 应用服务
└── core/              # 配置和工具
```

## 本地运行

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 测试

```bash
pip install -r tests/requirements.txt
pytest
```

## 环境变量

请参阅根目录 [README_zh.md](../README_zh.md#-配置说明) 中的完整配置选项。
