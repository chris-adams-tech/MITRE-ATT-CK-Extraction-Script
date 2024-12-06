---
data_sources:
- 'Command: Command Execution'
- 'Process: Process Access'
id: attack-pattern--1a80d097-54df-41d8-9d33-34e755ec5e72
mitre_attack_url: https://attack.mitre.org/techniques/T1555/002
name: Securityd Memory
platforms:
- Linux
- macOS
tactics:
- credential-access
title: credential-access - Securityd Memory
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS |
| **Data Sources** | Command: Command Execution, Process: Process Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1555/002](https://attack.mitre.org/techniques/T1555/002) |

# Securityd Memory (attack-pattern--1a80d097-54df-41d8-9d33-34e755ec5e72)

## Description
An adversary with root access may gather credentials by reading `securityd`’s memory. `securityd` is a service/daemon responsible for implementing security protocols such as encryption and authorization.(Citation: Apple Dev SecurityD) A privileged adversary may be able to scan through `securityd`'s memory to find the correct sequence of keys to decrypt the user’s logon keychain. This may provide the adversary with various plaintext passwords, such as those for users, WiFi, mail, browsers, certificates, secure notes, etc.(Citation: OS X Keychain)(Citation: OSX Keydnap malware)

In OS X prior to El Capitan, users with root access can read plaintext keychain passwords of logged-in users because Apple’s keychain implementation allows these credentials to be cached so that users are not repeatedly prompted for passwords.(Citation: OS X Keychain)(Citation: External to DA, the OS X Way) Apple’s `securityd` utility takes the user’s logon password, encrypts it with PBKDF2, and stores this master key in memory. Apple also uses a set of keys and algorithms to encrypt the user’s password, but once the master key is found, an adversary need only iterate over the other values to unlock the final password.(Citation: OS X Keychain)

## Detection
Monitor processes and command-line arguments for activity surrounded users searching for credentials or using automated tools to scan memory for passwords.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1555/002)
- [External to DA, the OS X Way](https://www.slideshare.net/slideshow/external-to-da-the-os-x-way/62021418)
- [Apple Dev SecurityD](https://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/Architecture/Architecture.html)
- [OS X Keychain](http://juusosalonen.com/post/30923743427/breaking-into-the-os-x-keychain)
- [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
