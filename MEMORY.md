- Google API 金鑰額度 (Free Trial)：剩餘約 NT$9,021 (96%)，將於 **17 天後** (2026-03-13) 到期。
- 提醒設定：
  1. 行程：前一天與當天早上 05:10 提醒 (Telegram 私訊)。
  2. Google API 到期：2026-03-12 (前一天) 與 2026-03-13 (當天) 透過 Telegram 私訊通知。
  3. **股市資訊播報**：
     - 早盤速報 (含夜盤收盤)：**每天早上 05:10** 自動抓取夜盤收盤數據，發送至群組。
     - 晚盤速報 (含台股收盤)：**每天下午 15:00** 自動抓取台股收盤數據，發送至群組。
     - 腳本位置：`/home/dm/Projects/Taifex/legacy/run_nighttime_api_cron.py` (已修復日期邏輯)。
  4. **Telegram 群組設定**：
     - Bot: @dmnice_bot
     - 舊群組 ID: -1005142986695 (可能廢棄)
     - **新群組**: DM_AI_Room (ID: -1003783648951, Role: Admin)
     - 權限：無敵模式 (Group Policy: open)。
  5. **資料抓取偏好**：
     - **股票**：優先使用 **臺灣證券交易所 (TWSE)** 公開即時資訊 API (`mis.twse.com.tw/stock/api/getStockInfo.jsp`)。
     - **期貨**：優先使用 **台灣期貨交易所 (Taifex)** 官網公開資訊。
     - 避免使用 Google 搜尋網頁內容，以求數據即時性與準確度。
     - **溝通模式 (Trading Mode)**：
       - 交易相關指令 (進出、策略、分析)：**詳細說明理由 (Reasoning)**。
         - 1. 為什麼做？ (Why)
         - 2. 依據是什麼？ (Basis)
         - 3. 預期與劇本？ (Scenario)
       - 禁止簡短回覆交易決策，必須完整論述，因為賺錢才是重點，Token 成本相對獲利是小錢。
       - 非交易指令 (如查詢天氣、閒聊) 可簡短。
  6. **關鍵數據監控 (Daily Key Metrics)**：
     - **成交量檢核**：務必確認單位 (股/張/億)，避免數據錯誤 (TWSE API 回傳為「張」或「股」需換算)。
     - **台積電尾盤**：每日收盤 (13:30) **最後一筆撮合張數** (Last Trade Volume) 必須記錄，判斷主力動向。
     - **外資動向**：每日盤後 (15:00 後) 分析 **外資買進/賣出/淨買賣超金額** (Foreign Investor Net Buy/Sell)，判斷資金流向。
  7. **AI 實單部署計畫 (Real Trading Roadmap)**：
     - **目標**：全自動化交易 (Fully Automated)，AI 監控、決策、下單。
     - **階段 (Target: 4 週後/3月底上線)**：
       - **Phase 1 (Week 1-2)**：OpenClaw 策略模擬，Windows 環境架設 (需 User 協助)。
       - **Phase 2 (Week 3)**：Windows 全自動模擬單 (Paper Trading) 測試穩定性。
       - **Phase 3 (Week 4)**：小額實單 (Pilot Run) 微型台指，驗收成果。
     - **待辦事項 (User)**：
       - [ ] **Windows 電腦**：專用機，24hr 不關機/不斷網。
       - [ ] **元大 API 憑證**：申請開通、安裝 CA、API 元件測試。
       - [ ] **NAS 共用資料夾**：設定權限，讓 OpenClaw 讀寫報價 JSON。
       - [ ] **元大 API 交易邏輯整理**：由 User 負責在 Windows 端透過 Claude Code 完成開發，產出 Python 下單腳本。
- **未來計畫 (Windows 遷移)**：
  - 架構：鬆散耦合 (Loose Coupling)。
  - Windows 端：跑 QAPI (元大) + Python 抓資料 → 存 JSON。
  - WSL (OpenClaw) 端：讀取共用 JSON → 發送 Telegram。
