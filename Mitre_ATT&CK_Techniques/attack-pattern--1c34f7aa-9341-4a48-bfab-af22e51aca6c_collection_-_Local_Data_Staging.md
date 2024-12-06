---
contributors:
- Massimiliano Romano, BT Security
data_sources:
- 'File: File Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'File: File Access'
- 'Command: Command Execution'
id: attack-pattern--1c34f7aa-9341-4a48-bfab-af22e51aca6c
mitre_attack_url: https://attack.mitre.org/techniques/T1074/001
name: Local Data Staging
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
title: collection - Local Data Staging
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Creation, Windows Registry: Windows Registry Key Modification, File: File Access, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1074/001](https://attack.mitre.org/techniques/T1074/001) |

# Local Data Staging (attack-pattern--1c34f7aa-9341-4a48-bfab-af22e51aca6c)

## Description
Adversaries may stage collected data in a central location or directory on the local system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.

Adversaries may also stage collected data in various available formats/locations of a system, including local storage databases/repositories or the Windows Registry.(Citation: Prevailion DarkWatchman 2021)

## Detection
Processes that appear to be reading files from disparate locations and writing them to the same directory or file may be an indication of data being staged, especially if they are suspected of performing encryption or compression on the files, such as 7zip, RAR, ZIP, or zlib. Monitor publicly writeable directories, central locations, and commonly used staging directories (recycle bin, temp folders, etc.) to regularly check for compressed or encrypted data that may be indicative of staging.

Monitor processes and command-line arguments for actions that could be taken to collect and combine files. Remote access tools with built-in features may interact directly with the Windows API to gather and copy to a location. Data may also be acquired and staged through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

Consider monitoring accesses and modifications to local storage repositories (such as the Windows Registry), especially from suspicious processes that could be related to malicious data collection.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1074/001)
- [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
