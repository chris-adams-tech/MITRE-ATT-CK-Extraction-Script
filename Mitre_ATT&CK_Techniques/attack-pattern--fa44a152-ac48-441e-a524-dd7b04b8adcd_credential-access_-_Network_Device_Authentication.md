---
data_sources:
- 'File: File Modification'
id: attack-pattern--fa44a152-ac48-441e-a524-dd7b04b8adcd
mitre_attack_url: https://attack.mitre.org/techniques/T1556/004
name: Network Device Authentication
platforms:
- Network
tactics:
- credential-access
- defense-evasion
- persistence
title: credential-access - Network Device Authentication
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, defense-evasion, persistence |
| **Platforms** | Network |
| **Data Sources** | File: File Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1556/004](https://attack.mitre.org/techniques/T1556/004) |

# Network Device Authentication (attack-pattern--fa44a152-ac48-441e-a524-dd7b04b8adcd)

## Description
Adversaries may use [Patch System Image](https://attack.mitre.org/techniques/T1601/001) to hard code a password in the operating system, thus bypassing of native authentication mechanisms for local accounts on network devices.

[Modify System Image](https://attack.mitre.org/techniques/T1601) may include implanted code to the operating system for network devices to provide access for adversaries using a specific password.  The modification includes a specific password which is implanted in the operating system image via the patch.  Upon authentication attempts, the inserted code will first check to see if the user input is the password. If so, access is granted. Otherwise, the implanted code will pass the credentials on for verification of potentially valid credentials.(Citation: Mandiant - Synful Knock)

## Detection
Consider verifying the checksum of the operating system file and verifying the image of the operating system in memory.(Citation: Cisco IOS Software Integrity Assurance - Image File Verification)(Citation: Cisco IOS Software Integrity Assurance - Run-Time Memory Verification)

Detection of this behavior may be difficult, detection efforts may be focused on closely related adversary behaviors, such as [Modify System Image](https://attack.mitre.org/techniques/T1601).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1556/004)
- [Mandiant - Synful Knock](https://www.mandiant.com/resources/synful-knock-acis)
- [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)
- [Cisco IOS Software Integrity Assurance - Run-Time Memory Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#13)
