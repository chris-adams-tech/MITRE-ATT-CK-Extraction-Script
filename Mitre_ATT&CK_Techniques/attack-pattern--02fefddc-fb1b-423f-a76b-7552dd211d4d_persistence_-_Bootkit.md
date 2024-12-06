---
id: attack-pattern--02fefddc-fb1b-423f-a76b-7552dd211d4d
mitre_attack_url: https://attack.mitre.org/techniques/T1067
name: Bootkit
platforms:
- Linux
- Windows
tactics:
- persistence
title: persistence - Bootkit
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Linux, Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1067](https://attack.mitre.org/techniques/T1067) |

# Bootkit (attack-pattern--02fefddc-fb1b-423f-a76b-7552dd211d4d)

## Description
A bootkit is a malware variant that modifies the boot sectors of a hard drive, including the Master Boot Record (MBR) and Volume Boot Record (VBR). (Citation: MTrends 2016)

Adversaries may use bootkits to persist on systems at a layer below the operating system, which may make it difficult to perform full remediation unless an organization suspects one was used and can act accordingly.

### Master Boot Record
The MBR is the section of disk that is first loaded after completing hardware initialization by the BIOS. It is the location of the boot loader. An adversary who has raw access to the boot drive may overwrite this area, diverting execution during startup from the normal boot loader to adversary code. (Citation: Lau 2011)

### Volume Boot Record
The MBR passes control of the boot process to the VBR. Similar to the case of MBR, an adversary who has raw access to the boot drive may overwrite the VBR to divert execution during startup to adversary code.

## Detection
Perform integrity checking on MBR and VBR. Take snapshots of MBR and VBR and compare against known good samples. Report changes to MBR and VBR as they occur for indicators of suspicious activity and further analysis.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1067)
- [MTrends 2016](https://www.fireeye.com/content/dam/fireeye-www/regional/fr_FR/offers/pdfs/ig-mtrends-2016.pdf)
- [Lau 2011](http://www.symantec.com/connect/blogs/are-mbr-infections-back-fashion)
