---
contributors:
- Austin Clark, @c2defense
data_sources:
- 'Command: Command Execution'
- 'Script: Script Execution'
- 'Process: Process Creation'
- 'Process: OS API Execution'
id: attack-pattern--707399d6-ab3e-4963-9315-d9d3818cd6a0
mitre_attack_url: https://attack.mitre.org/techniques/T1016
name: System Network Configuration Discovery
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- discovery
title: discovery - System Network Configuration Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Command: Command Execution, Script: Script Execution, Process: Process Creation, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1016](https://attack.mitre.org/techniques/T1016) |

# System Network Configuration Discovery (attack-pattern--707399d6-ab3e-4963-9315-d9d3818cd6a0)

## Description
Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of systems they access or through information discovery of remote systems. Several operating system administration utilities exist that can be used to gather this information. Examples include [Arp](https://attack.mitre.org/software/S0099), [ipconfig](https://attack.mitre.org/software/S0100)/[ifconfig](https://attack.mitre.org/software/S0101), [nbtstat](https://attack.mitre.org/software/S0102), and [route](https://attack.mitre.org/software/S0103).

Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes (e.g. <code>show ip route</code>, <code>show ip interface</code>).(Citation: US-CERT-TA18-106A)(Citation: Mandiant APT41 Global Intrusion )

Adversaries may use the information from [System Network Configuration Discovery](https://attack.mitre.org/techniques/T1016) during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next. 

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Further, {{LinkById|T1059.008} commands may also be used to gather system and network information with built-in features native to the network device platform.  Monitor CLI activity for unexpected or unauthorized use  commands being run by non-standard users from non-standard locations.  Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1016)
- [Mandiant APT41 Global Intrusion ](https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
