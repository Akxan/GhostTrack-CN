# 🎉 SpyEyes v1.3.0 — 全面 Rebrand（覆盖 v1.2.3）

**项目品牌升级**：`GhostTrack-CN` → `SpyEyes`。功能完全保留，焕然一新的标识。

> 💡 v1.3.0 = v1.2.3 + 完整改名（无功能变化）。所有 v1.2.x 用户**强烈建议升级**以使用新品牌。

## 🎨 改了什么

- **GitHub 仓库**：旧 URL `Akxan/GhostTrack-CN` 自动 301 重定向 → `Akxan/SpyEyes`
- **主脚本**：`GhostTR.py` → `spyeyes.py`
- **配置目录**：`~/.ghosttrack/` → `~/.spyeyes/`
- **ASCII Banner**：

```
███████╗██████╗ ██╗   ██╗███████╗██╗   ██╗███████╗███████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝
███████╗██████╔╝ ╚████╔╝ █████╗   ╚████╔╝ █████╗  ███████╗
╚════██║██╔═══╝   ╚██╔╝  ██╔══╝    ╚██╔╝  ██╔══╝  ╚════██║
███████║██║        ██║   ███████╗   ██║   ███████╗███████║
╚══════╝╚═╝        ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚══════╝
       👁  All-in-One OSINT Toolkit  ·  github.com/Akxan/SpyEyes  👁
```

## 🛡 保留

- HunxByts/GhostTrack 原作者致谢
- 所有 v1.0.x / v1.1.x / v1.2.x git tag
- LICENSE 中 derivative work 声明

## 升级（已经用 v1.2.x 的用户）

```bash
# 1. pull 最新代码（旧 URL 自动重定向）
cd /path/to/GhostTrack    # 你之前的本地路径
git pull

# 2. （可选）改本地目录名
cd ..
rm -rf GhostTrack/.venv   # venv 路径会失效，必须重建
mv GhostTrack SpyEyes
cd SpyEyes
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. 试一下
python3 spyeyes.py
```

## 全新安装

```bash
git clone https://github.com/Akxan/SpyEyes.git
cd SpyEyes
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 spyeyes.py
```

## 完整变更

详见 [CHANGELOG - 1.3.0](https://github.com/Akxan/SpyEyes/blob/main/docs/CHANGELOG.md#130--2026-04-29)

---

⭐ 觉得新名字好就给个 Star 支持下！
