---
contributors:
- Ed Williams, Trustwave, SpiderLabs
- Olaf Hartong, Falcon Force
data_sources:
- 'Command: Command Execution'
- 'File: File Access'
- 'Windows Registry: Windows Registry Key Access'
- 'File: File Creation'
id: attack-pattern--1644e709-12d2-41e5-a60f-3470991f5011
mitre_attack_url: https://attack.mitre.org/techniques/T1003/002
name: Security Account Manager
platforms:
- Windows
tactics:
- credential-access
title: credential-access - Security Account Manager
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, File: File Access, Windows Registry: Windows Registry Key Access, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1003/002](https://attack.mitre.org/techniques/T1003/002) |

# Security Account Manager (attack-pattern--1644e709-12d2-41e5-a60f-3470991f5011)

## Description
Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found with the <code>net user</code> command. Enumerating the SAM database requires SYSTEM level access.

A number of tools can be used to retrieve the SAM file through in-memory techniques:

* pwdumpx.exe
* [gsecdump](https://attack.mitre.org/software/S0008)
* [Mimikatz](https://attack.mitre.org/software/S0002)
* secretsdump.py

Alternatively, the SAM can be extracted from the Registry with Reg:

* <code>reg save HKLM\sam sam</code>
* <code>reg save HKLM\system system</code>

Creddump7 can then be used to process the SAM database locally to retrieve hashes.(Citation: GitHub Creddump7)

Notes: 

* RID 500 account is the local, built-in administrator.
* RID 501 is the guest account.
* User accounts start with a RID of 1,000+.


## Detection
Hash dumpers open the Security Accounts Manager (SAM) on the local file system (<code>%SystemRoot%/system32/config/SAM</code>) or create a dump of the Registry SAM key to access stored account password hashes. Some hash dumpers will open the local file system as a device and parse to the SAM table to avoid file access defenses. Others will make an in-memory copy of the SAM table before reading hashes. Detection of compromised [Valid Accounts](https://attack.mitre.org/techniques/T1078) in-use by adversaries may help as well.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1003/002)
- [GitHub Creddump7](https://github.com/Neohapsis/creddump7)
