---
contributors:
- Praetorian
data_sources:
- 'Command: Command Execution'
- 'Module: Module Load'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Modification'
id: attack-pattern--6836813e-8ec8-4375-b459-abb388cb1a35
mitre_attack_url: https://attack.mitre.org/techniques/T1547/004
name: Winlogon Helper DLL
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Winlogon Helper DLL
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Module: Module Load, Process: Process Creation, Windows Registry: Windows Registry Key Modification |
| **Permissions Required** | SYSTEM, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/004](https://attack.mitre.org/techniques/T1547/004) |

# Winlogon Helper DLL (attack-pattern--6836813e-8ec8-4375-b459-abb388cb1a35)

## Description
Adversaries may abuse features of Winlogon to execute DLLs and/or executables when a user logs in. Winlogon.exe is a Windows component responsible for actions at logon/logoff as well as the secure attention sequence (SAS) triggered by Ctrl-Alt-Delete. Registry entries in <code>HKLM\Software[\\Wow6432Node\\]\Microsoft\Windows NT\CurrentVersion\Winlogon\</code> and <code>HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\</code> are used to manage additional helper programs and functionalities that support Winlogon.(Citation: Cylance Reg Persistence Sept 2013) 

Malicious modifications to these Registry keys may cause Winlogon to load and execute malicious DLLs and/or executables. Specifically, the following subkeys have been known to be possibly vulnerable to abuse: (Citation: Cylance Reg Persistence Sept 2013)

* Winlogon\Notify - points to notification package DLLs that handle Winlogon events
* Winlogon\Userinit - points to userinit.exe, the user initialization program executed when a user logs on
* Winlogon\Shell - points to explorer.exe, the system shell executed when a user logs on

Adversaries may take advantage of these features to repeatedly execute malicious code and establish persistence.

## Detection
Monitor for changes to Registry entries associated with Winlogon that do not correlate with known software, patch cycles, etc. Tools such as Sysinternals Autoruns may also be used to detect system changes that could be attempts at persistence, including listing current Winlogon helper values. (Citation: TechNet Autoruns)  New DLLs written to System32 that do not correlate with known good software or patching may also be suspicious.

Look for abnormal process behavior that may be due to a process loading a malicious DLL. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/004)
- [Cylance Reg Persistence Sept 2013](https://blog.cylance.com/windows-registry-persistence-part-2-the-run-keys-and-search-order)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
