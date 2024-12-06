---
data_sources:
- 'File: File Creation'
- 'Network Traffic: Network Traffic Content'
- 'Application Log: Application Log Content'
- 'File: File Modification'
id: attack-pattern--8c41090b-aa47-4331-986b-8c9a51a91103
mitre_attack_url: https://attack.mitre.org/techniques/T1491/001
name: Internal Defacement
platforms:
- Linux
- macOS
- Windows
tactics:
- impact
title: impact - Internal Defacement
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Creation, Network Traffic: Network Traffic Content, Application Log: Application Log Content, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1491/001](https://attack.mitre.org/techniques/T1491/001) |

# Internal Defacement (attack-pattern--8c41090b-aa47-4331-986b-8c9a51a91103)

## Description
An adversary may deface systems internal to an organization in an attempt to intimidate or mislead users, thus discrediting the integrity of the systems. This may take the form of modifications to internal websites, or directly to user systems with the replacement of the desktop wallpaper.(Citation: Novetta Blockbuster) Disturbing or offensive images may be used as a part of [Internal Defacement](https://attack.mitre.org/techniques/T1491/001) in order to cause user discomfort, or to pressure compliance with accompanying messages. Since internally defacing systems exposes an adversary's presence, it often takes place after other intrusion goals have been accomplished.(Citation: Novetta Blockbuster Destructive Malware)

## Detection
Monitor internal and websites for unplanned content changes. Monitor application logs for abnormal behavior that may indicate attempted or successful exploitation. Use deep packet inspection to look for artifacts of common exploit traffic, such as SQL injection. Web Application Firewalls may detect improper inputs attempting exploitation.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1491/001)
- [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
