---
data_sources:
- 'File: File Modification'
- 'Process: Process Creation'
- 'Module: Module Load'
- 'File: File Creation'
id: attack-pattern--e64c62cf-9cd7-4a14-94ec-cdaac43ab44b
mitre_attack_url: https://attack.mitre.org/techniques/T1574/002
name: DLL Side-Loading
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - DLL Side-Loading
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | File: File Modification, Process: Process Creation, Module: Module Load, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/002](https://attack.mitre.org/techniques/T1574/002) |

# DLL Side-Loading (attack-pattern--e64c62cf-9cd7-4a14-94ec-cdaac43ab44b)

## Description
Adversaries may execute their own malicious payloads by side-loading DLLs. Similar to [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001), side-loading involves hijacking which DLL a program loads. But rather than just planting the DLL within the search order of a program then waiting for the victim application to be invoked, adversaries may directly side-load their payloads by planting then invoking a legitimate application that executes their payload(s).

Side-loading takes advantage of the DLL search order used by the loader by positioning both the victim application and malicious payload(s) alongside each other. Adversaries likely use side-loading as a means of masking actions they perform under a legitimate, trusted, and potentially elevated system or software process. Benign executables used to side-load payloads may not be flagged during delivery and/or execution. Adversary payloads may also be encrypted/packed or otherwise obfuscated until loaded into the memory of the trusted process.(Citation: FireEye DLL Side-Loading)

## Detection
Monitor processes for unusual activity (e.g., a process that does not use the network begins to do so) as well as the introduction of new files/programs. Track DLL metadata, such as a hash, and compare DLLs that are loaded at process execution time against previous executions to detect differences that do not correlate with patching or updates.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/002)
- [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)
