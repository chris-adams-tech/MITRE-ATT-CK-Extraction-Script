---
data_sources:
- 'File: File Metadata'
id: attack-pattern--b4b7458f-81f2-4d38-84be-1c5ba0167a52
mitre_attack_url: https://attack.mitre.org/techniques/T1036/001
name: Invalid Code Signature
platforms:
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Invalid Code Signature
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Windows |
| **Data Sources** | File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/001](https://attack.mitre.org/techniques/T1036/001) |

# Invalid Code Signature (attack-pattern--b4b7458f-81f2-4d38-84be-1c5ba0167a52)

## Description
Adversaries may attempt to mimic features of valid code signatures to increase the chance of deceiving a user, analyst, or tool. Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. Adversaries can copy the metadata and signature information from a signed program, then use it as a template for an unsigned program. Files with invalid code signatures will fail digital signature validation checks, but they may appear more legitimate to users and security tools may improperly handle these files.(Citation: Threatexpress MetaTwin 2017)

Unlike [Code Signing](https://attack.mitre.org/techniques/T1553/002), this activity will not result in a valid signature.

## Detection
Collect and analyze signing certificate metadata and check signature validity on software that executes within the environment, look for invalid signatures as well as unusual certificate characteristics and outliers.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/001)
- [Threatexpress MetaTwin 2017](https://threatexpress.com/blogs/2017/metatwin-borrowing-microsoft-metadata-and-digital-signatures-to-hide-binaries/)
