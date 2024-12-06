---
id: attack-pattern--0bf78622-e8d2-41da-a857-731472d61a92
mitre_attack_url: https://attack.mitre.org/techniques/T1492
name: Stored Data Manipulation
platforms:
  - Linux
  - macOS
  - Windows
tactics:
  - impact
title: T1492 - impact - Stored Data Manipulation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows |
| **Permissions Required** | User, Administrator, root, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1492](https://attack.mitre.org/techniques/T1492) |

# Stored Data Manipulation (attack-pattern--0bf78622-e8d2-41da-a857-731472d61a92)

## Description
Adversaries may insert, delete, or manipulate data at rest in order to manipulate external outcomes or hide activity.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating stored data, adversaries may attempt to affect a business process, organizational understanding, and decision making. 

Stored data could include a variety of file formats, such as Office files, databases, stored emails, and custom file formats. The type of modification and the impact it will have depends on the type of data as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Detection
Where applicable, inspect important file hashes, locations, and modifications for suspicious/unexpected values.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1492)
- [FireEye APT38 Oct 2018](https://content.fireeye.com/apt/rpt-apt38)
- [DOJ Lazarus Sony 2018](https://www.justice.gov/opa/press-release/file/1092091/download)
