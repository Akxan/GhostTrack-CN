---
layout: default
title: SpyEyes
---

# 🔍 SpyEyes

**OSINT 信息查询工具中文增强版** · One-shot lookup for IP · Phone · Username · WHOIS · MX · Email

> 一站式查询 IP / 电话 / 用户名 (3164 平台) / 域名 WHOIS / MX 记录 / 邮箱有效性 · 8 种本地化报告格式

[**📖 详细教程 / Tutorial**](TUTORIAL.html) · [**📝 更新日志 / Changelog**](CHANGELOG.html) · [**🤝 贡献指南 / Contributing**](CONTRIBUTING.html) · [**🔒 安全策略 / Security**](SECURITY.html)

[**⭐ Star on GitHub**](https://github.com/Akxan/SpyEyes) · [**🐛 Report Bug**](https://github.com/Akxan/SpyEyes/issues) · [**📦 Latest Release**](https://github.com/Akxan/SpyEyes/releases/latest)

---

## ✨ 核心特性 / Key Features

- **🌐 IP 追踪** — IPv4/IPv6 + 180+ 国家中文映射
- **📡 本机 IP 查询**
- **📱 电话号码追踪** — 中文归属地 + 中文运营商
- **👤 用户名扫描** — **3164 个平台**（Maigret + Sherlock + WhatsMyName 合并）
  - 48 中文圈 + 58 西语圈 + 91 成人/约会 + 733 论坛
  - 150 线程并发，~20 秒扫完
  - Maigret-style permute（全排列 × 4 种分隔符 + `--method strict|all`）
  - 递归扫描挖关联账号
- **🔍 WHOIS / 📨 MX / ✉️ 邮箱验证** — IDN 支持
- **📊 8 种报告格式** — `JSON / Markdown / HTML / PDF / TXT / CSV / XMind / Graph (D3.js)`
- **🌍 完整中英双语** UI **+ 报告内容** （v1.2.0+）

## 🔒 安全防护

经 **18 轮独立 fresh-eyes 盲审**收敛到「无真 bug」状态：

- SSRF / ReDoS / Domain 注入 / Username 注入 / Markdown 注入 / HTML XSS / CSV 公式注入防护
- WAF 高精度指纹检测（Cloudflare / AWS WAF / PerimeterX / DataDome / Akamai）
- 隐私选项：`SPYEYES_NO_HISTORY=1` 完全禁用历史
- 306 个 pytest 测试，0 红 / ruff / mypy / bandit 全清

## 🚀 快速开始

```bash
git clone https://github.com/Akxan/SpyEyes.git
cd SpyEyes
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 -m spyeyes --version    # spyeyes 1.2.0
```

立即体验：

```bash
python3 -m spyeyes ip 8.8.8.8                 # IP 追踪
python3 -m spyeyes phone +8613800138000       # 电话解析
python3 -m spyeyes user torvalds              # 3164 平台扫描（150 线程）
python3 -m spyeyes user torvalds --save report.html       # HTML 报告
python3 -m spyeyes user torvalds --save report.graph.html # D3.js 力导向图
python3 -m spyeyes user torvalds --save report.xmind      # XMind 思维导图
python3 -m spyeyes whois example.com          # WHOIS
python3 -m spyeyes mx 中国.cn                 # IDN 域名 MX
python3 -m spyeyes email user@中国.cn         # IDN email
SPYEYES_NO_HISTORY=1 python3 -m spyeyes ...   # 禁用历史（隐私模式）
```

完整文档见 [详细教程](TUTORIAL.html)。

---

**License**: Apache 2.0 · **Author**: [Akxan](https://github.com/Akxan)
