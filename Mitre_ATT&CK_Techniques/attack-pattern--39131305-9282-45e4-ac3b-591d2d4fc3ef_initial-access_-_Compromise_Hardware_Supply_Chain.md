---
data_sources:
- 'Sensor Health: Host Status'
id: attack-pattern--39131305-9282-45e4-ac3b-591d2d4fc3ef
mitre_attack_url: https://attack.mitre.org/techniques/T1195/003
name: Compromise Hardware Supply Chain
platforms:
- Linux
- macOS
- Windows
tactics:
- initial-access
title: initial-access - Compromise Hardware Supply Chain
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Sensor Health: Host Status |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1195/003](https://attack.mitre.org/techniques/T1195/003) |

# Compromise Hardware Supply Chain (attack-pattern--39131305-9282-45e4-ac3b-591d2d4fc3ef)

## Description
Adversaries may manipulate hardware components in products prior to receipt by a final consumer for the purpose of data or system compromise. By modifying hardware or firmware in the supply chain, adversaries can insert a backdoor into consumer networks that may be difficult to detect and give the adversary a high degree of control over the system. Hardware backdoors may be inserted into various devices, such as servers, workstations, network infrastructure, or peripherals.

## Detection
Perform physical inspection of hardware to look for potential tampering. Perform integrity checking on pre-OS boot mechanisms that can be manipulated for malicious purposes.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1195/003)
