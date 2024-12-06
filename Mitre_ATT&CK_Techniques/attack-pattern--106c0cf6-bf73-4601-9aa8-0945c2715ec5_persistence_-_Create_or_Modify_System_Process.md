---
data_sources:
- 'Service: Service Creation'
- 'Container: Container Creation'
- 'Driver: Driver Load'
- 'Service: Service Modification'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'File: File Modification'
- 'File: File Creation'
- 'Windows Registry: Windows Registry Key Creation'
- 'Process: OS API Execution'
- 'Command: Command Execution'
id: attack-pattern--106c0cf6-bf73-4601-9aa8-0945c2715ec5
mitre_attack_url: https://attack.mitre.org/techniques/T1543
name: Create or Modify System Process
platforms:
- Windows
- macOS
- Linux
- Containers
tactics:
- persistence
- privilege-escalation
title: persistence - Create or Modify System Process
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows, macOS, Linux, Containers |
| **Data Sources** | Service: Service Creation, Container: Container Creation, Driver: Driver Load, Service: Service Modification, Process: Process Creation, Windows Registry: Windows Registry Key Modification, File: File Modification, File: File Creation, Windows Registry: Windows Registry Key Creation, Process: OS API Execution, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1543](https://attack.mitre.org/techniques/T1543) |

# Create or Modify System Process (attack-pattern--106c0cf6-bf73-4601-9aa8-0945c2715ec5)

## Description
Adversaries may create or modify system-level processes to repeatedly execute malicious payloads as part of persistence. When operating systems boot up, they can start processes that perform background system functions. On Windows and Linux, these system processes are referred to as services.(Citation: TechNet Services) On macOS, launchd processes known as [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) and [Launch Agent](https://attack.mitre.org/techniques/T1543/001) are run to finish system initialization and load user specific parameters.(Citation: AppleDocs Launch Agent Daemons) 

Adversaries may install new services, daemons, or agents that can be configured to execute at startup or a repeatable interval in order to establish persistence. Similarly, adversaries may modify existing services, daemons, or agents to achieve the same effect.  

Services, daemons, or agents may be created with administrator privileges but executed under root/SYSTEM privileges. Adversaries may leverage this functionality to create or modify system processes in order to escalate privileges.(Citation: OSX Malware Detection)  

## Detection
Monitor for changes to system processes that do not correlate with known software, patch cycles, etc., including by comparing results against a trusted system baseline. New, benign system processes may be created during installation of new software. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.  

Command-line invocation of tools capable of modifying services may be unusual, depending on how systems are typically used in a particular environment. Look for abnormal process call trees from known services and for execution of other commands that could relate to Discovery or other adversary techniques. 

Monitor for changes to files associated with system-level processes.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1543)
- [AppleDocs Launch Agent Daemons](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
- [TechNet Services](https://technet.microsoft.com/en-us/library/cc772408.aspx)
- [OSX Malware Detection](https://www.synack.com/wp-content/uploads/2016/03/RSA_OSX_Malware.pdf)
