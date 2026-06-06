"""
AI DevOps - AI运维工具
支持监控、告警、故障排查
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDevOpsTools:
    """
    AI运维工具
    支持：监控、告警、故障
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def analyze_incident(self, logs: List[str], symptoms: str) -> Dict:
        """分析故障"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        logs_text = "\n".join(logs[:20])

        prompt = f"""请分析以下故障：

症状：{symptoms}
日志：
{logs_text}

请返回JSON格式：
{{
    "root_cause": "根因",
    "severity": "high/medium/low",
    "impact": "影响范围",
    "resolution": ["解决步骤"],
    "prevention": ["预防措施"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"incident": content}

    def generate_runbook(self, service: str, common_issues: List[str]) -> str:
        """生成运维手册"""
        if not self.client:
            return "LLM客户端未配置"

        issues_text = "\n".join(f"- {i}" for i in common_issues)

        prompt = f"""请为{service}生成运维手册：

常见问题：
{issues_text}

要求：
1. 健康检查
2. 故障排查
3. 扩缩容
4. 回滚操作"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_monitoring_config(self, services: List[str], tool: str = "prometheus") -> str:
        """生成监控配置"""
        if not self.client:
            return "LLM客户端未配置"

        services_text = ", ".join(services)

        prompt = f"""请生成{tool}监控配置：

服务：{services_text}

要求：
1. 指标收集
2. 告警规则
3. 仪表板"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def suggest_scaling(self, metrics: Dict, current_config: Dict) -> Dict:
        """建议扩缩容"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = json.dumps(metrics, ensure_ascii=False)
        config_text = json.dumps(current_config, ensure_ascii=False)

        prompt = f"""请根据以下指标建议扩缩容：

指标：{metrics_text}
当前配置：{config_text}

请返回JSON格式：
{{
    "recommendation": "scale-up/scale-down/maintain",
    "reason": "原因",
    "suggested_config": {{}},
    "estimated_cost": "预估成本变化"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"scaling": content}

    def generate_terraform_module(self, resource_type: str, requirements: str) -> str:
        """生成Terraform模块"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{resource_type}的Terraform模块：

需求：{requirements}

要求：
1. 模块化
2. 变量化
3. 输出
4. 最佳实践"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def analyze_costs(self, infrastructure: Dict) -> Dict:
        """分析成本"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        infra_text = json.dumps(infrastructure, ensure_ascii=False)

        prompt = f"""请分析以下基础设施成本：

{infra_text}

请返回JSON格式：
{{
    "total_monthly": "月度总成本",
    "breakdown": {{"resource": "成本"}},
    "optimizations": ["优化建议"],
    "potential_savings": "潜在节省"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"costs": content}


def create_tools(**kwargs) -> AIDevOpsTools:
    """创建运维工具"""
    return AIDevOpsTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI DevOps Tools")
    print()

    # 测试
    incident = tools.analyze_incident(
        ["ERROR: Connection timeout", "WARN: High CPU usage"],
        "服务响应缓慢"
    )
    print(json.dumps(incident, ensure_ascii=False, indent=2))
