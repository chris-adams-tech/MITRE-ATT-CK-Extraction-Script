---
id: attack-pattern--04ef4356-8926-45e2-9441-634b6f3dcecb
mitre_attack_url: https://attack.mitre.org/techniques/T1161
name: LC_LOAD_DYLIB Addition
platforms:
- macOS
tactics:
- persistence
title: persistence - LC_LOAD_DYLIB Addition
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1161](https://attack.mitre.org/techniques/T1161) |

# LC_LOAD_DYLIB Addition (attack-pattern--04ef4356-8926-45e2-9441-634b6f3dcecb)

## Description
Mach-O binaries have a series of headers that are used to perform certain operations when a binary is loaded. The LC_LOAD_DYLIB header in a Mach-O binary tells macOS and OS X which dynamic libraries (dylibs) to load during execution time. These can be added ad-hoc to the compiled binary as long adjustments are made to the rest of the fields and dependencies (Citation: Writing Bad Malware for OSX). There are tools available to perform these changes. Any changes will invalidate digital signatures on binaries because the binary is being modified. Adversaries can remediate this issue by simply removing the LC_CODE_SIGNATURE command from the binary so that the signature isn’t checked at load time (Citation: Malware Persistence on OS X).

## Detection
Monitor processes for those that may be used to modify binary headers. Monitor file systems for changes to application binaries and invalid checksums/signatures. Changes to binaries that do not line up with application updates or patches are also extremely suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1161)
- [Writing Bad Malware for OSX](https://www.blackhat.com/docs/us-15/materials/us-15-Wardle-Writing-Bad-A-Malware-For-OS-X.pdf)
- [Malware Persistence on OS X](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
