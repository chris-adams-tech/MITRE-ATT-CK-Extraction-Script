---
contributors:
- Harshal Tupsamudre, Qualys
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Process: OS API Execution'
id: attack-pattern--322bad5a-1c49-4d23-ab79-76d641794afa
mitre_attack_url: https://attack.mitre.org/techniques/T1007
name: System Service Discovery
platforms:
- Windows
- macOS
- Linux
tactics:
- discovery
title: discovery - System Service Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Command: Command Execution, Process: Process Creation, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1007](https://attack.mitre.org/techniques/T1007) |

# System Service Discovery (attack-pattern--322bad5a-1c49-4d23-ab79-76d641794afa)

## Description
Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as <code>sc query</code>, <code>tasklist /svc</code>, <code>systemctl --type=service</code>, and <code>net start</code>.

Adversaries may use the information from [System Service Discovery](https://attack.mitre.org/techniques/T1007) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system information related to services. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1007)
