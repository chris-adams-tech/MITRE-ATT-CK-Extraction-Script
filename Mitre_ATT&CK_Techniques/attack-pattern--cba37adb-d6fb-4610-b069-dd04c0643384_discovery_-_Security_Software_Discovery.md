---
contributors:
- Isif Ibrahima, Mandiant
data_sources:
- 'Process: Process Creation'
- 'Firewall: Firewall Metadata'
- 'Command: Command Execution'
- 'Process: OS API Execution'
- 'Firewall: Firewall Enumeration'
id: attack-pattern--cba37adb-d6fb-4610-b069-dd04c0643384
mitre_attack_url: https://attack.mitre.org/techniques/T1518/001
name: Security Software Discovery
platforms:
- Windows
- IaaS
- Linux
- macOS
tactics:
- discovery
title: discovery - Security Software Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Data Sources** | Process: Process Creation, Firewall: Firewall Metadata, Command: Command Execution, Process: OS API Execution, Firewall: Firewall Enumeration |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1518/001](https://attack.mitre.org/techniques/T1518/001) |

# Security Software Discovery (attack-pattern--cba37adb-d6fb-4610-b069-dd04c0643384)

## Description
Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors that are installed on a system or in a cloud environment. This may include things such as cloud monitoring agents and anti-virus. Adversaries may use the information from [Security Software Discovery](https://attack.mitre.org/techniques/T1518/001) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Example commands that can be used to obtain security software information are [netsh](https://attack.mitre.org/software/S0108), <code>reg query</code> with [Reg](https://attack.mitre.org/software/S0075), <code>dir</code> with [cmd](https://attack.mitre.org/software/S0106), and [Tasklist](https://attack.mitre.org/software/S0057), but other indicators of discovery behavior may be more specific to the type of software or security system the adversary is looking for. It is becoming more common to see macOS malware perform checks for LittleSnitch and KnockKnock software.

Adversaries may also utilize the [Cloud API](https://attack.mitre.org/techniques/T1059/009) to discover cloud-native security software installed on compute infrastructure, such as the AWS CloudWatch agent, Azure VM Agent, and Google Cloud Monitor agent. These agents  may collect  metrics and logs from the VM, which may be centrally aggregated in a cloud-based monitoring platform.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

In cloud environments, additionally monitor logs for the usage of APIs that may be used to gather information about security software configurations within the environment.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1518/001)
