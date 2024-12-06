---
data_sources:
- 'File: File Metadata'
id: attack-pattern--191cc6af-1bb2-4344-ab5f-28e496638720
mitre_attack_url: https://attack.mitre.org/techniques/T1195/001
name: Compromise Software Dependencies and Development Tools
platforms:
- Linux
- macOS
- Windows
tactics:
- initial-access
title: initial-access - Compromise Software Dependencies and Development Tools
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1195/001](https://attack.mitre.org/techniques/T1195/001) |

# Compromise Software Dependencies and Development Tools (attack-pattern--191cc6af-1bb2-4344-ab5f-28e496638720)

## Description
Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applications may be targeted as a means to add malicious code to users of the dependency.(Citation: Trendmicro NPM Compromise)  

Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims. 

## Detection
Use verification of distributed binaries through hash checking or other integrity checking mechanisms. Scan downloads for malicious signatures and attempt to test software and updates prior to deployment while taking note of potential suspicious activity. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1195/001)
- [Trendmicro NPM Compromise](https://www.trendmicro.com/vinfo/dk/security/news/cybercrime-and-digital-threats/hacker-infects-node-js-package-to-steal-from-bitcoin-wallets)
