---
data_sources:
- 'File: File Modification'
- 'Process: Process Metadata'
- 'Command: Command Execution'
- 'File: File Metadata'
id: attack-pattern--bd5b58a4-a52d-4a29-bc0d-3f1d3968eb6b
mitre_attack_url: https://attack.mitre.org/techniques/T1036/003
name: Rename System Utilities
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Rename System Utilities
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Modification, Process: Process Metadata, Command: Command Execution, File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/003](https://attack.mitre.org/techniques/T1036/003) |

# Rename System Utilities (attack-pattern--bd5b58a4-a52d-4a29-bc0d-3f1d3968eb6b)

## Description
Adversaries may rename legitimate system utilities to try to evade security mechanisms concerning the usage of those utilities. Security monitoring and control mechanisms may be in place for system utilities adversaries are capable of abusing. (Citation: LOLBAS Main Site) It may be possible to bypass those security mechanisms by renaming the utility prior to utilization (ex: rename <code>rundll32.exe</code>). (Citation: Elastic Masquerade Ball) An alternative case occurs when a legitimate utility is copied or moved to a different directory and renamed to avoid detections based on system utilities executing from non-standard paths. (Citation: F-Secure CozyDuke)

## Detection
If file names are mismatched between the file name on disk and that of the binary's PE metadata, this is a likely indicator that a binary was renamed after it was compiled. Collecting and comparing disk and resource filenames for binaries by looking to see if the InternalName, OriginalFilename, and/or ProductName match what is expected could provide useful leads, but may not always be indicative of malicious activity. (Citation: Elastic Masquerade Ball) Do not focus on the possible names a file could have, but instead on the command-line arguments that are known to be used and are distinct because it will have a better rate of detection.(Citation: Twitter ItsReallyNick Masquerading Update)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/003)
- [Twitter ItsReallyNick Masquerading Update](https://x.com/ItsReallyNick/status/1055321652777619457)
- [Elastic Masquerade Ball](https://www.elastic.co/blog/how-hunt-masquerade-ball)
- [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)
- [LOLBAS Main Site](https://lolbas-project.github.io/)
