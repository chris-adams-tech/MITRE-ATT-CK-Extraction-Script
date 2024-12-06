---
data_sources:
- 'File: File Metadata'
id: attack-pattern--bd369cd9-abb8-41ce-b5bb-fff23ee86c00
mitre_attack_url: https://attack.mitre.org/techniques/T1195/002
name: Compromise Software Supply Chain
platforms:
- Linux
- macOS
- Windows
tactics:
- initial-access
title: initial-access - Compromise Software Supply Chain
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1195/002](https://attack.mitre.org/techniques/T1195/002) |

# Compromise Software Supply Chain (attack-pattern--bd369cd9-abb8-41ce-b5bb-fff23ee86c00)

## Description
Adversaries may manipulate application software prior to receipt by a final consumer for the purpose of data or system compromise. Supply chain compromise of software can take place in a number of ways, including manipulation of the application source code, manipulation of the update/distribution mechanism for that software, or replacing compiled releases with a modified version.

Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims.(Citation: Avast CCleaner3 2018)(Citation: Command Five SK 2011)  

## Detection
Use verification of distributed binaries through hash checking or other integrity checking mechanisms. Scan downloads for malicious signatures and attempt to test software and updates prior to deployment while taking note of potential suspicious activity. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1195/002)
- [Avast CCleaner3 2018](https://blog.avast.com/new-investigations-in-ccleaner-incident-point-to-a-possible-third-stage-that-had-keylogger-capacities)
- [Command Five SK 2011](https://www.commandfive.com/papers/C5_APT_SKHack.pdf)
