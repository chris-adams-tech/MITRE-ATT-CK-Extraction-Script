---
contributors:
  - Tom Simpson, CrowdStrike Falcon OverWatch
data_sources:
  - "File: File Creation"
  - "Drive: Drive Access"
  - "Command: Command Execution"
id: attack-pattern--0c8ab3eb-df48-4b9c-ace7-beacaac81cc5
mitre_attack_url: https://attack.mitre.org/techniques/T1006
name: Direct Volume Access
platforms:
  - Windows
  - Network
tactics:
  - defense-evasion
title: T1006 - defense-evasion - Direct Volume Access
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, Network |
| **Data Sources** | File: File Creation, Drive: Drive Access, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1006](https://attack.mitre.org/techniques/T1006) |

# Direct Volume Access (attack-pattern--0c8ab3eb-df48-4b9c-ace7-beacaac81cc5)

## Description
Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools. (Citation: Hakobyan 2009)

Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell.(Citation: Github PowerSploit Ninjacopy) Adversaries may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and [esentutl](https://attack.mitre.org/software/S0404)) to create shadow copies or backups of data from system volumes.(Citation: LOLBAS Esentutl)

## Detection
Monitor handle opens on drive volumes that are made by processes to determine when they may directly access logical drives. (Citation: Github PowerSploit Ninjacopy)

Monitor processes and command-line arguments for actions that could be taken to copy files from the logical drive and evade common file system protections. Since this technique may also be used through [PowerShell](https://attack.mitre.org/techniques/T1059/001), additional logging of PowerShell scripts is recommended.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1006)
- [Github PowerSploit Ninjacopy](https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Invoke-NinjaCopy.ps1)
- [Hakobyan 2009](http://www.codeproject.com/Articles/32169/FDump-Dumping-File-Sectors-Directly-from-Disk-usin)
- [LOLBAS Esentutl](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)
