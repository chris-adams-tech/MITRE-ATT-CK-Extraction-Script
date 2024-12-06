---
contributors:
  - Allen DeRyke, ICE
  - Matt Green, @mgreen27
data_sources:
  - "File: File Modification"
  - "Command: Command Execution"
  - "Process: Process Creation"
  - "File: File Creation"
id: attack-pattern--0f2c410d-d740-4ed9-abb1-b8f4a7faf6c3
mitre_attack_url: https://attack.mitre.org/techniques/T1546/013
name: PowerShell Profile
platforms:
  - Windows
tactics:
  - privilege-escalation
  - persistence
title: T1546.013 - privilege-escalation - PowerShell Profile
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Windows |
| **Data Sources** | File: File Modification, Command: Command Execution, Process: Process Creation, File: File Creation |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/013](https://attack.mitre.org/techniques/T1546/013) |

# PowerShell Profile (attack-pattern--0f2c410d-d740-4ed9-abb1-b8f4a7faf6c3)

## Description
Adversaries may gain persistence and elevate privileges by executing malicious content triggered by PowerShell profiles. A PowerShell profile  (<code>profile.ps1</code>) is a script that runs when [PowerShell](https://attack.mitre.org/techniques/T1059/001) starts and can be used as a logon script to customize user environments.

[PowerShell](https://attack.mitre.org/techniques/T1059/001) supports several profiles depending on the user or host program. For example, there can be different profiles for [PowerShell](https://attack.mitre.org/techniques/T1059/001) host programs such as the PowerShell console, PowerShell ISE or Visual Studio Code. An administrator can also configure a profile that applies to all users and host programs on the local computer. (Citation: Microsoft About Profiles) 

Adversaries may modify these profiles to include arbitrary commands, functions, modules, and/or [PowerShell](https://attack.mitre.org/techniques/T1059/001) drives to gain persistence. Every time a user opens a [PowerShell](https://attack.mitre.org/techniques/T1059/001) session the modified script will be executed unless the <code>-NoProfile</code> flag is used when it is launched. (Citation: ESET Turla PowerShell May 2019) 

An adversary may also be able to escalate privileges if a script in a PowerShell profile is loaded and executed by an account with higher privileges, such as a domain administrator. (Citation: Wits End and Shady PowerShell Profiles)

## Detection
Locations where <code>profile.ps1</code> can be stored should be monitored for new profiles or modifications. (Citation: Malware Archaeology PowerShell Cheat Sheet)(Citation: Microsoft Profiles) Example profile locations (user defaults as well as program-specific) include:

* <code>$PsHome\Profile.ps1</code>
* <code>$PsHome\Microsoft.{HostProgram}_profile.ps1</code>
* <code>$Home\\\[My ]Documents\PowerShell\Profile.ps1</code>
* <code>$Home\\\[My ]Documents\PowerShell\Microsoft.{HostProgram}_profile.ps1</code>

Monitor abnormal PowerShell commands, unusual loading of PowerShell drives or modules, and/or execution of unknown programs.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/013)
- [Wits End and Shady PowerShell Profiles](https://witsendandshady.blogspot.com/2019/06/lab-notes-persistence-and-privilege.html)
- [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Malware Archaeology PowerShell Cheat Sheet](http://www.malwarearchaeology.com/s/Windows-PowerShell-Logging-Cheat-Sheet-ver-June-2016-v2.pdf)
- [Microsoft About Profiles](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-6)
- [Microsoft Profiles](https://docs.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles)
