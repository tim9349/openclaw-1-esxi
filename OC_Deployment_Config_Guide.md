# OpenClaw 部署指南與黃金範本 (OC2/OC3 適用)

## 1. 簡介 (Introduction)
本指南旨在將 N100 (OC1) 的成功配置複製到其他節點 (OC2/OC3)，以確保所有 OpenClaw 實例具備相同的功能與安全性。
**注意：** 不同節點必須使用 **不同的 Telegram Bot Token**，否則會造成衝突。

## 2. 部署步驟 (Deployment Steps)

1.  **備份舊設定** (如果有的話)：
    ```bash
    cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak
    ```

2.  **寫入新設定**：
    將下方「黃金範本」的 JSON 內容複製，並貼入 `~/.openclaw/openclaw.json`。
    *(建議使用 nano 或 vim)*

3.  **填入 Bot Token**：
    找到 `"botToken": "REPLACE_WITH_YOUR_BOT_TOKEN"`，將其替換為該節點專屬的 Telegram Bot Token (例如 `123456:ABC...`)。

4.  **重啟服務**：
    ```bash
    openclaw gateway restart
    ```

5.  **驗證**：
    - 檢查是否啟動成功：`openclaw status`
    - 檢查 Tailscale 是否自動啟動 Serve (HTTPS URL)。
    - 私訊該 Bot `/status` 測試回應。

## 3. 黃金範本 (Golden Template: openclaw.json)

### ⚠️ 修改重點 (Customize These Fields)
請務必修改以下欄位，否則設定將無效或造成衝突：
- **`"botToken"`**: 請務必替換為該節點專屬的 Telegram Bot Token！
  - OC1: `@dmnice_bot`
  - OC2: `@nice_oc2_bot`
  - OC3: `@nice_oc3_bot`
- **`"groupPolicy"`**: 設為 `"open"` 代表允許群組所有成員使用。若需限制，請改為 `"allowlist"` 並設定 `groupAllowFrom`。
- **`"allowFrom"`**: 設為 `["*"]` 代表允許任何人私訊。若需限制，請改為 `["您的TelegramID"]`。

```json
{
  "meta": {
    "version": "1.0",
    "description": "OC Standard Config (Based on OC1)"
  },
  "auth": {
    "profiles": {
      "google:default": {
        "provider": "google",
        "mode": "api_key"
      }
    }
  },
  "models": {
    "mode": "merge",
    "providers": {
      "deepseek-official": {
        "baseUrl": "https://api.deepseek.com/v1",
        "apiKey": "sk-2b0806e852f34ed99716b95c2e040fb5",
        "api": "openai-completions",
        "models": [
          {
            "id": "deepseek-chat",
            "name": "deepseek-chat",
            "contextWindow": 128000,
            "maxTokens": 8192
          }
        ]
      },
      "google": {
        "baseUrl": "https://generativelanguage.googleapis.com/v1beta",
        "apiKey": "AIzaSyB_vWiesWzw51IEQS5dGTninkayxwEj5qg",
        "api": "google-generative-ai",
        "models": [
          {
            "id": "gemini-3.1-pro-preview",
            "name": "Gemini 2.0 Flash",
            "contextWindow": 1048576,
            "maxTokens": 8192
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "google/gemini-3-pro-preview",
        "fallbacks": [
          "deepseek-official/deepseek-chat"
        ]
      },
      "contextPruning": {
        "mode": "cache-ttl",
        "ttl": "1h"
      },
      "compaction": {
        "mode": "safeguard"
      },
      "heartbeat": {
        "every": "30m"
      }
    }
  },
  "tools": {
    "web": {
      "search": {
        "apiKey": "BSAeB9C1ie108Qj1YT2YFi8NkS3XQ55"
      }
    }
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "dmPolicy": "open",
      "botToken": "REPLACE_WITH_YOUR_BOT_TOKEN",
      "allowFrom": [
        "*"
      ],
      "groupPolicy": "open",
      "streaming": "partial"
    }
  },
  "gateway": {
    "mode": "local",
    "bind": "loopback",
    "controlUi": {
      "allowedOrigins": [
        "http://localhost:18789",
        "http://127.0.0.1:18789"
      ]
    },
    "tailscale": {
      "mode": "serve"
    }
  }
}
```

## 4. 常見問題 (FAQ)
- **Q: 為什麼 Tailscale Serve 沒啟動？**
  - A: 確保您已經在該機器上執行 `sudo tailscale up` 並登入 Google 帳號。
- **Q: 為什麼私訊沒回？**
  - A: 檢查 `dmPolicy` 是否為 `open`，且 `allowFrom` 是否包含 `*` 或您的 ID。
