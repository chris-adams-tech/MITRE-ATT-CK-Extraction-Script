---
data_sources:
- 'Malware Repository: Malware Metadata'
id: attack-pattern--34b3f738-bd64-40e5-a112-29b0542bc8bf
mitre_attack_url: https://attack.mitre.org/techniques/T1587/002
name: Code Signing Certificates
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Code Signing Certificates
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Malware Repository: Malware Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1587/002](https://attack.mitre.org/techniques/T1587/002) |

# Code Signing Certificates (attack-pattern--34b3f738-bd64-40e5-a112-29b0542bc8bf)

## Description
Adversaries may create self-signed code signing certificates that can be used during targeting. Code signing is the process of digitally signing executables and scripts to confirm the software author and guarantee that the code has not been altered or corrupted. Code signing provides a level of authenticity for a program from the developer and a guarantee that the program has not been tampered with.(Citation: Wikipedia Code Signing) Users and/or security tools may trust a signed piece of code more than an unsigned piece of code even if they don't know who issued the certificate or who the author is.

Prior to [Code Signing](https://attack.mitre.org/techniques/T1553/002), adversaries may develop self-signed code signing certificates for use in operations.

## Detection
Consider analyzing self-signed code signing certificates for features that may be associated with the adversary and/or their developers, such as the thumbprint, algorithm used, validity period, and common name. Malware repositories can also be used to identify additional samples associated with the adversary and identify patterns an adversary has used in crafting self-signed code signing certificates.

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related follow-on behavior, such as [Code Signing](https://attack.mitre.org/techniques/T1553/002) or [Install Root Certificate](https://attack.mitre.org/techniques/T1553/004).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1587/002)
- [Wikipedia Code Signing](https://en.wikipedia.org/wiki/Code_signing)
