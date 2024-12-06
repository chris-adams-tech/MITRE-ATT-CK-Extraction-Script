---
contributors:
- Itzik Kotler, SafeBreach
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Content'
- 'File: File Access'
- 'Command: Command Execution'
id: attack-pattern--51ea26b1-ff1e-4faa-b1a0-1114cd298c87
mitre_attack_url: https://attack.mitre.org/techniques/T1011
name: Exfiltration Over Other Network Medium
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Exfiltration Over Other Network Medium
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Content, File: File Access, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1011](https://attack.mitre.org/techniques/T1011) |

# Exfiltration Over Other Network Medium (attack-pattern--51ea26b1-ff1e-4faa-b1a0-1114cd298c87)

## Description
Adversaries may attempt to exfiltrate data over a different network medium than the command and control channel. If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel.

Adversaries may choose to do this if they have sufficient access or proximity, and the connection might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

## Detection
Monitor for processes utilizing the network that do not normally have network communication or have never been seen before. Processes that normally require user-driven events to access the network (for example, a web browser opening with a mouse click or key press) but access the network without such may be malicious.

Monitor for and investigate changes to host adapter settings, such as addition and/or replication of communication interfaces.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1011)
