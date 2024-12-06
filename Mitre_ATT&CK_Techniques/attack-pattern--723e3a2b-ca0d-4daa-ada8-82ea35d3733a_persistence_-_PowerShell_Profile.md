---
contributors:
- Allen DeRyke, ICE
id: attack-pattern--723e3a2b-ca0d-4daa-ada8-82ea35d3733a
mitre_attack_url: https://attack.mitre.org/techniques/T1504
name: PowerShell Profile
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - PowerShell Profile
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1504](https://attack.mitre.org/techniques/T1504) |

# PowerShell Profile (attack-pattern--723e3a2b-ca0d-4daa-ada8-82ea35d3733a)

## Description
Adversaries may gain persistence and elevate privileges in certain situations by abusing [PowerShell](https://attack.mitre.org/techniques/T1086) profiles. A PowerShell profile  (<code>profile.ps1</code>) is a script that runs when PowerShell starts and can be used as a logon script to customize user environments. PowerShell supports several profiles depending on the user or host program. For example, there can be different profiles for PowerShell host programs such as the PowerShell console, PowerShell ISE or Visual Studio Code. An administrator can also configure a profile that applies to all users and host programs on the local computer. (Citation: Microsoft About Profiles) 

Adversaries may modify these profiles to include arbitrary commands, functions, modules, and/or PowerShell drives to gain persistence. Every time a user opens a PowerShell session the modified script will be executed unless the <code>-NoProfile</code> flag is used when it is launched. (Citation: ESET Turla PowerShell May 2019) 

An adversary may also be able to escalate privileges if a script in a PowerShell profile is loaded and executed by an account with higher privileges, such as a domain administrator. (Citation: Wits End and Shady PowerShell Profiles)

## Detection
Locations where <code>profile.ps1</code> can be stored should be monitored for new profiles or modifications. (Citation: Malware Archaeology PowerShell Cheat Sheet) Example profile locations include:

* <code>$PsHome\Profile.ps1</code>
* <code>$PsHome\Microsoft.{HostProgram}_profile.ps1</code>
* <code>$Home\My Documents\PowerShell\Profile.ps1</code>
* <code>$Home\My Documents\PowerShell\Microsoft.{HostProgram}_profile.ps1</code>

Monitor abnormal PowerShell commands, unusual loading of PowerShell drives or modules, and/or execution of unknown programs.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1504)
- [Microsoft About Profiles](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-6)
- [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Wits End and Shady PowerShell Profiles](https://witsendandshady.blogspot.com/2019/06/lab-notes-persistence-and-privilege.html)
- [Malware Archaeology PowerShell Cheat Sheet](http://www.malwarearchaeology.com/s/Windows-PowerShell-Logging-Cheat-Sheet-ver-June-2016-v2.pdf)
