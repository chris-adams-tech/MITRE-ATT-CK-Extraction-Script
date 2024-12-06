---
id: attack-pattern--aa8bfbc9-78dc-41a4-a03b-7453e0fdccda
mitre_attack_url: https://attack.mitre.org/techniques/T1157
name: Dylib Hijacking
platforms:
- macOS
tactics:
- persistence
- privilege-escalation
title: persistence - Dylib Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1157](https://attack.mitre.org/techniques/T1157) |

# Dylib Hijacking (attack-pattern--aa8bfbc9-78dc-41a4-a03b-7453e0fdccda)

## Description
macOS and OS X use a common method to look for required dynamic libraries (dylib) to load into a program based on search paths. Adversaries can take advantage of ambiguous paths to plant dylibs to gain privilege escalation or persistence.

A common method is to see what dylibs an application uses, then plant a malicious version with the same name higher up in the search path. This typically results in the dylib being in the same folder as the application itself. (Citation: Writing Bad Malware for OSX) (Citation: Malware Persistence on OS X)

If the program is configured to run at a higher privilege level than the current user, then when the dylib is loaded into the application, the dylib will also run at that elevated level. This can be used by adversaries as a privilege escalation technique.

## Detection
Objective-See's Dylib Hijacking Scanner can be used to detect potential cases of dylib hijacking. Monitor file systems for moving, renaming, replacing, or modifying dylibs. Changes in the set of dylibs that are loaded by a process (compared to past behavior) that do not correlate with known software, patches, etc., are suspicious. Check the system for multiple dylibs with the same name and monitor which versions have historically been loaded into a process.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1157)
- [capec](https://capec.mitre.org/data/definitions/471.html)
- [Writing Bad Malware for OSX](https://www.blackhat.com/docs/us-15/materials/us-15-Wardle-Writing-Bad-A-Malware-For-OS-X.pdf)
- [Malware Persistence on OS X](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
