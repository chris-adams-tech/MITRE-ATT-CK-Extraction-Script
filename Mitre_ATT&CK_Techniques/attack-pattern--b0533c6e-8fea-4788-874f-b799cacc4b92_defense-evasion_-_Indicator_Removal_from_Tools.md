---
data_sources:
- 'Application Log: Application Log Content'
id: attack-pattern--b0533c6e-8fea-4788-874f-b799cacc4b92
mitre_attack_url: https://attack.mitre.org/techniques/T1027/005
name: Indicator Removal from Tools
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Indicator Removal from Tools
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/005](https://attack.mitre.org/techniques/T1027/005) |

# Indicator Removal from Tools (attack-pattern--b0533c6e-8fea-4788-874f-b799cacc4b92)

## Description
Adversaries may remove indicators from tools if they believe their malicious tool was detected, quarantined, or otherwise curtailed. They can modify the tool by removing the indicator and using the updated version that is no longer detected by the target's defensive systems or subsequent targets that may use similar systems.

A good example of this is when malware is detected with a file signature and quarantined by anti-virus software. An adversary who can determine that the malware was quarantined because of its file signature may modify the file to explicitly avoid that signature, and then re-use the malware.

## Detection
The first detection of a malicious tool may trigger an anti-virus or other security tool alert. Similar events may also occur at the boundary through network IDS, email scanning appliance, etc. The initial detection should be treated as an indication of a potentially more invasive intrusion. The alerting system should be thoroughly investigated beyond that initial alert for activity that was not detected. Adversaries may continue with an operation, assuming that individual events like an anti-virus detect will not be investigated or that an analyst will not be able to conclusively link that event to other activity occurring on the network.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/005)
