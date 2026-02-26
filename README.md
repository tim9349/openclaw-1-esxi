# OpenClaw 1 (Ubuntu ESXi) - AI Trading Assistant Backup

這個 Repository 是 **OpenClaw (小股)** 在 Ubuntu ESXi 環境下的完整工作區備份。

## 📌 專案架構
- **Host**: Ubuntu 24.04 (on VMware ESXi)
- **Agent**: OpenClaw (Gemini-3-Pro-Preview)
- **Role**: AI 交易助手 (期貨/股票)

## 📂 檔案結構說明

| 檔案/目錄 | 用途說明 |
| :--- | :--- |
| **MEMORY.md** | 🧠 長期記憶核心 (API Key 期限、交易策略、重要設定) |
| **memory/** | 📅 每日對話與工作日誌歸檔 |
| **AGENTS.md** | 🤖 Agent 行為準則與角色設定 |
| **IDENTITY.md** | 🆔 Agent 身分設定 (小股) |
| **USER.md** | 👤 使用者偏好設定 (DM) |
| **TOOLS.md** | 🛠️ 工具設定與環境參數 |
| **test_taifex.py** | 🐍 台指期夜盤爬蟲測試腳本 |
| **output/** | 📊 爬蟲產出的報表與數據 (Markdown/CSV) |

## 🚀 常用指令

### 更新備份到 GitHub
```bash
cd ~/.openclaw/workspace
git add .
git commit -m "Update workspace backup"
git push origin main
```

### 從 GitHub 還原
```bash
git clone git@github.com:tim9349/openclaw-1-esxi.git ~/.openclaw/workspace
```
