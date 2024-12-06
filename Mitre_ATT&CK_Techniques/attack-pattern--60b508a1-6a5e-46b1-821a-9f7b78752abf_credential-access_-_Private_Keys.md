---
contributors:
- Itzik Kotler, SafeBreach
- Austin Clark, @c2defense
data_sources:
- 'Command: Command Execution'
- 'File: File Access'
id: attack-pattern--60b508a1-6a5e-46b1-821a-9f7b78752abf
mitre_attack_url: https://attack.mitre.org/techniques/T1552/004
name: Private Keys
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- credential-access
title: credential-access - Private Keys
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Command: Command Execution, File: File Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1552/004](https://attack.mitre.org/techniques/T1552/004) |

# Private Keys (attack-pattern--60b508a1-6a5e-46b1-821a-9f7b78752abf)

## Description
Adversaries may search for private key certificate files on compromised systems for insecurely stored credentials. Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures.(Citation: Wikipedia Public Key Crypto) Common key and certificate file extensions include: .key, .pgp, .gpg, .ppk., .p12, .pem, .pfx, .cer, .p7b, .asc. 

Adversaries may also look in common key directories, such as <code>~/.ssh</code> for SSH keys on * nix-based systems or <code>C:&#92;Users&#92;(username)&#92;.ssh&#92;</code> on Windows. Adversary tools may also search compromised systems for file extensions relating to cryptographic keys and certificates.(Citation: Kaspersky Careto)(Citation: Palo Alto Prince of Persia)

When a device is registered to Entra ID, a device key and a transport key are generated and used to verify the device’s identity.(Citation: Microsoft Primary Refresh Token) An adversary with access to the device may be able to export the keys in order to impersonate the device.(Citation: AADInternals Azure AD Device Identities)

On network devices, private keys may be exported via [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `crypto pki export`.(Citation: cisco_deploy_rsa_keys) 

Some private keys require a password or passphrase for operation, so an adversary may also use [Input Capture](https://attack.mitre.org/techniques/T1056) for keylogging or attempt to [Brute Force](https://attack.mitre.org/techniques/T1110) the passphrase off-line. These private keys can be used to authenticate to [Remote Services](https://attack.mitre.org/techniques/T1021) like SSH or for use in decrypting other collected files such as email.

## Detection
Monitor access to files and directories related to cryptographic keys and certificates as a means for potentially detecting access patterns that may indicate collection and exfiltration activity. Collect authentication logs and look for potentially abnormal activity that may indicate improper use of keys or certificates for remote authentication. For network infrastructure devices, collect AAA logging to monitor for private keys being exported.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1552/004)
- [Palo Alto Prince of Persia](https://researchcenter.paloaltonetworks.com/2016/06/unit42-prince-of-persia-game-over/)
- [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)
- [AADInternals Azure AD Device Identities](https://aadinternals.com/post/deviceidentity/)
- [Kaspersky Careto](https://web.archive.org/web/20141031134104/http://kasperskycontenthub.com/wp-content/uploads/sites/43/vlpdfs/unveilingthemask_v1.0.pdf)
- [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)
- [Wikipedia Public Key Crypto](https://en.wikipedia.org/wiki/Public-key_cryptography)
