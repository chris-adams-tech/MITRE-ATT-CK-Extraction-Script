---
data_sources:
- 'File: File Creation'
- 'Script: Script Execution'
id: attack-pattern--143c0cbb-a297-4142-9624-87ffc778980b
mitre_attack_url: https://attack.mitre.org/techniques/T1560/003
name: Archive via Custom Method
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
title: collection - Archive via Custom Method
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Creation, Script: Script Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1560/003](https://attack.mitre.org/techniques/T1560/003) |

# Archive via Custom Method (attack-pattern--143c0cbb-a297-4142-9624-87ffc778980b)

## Description
An adversary may compress or encrypt data that is collected prior to exfiltration using a custom method. Adversaries may choose to use custom archival methods, such as encryption with XOR or stream ciphers implemented with no external library or utility references. Custom implementations of well-known compression algorithms have also been used.(Citation: ESET Sednit Part 2)

## Detection
Custom archival methods can be very difficult to detect, since many of them use standard programming language concepts, such as bitwise operations.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1560/003)
- [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
