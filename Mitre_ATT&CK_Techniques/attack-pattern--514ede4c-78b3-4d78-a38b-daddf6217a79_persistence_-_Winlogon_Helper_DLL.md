---
contributors:
- Praetorian
id: attack-pattern--514ede4c-78b3-4d78-a38b-daddf6217a79
mitre_attack_url: https://attack.mitre.org/techniques/T1004
name: Winlogon Helper DLL
platforms:
- Windows
tactics:
- persistence
title: persistence - Winlogon Helper DLL
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1004](https://attack.mitre.org/techniques/T1004) |

# Winlogon Helper DLL (attack-pattern--514ede4c-78b3-4d78-a38b-daddf6217a79)

## Description
Winlogon.exe is a Windows component responsible for actions at logon/logoff as well as the secure attention sequence (SAS) triggered by Ctrl-Alt-Delete. Registry entries in <code>HKLM\Software\[Wow6432Node\]Microsoft\Windows NT\CurrentVersion\Winlogon\</code> and <code>HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\</code> are used to manage additional helper programs and functionalities that support Winlogon. (Citation: Cylance Reg Persistence Sept 2013) 

Malicious modifications to these Registry keys may cause Winlogon to load and execute malicious DLLs and/or executables. Specifically, the following subkeys have been known to be possibly vulnerable to abuse: (Citation: Cylance Reg Persistence Sept 2013)

* Winlogon\Notify - points to notification package DLLs that handle Winlogon events
* Winlogon\Userinit - points to userinit.exe, the user initialization program executed when a user logs on
* Winlogon\Shell - points to explorer.exe, the system shell executed when a user logs on

Adversaries may take advantage of these features to repeatedly execute malicious code and establish Persistence.

## Detection
Monitor for changes to Registry entries associated with Winlogon that do not correlate with known software, patch cycles, etc. Tools such as Sysinternals Autoruns may also be used to detect system changes that could be attempts at persistence, including listing current Winlogon helper values. (Citation: TechNet Autoruns)  New DLLs written to System32 that do not correlate with known good software or patching may also be suspicious.

Look for abnormal process behavior that may be due to a process loading a malicious DLL. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1004)
- [capec](https://capec.mitre.org/data/definitions/579.html)
- [Cylance Reg Persistence Sept 2013](https://blog.cylance.com/windows-registry-persistence-part-2-the-run-keys-and-search-order)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
