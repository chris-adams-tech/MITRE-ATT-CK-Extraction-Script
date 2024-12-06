---
contributors:
- Mohamed Kmal
data_sources:
- 'User Account: User Account Authentication'
- 'Application Log: Application Log Content'
id: attack-pattern--1d24cdee-9ea2-4189-b08e-af110bf2435d
mitre_attack_url: https://attack.mitre.org/techniques/T1110/002
name: Password Cracking
platforms:
- Linux
- macOS
- Windows
- Network
- Office Suite
- Identity Provider
tactics:
- credential-access
title: credential-access - Password Cracking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS, Windows, Network, Office Suite, Identity Provider |
| **Data Sources** | User Account: User Account Authentication, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1110/002](https://attack.mitre.org/techniques/T1110/002) |

# Password Cracking (attack-pattern--1d24cdee-9ea2-4189-b08e-af110bf2435d)

## Description
Adversaries may use password cracking to attempt to recover usable credentials, such as plaintext passwords, when credential material such as password hashes are obtained. [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) can be used to obtain password hashes, this may only get an adversary so far when [Pass the Hash](https://attack.mitre.org/techniques/T1550/002) is not an option. Further,  adversaries may leverage [Data from Configuration Repository](https://attack.mitre.org/techniques/T1602) in order to obtain hashed credentials for network devices.(Citation: US-CERT-TA18-106A) 

Techniques to systematically guess the passwords used to compute hashes are available, or the adversary may use a pre-computed rainbow table to crack hashes. Cracking hashes is usually done on adversary-controlled systems outside of the target network.(Citation: Wikipedia Password cracking) The resulting plaintext password resulting from a successfully cracked hash may be used to log into systems, resources, and services in which the account has access.

## Detection
It is difficult to detect when hashes are cracked, since this is generally done outside the scope of the target network. Consider focusing efforts on detecting other adversary behavior used to acquire credential materials, such as [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) or [Kerberoasting](https://attack.mitre.org/techniques/T1558/003).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1110/002)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [Wikipedia Password cracking](https://en.wikipedia.org/wiki/Password_cracking)
