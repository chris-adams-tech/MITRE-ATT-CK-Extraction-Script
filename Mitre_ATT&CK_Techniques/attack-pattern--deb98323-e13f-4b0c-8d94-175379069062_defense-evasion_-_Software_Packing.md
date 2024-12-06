---
contributors:
- Filip Kafka, ESET
data_sources:
- 'File: File Metadata'
id: attack-pattern--deb98323-e13f-4b0c-8d94-175379069062
mitre_attack_url: https://attack.mitre.org/techniques/T1027/002
name: Software Packing
platforms:
- macOS
- Windows
- Linux
tactics:
- defense-evasion
title: defense-evasion - Software Packing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Windows, Linux |
| **Data Sources** | File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/002](https://attack.mitre.org/techniques/T1027/002) |

# Software Packing (attack-pattern--deb98323-e13f-4b0c-8d94-175379069062)

## Description
Adversaries may perform software packing or virtual machine software protection to conceal their code. Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techniques decompress the executable code in memory. Virtual machine software protection translates an executable's original code into a special format that only a special virtual machine can run. A virtual machine is then called to run this code.(Citation: ESET FinFisher Jan 2018) 

Utilities used to perform software packing are called packers. Example packers are MPRESS and UPX. A more comprehensive list of known packers is available, but adversaries may create their own packing techniques that do not leave the same artifacts as well-known packers to evade defenses.(Citation: Awesome Executable Packing)  

## Detection
Use file scanning to look for known software packers or artifacts of packing techniques. Packing is not a definitive indicator of malicious activity, because legitimate software may use packing techniques to reduce binary size or to protect proprietary code.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/002)
- [Awesome Executable Packing](https://github.com/dhondta/awesome-executable-packing)
- [ESET FinFisher Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/WP-FinFisher.pdf)
