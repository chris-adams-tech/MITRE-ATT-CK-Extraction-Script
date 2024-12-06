---
contributors:
- Matt Burrough, @mattburrough, Microsoft
data_sources:
- 'Process: Process Access'
- 'Process: OS API Execution'
- 'File: File Access'
- 'Command: Command Execution'
id: attack-pattern--315f51f0-6b03-4c1e-bfb2-84740afb8e21
mitre_attack_url: https://attack.mitre.org/techniques/T1555/005
name: Password Managers
platforms:
- Linux
- macOS
- Windows
tactics:
- credential-access
title: credential-access - Password Managers
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Access, Process: OS API Execution, File: File Access, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1555/005](https://attack.mitre.org/techniques/T1555/005) |

# Password Managers (attack-pattern--315f51f0-6b03-4c1e-bfb2-84740afb8e21)

## Description
Adversaries may acquire user credentials from third-party password managers.(Citation: ise Password Manager February 2019) Password managers are applications designed to store user credentials, normally in an encrypted database. Credentials are typically accessible after a user provides a master password that unlocks the database. After the database is unlocked, these credentials may be copied to memory. These databases can be stored as files on disk.(Citation: ise Password Manager February 2019)

Adversaries may acquire user credentials from password managers by extracting the master password and/or plain-text credentials from memory.(Citation: FoxIT Wocao December 2019)(Citation: Github KeeThief) Adversaries may extract credentials from memory via [Exploitation for Credential Access](https://attack.mitre.org/techniques/T1212).(Citation: NVD CVE-2019-3610)
 Adversaries may also try brute forcing via [Password Guessing](https://attack.mitre.org/techniques/T1110/001) to obtain the master password of a password manager.(Citation: Cyberreason Anchor December 2019)

## Detection
Consider monitoring API calls, file read events, and processes for suspicious activity that could indicate searching in process memory of password managers. 

Consider monitoring file reads surrounding known password manager applications.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1555/005)
- [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [FoxIT Wocao December 2019](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [ise Password Manager February 2019](https://www.ise.io/casestudies/password-manager-hacking/)
- [Github KeeThief](https://github.com/GhostPack/KeeThief)
- [NVD CVE-2019-3610](https://nvd.nist.gov/vuln/detail/CVE-2019-3610)
