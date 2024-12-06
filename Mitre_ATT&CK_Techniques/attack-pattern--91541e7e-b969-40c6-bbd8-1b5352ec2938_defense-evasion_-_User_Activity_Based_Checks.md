---
contributors:
- Deloitte Threat Library Team
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--91541e7e-b969-40c6-bbd8-1b5352ec2938
mitre_attack_url: https://attack.mitre.org/techniques/T1497/002
name: User Activity Based Checks
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
- discovery
title: defense-evasion - User Activity Based Checks
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, discovery |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: OS API Execution, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1497/002](https://attack.mitre.org/techniques/T1497/002) |

# User Activity Based Checks (attack-pattern--91541e7e-b969-40c6-bbd8-1b5352ec2938)

## Description
Adversaries may employ various user activity checks to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) during automated discovery to shape follow-on behaviors.(Citation: Deloitte Environment Awareness)

Adversaries may search for user activity on the host based on variables such as the speed/frequency of mouse movements and clicks (Citation: Sans Virtual Jan 2016) , browser history, cache, bookmarks, or number of files in common directories such as home or the desktop. Other methods may rely on specific user interaction with the system before the malicious code is activated, such as waiting for a document to close before activating a macro (Citation: Unit 42 Sofacy Nov 2018) or waiting for a user to double click on an embedded image to activate.(Citation: FireEye FIN7 April 2017) 

## Detection
User activity-based checks will likely occur in the first steps of an operation but may also occur throughout as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained. Detecting actions related to virtualization and sandbox identification may be difficult depending on the adversary's implementation and monitoring required. Monitoring for suspicious processes being spawned that gather a variety of system information or perform other forms of Discovery, especially in a short period of time, may aid in detection. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1497/002)
- [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
- [Unit 42 Sofacy Nov 2018](https://unit42.paloaltonetworks.com/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [Sans Virtual Jan 2016](https://www.sans.org/reading-room/whitepapers/forensics/detecting-malware-sandbox-evasion-techniques-36667)
- [Deloitte Environment Awareness](https://drive.google.com/file/d/1t0jn3xr4ff2fR30oQAUn_RsWSnMpOAQc/edit)
