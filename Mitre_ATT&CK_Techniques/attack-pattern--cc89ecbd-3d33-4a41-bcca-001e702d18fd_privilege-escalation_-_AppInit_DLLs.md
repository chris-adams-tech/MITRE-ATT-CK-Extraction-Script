---
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Module: Module Load'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: OS API Execution'
id: attack-pattern--cc89ecbd-3d33-4a41-bcca-001e702d18fd
mitre_attack_url: https://attack.mitre.org/techniques/T1546/010
name: AppInit DLLs
platforms:
- Windows
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - AppInit DLLs
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution, Module: Module Load, Windows Registry: Windows Registry Key Modification, Process: OS API Execution |
| **Permissions Required** | Administrator |
| **System Requirements** | Secure boot disabled on systems running Windows 8 and later |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/010](https://attack.mitre.org/techniques/T1546/010) |

# AppInit DLLs (attack-pattern--cc89ecbd-3d33-4a41-bcca-001e702d18fd)

## Description
Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by AppInit DLLs loaded into processes. Dynamic-link libraries (DLLs) that are specified in the <code>AppInit_DLLs</code> value in the Registry keys <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Windows</code> or <code>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows</code> are loaded by user32.dll into every process that loads user32.dll. In practice this is nearly every program, since user32.dll is a very common library. (Citation: Elastic Process Injection July 2017)

Similar to Process Injection, these values can be abused to obtain elevated privileges by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. (Citation: AppInit Registry) Malicious AppInit DLLs may also provide persistence by continuously being triggered by API activity. 

The AppInit DLL functionality is disabled in Windows 8 and later versions when secure boot is enabled. (Citation: AppInit Secure Boot)

## Detection
Monitor DLL loads by processes that load user32.dll and look for DLLs that are not recognized or not normally loaded into a process. Monitor the AppInit_DLLs Registry values for modifications that do not correlate with known software, patch cycles, etc. Monitor and analyze application programming interface (API) calls that are indicative of Registry edits such as <code>RegCreateKeyEx</code> and <code>RegSetValueEx</code>. (Citation: Elastic Process Injection July 2017)

Tools such as Sysinternals Autoruns may also be used to detect system changes that could be attempts at persistence, including listing current AppInit DLLs. (Citation: TechNet Autoruns) 

Look for abnormal process behavior that may be due to a process loading a malicious DLL. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as making network connections for Command and Control, learning details about the environment through Discovery, and conducting Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/010)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [AppInit Registry](https://support.microsoft.com/en-us/kb/197571)
- [AppInit Secure Boot](https://msdn.microsoft.com/en-us/library/dn280412)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
