---
data_sources:
- 'Command: Command Execution'
- 'File: File Metadata'
- 'Process: Process Creation'
- 'File: File Modification'
- 'Module: Module Load'
id: attack-pattern--10ff21b9-5a01-4268-a1b5-3b55015f1847
mitre_attack_url: https://attack.mitre.org/techniques/T1546/006
name: LC_LOAD_DYLIB Addition
platforms:
- macOS
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - LC_LOAD_DYLIB Addition
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | macOS |
| **Data Sources** | Command: Command Execution, File: File Metadata, Process: Process Creation, File: File Modification, Module: Module Load |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/006](https://attack.mitre.org/techniques/T1546/006) |

# LC_LOAD_DYLIB Addition (attack-pattern--10ff21b9-5a01-4268-a1b5-3b55015f1847)

## Description
Adversaries may establish persistence by executing malicious content triggered by the execution of tainted binaries. Mach-O binaries have a series of headers that are used to perform certain operations when a binary is loaded. The LC_LOAD_DYLIB header in a Mach-O binary tells macOS and OS X which dynamic libraries (dylibs) to load during execution time. These can be added ad-hoc to the compiled binary as long as adjustments are made to the rest of the fields and dependencies.(Citation: Writing Bad Malware for OSX) There are tools available to perform these changes.

Adversaries may modify Mach-O binary headers to load and execute malicious dylibs every time the binary is executed. Although any changes will invalidate digital signatures on binaries because the binary is being modified, this can be remediated by simply removing the LC_CODE_SIGNATURE command from the binary so that the signature isn’t checked at load time.(Citation: Malware Persistence on OS X)

## Detection
Monitor processes for those that may be used to modify binary headers. Monitor file systems for changes to application binaries and invalid checksums/signatures. Changes to binaries that do not line up with application updates or patches are also extremely suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/006)
- [Malware Persistence on OS X](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [Writing Bad Malware for OSX](https://www.blackhat.com/docs/us-15/materials/us-15-Wardle-Writing-Bad-A-Malware-For-OS-X.pdf)
