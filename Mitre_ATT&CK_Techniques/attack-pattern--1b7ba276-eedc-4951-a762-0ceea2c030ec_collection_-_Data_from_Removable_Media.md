---
contributors:
- William Cain
data_sources:
- 'Command: Command Execution'
- 'File: File Access'
id: attack-pattern--1b7ba276-eedc-4951-a762-0ceea2c030ec
mitre_attack_url: https://attack.mitre.org/techniques/T1025
name: Data from Removable Media
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
title: collection - Data from Removable Media
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Command: Command Execution, File: File Access |
| **System Requirements** | Privileges to access removable media drive and files |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1025](https://attack.mitre.org/techniques/T1025) |

# Data from Removable Media (attack-pattern--1b7ba276-eedc-4951-a762-0ceea2c030ec)

## Description
Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [cmd](https://attack.mitre.org/software/S0106) may be used to gather information. 

Some adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on removable media.

## Detection
Monitor processes and command-line arguments for actions that could be taken to collect files from a system's connected removable media. Remote access tools with built-in features may interact directly with the Windows API to gather data. Data may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1025)
