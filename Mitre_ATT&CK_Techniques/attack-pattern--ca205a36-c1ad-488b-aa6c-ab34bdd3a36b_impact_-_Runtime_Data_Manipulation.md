---
id: attack-pattern--ca205a36-c1ad-488b-aa6c-ab34bdd3a36b
mitre_attack_url: https://attack.mitre.org/techniques/T1494
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
| **Permissions Required** | User, Administrator, root, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1494](https://attack.mitre.org/techniques/T1494) |

# Runtime Data Manipulation (attack-pattern--ca205a36-c1ad-488b-aa6c-ab34bdd3a36b)

## Description
Adversaries may modify systems in order to manipulate the data as it is accessed and displayed to an end user.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating runtime data, adversaries may attempt to affect a business process, organizational understanding, and decision making. 

Adversaries may alter application binaries used to display data in order to cause runtime manipulations. Adversaries may also conduct [Change Default File Association](https://attack.mitre.org/techniques/T1042) and [Masquerading](https://attack.mitre.org/techniques/T1036) to cause a similar effect. The type of modification and the impact it will have depends on the target application and process as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Detection
Inspect important application binary file hashes, locations, and modifications for suspicious/unexpected values.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1494)
- [FireEye APT38 Oct 2018](https://content.fireeye.com/apt/rpt-apt38)
- [DOJ Lazarus Sony 2018](https://www.justice.gov/opa/press-release/file/1092091/download)
