---
data_sources:
- 'File: File Metadata'
id: attack-pattern--32901740-b42c-4fdd-bc02-345b5dc57082
mitre_attack_url: https://attack.mitre.org/techniques/T1553/002
name: Code Signing
platforms:
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Code Signing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Windows |
| **Data Sources** | File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1553/002](https://attack.mitre.org/techniques/T1553/002) |

# Code Signing (attack-pattern--32901740-b42c-4fdd-bc02-345b5dc57082)

## Description
Adversaries may create, acquire, or steal code signing materials to sign their malware or tools. Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. (Citation: Wikipedia Code Signing) The certificates used during an operation may be created, acquired, or stolen by the adversary. (Citation: Securelist Digital Certificates) (Citation: Symantec Digital Certificates) Unlike [Invalid Code Signature](https://attack.mitre.org/techniques/T1036/001), this activity will result in a valid signature.

Code signing to verify software on first run can be used on modern Windows and macOS systems. It is not used on Linux due to the decentralized nature of the platform. (Citation: Wikipedia Code Signing)(Citation: EclecticLightChecksonEXECodeSigning)

Code signing certificates may be used to bypass security policies that require signed code to execute on a system. 

## Detection
Collect and analyze signing certificate metadata on software that executes within the environment to look for unusual certificate characteristics and outliers.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1553/002)
- [EclecticLightChecksonEXECodeSigning](https://eclecticlight.co/2020/11/16/checks-on-executable-code-in-catalina-and-big-sur-a-first-draft/)
- [Securelist Digital Certificates](https://securelist.com/why-you-shouldnt-completely-trust-files-signed-with-digital-certificates/68593/)
- [Symantec Digital Certificates](http://www.symantec.com/connect/blogs/how-attackers-steal-private-keys-digital-certificates)
- [Wikipedia Code Signing](https://en.wikipedia.org/wiki/Code_signing)
