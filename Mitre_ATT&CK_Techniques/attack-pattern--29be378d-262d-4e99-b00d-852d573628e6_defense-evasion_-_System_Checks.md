---
contributors:
- Deloitte Threat Library Team
- Kostya Vasilkov
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Process: OS API Execution'
id: attack-pattern--29be378d-262d-4e99-b00d-852d573628e6
mitre_attack_url: https://attack.mitre.org/techniques/T1497/001
name: System Checks
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
- discovery
title: defense-evasion - System Checks
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, discovery |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1497/001](https://attack.mitre.org/techniques/T1497/001) |

# System Checks (attack-pattern--29be378d-262d-4e99-b00d-852d573628e6)

## Description
Adversaries may employ various system checks to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) during automated discovery to shape follow-on behaviors.(Citation: Deloitte Environment Awareness)

Specific checks will vary based on the target and/or adversary, but may involve behaviors such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047), [PowerShell](https://attack.mitre.org/techniques/T1059/001), [System Information Discovery](https://attack.mitre.org/techniques/T1082), and [Query Registry](https://attack.mitre.org/techniques/T1012) to obtain system information and search for VME artifacts. Adversaries may search for VME artifacts in memory, processes, file system, hardware, and/or the Registry. Adversaries may use scripting to automate these checks  into one script and then have the program exit if it determines the system to be a virtual environment. 

Checks could include generic system properties such as host/domain name and samples of network traffic. Adversaries may also check the network adapters addresses, CPU core count, and available memory/drive size. Once executed, malware may also use [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) to check if it was saved in a folder or file with unexpected or even analysis-related naming artifacts such as `malware`, `sample`, or `hash`.

Other common checks may enumerate services running that are unique to these applications, installed programs on the system, manufacturer/product fields for strings relating to virtual machine applications, and VME-specific hardware/processor instructions.(Citation: McAfee Virtual Jan 2017) In applications like VMWare, adversaries can also use a special I/O port to send commands and receive output. 
 
Hardware checks, such as the presence of the fan, temperature, and audio devices, could also be used to gather evidence that can be indicative a virtual environment. Adversaries may also query for specific readings from these devices.(Citation: Unit 42 OilRig Sept 2018)

## Detection
Virtualization/sandbox related system checks will likely occur in the first steps of an operation but may also occur throughout as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained. Detecting actions related to virtualization and sandbox identification may be difficult depending on the adversary's implementation and monitoring required. Monitoring for suspicious processes being spawned that gather a variety of system information or perform other forms of Discovery, especially in a short period of time, may aid in detection.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1497/001)
- [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
- [McAfee Virtual Jan 2017](https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/stopping-malware-fake-virtual-machine/)
- [Deloitte Environment Awareness](https://drive.google.com/file/d/1t0jn3xr4ff2fR30oQAUn_RsWSnMpOAQc/edit)
