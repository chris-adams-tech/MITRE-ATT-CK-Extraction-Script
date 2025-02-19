---
contributors:
- Mayan Arora aka Mayan Mohan
- Mark Wee
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'File: File Creation'
id: attack-pattern--00f90846-cbd1-4fc5-9233-df5c2bf2a662
mitre_attack_url: https://attack.mitre.org/techniques/T1560/001
name: Archive via Utility
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
title: collection - Archive via Utility
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1560/001](https://attack.mitre.org/techniques/T1560/001) |

# Archive via Utility (attack-pattern--00f90846-cbd1-4fc5-9233-df5c2bf2a662)

## Description
Adversaries may use utilities to compress and/or encrypt collected data prior to exfiltration. Many utilities include functionalities to compress, encrypt, or otherwise package data into a format that is easier/more secure to transport.

Adversaries may abuse various utilities to compress or encrypt data before exfiltration. Some third party utilities may be preinstalled, such as <code>tar</code> on Linux and macOS or <code>zip</code> on Windows systems. 

On Windows, <code>diantz</code> or <code> makecab</code> may be used to package collected files into a cabinet (.cab) file. <code>diantz</code> may also be used to download and compress files from remote locations (i.e. [Remote Data Staging](https://attack.mitre.org/techniques/T1074/002)).(Citation: diantz.exe_lolbas) <code>xcopy</code> on Windows can copy files and directories with a variety of options. Additionally, adversaries may use [certutil](https://attack.mitre.org/software/S0160) to Base64 encode collected data before exfiltration. 

Adversaries may use also third party utilities, such as 7-Zip, WinRAR, and WinZip, to perform similar activities.(Citation: 7zip Homepage)(Citation: WinRAR Homepage)(Citation: WinZip Homepage)

## Detection
Common utilities that may be present on the system or brought in by an adversary may be detectable through process monitoring and monitoring for command-line arguments for known archival utilities. This may yield a significant number of benign events, depending on how systems in the environment are typically used.

Consider detecting writing of files with extensions and/or headers associated with compressed or encrypted file types. Detection efforts may focus on follow-on exfiltration activity, where compressed or encrypted files can be detected in transit with a network intrusion detection or data loss prevention system analyzing file headers.(Citation: Wikipedia File Header Signatures)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1560/001)
- [WinRAR Homepage](https://www.rarlab.com/)
- [WinZip Homepage](https://www.winzip.com/win/en/)
- [7zip Homepage](https://www.7-zip.org/)
- [diantz.exe_lolbas](https://lolbas-project.github.io/lolbas/Binaries/Diantz/)
- [Wikipedia File Header Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
