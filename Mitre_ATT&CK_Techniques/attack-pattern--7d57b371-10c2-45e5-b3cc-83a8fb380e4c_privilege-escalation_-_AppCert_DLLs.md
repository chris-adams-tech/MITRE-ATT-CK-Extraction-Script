---
data_sources:
- 'Module: Module Load'
- 'Command: Command Execution'
- 'Process: OS API Execution'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Creation'
id: attack-pattern--7d57b371-10c2-45e5-b3cc-83a8fb380e4c
mitre_attack_url: https://attack.mitre.org/techniques/T1546/009
name: AppCert DLLs
platforms:
- Windows
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - AppCert DLLs
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Windows |
| **Data Sources** | Module: Module Load, Command: Command Execution, Process: OS API Execution, Windows Registry: Windows Registry Key Modification, Process: Process Creation |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/009](https://attack.mitre.org/techniques/T1546/009) |

# AppCert DLLs (attack-pattern--7d57b371-10c2-45e5-b3cc-83a8fb380e4c)

## Description
Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by AppCert DLLs loaded into processes. Dynamic-link libraries (DLLs) that are specified in the <code>AppCertDLLs</code> Registry key under <code>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\</code> are loaded into every process that calls the ubiquitously used application programming interface (API) functions <code>CreateProcess</code>, <code>CreateProcessAsUser</code>, <code>CreateProcessWithLoginW</code>, <code>CreateProcessWithTokenW</code>, or <code>WinExec</code>. (Citation: Elastic Process Injection July 2017)

Similar to [Process Injection](https://attack.mitre.org/techniques/T1055), this value can be abused to obtain elevated privileges by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. Malicious AppCert DLLs may also provide persistence by continuously being triggered by API activity. 

## Detection
Monitor DLL loads by processes, specifically looking for DLLs that are not recognized or not normally loaded into a process. Monitor the AppCertDLLs Registry value for modifications that do not correlate with known software, patch cycles, etc. Monitor and analyze application programming interface (API) calls that are indicative of Registry edits such as RegCreateKeyEx and RegSetValueEx. (Citation: Elastic Process Injection July 2017) 

Tools such as Sysinternals Autoruns may overlook AppCert DLLs as an auto-starting location. (Citation: TechNet Autoruns) (Citation: Sysinternals AppCertDlls Oct 2007)

Look for abnormal process behavior that may be due to a process loading a malicious DLL. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as making network connections for Command and Control, learning details about the environment through Discovery, and conducting Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/009)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
- [Sysinternals AppCertDlls Oct 2007](https://forum.sysinternals.com/appcertdlls_topic12546.html)
