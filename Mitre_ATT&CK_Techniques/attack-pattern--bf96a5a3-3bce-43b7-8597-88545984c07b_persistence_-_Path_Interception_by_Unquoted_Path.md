---
contributors:
- Stefan Kanthak
data_sources:
- 'File: File Modification'
- 'File: File Creation'
- 'Process: Process Creation'
id: attack-pattern--bf96a5a3-3bce-43b7-8597-88545984c07b
mitre_attack_url: https://attack.mitre.org/techniques/T1574/009
name: Path Interception by Unquoted Path
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - Path Interception by Unquoted Path
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | File: File Modification, File: File Creation, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/009](https://attack.mitre.org/techniques/T1574/009) |

# Path Interception by Unquoted Path (attack-pattern--bf96a5a3-3bce-43b7-8597-88545984c07b)

## Description
Adversaries may execute their own malicious payloads by hijacking vulnerable file path references. Adversaries can take advantage of paths that lack surrounding quotations by placing an executable in a higher level directory within the path, so that Windows will choose the adversary's executable to launch.

Service paths (Citation: Microsoft CurrentControlSet Services) and shortcut paths may also be vulnerable to path interception if the path has one or more spaces and is not surrounded by quotation marks (e.g., <code>C:\unsafe path with space\program.exe</code> vs. <code>"C:\safe path with space\program.exe"</code>). (Citation: Help eliminate unquoted path) (stored in Windows Registry keys) An adversary can place an executable in a higher level directory of the path, and Windows will resolve that executable instead of the intended executable. For example, if the path in a shortcut is <code>C:\program files\myapp.exe</code>, an adversary may create a program at <code>C:\program.exe</code> that will be run instead of the intended program. (Citation: Windows Unquoted Services) (Citation: Windows Privilege Escalation Guide)

This technique can be used for persistence if executables are called on a regular basis, as well as privilege escalation if intercepted executables are started by a higher privileged process.

## Detection
Monitor file creation for files named after partial directories and in locations that may be searched for common processes through the environment variable, or otherwise should not be user writable. Monitor the executing process for process executable paths that are named for partial directories. Monitor file creation for programs that are named after Windows system programs or programs commonly executed without a path (such as "findstr," "net," and "python"). If this activity occurs outside of known administration activity, upgrades, installations, or patches, then it may be suspicious.

Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/009)
- [Windows Privilege Escalation Guide](https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/)
- [Windows Unquoted Services](https://securityboulevard.com/2018/04/windows-privilege-escalation-unquoted-services/)
- [Help eliminate unquoted path](https://isc.sans.edu/diary/Help+eliminate+unquoted+path+vulnerabilities/14464)
- [Microsoft CurrentControlSet Services](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree)
