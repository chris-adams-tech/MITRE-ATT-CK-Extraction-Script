---
id: attack-pattern--317fefa6-46c7-4062-adb6-2008cf6bcb41
mitre_attack_url: https://attack.mitre.org/techniques/T1103
name: AppInit DLLs
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - AppInit DLLs
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Permissions Required** | Administrator |
| **System Requirements** | Secure boot disabled on systems running Windows 8 and later |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1103](https://attack.mitre.org/techniques/T1103) |

# AppInit DLLs (attack-pattern--317fefa6-46c7-4062-adb6-2008cf6bcb41)

## Description
Dynamic-link libraries (DLLs) that are specified in the AppInit_DLLs value in the Registry keys <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Windows</code> or <code>HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows</code> are loaded by user32.dll into every process that loads user32.dll. In practice this is nearly every program, since user32.dll is a very common library. (Citation: Elastic Process Injection July 2017) Similar to [Process Injection](https://attack.mitre.org/techniques/T1055), these values can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. (Citation: AppInit Registry)

The AppInit DLL functionality is disabled in Windows 8 and later versions when secure boot is enabled. (Citation: AppInit Secure Boot)

## Detection
Monitor DLL loads by processes that load user32.dll and look for DLLs that are not recognized or not normally loaded into a process. Monitor the AppInit_DLLs Registry values for modifications that do not correlate with known software, patch cycles, etc. Monitor and analyze application programming interface (API) calls that are indicative of Registry edits such as RegCreateKeyEx and RegSetValueEx. (Citation: Elastic Process Injection July 2017) Tools such as Sysinternals Autoruns may also be used to detect system changes that could be attempts at persistence, including listing current AppInit DLLs. (Citation: TechNet Autoruns) 

Look for abnormal process behavior that may be due to a process loading a malicious DLL. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as making network connections for Command and Control, learning details about the environment through Discovery, and conducting Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1103)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [AppInit Registry](https://support.microsoft.com/en-us/kb/197571)
- [AppInit Secure Boot](https://msdn.microsoft.com/en-us/library/dn280412)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
