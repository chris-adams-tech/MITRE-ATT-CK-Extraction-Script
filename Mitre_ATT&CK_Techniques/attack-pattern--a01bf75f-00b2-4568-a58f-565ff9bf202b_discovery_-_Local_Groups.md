---
contributors:
- Harshal Tupsamudre, Qualys
- Miriam Wiesner, @miriamxyra, Microsoft Security
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Creation'
- 'Group: Group Enumeration'
- 'Command: Command Execution'
id: attack-pattern--a01bf75f-00b2-4568-a58f-565ff9bf202b
mitre_attack_url: https://attack.mitre.org/techniques/T1069/001
name: Local Groups
platforms:
- Linux
- macOS
- Windows
tactics:
- discovery
title: discovery - Local Groups
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: OS API Execution, Process: Process Creation, Group: Group Enumeration, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1069/001](https://attack.mitre.org/techniques/T1069/001) |

# Local Groups (attack-pattern--a01bf75f-00b2-4568-a58f-565ff9bf202b)

## Description
Adversaries may attempt to find local system groups and permission settings. The knowledge of local system permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as the users found within the local administrators group.

Commands such as <code>net localgroup</code> of the [Net](https://attack.mitre.org/software/S0039) utility, <code>dscl . -list /Groups</code> on macOS, and <code>groups</code> on Linux can list local groups.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1069/001)
