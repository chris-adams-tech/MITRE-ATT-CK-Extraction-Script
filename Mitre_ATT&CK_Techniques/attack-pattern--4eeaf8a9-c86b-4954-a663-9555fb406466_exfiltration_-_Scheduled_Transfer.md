---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--4eeaf8a9-c86b-4954-a663-9555fb406466
mitre_attack_url: https://attack.mitre.org/techniques/T1029
name: Scheduled Transfer
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Scheduled Transfer
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1029](https://attack.mitre.org/techniques/T1029) |

# Scheduled Transfer (attack-pattern--4eeaf8a9-c86b-4954-a663-9555fb406466)

## Description
Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.

When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041) or [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048).

## Detection
Monitor process file access patterns and network behavior. Unrecognized processes or scripts that appear to be traversing file systems and sending network traffic may be suspicious. Network connections to the same destination that occur at the same time of day for multiple days are suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1029)
