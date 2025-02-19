---
data_sources:
- 'Process: OS API Execution'
- 'Windows Registry: Windows Registry Key Access'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--c32f7008-9fea-41f7-8366-5eb9b74bd896
mitre_attack_url: https://attack.mitre.org/techniques/T1012
name: Query Registry
platforms:
- Windows
tactics:
- discovery
title: discovery - Query Registry
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows |
| **Data Sources** | Process: OS API Execution, Windows Registry: Windows Registry Key Access, Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1012](https://attack.mitre.org/techniques/T1012) |

# Query Registry (attack-pattern--c32f7008-9fea-41f7-8366-5eb9b74bd896)

## Description
Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

The Registry contains a significant amount of information about the operating system, configuration, software, and security.(Citation: Wikipedia Windows Registry) Information can easily be queried using the [Reg](https://attack.mitre.org/software/S0075) utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from [Query Registry](https://attack.mitre.org/techniques/T1012) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Interaction with the Windows Registry may come from the command line using utilities such as [Reg](https://attack.mitre.org/software/S0075) or through running malware that may interact with the Registry through an API. Command-line invocation of utilities used to query the Registry may be detected through process and command-line monitoring. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1012)
- [Wikipedia Windows Registry](https://en.wikipedia.org/wiki/Windows_Registry)
