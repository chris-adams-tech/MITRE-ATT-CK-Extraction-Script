---
contributors:
- Michal Dida, ESET
- David Routin
data_sources:
- 'Network Share: Network Share Access'
- 'Process: Process Creation'
- 'File: File Modification'
- 'File: File Creation'
id: attack-pattern--246fd3c7-f5e3-466d-8787-4c13d9e3b61c
mitre_attack_url: https://attack.mitre.org/techniques/T1080
name: Taint Shared Content
platforms:
- Windows
- SaaS
- Linux
- macOS
- Office Suite
tactics:
- lateral-movement
title: lateral-movement - Taint Shared Content
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows, SaaS, Linux, macOS, Office Suite |
| **Data Sources** | Network Share: Network Share Access, Process: Process Creation, File: File Modification, File: File Creation |
| **System Requirements** | Access to shared folders and content with write permissions |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1080](https://attack.mitre.org/techniques/T1080) |

# Taint Shared Content (attack-pattern--246fd3c7-f5e3-466d-8787-4c13d9e3b61c)

## Description

Adversaries may deliver payloads to remote systems by adding content to shared storage locations, such as network drives or internal code repositories. Content stored on network drives or in other shared locations may be tainted by adding malicious programs, scripts, or exploit code to otherwise valid files. Once a user opens the shared tainted content, the malicious portion can be executed to run the adversary's code on a remote system. Adversaries may use tainted shared content to move laterally.

A directory share pivot is a variation on this technique that uses several other techniques to propagate malware when users access a shared network directory. It uses [Shortcut Modification](https://attack.mitre.org/techniques/T1547/009) of directory .LNK files that use [Masquerading](https://attack.mitre.org/techniques/T1036) to look like the real directories, which are hidden through [Hidden Files and Directories](https://attack.mitre.org/techniques/T1564/001). The malicious .LNK-based directories have an embedded command that executes the hidden malware file in the directory and then opens the real intended directory so that the user's expected action still occurs. When used with frequently used network directories, the technique may result in frequent reinfections and broad access to systems and potentially to new and higher privileged accounts. (Citation: Retwin Directory Share Pivot)

Adversaries may also compromise shared network directories through binary infections by appending or prepending its code to the healthy binary on the shared network directory. The malware may modify the original entry point (OEP) of the healthy binary to ensure that it is executed before the legitimate code. The infection could continue to spread via the newly infected file when it is executed by a remote system. These infections may target both binary and non-binary formats that end with extensions including, but not limited to, .EXE, .DLL, .SCR, .BAT, and/or .VBS.

## Detection
Processes that write or overwrite many files to a network shared directory may be suspicious. Monitor processes that are executed from removable media for malicious or abnormal activity such as network connections due to Command and Control and possible network Discovery techniques.

Frequently scan shared network directories for malicious files, hidden files, .LNK files, and other file types that may not typical exist in directories used to share specific types of content.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1080)
- [Retwin Directory Share Pivot](https://rewtin.blogspot.ch/2017/11/abusing-user-shares-for-efficient.html)
