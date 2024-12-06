---
id: attack-pattern--2e0dd10b-676d-4964-acd0-8a404c92b044
mitre_attack_url: https://attack.mitre.org/techniques/T1089
name: Disabling Security Tools
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Disabling Security Tools
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1089](https://attack.mitre.org/techniques/T1089) |

# Disabling Security Tools (attack-pattern--2e0dd10b-676d-4964-acd0-8a404c92b044)

## Description
Adversaries may disable security tools to avoid possible detection of their tools and activities. This can take the form of killing security software or event logging processes, deleting Registry keys so that tools do not start at run time, or other methods to interfere with security scanning or event reporting.

## Detection
Monitor processes and command-line arguments to see if security tools are killed or stop running. Monitor Registry edits for modifications to services and startup programs that correspond to security tools. Lack of log or event file reporting may be suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1089)
- [capec](https://capec.mitre.org/data/definitions/578.html)
