---
data_sources:
- 'Drive: Drive Modification'
id: attack-pattern--1b7b1806-7746-41a1-a35d-e48dae25ddba
mitre_attack_url: https://attack.mitre.org/techniques/T1542/003
name: Bootkit
platforms:
- Linux
- Windows
tactics:
- persistence
- defense-evasion
title: persistence - Bootkit
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, defense-evasion |
| **Platforms** | Linux, Windows |
| **Data Sources** | Drive: Drive Modification |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1542/003](https://attack.mitre.org/techniques/T1542/003) |

# Bootkit (attack-pattern--1b7b1806-7746-41a1-a35d-e48dae25ddba)

## Description
Adversaries may use bootkits to persist on systems. Bootkits reside at a layer below the operating system and may make it difficult to perform full remediation unless an organization suspects one was used and can act accordingly.

A bootkit is a malware variant that modifies the boot sectors of a hard drive, including the Master Boot Record (MBR) and Volume Boot Record (VBR). (Citation: Mandiant M Trends 2016) The MBR is the section of disk that is first loaded after completing hardware initialization by the BIOS. It is the location of the boot loader. An adversary who has raw access to the boot drive may overwrite this area, diverting execution during startup from the normal boot loader to adversary code. (Citation: Lau 2011)

The MBR passes control of the boot process to the VBR. Similar to the case of MBR, an adversary who has raw access to the boot drive may overwrite the VBR to divert execution during startup to adversary code.

## Detection
Perform integrity checking on MBR and VBR. Take snapshots of MBR and VBR and compare against known good samples. Report changes to MBR and VBR as they occur for indicators of suspicious activity and further analysis.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1542/003)
- [Mandiant M Trends 2016](https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/rpt-mtrends-2016.pdf)
- [Lau 2011](http://www.symantec.com/connect/blogs/are-mbr-infections-back-fashion)
