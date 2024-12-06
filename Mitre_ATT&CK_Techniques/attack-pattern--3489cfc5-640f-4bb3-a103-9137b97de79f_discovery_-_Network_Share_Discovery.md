---
contributors:
- Praetorian
data_sources:
- 'Process: OS API Execution'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--3489cfc5-640f-4bb3-a103-9137b97de79f
mitre_attack_url: https://attack.mitre.org/techniques/T1135
name: Network Share Discovery
platforms:
- macOS
- Windows
- Linux
tactics:
- discovery
title: discovery - Network Share Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | macOS, Windows, Linux |
| **Data Sources** | Process: OS API Execution, Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1135](https://attack.mitre.org/techniques/T1135) |

# Network Share Discovery (attack-pattern--3489cfc5-640f-4bb3-a103-9137b97de79f)

## Description
Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. 

File sharing over a Windows network occurs over the SMB protocol. (Citation: Wikipedia Shared Resource) (Citation: TechNet Shared Folder) [Net](https://attack.mitre.org/software/S0039) can be used to query a remote system for available shared drives using the <code>net view \\\\remotesystem</code> command. It can also be used to query shared drives on the local system using <code>net share</code>. For macOS, the <code>sharing -l</code> command lists all shared points used for smb services.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Normal, benign system and network events related to legitimate remote system discovery may be uncommon, depending on the environment and how they are used. Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1135)
- [TechNet Shared Folder](https://technet.microsoft.com/library/cc770880.aspx)
- [Wikipedia Shared Resource](https://en.wikipedia.org/wiki/Shared_resource)
