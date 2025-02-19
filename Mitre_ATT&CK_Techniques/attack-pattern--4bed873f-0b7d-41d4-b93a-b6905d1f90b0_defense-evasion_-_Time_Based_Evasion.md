---
contributors:
- Jorge Orchilles, SCYTHE
- Ruben Dodge, @shotgunner101
- Jeff Felling, Red Canary
- Deloitte Threat Library Team
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--4bed873f-0b7d-41d4-b93a-b6905d1f90b0
mitre_attack_url: https://attack.mitre.org/techniques/T1497/003
name: Time Based Evasion
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
- discovery
title: defense-evasion - Time Based Evasion
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, discovery |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: OS API Execution, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1497/003](https://attack.mitre.org/techniques/T1497/003) |

# Time Based Evasion (attack-pattern--4bed873f-0b7d-41d4-b93a-b6905d1f90b0)

## Description
Adversaries may employ various time-based methods to detect and avoid virtualization and analysis environments. This may include enumerating time-based properties, such as uptime or the system clock, as well as the use of timers or other triggers to avoid a virtual machine environment (VME) or sandbox, specifically those that are automated or only operate for a limited amount of time.

Adversaries may employ various time-based evasions, such as delaying malware functionality upon initial execution using programmatic sleep commands or native system scheduling functionality (ex: [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053)). Delays may also be based on waiting for specific victim conditions to be met (ex: system time, events, etc.) or employ scheduled [Multi-Stage Channels](https://attack.mitre.org/techniques/T1104) to avoid analysis and scrutiny.(Citation: Deloitte Environment Awareness)

Benign commands or other operations may also be used to delay malware execution. Loops or otherwise needless repetitions of commands, such as [Ping](https://attack.mitre.org/software/S0097)s, may be used to delay malware execution and potentially exceed time thresholds of automated analysis environments.(Citation: Revil Independence Day)(Citation: Netskope Nitol) Another variation, commonly referred to as API hammering, involves making various calls to [Native API](https://attack.mitre.org/techniques/T1106) functions in order to delay execution (while also potentially overloading analysis environments with junk data).(Citation: Joe Sec Nymaim)(Citation: Joe Sec Trickbot)

Adversaries may also use time as a metric to detect sandboxes and analysis environments, particularly those that attempt to manipulate time mechanisms to simulate longer elapses of time. For example, an adversary may be able to identify a sandbox accelerating time by sampling and calculating the expected value for an environment's timestamp before and after execution of a sleep function.(Citation: ISACA Malware Tricks)

## Detection
Time-based evasion will likely occur in the first steps of an operation but may also occur throughout as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained. Detecting actions related to virtualization and sandbox identification may be difficult depending on the adversary's implementation and monitoring required. Monitoring for suspicious processes being spawned that gather a variety of system information or perform other forms of Discovery, especially in a short period of time, may aid in detection. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1497/003)
- [Joe Sec Nymaim](https://www.joesecurity.org/blog/3660886847485093803)
- [Joe Sec Trickbot](https://www.joesecurity.org/blog/498839998833561473)
- [ISACA Malware Tricks](https://www.isaca.org/resources/isaca-journal/issues/2017/volume-6/evasive-malware-tricks-how-malware-evades-detection-by-sandboxes)
- [Revil Independence Day](https://news.sophos.com/en-us/2021/07/04/independence-day-revil-uses-supply-chain-exploit-to-attack-hundreds-of-businesses/)
- [Netskope Nitol](https://www.netskope.com/blog/nitol-botnet-makes-resurgence-evasive-sandbox-analysis-technique)
- [Deloitte Environment Awareness](https://drive.google.com/file/d/1t0jn3xr4ff2fR30oQAUn_RsWSnMpOAQc/edit)
