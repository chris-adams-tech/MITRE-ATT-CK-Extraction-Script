---
data_sources:
- 'File: File Creation'
id: attack-pattern--09b008a9-b4eb-462a-a751-a0eb58050cd9
mitre_attack_url: https://attack.mitre.org/techniques/T1564/012
name: File/Path Exclusions
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - File/Path Exclusions
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1564/012](https://attack.mitre.org/techniques/T1564/012) |

# File/Path Exclusions (attack-pattern--09b008a9-b4eb-462a-a751-a0eb58050cd9)

## Description
Adversaries may attempt to hide their file-based artifacts by writing them to specific folders or file names excluded from antivirus (AV) scanning and other defensive capabilities. AV and other file-based scanners often include exclusions to optimize performance as well as ease installation and legitimate use of applications. These exclusions may be contextual (e.g., scans are only initiated in response to specific triggering events/alerts), but are also often hardcoded strings referencing specific folders and/or files assumed to be trusted and legitimate.(Citation: Microsoft File Folder Exclusions)

Adversaries may abuse these exclusions to hide their file-based artifacts. For example, rather than  tampering with tool settings to add a new exclusion (i.e., [Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001)), adversaries may drop their file-based payloads in default or otherwise well-known exclusions. Adversaries may also use [Security Software Discovery](https://attack.mitre.org/techniques/T1518/001) and other [Discovery](https://attack.mitre.org/tactics/TA0007)/[Reconnaissance](https://attack.mitre.org/tactics/TA0043) activities to both discover and verify existing exclusions in a victim environment.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1564/012)
- [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)
