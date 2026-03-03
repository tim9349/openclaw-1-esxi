# OpenClaw 雙機連線與 Tailscale 部署記錄 (2026/03/03)

## 1. 架構概述
- **OC1 (主力機)**: N100 (192.168.1.5)
- **OC2 (備援機)**: VMware ESXi (192.168.1.6)
- **連線方式**: Tailscale Mesh VPN (Zero Trust Network)
- **目標**: 建立安全的內部通訊網路 (100.x.x.x)，不受實體網路 (NAT/Firewall) 限制。

## 2. Tailscale 部署 (已完成)
### 安裝指令 (兩台皆同)
```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

### 啟動與命名
- **OC1**: `sudo tailscale up --hostname=oc1`
- **OC2**: `sudo tailscale up --hostname=oc2`

### 狀態
- **Tailnet**: `tim9349@gmail.com`
- **OC1 IP**: `100.127.163.59` (MagicDNS: `oc1.tail414e06.ts.net`)
- **OC2 IP**: `100.118.61.124` (MagicDNS: `oc2.tail414e06.ts.net`)
- **互通性**: 已驗證 `ping oc2` (延遲 <1ms，直連模式)。

## 3. OpenClaw Nodes 配對 (卡關記錄)
- **嘗試 1 (Direct Connect)**: `openclaw nodes connect 192.168.1.6` -> 指令不存在 (v2026.3.1)。
- **嘗試 2 (Pairing Code)**: `openclaw nodes invite` -> 指令不存在。
- **嘗試 3 (Gateway Mode Switch)**: `openclaw config set gateway.mode "node"` -> 驗證失敗 (`Invalid input`)。
- **嘗試 4 (Tailscale Serve)**:
  - OC1 成功啟動 Serve (`https://oc1.tail414e06.ts.net`)。
  - OC2 無法切換為 Node 模式去連接。

### 結論
- OpenClaw 2026.3.1 的 Linux CLI 似乎移除了「被控端 (Node)」模式，目前僅支援「主控端 (Gateway)」模式。
- **解決方案**: 放棄官方 Nodes 功能，改用 **Tailscale 內網 (SSH/HTTP API)** 進行互通。

## 4. 下一步計畫
- **新加坡 VPS (OC3)**: 同樣安裝 Tailscale (`--hostname=oc3`) 加入內網。
- **微信接入**: 利用 OC3 的新加坡線路，透過企業微信 API (或自建 Wechaty) 實現微信群對話。
