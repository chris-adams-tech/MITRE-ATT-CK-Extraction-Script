---
contributors:
- Filip Kafka, ESET
id: attack-pattern--6ff403bc-93e3-48be-8687-e102fdba8c88
mitre_attack_url: https://attack.mitre.org/techniques/T1045
name: Software Packing
platforms:
- Windows
- macOS
tactics:
- defense-evasion
title: defense-evasion - Software Packing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, macOS |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1045](https://attack.mitre.org/techniques/T1045) |

# Software Packing (attack-pattern--6ff403bc-93e3-48be-8687-e102fdba8c88)

## Description
Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techniques decompress the executable code in memory.

Utilities used to perform software packing are called packers. Example packers are MPRESS and UPX. A more comprehensive list of known packers is available, (Citation: Wikipedia Exe Compression) but adversaries may create their own packing techniques that do not leave the same artifacts as well-known packers to evade defenses.

Adversaries may use virtual machine software protection as a form of software packing to protect their code. Virtual machine software protection translates an executable's original code into a special format that only a special virtual machine can run. A virtual machine is then called to run this code.(Citation: ESET FinFisher Jan 2018)

## Detection
Use file scanning to look for known software packers or artifacts of packing techniques. Packing is not a definitive indicator of malicious activity, because legitimate software may use packing techniques to reduce binary size or to protect proprietary code.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1045)
- [capec](https://capec.mitre.org/data/definitions/570.html)
- [Wikipedia Exe Compression](http://en.wikipedia.org/wiki/Executable_compression)
- [ESET FinFisher Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/WP-FinFisher.pdf)
