---
data_sources:
- 'Process: OS API Execution'
- 'Network Traffic: Network Traffic Content'
- 'File: File Creation'
- 'Network Traffic: Network Traffic Flow'
- 'File: File Deletion'
- 'File: File Modification'
- 'File: File Metadata'
id: attack-pattern--ac9e6b22-11bf-45d7-9181-c1cb08360931
mitre_attack_url: https://attack.mitre.org/techniques/T1565
name: Data Manipulation
platforms:
- Linux
- macOS
- Windows
tactics:
- impact
title: impact - Data Manipulation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: OS API Execution, Network Traffic: Network Traffic Content, File: File Creation, Network Traffic: Network Traffic Flow, File: File Deletion, File: File Modification, File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1565](https://attack.mitre.org/techniques/T1565) |

# Data Manipulation (attack-pattern--ac9e6b22-11bf-45d7-9181-c1cb08360931)

## Description
Adversaries may insert, delete, or manipulate data in order to influence external outcomes or hide activity, thus threatening the integrity of the data.(Citation: Sygnia Elephant Beetle Jan 2022) By manipulating data, adversaries may attempt to affect a business process, organizational understanding, or decision making.

The type of modification and the impact it will have depends on the target application and process as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Detection
Where applicable, inspect important file hashes, locations, and modifications for suspicious/unexpected values. With some critical processes involving transmission of data, manual or out-of-band integrity checking may be useful for identifying manipulated data.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1565)
- [Sygnia Elephant Beetle Jan 2022](https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf?__hstc=147695848.3e8f1a482c8f8d4531507747318e660b.1680005306711.1680005306711.1680005306711.1&__hssc=147695848.1.1680005306711&__hsfp=3000179024&hsCtaTracking=189ec409-ae2d-4909-8bf1-62dcdd694372%7Cca91d317-8f10-4a38-9f80-367f551ad64d)
