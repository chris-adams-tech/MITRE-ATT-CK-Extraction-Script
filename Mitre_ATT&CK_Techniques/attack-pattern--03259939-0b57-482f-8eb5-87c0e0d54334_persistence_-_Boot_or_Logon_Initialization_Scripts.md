---
data_sources:
- 'File: File Modification'
- 'Windows Registry: Windows Registry Key Creation'
- 'Command: Command Execution'
- 'File: File Creation'
- 'Process: Process Creation'
- 'Active Directory: Active Directory Object Modification'
id: attack-pattern--03259939-0b57-482f-8eb5-87c0e0d54334
mitre_attack_url: https://attack.mitre.org/techniques/T1037
name: Boot or Logon Initialization Scripts
platforms:
- macOS
- Windows
- Linux
- Network
tactics:
- persistence
- privilege-escalation
title: persistence - Boot or Logon Initialization Scripts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS, Windows, Linux, Network |
| **Data Sources** | File: File Modification, Windows Registry: Windows Registry Key Creation, Command: Command Execution, File: File Creation, Process: Process Creation, Active Directory: Active Directory Object Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1037](https://attack.mitre.org/techniques/T1037) |

# Boot or Logon Initialization Scripts (attack-pattern--03259939-0b57-482f-8eb5-87c0e0d54334)

## Description
Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.(Citation: Mandiant APT29 Eye Spy Email Nov 22)(Citation: Anomali Rocke March 2019) Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.  

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.

## Detection
Monitor logon scripts for unusual access by abnormal users or at abnormal times. Look for files added or modified by unusual accounts outside of normal administration duties. Monitor running process for actions that could be indicative of abnormal programs or executables running upon logon.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1037)
- [Anomali Rocke March 2019](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
