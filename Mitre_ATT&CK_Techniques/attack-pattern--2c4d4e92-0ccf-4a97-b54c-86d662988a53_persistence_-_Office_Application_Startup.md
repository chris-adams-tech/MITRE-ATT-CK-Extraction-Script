---
contributors:
- Nick Carr, Mandiant
- Microsoft Threat Intelligence Center (MSTIC)
- Sahar Shukrun
- Praetorian
- Loic Jaquemet
- Ricardo Dias
data_sources:
- 'File: File Creation'
- 'Application Log: Application Log Content'
- 'Windows Registry: Windows Registry Key Modification'
- 'File: File Modification'
- 'Module: Module Load'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Creation'
- 'Command: Command Execution'
id: attack-pattern--2c4d4e92-0ccf-4a97-b54c-86d662988a53
mitre_attack_url: https://attack.mitre.org/techniques/T1137
name: Office Application Startup
platforms:
- Windows
- Office Suite
tactics:
- persistence
title: persistence - Office Application Startup
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | File: File Creation, Application Log: Application Log Content, Windows Registry: Windows Registry Key Modification, File: File Modification, Module: Module Load, Process: Process Creation, Windows Registry: Windows Registry Key Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1137](https://attack.mitre.org/techniques/T1137) |

# Office Application Startup (attack-pattern--2c4d4e92-0ccf-4a97-b54c-86d662988a53)

## Description
Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the use of Office Template Macros and add-ins.

A variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms, and Home Page.(Citation: SensePost Ruler GitHub) These persistence mechanisms can work within Outlook or be used through Office 365.(Citation: TechNet O365 Outlook Rules)

## Detection
Collect process execution information including process IDs (PID) and parent process IDs (PPID) and look for abnormal chains of activity resulting from Office processes. Non-standard process execution trees may also indicate suspicious or malicious behavior. If winword.exe is the parent process for suspicious processes and activity relating to other adversarial techniques, then it could indicate that the application was used maliciously.

Many Office-related persistence mechanisms require changes to the Registry and for binaries, files, or scripts to be written to disk or existing files modified to include malicious scripts. Collect events related to Registry key creation and modification for keys that could be used for Office-based persistence.(Citation: CrowdStrike Outlook Forms)(Citation: Outlook Today Home Page)

Microsoft has released a PowerShell script to safely gather mail forwarding rules and custom forms in your mail environment as well as steps to interpret the output.(Citation: Microsoft Detect Outlook Forms) SensePost, whose tool [Ruler](https://attack.mitre.org/software/S0358) can be used to carry out malicious rules, forms, and Home Page attacks, has released a tool to detect Ruler usage.(Citation: SensePost NotRuler)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1137)
- [Microsoft Detect Outlook Forms](https://docs.microsoft.com/en-us/office365/securitycompliance/detect-and-remediate-outlook-rules-forms-attack)
- [TechNet O365 Outlook Rules](https://blogs.technet.microsoft.com/office365security/defending-against-rules-and-forms-injection/)
- [CrowdStrike Outlook Forms](https://malware.news/t/using-outlook-forms-for-lateral-movement-and-persistence/13746)
- [SensePost Ruler GitHub](https://github.com/sensepost/ruler)
- [SensePost NotRuler](https://github.com/sensepost/notruler)
- [Outlook Today Home Page](https://medium.com/@bwtech789/outlook-today-homepage-persistence-33ea9b505943)
