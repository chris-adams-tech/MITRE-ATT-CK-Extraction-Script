---
data_sources:
- 'File: File Access'
- 'Command: Command Execution'
- 'Process: Process Access'
- 'Cloud Service: Cloud Service Enumeration'
- 'Process: Process Creation'
- 'Process: OS API Execution'
id: attack-pattern--3fc9b85a-2862-4363-a64d-d692e3ffbee0
mitre_attack_url: https://attack.mitre.org/techniques/T1555
name: Credentials from Password Stores
platforms:
- Linux
- macOS
- Windows
- IaaS
tactics:
- credential-access
title: credential-access - Credentials from Password Stores
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS, Windows, IaaS |
| **Data Sources** | File: File Access, Command: Command Execution, Process: Process Access, Cloud Service: Cloud Service Enumeration, Process: Process Creation, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1555](https://attack.mitre.org/techniques/T1555) |

# Credentials from Password Stores (attack-pattern--3fc9b85a-2862-4363-a64d-d692e3ffbee0)

## Description
Adversaries may search for common password storage locations to obtain user credentials.(Citation: F-Secure The Dukes) Passwords are stored in several places on a system, depending on the operating system or application holding the credentials. There are also specific applications and services that store passwords to make them easier for users to manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Detection
Monitor system calls, file read events, and processes for suspicious activity that could indicate searching for a password  or other activity related to performing keyword searches (e.g. password, pwd, login, store, secure, credentials, etc.) in process memory for credentials. File read events should be monitored surrounding known password storage applications.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1555)
- [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
