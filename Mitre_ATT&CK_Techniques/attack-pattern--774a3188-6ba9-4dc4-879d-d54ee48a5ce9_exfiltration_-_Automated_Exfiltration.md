---
contributors:
- ExtraHop
data_sources:
- 'Command: Command Execution'
- 'Network Traffic: Network Traffic Flow'
- 'File: File Access'
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Content'
- 'Script: Script Execution'
id: attack-pattern--774a3188-6ba9-4dc4-879d-d54ee48a5ce9
mitre_attack_url: https://attack.mitre.org/techniques/T1020
name: Automated Exfiltration
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- exfiltration
title: exfiltration - Automated Exfiltration
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Command: Command Execution, Network Traffic: Network Traffic Flow, File: File Access, Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Content, Script: Script Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1020](https://attack.mitre.org/techniques/T1020) |

# Automated Exfiltration (attack-pattern--774a3188-6ba9-4dc4-879d-d54ee48a5ce9)

## Description
Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after being gathered during Collection.(Citation: ESET Gamaredon June 2020) 

When automated exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041) and [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048).

## Detection
Monitor process file access patterns and network behavior. Unrecognized processes or scripts that appear to be traversing file systems and sending network traffic may be suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1020)
- [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
