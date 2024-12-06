---
contributors:
- Romain Dumont, ESET
id: attack-pattern--128c55d3-aeba-469f-bd3e-c8996ab4112a
mitre_attack_url: https://attack.mitre.org/techniques/T1099
name: Timestomp
platforms:
- Linux
- Windows
- macOS
tactics:
- defense-evasion
title: defense-evasion - Timestomp
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, Windows, macOS |
| **Permissions Required** | User, Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1099](https://attack.mitre.org/techniques/T1099) |

# Timestomp (attack-pattern--128c55d3-aeba-469f-bd3e-c8996ab4112a)

## Description
Adversaries may take actions to hide the deployment of new, or modification of existing files to obfuscate their activities. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder. This is done, for example, on files that have been modified or created by the adversary so that they do not appear conspicuous to forensic investigators or file analysis tools. Timestomping may be used along with file name [Masquerading](https://attack.mitre.org/techniques/T1036) to hide malware and tools. (Citation: WindowsIR Anti-Forensic Techniques)

## Detection
Forensic techniques exist to detect aspects of files that have had their timestamps modified. (Citation: WindowsIR Anti-Forensic Techniques) It may be possible to detect timestomping using file modification monitoring that collects information on file handle opens and can compare timestamp values.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1099)
- [WindowsIR Anti-Forensic Techniques](http://windowsir.blogspot.com/2013/07/howto-determinedetect-use-of-anti.html)
