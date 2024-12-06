---
data_sources:
- 'File: File Metadata'
- 'Application Log: Application Log Content'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'File: File Modification'
- 'Firmware: Firmware Modification'
- 'Service: Service Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Script: Script Execution'
- 'User Account: User Account Creation'
- 'Process: OS API Execution'
- 'User Account: User Account Metadata'
- 'File: File Creation'
id: attack-pattern--22905430-4901-4c2a-84f6-98243cb173f8
mitre_attack_url: https://attack.mitre.org/techniques/T1564
name: Hide Artifacts
platforms:
- Linux
- macOS
- Windows
- Office Suite
tactics:
- defense-evasion
title: defense-evasion - Hide Artifacts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, Office Suite |
| **Data Sources** | File: File Metadata, Application Log: Application Log Content, Process: Process Creation, Command: Command Execution, File: File Modification, Firmware: Firmware Modification, Service: Service Creation, Windows Registry: Windows Registry Key Modification, Script: Script Execution, User Account: User Account Creation, Process: OS API Execution, User Account: User Account Metadata, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1564](https://attack.mitre.org/techniques/T1564) |

# Hide Artifacts (attack-pattern--22905430-4901-4c2a-84f6-98243cb173f8)

## Description
Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems may have features to hide various artifacts, such as important system files and administrative task execution, to avoid disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection.(Citation: Sofacy Komplex Trojan)(Citation: Cybereason OSX Pirrit)(Citation: MalwareBytes ADS July 2015)

Adversaries may also attempt to hide artifacts associated with malicious behavior by creating computing regions that are isolated from common security instrumentation, such as through the use of virtualization technology.(Citation: Sophos Ragnar May 2020)

## Detection
Monitor files, processes, and command-line arguments for actions indicative of hidden artifacts. Monitor event and authentication logs for records of hidden artifacts being used. Monitor the file system and shell commands for hidden attribute usage.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1564)
- [Cybereason OSX Pirrit](https://cdn2.hubspot.net/hubfs/3354902/Content%20PDFs/Cybereason-Lab-Analysis-OSX-Pirrit-4-6-16.pdf)
- [MalwareBytes ADS July 2015](https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/)
- [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
- [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
