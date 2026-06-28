#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "tools.json"
README = ROOT / "README.md"
DOCS = ROOT / "docs" / "tools"


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    tools = sorted(payload["tools"], key=lambda item: item["priority"])
    DOCS.mkdir(parents=True, exist_ok=True)
    README.write_text(render_readme(payload["meta"], tools), encoding="utf-8")
    for tool in tools:
        (DOCS / f"{tool['slug']}.md").write_text(render_tool(tool), encoding="utf-8")
    print(f"Generated README and {len(tools)} tool pages.")


def render_readme(meta: Dict[str, Any], tools: List[Dict[str, Any]]) -> str:
    lines = [
        '<h1 align="center">AI 编程工具中文选型指南</h1>',
        "",
        '<p align="center">',
        "  <strong>Codex · Claude Code · Gemini CLI · Cursor · Cline · Aider · Continue · Qwen Code · Roo Code · opencode</strong>",
        "</p>",
        "",
        '<p align="center">',
        '  <img src="assets/ai-coding-tools-map.svg" alt="AI 编程工具中文选型图" width="930">',
        "</p>",
        "",
        "> 面向学生、研究生、开发者和科研党：用中文讲清楚 2026 年主流 AI coding 工具怎么选。",
        "",
        f"最后人工核验：**{meta['last_verified']}**",
        "",
        f"> GitHub star 快照：**{meta['star_snapshot_date']}**，仅作热度参考。",
        "",
        "如果这个项目帮你少踩一个 AI coding 工具坑，欢迎 star。后续会继续补充截图、配置模板、真实工作流和中文避坑。",
        "",
        "## 一句话结论",
        "",
        "- 想在终端里让 agent 改 repo：优先看 **OpenAI Codex CLI**、**Claude Code**、**Gemini CLI**、**Aider**。",
        "- 想开箱即用 AI IDE：优先看 **Cursor**、**Windsurf**。",
        "- 想继续用 VS Code：优先看 **Cline**、**Roo Code**、**GitHub Copilot**、**Continue**。",
        "- 想开源可控：优先看 **Continue**、**Aider**、**Cline**、**Gemini CLI**、**Qwen Code**、**opencode**。",
        "- 想跟中文/国产模型生态结合：关注 **Qwen Code**。",
        "",
        "## 快速选型表",
        "",
        "| 工具 | 类型 | 状态 | 开源 | Stars 快照 | 最适合 | 官方入口 |",
        "| --- | --- | --- | --- | ---: | --- | --- |",
    ]
    for tool in tools:
        stars = "-" if tool["github_stars"] is None else f"{tool['github_stars']:,}"
        lines.append(
            "| [{name}](docs/tools/{slug}.md) | `{category}` | {status} | {open_source} | {stars} | {best_for} | [Official]({official_url}) |".format(
                name=tool["name"],
                slug=tool["slug"],
                category=tool["category"],
                status=tool["status"],
                open_source=tool["open_source"],
                stars=stars,
                best_for=escape_cell(tool["best_for"]),
                official_url=tool["official_url"],
            )
        )
    lines.extend(
        [
            "",
            "## 按人群推荐",
            "",
            "### 学生党 / 课程作业",
            "",
            "```text",
            "GitHub Copilot + Cursor / VS Code + Cline",
            "```",
            "",
            "重点是少折腾、能快速完成课程项目，同时不要把 API key 和成本管理搞崩。",
            "",
            "### 研究生 / 科研代码",
            "",
            "```text",
            "Codex CLI / Claude Code / Aider + Git + pytest",
            "```",
            "",
            "重点是让 agent 读懂 repo、改实验脚本、跑测试、写 README 和复现实验说明。",
            "",
            "### 开源项目维护者",
            "",
            "```text",
            "Codex CLI + Continue / Cline + CI",
            "```",
            "",
            "重点是 issue triage、PR 小修、文档更新、测试补齐和 release notes。",
            "",
            "### 想自建/可控",
            "",
            "```text",
            "Continue + Aider + Qwen Code / Gemini CLI",
            "```",
            "",
            "重点是模型可换、配置可控、成本透明。",
            "",
            "## 选择 AI coding 工具时最重要的 8 个问题",
            "",
            "1. 你想在 IDE 里用，还是终端里用？",
            "2. 你需要自动改代码，还是只要补全/聊天？",
            "3. 你能接受闭源商业产品吗？",
            "4. 你愿意管理 API key 和 token 成本吗？",
            "5. 你是否需要中文模型或国内模型生态？",
            "6. 你是否需要读整个 repo、跑测试、改多文件？",
            "7. 你能否接受 agent 直接操作本地文件？",
            "8. 团队是否需要统一配置、审计和权限边界？",
            "",
            "## 安全与成本底线",
            "",
            "- 不要把生产密钥、云账号、支付 key 暴露给 agent。",
            "- 大仓库自动修改前先开分支，保留 git diff。",
            "- 开启自动命令执行前，先理解工具的权限模型。",
            "- API key 模式一定要设预算、限额和日志。",
            "- 不要迷信 star 排名，最终要看你的项目类型和工作流。",
            "",
            "## 数据维护",
            "",
            "结构化数据在 [`data/tools.json`](data/tools.json)。",
            "",
            "重新生成：",
            "",
            "```bash",
            "python3 scripts/generate.py",
            "```",
            "",
            "## 贡献方式",
            "",
            "欢迎 PR 补充：",
            "",
            "- 新 AI coding 工具",
            "- 中文使用体验",
            "- 官方文档链接",
            "- 价格/学生计划变化",
            "- 安全和成本避坑",
            "- 真实截图或原创信息图",
            "",
            "请不要提交：",
            "",
            "- 返利链接",
            "- 未经授权搬运的付费教程截图",
            "- 夸大工具能力的营销文案",
            "- 无法验证的价格和额度",
            "",
            "## Disclaimer",
            "",
            "本项目是公开信息整理，不代表任何工具官方。模型、额度、价格、账号限制和产品能力变化很快，请以官方页面为准。",
            "",
            "## License",
            "",
            "MIT.",
            "",
        ]
    )
    return "\n".join(lines)


def render_tool(tool: Dict[str, Any]) -> str:
    choose_if = "\n".join(f"- {item}" for item in tool["choose_if"])
    avoid_if = "\n".join(f"- {item}" for item in tool["avoid_if"])
    strengths = "\n".join(f"- {item}" for item in tool["strengths"])
    watchouts = "\n".join(f"- {item}" for item in tool["watchouts"])
    tags = ", ".join(f"`{tag}`" for tag in tool["tags"])
    stars = "无公开 GitHub star 快照" if tool["github_stars"] is None else f"{tool['github_stars']:,}"
    github_line = f"- GitHub：{tool['github_url']}\n" if tool["github_url"] else ""
    return f"""# {tool['name']}

> 类型：`{tool['category']}`
> 状态：**{tool['status']}**
> 开源：**{tool['open_source']}**
> Stars 快照：**{stars}**

## 一句话

{tool['one_liner']}

## 最适合

{tool['best_for']}

## 官方入口

- 官网/主页：{tool['official_url']}
{github_line}- 文档：{tool['docs_url']}

## 适合选择它，如果

{choose_if}

## 不太适合，如果

{avoid_if}

## 优点

{strengths}

## 注意点

{watchouts}

## 中文使用建议

先用一个小仓库试：让它读 README、修一个小 bug、补一个测试、跑一次 lint。不要一上来就把毕业论文代码或生产仓库交给自动 agent 大改。

## Tags

{tags}
"""


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|")


if __name__ == "__main__":
    main()
