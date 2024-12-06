---
id: attack-pattern--1c338d0f-a65e-4073-a5c1-c06878849f21
mitre_attack_url: https://attack.mitre.org/techniques/T1093
name: Process Hollowing
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Process Hollowing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1093](https://attack.mitre.org/techniques/T1093) |

# Process Hollowing (attack-pattern--1c338d0f-a65e-4073-a5c1-c06878849f21)

## Description
Process hollowing occurs when a process is created in a suspended state then its memory is unmapped and replaced with malicious code. Similar to [Process Injection](https://attack.mitre.org/techniques/T1055), execution of the malicious code is masked under a legitimate process and may evade defenses and detection analysis. (Citation: Leitch Hollowing) (Citation: Elastic Process Injection July 2017)

## Detection
Monitoring API calls may generate a significant amount of data and may not be directly useful for defense unless collected under specific circumstances for known bad sequences of calls, since benign use of API functions may be common and difficult to distinguish from malicious behavior. API calls that unmap process memory, such as ZwUnmapViewOfSection or NtUnmapViewOfSection, and those that can be used to modify memory within another process, such as WriteProcessMemory, may be used for this technique. (Citation: Elastic Process Injection July 2017)

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1093)
- [Leitch Hollowing](http://www.autosectools.com/process-hollowing.pdf)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
