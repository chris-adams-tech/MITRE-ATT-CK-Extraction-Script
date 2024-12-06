---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Command: Command Execution'
- 'File: File Access'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--613d08bc-e8f4-4791-80b0-c8b974340dfd
mitre_attack_url: https://attack.mitre.org/techniques/T1011/001
name: Exfiltration Over Bluetooth
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Exfiltration Over Bluetooth
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Command: Command Execution, File: File Access, Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1011/001](https://attack.mitre.org/techniques/T1011/001) |

# Exfiltration Over Bluetooth (attack-pattern--613d08bc-e8f4-4791-80b0-c8b974340dfd)

## Description
Adversaries may attempt to exfiltrate data over Bluetooth rather than the command and control channel. If the command and control network is a wired Internet connection, an adversary may opt to exfiltrate data using a Bluetooth communication channel.

Adversaries may choose to do this if they have sufficient access and proximity. Bluetooth connections might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

## Detection
Monitor for processes utilizing the network that do not normally have network communication or have never been seen before. Processes that normally require user-driven events to access the network (for example, a web browser opening with a mouse click or key press) but access the network without such may be malicious.

Monitor for and investigate changes to host adapter settings, such as addition and/or replication of communication interfaces.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1011/001)
