---
contributors:
- William Cain
data_sources:
- 'Process: Process Creation'
- 'Drive: Drive Creation'
- 'File: File Access'
- 'Command: Command Execution'
id: attack-pattern--a3e1e6c5-9c74-4fc0-a16c-a9d228c17829
mitre_attack_url: https://attack.mitre.org/techniques/T1052/001
name: Exfiltration over USB
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Exfiltration over USB
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Creation, Drive: Drive Creation, File: File Access, Command: Command Execution |
| **System Requirements** | Presence of physical medium or device |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1052/001](https://attack.mitre.org/techniques/T1052/001) |

# Exfiltration over USB (attack-pattern--a3e1e6c5-9c74-4fc0-a16c-a9d228c17829)

## Description
Adversaries may attempt to exfiltrate data over a USB connected physical device. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a USB device introduced by a user. The USB device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

## Detection
Monitor file access on removable media. Detect processes that execute when removable media are mounted.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1052/001)
