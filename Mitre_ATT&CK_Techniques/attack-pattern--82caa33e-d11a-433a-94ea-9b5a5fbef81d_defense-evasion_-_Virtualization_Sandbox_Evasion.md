---
contributors:
- Deloitte Threat Library Team
- Sunny Neo
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Process: OS API Execution'
id: attack-pattern--82caa33e-d11a-433a-94ea-9b5a5fbef81d
mitre_attack_url: https://attack.mitre.org/techniques/T1497
name: Virtualization/Sandbox Evasion
platforms:
- Windows
- macOS
- Linux
tactics:
- defense-evasion
- discovery
title: defense-evasion - Virtualization/Sandbox Evasion
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, discovery |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Command: Command Execution, Process: Process Creation, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1497](https://attack.mitre.org/techniques/T1497) |

# Virtualization/Sandbox Evasion (attack-pattern--82caa33e-d11a-433a-94ea-9b5a5fbef81d)

## Description
Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) during automated discovery to shape follow-on behaviors.(Citation: Deloitte Environment Awareness)

Adversaries may use several methods to accomplish [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) such as checking for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) or other system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandbox.(Citation: Unit 42 Pirpi July 2015)



## Detection
Virtualization, sandbox, user activity, and related discovery techniques will likely occur in the first steps of an operation but may also occur throughout as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained. Detecting actions related to virtualization and sandbox identification may be difficult depending on the adversary's implementation and monitoring required. Monitoring for suspicious processes being spawned that gather a variety of system information or perform other forms of Discovery, especially in a short period of time, may aid in detection.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1497)
- [Unit 42 Pirpi July 2015](https://unit42.paloaltonetworks.com/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
- [Deloitte Environment Awareness](https://drive.google.com/file/d/1t0jn3xr4ff2fR30oQAUn_RsWSnMpOAQc/edit)
