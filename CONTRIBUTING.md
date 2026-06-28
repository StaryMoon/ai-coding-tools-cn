# 贡献指南

欢迎补充 AI coding 工具、中文使用体验、官方链接、真实截图和避坑。

## 收录标准

优先收录：

- 官方工具或活跃开源项目
- AI 编程、代码补全、coding agent、AI IDE、terminal agent、VS Code agent
- 有官方文档或 GitHub repo
- 对学生、研究生、开发者、开源维护者有明确使用场景
- 中文用户容易理解和验证的信息

暂不收录：

- 纯营销软文
- 返利链接
- 未经授权搬运的付费课程截图
- 无法验证的价格、额度、账号限制
- 只换壳没有明确差异的工具

## 修改方式

1. 修改 `data/tools.json`
2. 运行：

```bash
python3 scripts/generate.py
```

3. 检查：

```bash
python3 -m json.tool data/tools.json >/tmp/ai-coding-tools-cn.json
git diff --check
```

4. 提交 PR。

## 文风

- 中文为主。
- 结论前置。
- 不吹“彻底替代程序员”。
- 不把 star 数当绝对排名。
- 所有价格、额度、模型能力都要留出变化空间。
