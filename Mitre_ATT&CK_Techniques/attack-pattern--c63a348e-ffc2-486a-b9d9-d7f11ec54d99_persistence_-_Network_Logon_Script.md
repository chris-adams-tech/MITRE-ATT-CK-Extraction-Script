---
data_sources:
- 'Command: Command Execution'
- 'Active Directory: Active Directory Object Modification'
- 'File: File Modification'
- 'Process: Process Creation'
- 'File: File Creation'
id: attack-pattern--c63a348e-ffc2-486a-b9d9-d7f11ec54d99
mitre_attack_url: https://attack.mitre.org/techniques/T1037/003
name: Network Logon Script
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Network Logon Script
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Active Directory: Active Directory Object Modification, File: File Modification, Process: Process Creation, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1037/003](https://attack.mitre.org/techniques/T1037/003) |

# Network Logon Script (attack-pattern--c63a348e-ffc2-486a-b9d9-d7f11ec54d99)

## Description
Adversaries may use network logon scripts automatically executed at logon initialization to establish persistence. Network logon scripts can be assigned using Active Directory or Group Policy Objects.(Citation: Petri Logon Script AD) These logon scripts run with the privileges of the user they are assigned to. Depending on the systems within the network, initializing one of these scripts could apply to more than one or potentially all systems.  
 
Adversaries may use these scripts to maintain persistence on a network. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary.

## Detection
Monitor logon scripts for unusual access by abnormal users or at abnormal times. Look for files added or modified by unusual accounts outside of normal administration duties. Monitor running process for actions that could be indicative of abnormal programs or executables running upon logon.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1037/003)
- [Petri Logon Script AD](https://www.petri.com/setting-up-logon-script-through-active-directory-users-computers-windows-server-2008)
