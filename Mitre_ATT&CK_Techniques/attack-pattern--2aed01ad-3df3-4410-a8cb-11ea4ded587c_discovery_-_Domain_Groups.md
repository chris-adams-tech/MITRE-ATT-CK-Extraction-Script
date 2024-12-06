---
contributors:
- Harshal Tupsamudre, Qualys
- Miriam Wiesner, @miriamxyra, Microsoft Security
data_sources:
- 'Group: Group Enumeration'
- 'Command: Command Execution'
- 'Process: OS API Execution'
- 'Process: Process Creation'
id: attack-pattern--2aed01ad-3df3-4410-a8cb-11ea4ded587c
mitre_attack_url: https://attack.mitre.org/techniques/T1069/002
name: Domain Groups
platforms:
- Linux
- macOS
- Windows
tactics:
- discovery
title: discovery - Domain Groups
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Group: Group Enumeration, Command: Command Execution, Process: OS API Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1069/002](https://attack.mitre.org/techniques/T1069/002) |

# Domain Groups (attack-pattern--2aed01ad-3df3-4410-a8cb-11ea4ded587c)

## Description
Adversaries may attempt to find domain-level groups and permission settings. The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators.

Commands such as <code>net group /domain</code> of the [Net](https://attack.mitre.org/software/S0039) utility,  <code>dscacheutil -q group</code> on macOS, and <code>ldapsearch</code> on Linux can list domain-level groups.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1069/002)
