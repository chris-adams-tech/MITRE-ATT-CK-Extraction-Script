---
contributors:
- Stefan Kanthak
data_sources:
- 'Process: Process Creation'
- 'File: File Modification'
- 'File: File Creation'
id: attack-pattern--58af3705-8740-4c68-9329-ec015a7013c2
mitre_attack_url: https://attack.mitre.org/techniques/T1574/008
name: Path Interception by Search Order Hijacking
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - Path Interception by Search Order Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, File: File Modification, File: File Creation |
| **Permissions Required** | Administrator, User, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/008](https://attack.mitre.org/techniques/T1574/008) |

# Path Interception by Search Order Hijacking (attack-pattern--58af3705-8740-4c68-9329-ec015a7013c2)

## Description
Adversaries may execute their own malicious payloads by hijacking the search order used to load other programs. Because some programs do not call other programs using the full path, adversaries may place their own file in the directory where the calling program is located, causing the operating system to launch their malicious software at the request of the calling program.

Search order hijacking occurs when an adversary abuses the order in which Windows searches for programs that are not given a path. Unlike [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001), the search order differs depending on the method that is used to execute the program. (Citation: Microsoft CreateProcess) (Citation: Windows NT Command Shell) (Citation: Microsoft WinExec) However, it is common for Windows to search in the directory of the initiating program before searching through the Windows system directory. An adversary who finds a program vulnerable to search order hijacking (i.e., a program that does not specify the path to an executable) may take advantage of this vulnerability by creating a program named after the improperly specified program and placing it within the initiating program's directory.

For example, "example.exe" runs "cmd.exe" with the command-line argument <code>net user</code>. An adversary may place a program called "net.exe" within the same directory as example.exe, "net.exe" will be run instead of the Windows system utility net. In addition, if an adversary places a program called "net.com" in the same directory as "net.exe", then <code>cmd.exe /C net user</code> will execute "net.com" instead of "net.exe" due to the order of executable extensions defined under PATHEXT. (Citation: Microsoft Environment Property)

Search order hijacking is also a common practice for hijacking DLL loads and is covered in [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001).

## Detection
Monitor file creation for files named after partial directories and in locations that may be searched for common processes through the environment variable, or otherwise should not be user writable. Monitor the executing process for process executable paths that are named for partial directories. Monitor file creation for programs that are named after Windows system programs or programs commonly executed without a path (such as "findstr," "net," and "python"). If this activity occurs outside of known administration activity, upgrades, installations, or patches, then it may be suspicious.

Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.


## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/008)
- [Microsoft Environment Property](https://docs.microsoft.com/en-us/previous-versions//fd7hxfdd(v=vs.85)?redirectedfrom=MSDN)
- [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)
- [Microsoft WinExec](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-winexec)
- [Windows NT Command Shell](https://docs.microsoft.com/en-us/previous-versions//cc723564(v=technet.10)?redirectedfrom=MSDN#XSLTsection127121120120)
