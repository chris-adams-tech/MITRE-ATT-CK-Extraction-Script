---
data_sources:
- 'File: File Access'
- 'Command: Command Execution'
id: attack-pattern--1e9eb839-294b-48cc-b0d3-c45555a2a004
mitre_attack_url: https://attack.mitre.org/techniques/T1114/001
name: Local Email Collection
platforms:
- Windows
tactics:
- collection
title: collection - Local Email Collection
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Windows |
| **Data Sources** | File: File Access, Command: Command Execution |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1114/001](https://attack.mitre.org/techniques/T1114/001) |

# Local Email Collection (attack-pattern--1e9eb839-294b-48cc-b0d3-c45555a2a004)

## Description
Adversaries may target user email on local systems to collect sensitive information. Files containing email data can be acquired from a user’s local system, such as Outlook storage or cache files.

Outlook stores data locally in offline data files with an extension of .ost. Outlook 2010 and later supports .ost file sizes up to 50GB, while earlier versions of Outlook support up to 20GB.(Citation: Outlook File Sizes) IMAP accounts in Outlook 2013 (and earlier) and POP accounts use Outlook Data Files (.pst) as opposed to .ost, whereas IMAP accounts in Outlook 2016 (and later) use .ost files. Both types of Outlook data files are typically stored in `C:\Users\<username>\Documents\Outlook Files` or `C:\Users\<username>\AppData\Local\Microsoft\Outlook`.(Citation: Microsoft Outlook Files)

## Detection
Monitor processes and command-line arguments for actions that could be taken to gather local email files. Monitor for unusual processes accessing local email files. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1114/001)
- [Outlook File Sizes](https://practical365.com/clients/office-365-proplus/outlook-cached-mode-ost-file-sizes/)
- [Microsoft Outlook Files](https://support.office.com/en-us/article/introduction-to-outlook-data-files-pst-and-ost-222eaf92-a995-45d9-bde2-f331f60e2790)
