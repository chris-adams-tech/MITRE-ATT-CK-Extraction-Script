---
id: attack-pattern--1b84d551-6de8-4b96-9930-d177677c3b1d
mitre_attack_url: https://attack.mitre.org/techniques/T1116
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
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1116](https://attack.mitre.org/techniques/T1116) |

# Code Signing (attack-pattern--1b84d551-6de8-4b96-9930-d177677c3b1d)

## Description
Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. (Citation: Wikipedia Code Signing) However, adversaries are known to use code signing certificates to masquerade malware and tools as legitimate binaries (Citation: Janicab). The certificates used during an operation may be created, forged, or stolen by the adversary. (Citation: Securelist Digital Certificates) (Citation: Symantec Digital Certificates)

Code signing to verify software on first run can be used on modern Windows and macOS/OS X systems. It is not used on Linux due to the decentralized nature of the platform. (Citation: Wikipedia Code Signing)

Code signing certificates may be used to bypass security policies that require signed code to execute on a system.

## Detection
Collect and analyze signing certificate metadata on software that executes within the environment to look for unusual certificate characteristics and outliers.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1116)
- [Wikipedia Code Signing](https://en.wikipedia.org/wiki/Code_signing)
- [Janicab](http://www.thesafemac.com/new-signed-malware-called-janicab/)
- [Securelist Digital Certificates](https://securelist.com/why-you-shouldnt-completely-trust-files-signed-with-digital-certificates/68593/)
- [Symantec Digital Certificates](http://www.symantec.com/connect/blogs/how-attackers-steal-private-keys-digital-certificates)
