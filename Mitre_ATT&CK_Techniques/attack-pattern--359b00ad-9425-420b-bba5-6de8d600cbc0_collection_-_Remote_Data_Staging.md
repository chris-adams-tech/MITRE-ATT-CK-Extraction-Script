---
contributors:
- Praetorian
data_sources:
- 'File: File Creation'
- 'Command: Command Execution'
- 'File: File Access'
id: attack-pattern--359b00ad-9425-420b-bba5-6de8d600cbc0
mitre_attack_url: https://attack.mitre.org/techniques/T1074/002
name: Remote Data Staging
platforms:
- Windows
- IaaS
- Linux
- macOS
tactics:
- collection
title: collection - Remote Data Staging
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Data Sources** | File: File Creation, Command: Command Execution, File: File Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1074/002](https://attack.mitre.org/techniques/T1074/002) |

# Remote Data Staging (attack-pattern--359b00ad-9425-420b-bba5-6de8d600cbc0)

## Description
Adversaries may stage data collected from multiple systems in a central location or directory on one system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and stage data in that instance.(Citation: Mandiant M-Trends 2020)

By staging data on one system prior to Exfiltration, adversaries can minimize the number of connections made to their C2 server and better evade detection.

## Detection
Processes that appear to be reading files from disparate locations and writing them to the same directory or file may be an indication of data being staged, especially if they are suspected of performing encryption or compression on the files, such as 7zip, RAR, ZIP, or zlib. Monitor publicly writeable directories, central locations, and commonly used staging directories (recycle bin, temp folders, etc.) to regularly check for compressed or encrypted data that may be indicative of staging.

Monitor processes and command-line arguments for actions that could be taken to collect and combine files. Remote access tools with built-in features may interact directly with the Windows API to gather and copy to a location. Data may also be acquired and staged through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1074/002)
- [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
