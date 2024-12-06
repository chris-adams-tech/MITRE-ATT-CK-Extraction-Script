---
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Creation'
id: attack-pattern--eb125d40-0b2d-41ac-a71a-3229241c2cd3
mitre_attack_url: https://attack.mitre.org/techniques/T1037/001
name: Logon Script (Windows)
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Logon Script (Windows)
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation, Windows Registry: Windows Registry Key Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1037/001](https://attack.mitre.org/techniques/T1037/001) |

# Logon Script (Windows) (attack-pattern--eb125d40-0b2d-41ac-a71a-3229241c2cd3)

## Description
Adversaries may use Windows logon scripts automatically executed at logon initialization to establish persistence. Windows allows logon scripts to be run whenever a specific user or group of users log into a system.(Citation: TechNet Logon Scripts) This is done via adding a path to a script to the <code>HKCU\Environment\UserInitMprLogonScript</code> Registry key.(Citation: Hexacorn Logon Scripts)

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

## Detection
Monitor for changes to Registry values associated with Windows logon scrips, nameley <code>HKCU\Environment\UserInitMprLogonScript</code>.

Monitor running process for actions that could be indicative of abnormal programs or executables running upon logon.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1037/001)
- [TechNet Logon Scripts](https://technet.microsoft.com/en-us/library/cc758918(v=ws.10).aspx)
- [Hexacorn Logon Scripts](http://www.hexacorn.com/blog/2014/11/14/beyond-good-ol-run-key-part-18/)
