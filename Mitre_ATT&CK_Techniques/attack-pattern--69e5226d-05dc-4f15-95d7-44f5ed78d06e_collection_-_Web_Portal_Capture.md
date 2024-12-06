---
data_sources:
- 'File: File Modification'
id: attack-pattern--69e5226d-05dc-4f15-95d7-44f5ed78d06e
mitre_attack_url: https://attack.mitre.org/techniques/T1056/003
name: Web Portal Capture
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
- credential-access
title: collection - Web Portal Capture
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection, credential-access |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Modification |
| **System Requirements** | An externally facing login portal is configured. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1056/003](https://attack.mitre.org/techniques/T1056/003) |

# Web Portal Capture (attack-pattern--69e5226d-05dc-4f15-95d7-44f5ed78d06e)

## Description
Adversaries may install code on externally facing portals, such as a VPN login page, to capture and transmit credentials of users who attempt to log into the service. For example, a compromised login page may log provided user credentials before logging the user in to the service.

This variation on input capture may be conducted post-compromise using legitimate administrative access as a backup measure to maintain network access through [External Remote Services](https://attack.mitre.org/techniques/T1133) and [Valid Accounts](https://attack.mitre.org/techniques/T1078) or as part of the initial compromise by exploitation of the externally facing web service.(Citation: Volexity Virtual Private Keylogging)

## Detection
File monitoring may be used to detect changes to files in the Web directory for organization login pages that do not match with authorized updates to the Web server's content.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1056/003)
- [Volexity Virtual Private Keylogging](https://www.volexity.com/blog/2015/10/07/virtual-private-keylogging-cisco-web-vpns-leveraged-for-access-and-persistence/)
