---
contributors:
- Shailesh Tiwary (Indian Army)
data_sources:
- 'Named Pipe: Named Pipe Metadata'
- 'Network Share: Network Share Access'
- 'Network Traffic: Network Traffic Flow'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'File: File Creation'
- 'Network Traffic: Network Traffic Content'
- 'File: File Metadata'
id: attack-pattern--bf90d72c-c00b-45e3-b3aa-68560560d4c5
mitre_attack_url: https://attack.mitre.org/techniques/T1570
name: Lateral Tool Transfer
platforms:
- Linux
- macOS
- Windows
tactics:
- lateral-movement
title: lateral-movement - Lateral Tool Transfer
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Named Pipe: Named Pipe Metadata, Network Share: Network Share Access, Network Traffic: Network Traffic Flow, Command: Command Execution, Process: Process Creation, File: File Creation, Network Traffic: Network Traffic Content, File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1570](https://attack.mitre.org/techniques/T1570) |

# Lateral Tool Transfer (attack-pattern--bf90d72c-c00b-45e3-b3aa-68560560d4c5)

## Description
Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.

Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) to connected network shares or with authenticated connections via [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001).(Citation: Unit42 LockerGoga 2019)

Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and [ftp](https://attack.mitre.org/software/S0095). In some cases, adversaries may be able to leverage [Web Service](https://attack.mitre.org/techniques/T1102)s such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.(Citation: Dropbox Malware Sync)

## Detection
Monitor for file creation and files transferred within a network using protocols such as SMB or FTP. Unusual processes with internal network connections creating files on-system may be suspicious. Consider monitoring for abnormal usage of utilities and command-line arguments that may be used in support of remote transfer of files. Considering monitoring for alike file hashes or characteristics (ex: filename) that are created on multiple hosts.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1570)
- [Dropbox Malware Sync](https://www.technologyreview.com/2013/08/21/83143/dropbox-and-similar-services-can-sync-malware/)
- [Unit42 LockerGoga 2019](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)
