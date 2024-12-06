---
contributors:
- Maril Vernon @shewhohacks
- Praetorian
- Austin Clark, @c2defense
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--354a7f88-63fb-41b5-a801-ce3b377b36f1
mitre_attack_url: https://attack.mitre.org/techniques/T1082
name: System Information Discovery
platforms:
- Windows
- IaaS
- Linux
- macOS
- Network
tactics:
- discovery
title: discovery - System Information Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, IaaS, Linux, macOS, Network |
| **Data Sources** | Process: OS API Execution, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1082](https://attack.mitre.org/techniques/T1082) |

# System Information Discovery (attack-pattern--354a7f88-63fb-41b5-a801-ce3b377b36f1)

## Description
An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use the information from [System Information Discovery](https://attack.mitre.org/techniques/T1082) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Tools such as [Systeminfo](https://attack.mitre.org/software/S0096) can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the <code>systemsetup</code> configuration tool on macOS. As an example, adversaries with user-level access can execute the <code>df -aH</code> command to obtain currently mounted disks and associated freely available space. Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to gather detailed system information (e.g. <code>show version</code>).(Citation: US-CERT-TA18-106A) [System Information Discovery](https://attack.mitre.org/techniques/T1082) combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.(Citation: OSX.FairyTale)(Citation: 20 macOS Common Tools and Techniques)

Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.(Citation: Amazon Describe Instance)(Citation: Google Instances Resource)(Citation: Microsoft Virutal Machine API)

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Further, [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands may also be used to gather  detailed system information with built-in features native to the network device platform.  Monitor CLI activity for unexpected or unauthorized use  commands being run by non-standard users from non-standard locations. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

In cloud-based systems, native logging can be used to identify access to certain APIs and dashboards that may contain system information. Depending on how the environment is used, that data alone may not be useful due to benign use during normal operations.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1082)
- [Amazon Describe Instance](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html)
- [Google Instances Resource](https://cloud.google.com/compute/docs/reference/rest/v1/instances)
- [Microsoft Virutal Machine API](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines/get)
- [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [OSX.FairyTale](https://www.sentinelone.com/blog/trail-osx-fairytale-adware-playing-malware/)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
