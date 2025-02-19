---
id: attack-pattern--241814ae-de3f-4656-b49e-f9a80764d4b7
mitre_attack_url: https://attack.mitre.org/techniques/T1063
name: Security Software Discovery
platforms:
- macOS
- Windows
tactics:
- discovery
title: discovery - Security Software Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | macOS, Windows |
| **Permissions Required** | User, Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1063](https://attack.mitre.org/techniques/T1063) |

# Security Software Discovery (attack-pattern--241814ae-de3f-4656-b49e-f9a80764d4b7)

## Description
Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors that are installed on the system. This may include things such as local firewall rules and anti-virus. Adversaries may use the information from [Security Software Discovery](https://attack.mitre.org/techniques/T1063) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.


### Windows

Example commands that can be used to obtain security software information are [netsh](https://attack.mitre.org/software/S0108), <code>reg query</code> with [Reg](https://attack.mitre.org/software/S0075), <code>dir</code> with [cmd](https://attack.mitre.org/software/S0106), and [Tasklist](https://attack.mitre.org/software/S0057), but other indicators of discovery behavior may be more specific to the type of software or security system the adversary is looking for.

### Mac

It's becoming more common to see macOS malware perform checks for LittleSnitch and KnockKnock software.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1086).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1063)
