---
contributors:
- William Cain
data_sources:
- 'File: File Access'
- 'Drive: Drive Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--e6415f09-df0e-48de-9aba-928c902b7549
mitre_attack_url: https://attack.mitre.org/techniques/T1052
name: Exfiltration Over Physical Medium
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Exfiltration Over Physical Medium
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Access, Drive: Drive Creation, Process: Process Creation, Command: Command Execution |
| **System Requirements** | Presence of physical medium or device |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1052](https://attack.mitre.org/techniques/T1052) |

# Exfiltration Over Physical Medium (attack-pattern--e6415f09-df0e-48de-9aba-928c902b7549)

## Description
Adversaries may attempt to exfiltrate data via a physical medium, such as a removable drive. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a physical medium or device introduced by a user. Such media could be an external hard drive, USB drive, cellular phone, MP3 player, or other removable storage and processing device. The physical medium or device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

## Detection
Monitor file access on removable media. Detect processes that execute when removable media are mounted.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1052)
