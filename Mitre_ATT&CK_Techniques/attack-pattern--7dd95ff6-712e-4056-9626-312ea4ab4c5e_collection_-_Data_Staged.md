---
contributors:
- Praetorian
- Shane Tully, @securitygypsy
data_sources:
- 'File: File Access'
- 'File: File Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
id: attack-pattern--7dd95ff6-712e-4056-9626-312ea4ab4c5e
mitre_attack_url: https://attack.mitre.org/techniques/T1074
name: Data Staged
platforms:
- Windows
- IaaS
- Linux
- macOS
tactics:
- collection
title: collection - Data Staged
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Data Sources** | File: File Access, File: File Creation, Windows Registry: Windows Registry Key Modification, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1074](https://attack.mitre.org/techniques/T1074) |

# Data Staged (attack-pattern--7dd95ff6-712e-4056-9626-312ea4ab4c5e)

## Description
Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.(Citation: PWC Cloud Hopper April 2017)

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and stage data in that instance.(Citation: Mandiant M-Trends 2020)

Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.

## Detection
Processes that appear to be reading files from disparate locations and writing them to the same directory or file may be an indication of data being staged, especially if they are suspected of performing encryption or compression on the files, such as 7zip, RAR, ZIP, or zlib. Monitor publicly writeable directories, central locations, and commonly used staging directories (recycle bin, temp folders, etc.) to regularly check for compressed or encrypted data that may be indicative of staging.

Monitor processes and command-line arguments for actions that could be taken to collect and combine files. Remote access tools with built-in features may interact directly with the Windows API to gather and copy to a location. Data may also be acquired and staged through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

Consider monitoring accesses and modifications to storage repositories (such as the Windows Registry), especially from suspicious processes that could be related to malicious data collection.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1074)
- [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
- [PWC Cloud Hopper April 2017](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)
