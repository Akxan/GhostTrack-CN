# 🎯 SpyEyes v1.2.2 — Sherlock 完整体（regex 预过滤 + WAF 检测）

整合 Sherlock 项目剩下的核心思路：**`regex_check` 预过滤** + **WAF 拦截识别**，让结果更准、对反爬墙透明。

> 💡 v1.2.2 = v1.2.1 + Sherlock-completeness。强烈建议升级。

## 🆕 两大新功能

### 1. 🎯 `regex_check` 预过滤

88 个主流平台（Twitter/Facebook/YouTube/Instagram/...）从 Sherlock + Maigret 上游提取了用户名规则正则。**当 username 不符合规则时直接跳过 HTTP 请求**：

```bash
# 含空格的用户名 → 18 个平台被跳过（不发请求）
gt user "joe smith" --quick
# [ note ] 8 WAF-blocked · 18 skipped (regex) · 63 network errors
```

### 2. 🛡 WAF / CDN 拦截识别

新增 `_detect_waf()` 检测 Cloudflare / AWS WAF / PerimeterX / DataDome 等反爬墙。**被拦截的平台不再误报「找到」**：

```
 [ - ] ★★★ GitLab               [ WAF blocked ]   ← 之前会误报为 ★★★ 命中
 [ - ] ★★  Pinterest            [ WAF blocked ]
```

### 3. 📊 状态摘要

扫描结果顶部新增 `[ note ]` 行，让你知道结果可信度：

```
共扫描 727 个平台，命中 179 个：
[ note ] 8 WAF-blocked · 2 skipped (regex) · 63 network errors
```

「未找到」也细分显示：
- `未找到` — 普通未找到
- `[ WAF blocked ]` 紫色 — 被反爬墙拦截
- `[ skipped ]` 暗色 — username 不符合该平台规则

## 🧪 验证

- **93 测试**全过（+10 新增 regex/WAF 测试）
- **5 路审计全清**：ruff / mypy / bandit / pytest / agent
- 实测对比：扫 torvalds 检测出 8 WAF 阻挡（之前会被误报为命中或未找到）

## 升级

```bash
git pull && pip install -r requirements.txt
```

## 完整变更

详见 [CHANGELOG - 1.2.2](https://github.com/Akxan/SpyEyes/blob/main/docs/CHANGELOG.md#122--2026-04-29)

---

**至此 Sherlock 的 4 大核心 (data + Session + HEAD/stream + regex/WAF) 全部整合**。

⭐ 觉得好用就给个 Star，谢谢！
