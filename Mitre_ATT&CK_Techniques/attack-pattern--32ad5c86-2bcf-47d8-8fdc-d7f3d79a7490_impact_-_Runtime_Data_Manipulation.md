---
data_sources:
- 'File: File Modification'
- 'File: File Deletion'
- 'Process: OS API Execution'
- 'File: File Metadata'
- 'File: File Creation'
id: attack-pattern--32ad5c86-2bcf-47d8-8fdc-d7f3d79a7490
mitre_attack_url: https://attack.mitre.org/techniques/T1565/003
name: Runtime Data Manipulation
platforms:
- Linux
- macOS
- Windows
tactics:
- impact
title: impact - Runtime Data Manipulation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Modification, File: File Deletion, Process: OS API Execution, File: File Metadata, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1565/003](https://attack.mitre.org/techniques/T1565/003) |

# Runtime Data Manipulation (attack-pattern--32ad5c86-2bcf-47d8-8fdc-d7f3d79a7490)

## Description
Adversaries may modify systems in order to manipulate the data as it is accessed and displayed to an end user, thus threatening the integrity of the data.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating runtime data, adversaries may attempt to affect a business process, organizational understanding, and decision making.

Adversaries may alter application binaries used to display data in order to cause runtime manipulations. Adversaries may also conduct [Change Default File Association](https://attack.mitre.org/techniques/T1546/001) and [Masquerading](https://attack.mitre.org/techniques/T1036) to cause a similar effect. The type of modification and the impact it will have depends on the target application and process as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Detection
Inspect important application binary file hashes, locations, and modifications for suspicious/unexpected values.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1565/003)
- [DOJ Lazarus Sony 2018](https://www.justice.gov/opa/press-release/file/1092091/download)
- [FireEye APT38 Oct 2018](https://www.mandiant.com/sites/default/files/2021-09/rpt-apt38-2018-web_v5-1.pdf)
