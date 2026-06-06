# 🛠️ AI DevOps

AI运维工具，支持监控、告警、故障排查。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🔍 故障分析
- 📖 运维手册生成
- 📊 监控配置生成
- 📈 扩缩容建议
- 🏗️ Terraform模块
- 💰 成本分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_devops import create_tools

tools = create_tools()

# 故障分析
incident = tools.analyze_incident(logs, "服务响应缓慢")

# 运维手册
runbook = tools.generate_runbook("API服务", common_issues)

# 监控配置
monitoring = tools.generate_monitoring_config(["api", "database"])

# 扩缩容建议
scaling = tools.suggest_scaling(metrics, current_config)

# Terraform模块
terraform = tools.generate_terraform_module("ECS", requirements)

# 成本分析
costs = tools.analyze_costs(infrastructure)
```

## 📁 项目结构

```
ai-devops/
├── tools.py       # 运维工具核心
└── README.md
```

## 📄 许可证

MIT License
