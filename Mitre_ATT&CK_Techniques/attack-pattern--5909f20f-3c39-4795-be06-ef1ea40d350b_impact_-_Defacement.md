---
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'File: File Creation'
- 'Application Log: Application Log Content'
- 'File: File Modification'
id: attack-pattern--5909f20f-3c39-4795-be06-ef1ea40d350b
mitre_attack_url: https://attack.mitre.org/techniques/T1491
name: Defacement
platforms:
- Windows
- IaaS
- Linux
- macOS
tactics:
- impact
title: impact - Defacement
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Data Sources** | Network Traffic: Network Traffic Content, File: File Creation, Application Log: Application Log Content, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1491](https://attack.mitre.org/techniques/T1491) |

# Defacement (attack-pattern--5909f20f-3c39-4795-be06-ef1ea40d350b)

## Description
Adversaries may modify visual content available internally or externally to an enterprise network, thus affecting the integrity of the original content. Reasons for [Defacement](https://attack.mitre.org/techniques/T1491) include delivering messaging, intimidation, or claiming (possibly false) credit for an intrusion. Disturbing or offensive images may be used as a part of [Defacement](https://attack.mitre.org/techniques/T1491) in order to cause user discomfort, or to pressure compliance with accompanying messages. 


## Detection
Monitor internal and external websites for unplanned content changes. Monitor application logs for abnormal behavior that may indicate attempted or successful exploitation. Use deep packet inspection to look for artifacts of common exploit traffic, such as SQL injection. Web Application Firewalls may detect improper inputs attempting exploitation.



## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1491)
