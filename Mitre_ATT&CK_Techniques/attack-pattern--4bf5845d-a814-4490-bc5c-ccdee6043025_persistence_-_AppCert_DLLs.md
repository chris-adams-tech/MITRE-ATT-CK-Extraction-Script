---
id: attack-pattern--4bf5845d-a814-4490-bc5c-ccdee6043025
mitre_attack_url: https://attack.mitre.org/techniques/T1182
name: AppCert DLLs
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - AppCert DLLs
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1182](https://attack.mitre.org/techniques/T1182) |

# AppCert DLLs (attack-pattern--4bf5845d-a814-4490-bc5c-ccdee6043025)

## Description
Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs Registry key under <code>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager</code> are loaded into every process that calls the ubiquitously used application programming interface (API) functions CreateProcess, CreateProcessAsUser, CreateProcessWithLoginW, CreateProcessWithTokenW, or WinExec. (Citation: Elastic Process Injection July 2017)

Similar to [Process Injection](https://attack.mitre.org/techniques/T1055), this value can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer.

## Detection
Monitor DLL loads by processes, specifically looking for DLLs that are not recognized or not normally loaded into a process. Monitor the AppCertDLLs Registry value for modifications that do not correlate with known software, patch cycles, etc. Monitor and analyze application programming interface (API) calls that are indicative of Registry edits such as RegCreateKeyEx and RegSetValueEx. (Citation: Elastic Process Injection July 2017) 

Tools such as Sysinternals Autoruns may overlook AppCert DLLs as an auto-starting location. (Citation: TechNet Autoruns) (Citation: Sysinternals AppCertDlls Oct 2007)

Look for abnormal process behavior that may be due to a process loading a malicious DLL. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as making network connections for Command and Control, learning details about the environment through Discovery, and conducting Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1182)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
- [Sysinternals AppCertDlls Oct 2007](https://forum.sysinternals.com/appcertdlls_topic12546.html)
