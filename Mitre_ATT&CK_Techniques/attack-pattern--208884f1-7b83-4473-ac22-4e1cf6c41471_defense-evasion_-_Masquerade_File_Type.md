---
contributors:
- CrowdStrike Falcon OverWatch
- Ben Smith, @ezaspy
data_sources:
- 'File: File Modification'
- 'Command: Command Execution'
id: attack-pattern--208884f1-7b83-4473-ac22-4e1cf6c41471
mitre_attack_url: https://attack.mitre.org/techniques/T1036/008
name: Masquerade File Type
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Masquerade File Type
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Modification, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/008](https://attack.mitre.org/techniques/T1036/008) |

# Masquerade File Type (attack-pattern--208884f1-7b83-4473-ac22-4e1cf6c41471)

## Description
Adversaries may masquerade malicious payloads as legitimate files through changes to the payload's formatting, including the file’s signature, extension, and contents. Various file types have a typical standard format, including how they are encoded and organized. For example, a file’s signature (also known as header or magic bytes) is the beginning bytes of a file and is often used to identify the file’s type. For example, the header of a JPEG file,  is <code> 0xFF 0xD8</code> and the file extension is either `.JPE`, `.JPEG` or `.JPG`. 

Adversaries may edit the header’s hex code and/or the file extension of a malicious payload in order to bypass file validation checks and/or input sanitization. This behavior is commonly used when payload files are transferred (e.g., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) and stored (e.g., [Upload Malware](https://attack.mitre.org/techniques/T1608/001)) so that adversaries may move their malware without triggering detections. 

Common non-executable file types and extensions, such as text files (`.txt`) and image files (`.jpg`, `.gif`, etc.) may be typically treated as benign.  Based on this, adversaries may use a file extension to disguise malware, such as naming a PHP backdoor code with a file name of <code>test.gif</code>. A user may not know that a file is malicious due to the benign appearance and file extension.

Polygot files, which are files that have multiple different file types and that function differently based on the application that will execute them, may also be used to disguise malicious malware and capabilities.(Citation: polygot_icedID)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/008)
- [polygot_icedID](https://unit42.paloaltonetworks.com/polyglot-file-icedid-payload)
