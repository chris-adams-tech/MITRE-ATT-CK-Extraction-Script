---
contributors:
- Praetorian
- Austin Clark, @c2defense
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--7e150503-88e7-4861-866b-ff1ac82c4475
mitre_attack_url: https://attack.mitre.org/techniques/T1049
name: System Network Connections Discovery
platforms:
- Windows
- IaaS
- Linux
- macOS
- Network
tactics:
- discovery
title: discovery - System Network Connections Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, IaaS, Linux, macOS, Network |
| **Data Sources** | Process: OS API Execution, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1049](https://attack.mitre.org/techniques/T1049) |

# System Network Connections Discovery (attack-pattern--7e150503-88e7-4861-866b-ff1ac82c4475)

## Description
Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network. 

An adversary who gains access to a system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine what systems and services are connected. The actions performed are likely the same types of discovery techniques depending on the operating system, but the resulting information may include details about the networked cloud environment relevant to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate.(Citation: Amazon AWS VPC Guide)(Citation: Microsoft Azure Virtual Network Overview)(Citation: Google VPC Overview) Similarly, adversaries who gain access to network devices may also perform similar discovery activities to gather information about connected systems and services.

Utilities and commands that acquire this information include [netstat](https://attack.mitre.org/software/S0104), "net use," and "net session" with [Net](https://attack.mitre.org/software/S0039). In Mac and Linux, [netstat](https://attack.mitre.org/software/S0104) and <code>lsof</code> can be used to list current connections. <code>who -a</code> and <code>w</code> can be used to show which users are currently logged in, similar to "net session". Additionally, built-in features native to network devices and [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) may be used (e.g. <code>show ip sockets</code>, <code>show tcp brief</code>).(Citation: US-CERT-TA18-106A)

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Further, [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands may also be used to gather system and network information with built-in features native to the network device platform.  Monitor CLI activity for unexpected or unauthorized use commands being run by non-standard users from non-standard locations. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1049)
- [Amazon AWS VPC Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Microsoft Azure Virtual Network Overview](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Google VPC Overview](https://cloud.google.com/vpc/docs/vpc)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
