---
contributors:
- Itzik Kotler, SafeBreach
id: attack-pattern--56ff457d-5e39-492b-974c-dfd2b8603ffe
mitre_attack_url: https://attack.mitre.org/techniques/T1145
name: Private Keys
platforms:
- Linux
- macOS
- Windows
tactics:
- credential-access
title: credential-access - Private Keys
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS, Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1145](https://attack.mitre.org/techniques/T1145) |

# Private Keys (attack-pattern--56ff457d-5e39-492b-974c-dfd2b8603ffe)

## Description
Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures. (Citation: Wikipedia Public Key Crypto)

Adversaries may gather private keys from compromised systems for use in authenticating to [Remote Services](https://attack.mitre.org/techniques/T1021) like SSH or for use in decrypting other collected files such as email. Common key and certificate file extensions include: .key, .pgp, .gpg, .ppk., .p12, .pem, .pfx, .cer, .p7b, .asc. Adversaries may also look in common key directories, such as <code>~/.ssh</code> for SSH keys on * nix-based systems or <code>C:\Users\(username)\.ssh\</code> on Windows.

Private keys should require a password or passphrase for operation, so an adversary may also use [Input Capture](https://attack.mitre.org/techniques/T1056) for keylogging or attempt to [Brute Force](https://attack.mitre.org/techniques/T1110) the passphrase off-line.

Adversary tools have been discovered that search compromised systems for file extensions relating to cryptographic keys and certificates. (Citation: Kaspersky Careto) (Citation: Palo Alto Prince of Persia)

## Detection
Monitor access to files and directories related to cryptographic keys and certificates as a means for potentially detecting access patterns that may indicate collection and exfiltration activity. Collect authentication logs and look for potentially abnormal activity that may indicate improper use of keys or certificates for remote authentication.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1145)
- [Wikipedia Public Key Crypto](https://en.wikipedia.org/wiki/Public-key_cryptography)
- [Kaspersky Careto](https://kasperskycontenthub.com/wp-content/uploads/sites/43/vlpdfs/unveilingthemask_v1.0.pdf)
- [Palo Alto Prince of Persia](https://researchcenter.paloaltonetworks.com/2016/06/unit42-prince-of-persia-game-over/)
