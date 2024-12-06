---
contributors:
- Praetorian
- Arun Seelagan, CISA
data_sources:
- 'User Account: User Account Authentication'
- 'Command: Command Execution'
- 'File: File Access'
- 'Script: Script Execution'
id: attack-pattern--30208d3e-0d6b-43c8-883e-44462a514619
mitre_attack_url: https://attack.mitre.org/techniques/T1119
name: Automated Collection
platforms:
- Linux
- macOS
- Windows
- IaaS
- SaaS
- Office Suite
tactics:
- collection
title: collection - Automated Collection
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows, IaaS, SaaS, Office Suite |
| **Data Sources** | User Account: User Account Authentication, Command: Command Execution, File: File Access, Script: Script Execution |
| **System Requirements** | Permissions to access directories, files, and API endpoints that store information of interest. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1119](https://attack.mitre.org/techniques/T1119) |

# Automated Collection (attack-pattern--30208d3e-0d6b-43c8-883e-44462a514619)

## Description
Once established within a system or network, an adversary may use automated techniques for collecting internal data. Methods for performing this technique could include use of a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals. 

In cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract, transform, and load (ETL) services to automatically collect data.(Citation: Mandiant UNC3944 SMS Phishing 2023) 

This functionality could also be built into remote access tools. 

This technique may incorporate use of other techniques such as [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) and [Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570) to identify and move files, as well as [Cloud Service Dashboard](https://attack.mitre.org/techniques/T1538) and [Cloud Storage Object Discovery](https://attack.mitre.org/techniques/T1619) to identify resources in cloud environments.

## Detection
Depending on the method used, actions could include common file system commands and parameters on the command-line interface within batch files or scripts. A sequence of actions like this may be unusual, depending on the system and network environment. Automated collection may occur along with other techniques such as [Data Staged](https://attack.mitre.org/techniques/T1074). As such, file access monitoring that shows an unusual process performing sequential file opens and potentially copy actions to another location on the file system for many files at once may indicate automated collection behavior. Remote access tools with built-in features may interact directly with the Windows API to gather data. Data may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001), as well as through cloud APIs and command line interfaces.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1119)
- [Mandiant UNC3944 SMS Phishing 2023](https://www.mandiant.com/resources/blog/unc3944-sms-phishing-sim-swapping-ransomware)
