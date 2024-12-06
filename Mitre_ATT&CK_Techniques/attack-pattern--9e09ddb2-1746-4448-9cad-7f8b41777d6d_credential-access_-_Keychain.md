---
id: attack-pattern--9e09ddb2-1746-4448-9cad-7f8b41777d6d
mitre_attack_url: https://attack.mitre.org/techniques/T1142
name: Keychain
platforms:
- macOS
tactics:
- credential-access
title: credential-access - Keychain
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | macOS |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1142](https://attack.mitre.org/techniques/T1142) |

# Keychain (attack-pattern--9e09ddb2-1746-4448-9cad-7f8b41777d6d)

## Description
Keychains are the built-in way for macOS to keep track of users' passwords and credentials for many services and features such as WiFi passwords, websites, secure notes, certificates, and Kerberos. Keychain files are located in <code>~/Library/Keychains/</code>,<code>/Library/Keychains/</code>, and <code>/Network/Library/Keychains/</code>. (Citation: Wikipedia keychain) The <code>security</code> command-line utility, which is built into macOS by default, provides a useful way to manage these credentials.

To manage their credentials, users have to use additional credentials to access their keychain. If an adversary knows the credentials for the login keychain, then they can get access to all the other credentials stored in this vault. (Citation: External to DA, the OS X Way) By default, the passphrase for the keychain is the user’s logon credentials.

## Detection
Unlocking the keychain and using passwords from it is a very common process, so there is likely to be a lot of noise in any detection technique. Monitoring of system calls to the keychain can help determine if there is a suspicious process trying to access it.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1142)
- [Wikipedia keychain](https://en.wikipedia.org/wiki/Keychain_(software))
- [External to DA, the OS X Way](http://www.slideshare.net/StephanBorosh/external-to-da-the-os-x-way)
