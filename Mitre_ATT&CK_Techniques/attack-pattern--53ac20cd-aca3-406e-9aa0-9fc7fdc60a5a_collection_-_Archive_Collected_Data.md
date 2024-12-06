---
data_sources:
- 'Command: Command Execution'
- 'Script: Script Execution'
- 'Process: Process Creation'
- 'File: File Creation'
id: attack-pattern--53ac20cd-aca3-406e-9aa0-9fc7fdc60a5a
mitre_attack_url: https://attack.mitre.org/techniques/T1560
name: Archive Collected Data
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
title: collection - Archive Collected Data
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Command: Command Execution, Script: Script Execution, Process: Process Creation, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1560](https://attack.mitre.org/techniques/T1560) |

# Archive Collected Data (attack-pattern--53ac20cd-aca3-406e-9aa0-9fc7fdc60a5a)

## Description
An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network.(Citation: DOJ GRU Indictment Jul 2018) Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

## Detection
Archival software and archived files can be detected in many ways. Common utilities that may be present on the system or brought in by an adversary may be detectable through process monitoring and monitoring for command-line arguments for known archival utilities. This may yield a significant number of benign events, depending on how systems in the environment are typically used.

A process that loads the Windows DLL crypt32.dll may be used to perform encryption, decryption, or verification of file signatures.

Consider detecting writing of files with extensions and/or headers associated with compressed or encrypted file types. Detection efforts may focus on follow-on exfiltration activity, where compressed or encrypted files can be detected in transit with a network intrusion detection or data loss prevention system analyzing file headers.(Citation: Wikipedia File Header Signatures)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1560)
- [DOJ GRU Indictment Jul 2018](https://www.justice.gov/file/1080281/download)
- [Wikipedia File Header Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
