---
contributors:
- Menachem Goldstein
data_sources:
- 'Process: Process Creation'
- 'Sensor Health: Host Status'
id: attack-pattern--bef8aaee-961d-4359-a308-4c2182bcedff
mitre_attack_url: https://attack.mitre.org/techniques/T1562/011
name: Spoof Security Alerting
platforms:
- Windows
- macOS
- Linux
tactics:
- defense-evasion
title: defense-evasion - Spoof Security Alerting
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Process: Process Creation, Sensor Health: Host Status |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/011](https://attack.mitre.org/techniques/T1562/011) |

# Spoof Security Alerting (attack-pattern--bef8aaee-961d-4359-a308-4c2182bcedff)

## Description
Adversaries may spoof security alerting from tools, presenting false evidence to impair defenders’ awareness of malicious activity.(Citation: BlackBasta) Messages produced by defensive tools contain information about potential security events as well as the functioning status of security software and the system. Security reporting messages are important for monitoring the normal operation of a system and identifying important events that can signal a security incident.

Rather than or in addition to [Indicator Blocking](https://attack.mitre.org/techniques/T1562/006), an adversary can spoof positive affirmations that security tools are continuing to function even after legitimate security tools have been disabled (e.g., [Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001)). An adversary can also present a “healthy” system status even after infection. This can be abused to enable further malicious activity by delaying defender responses.

For example, adversaries may show a fake Windows Security GUI and tray icon with a “healthy” system status after Windows Defender and other system tools have been disabled.(Citation: BlackBasta)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/011)
- [BlackBasta](https://www.sentinelone.com/labs/black-basta-ransomware-attacks-deploy-custom-edr-evasion-tools-tied-to-fin7-threat-actor/)
