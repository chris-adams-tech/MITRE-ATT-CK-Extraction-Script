---
id: attack-pattern--2715c335-1bf2-4efe-9f18-0691317ff83b
mitre_attack_url: https://attack.mitre.org/techniques/T1167
name: Securityd Memory
platforms:
- macOS
tactics:
- credential-access
title: credential-access - Securityd Memory
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | macOS |
| **Permissions Required** | root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1167](https://attack.mitre.org/techniques/T1167) |

# Securityd Memory (attack-pattern--2715c335-1bf2-4efe-9f18-0691317ff83b)

## Description
In OS X prior to El Capitan, users with root access can read plaintext keychain passwords of logged-in users because Apple’s keychain implementation allows these credentials to be cached so that users are not repeatedly prompted for passwords. (Citation: OS X Keychain) (Citation: External to DA, the OS X Way) Apple’s securityd utility takes the user’s logon password, encrypts it with PBKDF2, and stores this master key in memory. Apple also uses a set of keys and algorithms to encrypt the user’s password, but once the master key is found, an attacker need only iterate over the other values to unlock the final password. (Citation: OS X Keychain)

If an adversary can obtain root access (allowing them to read securityd’s memory), then they can scan through memory to find the correct sequence of keys in relatively few tries to decrypt the user’s logon keychain. This provides the adversary with all the plaintext passwords for users, WiFi, mail, browsers, certificates, secure notes, etc. (Citation: OS X Keychain) (Citation: OSX Keydnap malware)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1167)
- [OS X Keychain](http://juusosalonen.com/post/30923743427/breaking-into-the-os-x-keychain)
- [External to DA, the OS X Way](http://www.slideshare.net/StephanBorosh/external-to-da-the-os-x-way)
- [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
