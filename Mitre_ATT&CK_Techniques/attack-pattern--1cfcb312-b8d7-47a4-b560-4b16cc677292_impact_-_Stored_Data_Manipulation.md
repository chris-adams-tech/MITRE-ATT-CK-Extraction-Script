---
data_sources:
- 'File: File Modification'
- 'File: File Creation'
- 'File: File Deletion'
id: attack-pattern--1cfcb312-b8d7-47a4-b560-4b16cc677292
mitre_attack_url: https://attack.mitre.org/techniques/T1565/001
name: Stored Data Manipulation
platforms:
- Linux
- macOS
- Windows
tactics:
- impact
title: impact - Stored Data Manipulation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Modification, File: File Creation, File: File Deletion |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1565/001](https://attack.mitre.org/techniques/T1565/001) |

# Stored Data Manipulation (attack-pattern--1cfcb312-b8d7-47a4-b560-4b16cc677292)

## Description
Adversaries may insert, delete, or manipulate data at rest in order to influence external outcomes or hide activity, thus threatening the integrity of the data.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating stored data, adversaries may attempt to affect a business process, organizational understanding, and decision making.

Stored data could include a variety of file formats, such as Office files, databases, stored emails, and custom file formats. The type of modification and the impact it will have depends on the type of data as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Detection
Where applicable, inspect important file hashes, locations, and modifications for suspicious/unexpected values.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1565/001)
- [DOJ Lazarus Sony 2018](https://www.justice.gov/opa/press-release/file/1092091/download)
- [FireEye APT38 Oct 2018](https://www.mandiant.com/sites/default/files/2021-09/rpt-apt38-2018-web_v5-1.pdf)
