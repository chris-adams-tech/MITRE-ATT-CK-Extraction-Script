---
contributors:
- Ed Williams, Trustwave, SpiderLabs
data_sources:
- 'Command: Command Execution'
- 'File: File Access'
id: attack-pattern--edf91964-b26e-4b4a-9600-ccacd7d7df24
mitre_attack_url: https://attack.mitre.org/techniques/T1003/003
name: NTDS
platforms:
- Windows
tactics:
- credential-access
title: credential-access - NTDS
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, File: File Access |
| **System Requirements** | Access to Domain Controller or backup |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1003/003](https://attack.mitre.org/techniques/T1003/003) |

# NTDS (attack-pattern--edf91964-b26e-4b4a-9600-ccacd7d7df24)

## Description
Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal credential information, as well as obtain other information about domain members such as devices, users, and access rights. By default, the NTDS file (NTDS.dit) is located in <code>%SystemRoot%\NTDS\Ntds.dit</code> of a domain controller.(Citation: Wikipedia Active Directory)

In addition to looking for NTDS files on active Domain Controllers, adversaries may search for backups that contain the same or similar information.(Citation: Metcalf 2015)

The following tools and techniques can be used to enumerate the NTDS file and the contents of the entire Active Directory hashes.

* Volume Shadow Copy
* secretsdump.py
* Using the in-built Windows tool, ntdsutil.exe
* Invoke-NinjaCopy


## Detection
Monitor processes and command-line arguments for program execution that may be indicative of credential dumping, especially attempts to access or copy the NTDS.dit.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1003/003)
- [Metcalf 2015](http://adsecurity.org/?p=1275)
- [Wikipedia Active Directory](https://en.wikipedia.org/wiki/Active_Directory)
