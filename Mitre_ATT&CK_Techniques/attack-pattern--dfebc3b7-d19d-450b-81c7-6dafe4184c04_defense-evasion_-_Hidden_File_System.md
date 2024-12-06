---
data_sources:
- 'Firmware: Firmware Modification'
- 'File: File Modification'
- 'Windows Registry: Windows Registry Key Modification'
id: attack-pattern--dfebc3b7-d19d-450b-81c7-6dafe4184c04
mitre_attack_url: https://attack.mitre.org/techniques/T1564/005
name: Hidden File System
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Hidden File System
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Firmware: Firmware Modification, File: File Modification, Windows Registry: Windows Registry Key Modification |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1564/005](https://attack.mitre.org/techniques/T1564/005) |

# Hidden File System (attack-pattern--dfebc3b7-d19d-450b-81c7-6dafe4184c04)

## Description
Adversaries may use a hidden file system to conceal malicious activity from users and security tools. File systems provide a structure to store and access data from physical storage. Typically, a user engages with a file system through applications that allow them to access files and directories, which are an abstraction from their physical location (ex: disk sector). Standard file systems include FAT, NTFS, ext4, and APFS. File systems can also contain other structures, such as the Volume Boot Record (VBR) and Master File Table (MFT) in NTFS.(Citation: MalwareTech VFS Nov 2014)

Adversaries may use their own abstracted file system, separate from the standard file system present on the infected system. In doing so, adversaries can hide the presence of malicious components and file input/output from security tools. Hidden file systems, sometimes referred to as virtual file systems, can be implemented in numerous ways. One implementation would be to store a file system in reserved disk space unused by disk structures or standard file system partitions.(Citation: MalwareTech VFS Nov 2014)(Citation: FireEye Bootkits) Another implementation could be for an adversary to drop their own portable partition image as a file on top of the standard file system.(Citation: ESET ComRAT May 2020) Adversaries may also fragment files across the existing file system structure in non-standard ways.(Citation: Kaspersky Equation QA)

## Detection
Detecting the use of a hidden file system may be exceptionally difficult depending on the implementation. Emphasis may be placed on detecting related aspects of the adversary lifecycle, such as how malware interacts with the hidden file system or how a hidden file system is loaded. Consider looking for anomalous interactions with the Registry or with a particular file on disk. Likewise, if the hidden file system is loaded on boot from reserved disk space, consider shifting focus to detecting [Bootkit](https://attack.mitre.org/techniques/T1542/003) activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1564/005)
- [MalwareTech VFS Nov 2014](https://www.malwaretech.com/2014/11/virtual-file-systems-for-beginners.html)
- [FireEye Bootkits](https://www.fireeye.com/blog/threat-research/2015/12/fin1-targets-boot-record.html)
- [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Kaspersky Equation QA](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064459/Equation_group_questions_and_answers.pdf)
