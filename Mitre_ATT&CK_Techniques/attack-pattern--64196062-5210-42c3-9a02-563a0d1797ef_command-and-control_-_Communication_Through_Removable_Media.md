---
data_sources:
- 'Drive: Drive Creation'
- 'Drive: Drive Access'
id: attack-pattern--64196062-5210-42c3-9a02-563a0d1797ef
mitre_attack_url: https://attack.mitre.org/techniques/T1092
name: Communication Through Removable Media
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Communication Through Removable Media
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Drive: Drive Creation, Drive: Drive Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1092](https://attack.mitre.org/techniques/T1092) |

# Communication Through Removable Media (attack-pattern--64196062-5210-42c3-9a02-563a0d1797ef)

## Description
Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system.(Citation: ESET Sednit USBStealer 2014) Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091). Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

## Detection
Monitor file access on removable media. Detect processes that execute when removable media is mounted.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1092)
- [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
