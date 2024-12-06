---
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--132d5b37-aac5-4378-a8dc-3127b18a73dc
mitre_attack_url: https://attack.mitre.org/techniques/T1016/001
name: Internet Connection Discovery
platforms:
- Windows
- Linux
- macOS
tactics:
- discovery
title: discovery - Internet Connection Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Process: Process Creation, Command: Command Execution |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1016/001](https://attack.mitre.org/techniques/T1016/001) |

# Internet Connection Discovery (attack-pattern--132d5b37-aac5-4378-a8dc-3127b18a73dc)

## Description
Adversaries may check for Internet connectivity on compromised systems. This may be performed during automated discovery and can be accomplished in numerous ways such as using [Ping](https://attack.mitre.org/software/S0097), <code>tracert</code>, and GET requests to websites.

Adversaries may use the results and responses from these requests to determine if the system is capable of communicating with their C2 servers before attempting to connect to them. The results may also be used to identify routes, redirectors, and proxy servers.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Command and Control, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to check Internet connectivity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1016/001)
