---
contributors:
- David Fiser, @anu4is, Trend Micro
- Alfredo Oliveira, Trend Micro
- Jay Chen, Palo Alto Networks
- Magno Logan, @magnologan, Trend Micro
- Vishwas Manral, McAfee
- Yossi Weizman, Azure Defender Research Team
- Menachem Goldstein
data_sources:
- 'Cloud Service: Cloud Service Modification'
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
- 'File: File Creation'
- 'Network Traffic: Network Connection Creation'
- 'Sensor Health: Host Status'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--cd25c1b4-935c-4f0e-ba8d-552f28bc4783
mitre_attack_url: https://attack.mitre.org/techniques/T1496
name: Resource Hijacking
platforms:
- Windows
- IaaS
- Linux
- macOS
- Containers
- SaaS
tactics:
- impact
title: impact - Resource Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, IaaS, Linux, macOS, Containers, SaaS |
| **Data Sources** | Cloud Service: Cloud Service Modification, Application Log: Application Log Content, Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow, File: File Creation, Network Traffic: Network Connection Creation, Sensor Health: Host Status, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1496](https://attack.mitre.org/techniques/T1496) |

# Resource Hijacking (attack-pattern--cd25c1b4-935c-4f0e-ba8d-552f28bc4783)

## Description
Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. 

Resource hijacking may take a number of different forms. For example, adversaries may:

* Leverage compute resources in order to mine cryptocurrency
* Sell network bandwidth to proxy networks
* Generate SMS traffic for profit
* Abuse cloud-based messaging services to send large quantities of spam messages

In some cases, adversaries may leverage multiple types of Resource Hijacking at once.(Citation: Sysdig Cryptojacking Proxyjacking 2023)

## Detection
Consider monitoring process resource usage to determine anomalous activity associated with malicious hijacking of computer resources such as CPU, memory, and graphics processing resources. Monitor for suspicious use of network resources associated with cryptocurrency mining software. Monitor for common cryptomining software process names and files on local systems that may indicate compromise and resource usage.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1496)
- [Sysdig Cryptojacking Proxyjacking 2023](https://sysdig.com/blog/labrat-cryptojacking-proxyjacking-campaign/)
