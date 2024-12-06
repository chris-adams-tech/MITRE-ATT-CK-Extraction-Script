---
data_sources:
- 'Windows Registry: Windows Registry Key Modification'
- 'File: File Modification'
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Creation'
- 'Process: Process Creation'
- 'File: File Creation'
id: attack-pattern--34f1d81d-fe88-4f97-bd3b-a3164536255d
mitre_attack_url: https://attack.mitre.org/techniques/T1137/006
name: Add-ins
platforms:
- Windows
- Office Suite
tactics:
- persistence
title: persistence - Add-ins
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | Windows Registry: Windows Registry Key Modification, File: File Modification, Command: Command Execution, Windows Registry: Windows Registry Key Creation, Process: Process Creation, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1137/006](https://attack.mitre.org/techniques/T1137/006) |

# Add-ins (attack-pattern--34f1d81d-fe88-4f97-bd3b-a3164536255d)

## Description
Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised system. Office add-ins can be used to add functionality to Office programs. (Citation: Microsoft Office Add-ins) There are different types of add-ins that can be used by the various Office products; including Word/Excel add-in Libraries (WLL/XLL), VBA add-ins, Office Component Object Model (COM) add-ins, automation add-ins, VBA Editor (VBE), Visual Studio Tools for Office (VSTO) add-ins, and Outlook add-ins. (Citation: MRWLabs Office Persistence Add-ins)(Citation: FireEye Mail CDS 2018)

Add-ins can be used to obtain persistence because they can be set to execute code when an Office application starts. 

## Detection
Monitor and validate the Office trusted locations on the file system and audit the Registry entries relevant for enabling add-ins.(Citation: GlobalDotName Jun 2019)(Citation: MRWLabs Office Persistence Add-ins)

Collect process execution information including process IDs (PID) and parent process IDs (PPID) and look for abnormal chains of activity resulting from Office processes. Non-standard process execution trees may also indicate suspicious or malicious behavior

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1137/006)
- [FireEye Mail CDS 2018](https://summit.fireeye.com/content/dam/fireeye-www/summit/cds-2018/presentations/cds18-technical-s03-youve-got-mail.pdf)
- [MRWLabs Office Persistence Add-ins](https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)
- [Microsoft Office Add-ins](https://support.office.com/article/Add-or-remove-add-ins-0af570c4-5cf3-4fa9-9b88-403625a0b460)
- [GlobalDotName Jun 2019](https://www.221bluestreet.com/post/office-templates-and-globaldotname-a-stealthy-office-persistence-technique)
