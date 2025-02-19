---
id: attack-pattern--00d0b012-8a03-410e-95de-5826bf542de6
mitre_attack_url: https://attack.mitre.org/techniques/T1066
name: Indicator Removal from Tools
platforms:
  - Linux
  - macOS
  - Windows
tactics:
  - defense-evasion
title: T1066 - defense-evasion - Indicator Removal from Tools
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1066](https://attack.mitre.org/techniques/T1066) |

# Indicator Removal from Tools (attack-pattern--00d0b012-8a03-410e-95de-5826bf542de6)

## Description
If a malicious tool is detected and quarantined or otherwise curtailed, an adversary may be able to determine why the malicious tool was detected (the indicator), modify the tool by removing the indicator, and use the updated version that is no longer detected by the target's defensive systems or subsequent targets that may use similar systems.

A good example of this is when malware is detected with a file signature and quarantined by anti-virus software. An adversary who can determine that the malware was quarantined because of its file signature may use [Software Packing](https://attack.mitre.org/techniques/T1045) or otherwise modify the file so it has a different signature, and then re-use the malware.

## Detection
The first detection of a malicious tool may trigger an anti-virus or other security tool alert. Similar events may also occur at the boundary through network IDS, email scanning appliance, etc. The initial detection should be treated as an indication of a potentially more invasive intrusion. The alerting system should be thoroughly investigated beyond that initial alert for activity that was not detected. Adversaries may continue with an operation, assuming that individual events like an anti-virus detect will not be investigated or that an analyst will not be able to conclusively link that event to other activity occurring on the network.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1066)
