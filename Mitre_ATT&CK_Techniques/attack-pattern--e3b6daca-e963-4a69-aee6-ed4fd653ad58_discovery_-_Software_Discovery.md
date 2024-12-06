---
data_sources:
- 'Process: OS API Execution'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Firewall: Firewall Enumeration'
- 'Firewall: Firewall Metadata'
id: attack-pattern--e3b6daca-e963-4a69-aee6-ed4fd653ad58
mitre_attack_url: https://attack.mitre.org/techniques/T1518
name: Software Discovery
platforms:
- Windows
- IaaS
- Linux
- macOS
tactics:
- discovery
title: discovery - Software Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Data Sources** | Process: OS API Execution, Command: Command Execution, Process: Process Creation, Firewall: Firewall Enumeration, Firewall: Firewall Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1518](https://attack.mitre.org/techniques/T1518) |

# Software Discovery (attack-pattern--e3b6daca-e963-4a69-aee6-ed4fd653ad58)

## Description
Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from [Software Discovery](https://attack.mitre.org/techniques/T1518) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Such software may be deployed widely across the environment for configuration management or security reasons, such as [Software Deployment Tools](https://attack.mitre.org/techniques/T1072), and may allow adversaries broad access to infect devices or move laterally.

Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1518)
