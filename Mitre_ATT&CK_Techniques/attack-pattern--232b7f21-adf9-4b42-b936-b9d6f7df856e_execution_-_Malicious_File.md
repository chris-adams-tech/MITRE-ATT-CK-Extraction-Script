---
contributors:
- TruKno
data_sources:
- 'Process: Process Creation'
- 'File: File Creation'
id: attack-pattern--232b7f21-adf9-4b42-b936-b9d6f7df856e
mitre_attack_url: https://attack.mitre.org/techniques/T1204/002
name: Malicious File
platforms:
- Linux
- macOS
- Windows
tactics:
- execution
title: execution - Malicious File
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Creation, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1204/002](https://attack.mitre.org/techniques/T1204/002) |

# Malicious File (attack-pattern--232b7f21-adf9-4b42-b936-b9d6f7df856e)

## Description
An adversary may rely upon a user opening a malicious file in order to gain execution. Users may be subjected to social engineering to get them to open a file that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001). Adversaries may use several types of files that require a user to execute them, including .doc, .pdf, .xls, .rtf, .scr, .exe, .lnk, .pif, .cpl, and .reg.

Adversaries may employ various forms of [Masquerading](https://attack.mitre.org/techniques/T1036) and [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027) to increase the likelihood that a user will open and successfully execute a malicious file. These methods may include using a familiar naming convention and/or password protecting the file and supplying instructions to a user on how to open it.(Citation: Password Protected Word Docs) 

While [Malicious File](https://attack.mitre.org/techniques/T1204/002) frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [Internal Spearphishing](https://attack.mitre.org/techniques/T1534).

## Detection
Monitor the execution of and command-line arguments for applications that may be used by an adversary to gain initial access that require user interaction. This includes compression applications, such as those for zip files, that can be used to [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140) in payloads.

Anti-virus can potentially detect malicious documents and files that are downloaded and executed on the user's computer. Endpoint sensing or network sensing can potentially detect malicious events once the file is opened (such as a Microsoft Word document or PDF reaching out to the internet or spawning powershell.exe).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1204/002)
- [Password Protected Word Docs](https://www.bleepingcomputer.com/news/security/psa-dont-open-spam-containing-password-protected-word-docs/)
