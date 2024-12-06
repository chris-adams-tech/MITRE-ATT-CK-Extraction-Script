---
id: attack-pattern--cc1e737c-236c-4e3b-83ba-32039a626ef8
mitre_attack_url: https://attack.mitre.org/techniques/T1493
name: Transmitted Data Manipulation
platforms:
- Linux
- macOS
- Windows
tactics:
- impact
title: impact - Transmitted Data Manipulation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows |
| **Permissions Required** | User, Administrator, root, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1493](https://attack.mitre.org/techniques/T1493) |

# Transmitted Data Manipulation (attack-pattern--cc1e737c-236c-4e3b-83ba-32039a626ef8)

## Description
Adversaries may alter data en route to storage or other systems in order to manipulate external outcomes or hide activity.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating transmitted data, adversaries may attempt to affect a business process, organizational understanding, and decision making. 

Manipulation may be possible over a network connection or between system processes where there is an opportunity deploy a tool that will intercept and change information. The type of modification and the impact it will have depends on the target transmission mechanism as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Detection
Detecting the manipulation of data as at passes over a network can be difficult without the appropriate tools. In some cases integrity verification checks, such as file hashing, may be used on critical files as they transit a network. With some critical processes involving transmission of data, manual or out-of-band integrity checking may be useful for identifying manipulated data.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1493)
- [FireEye APT38 Oct 2018](https://content.fireeye.com/apt/rpt-apt38)
- [DOJ Lazarus Sony 2018](https://www.justice.gov/opa/press-release/file/1092091/download)
