---
contributors:
- Praetorian
id: attack-pattern--f4882e23-8aa7-4b12-b28a-b349c12ee9e0
mitre_attack_url: https://attack.mitre.org/techniques/T1086
name: PowerShell
platforms:
- Windows
tactics:
- execution
title: execution - PowerShell
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1086](https://attack.mitre.org/techniques/T1086) |

# PowerShell (attack-pattern--f4882e23-8aa7-4b12-b28a-b349c12ee9e0)

## Description
PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system. (Citation: TechNet PowerShell) Adversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code. Examples include the Start-Process cmdlet which can be used to run an executable and the Invoke-Command cmdlet which runs a command locally or on a remote computer. 

PowerShell may also be used to download and run executables from the Internet, which can be executed from disk or in memory without touching disk.

Administrator permissions are required to use PowerShell to connect to remote systems.

A number of PowerShell-based offensive testing tools are available, including [Empire](https://attack.mitre.org/software/S0363),  PowerSploit, (Citation: Powersploit) and PSAttack. (Citation: Github PSAttack)

PowerShell commands/scripts can also be executed without directly invoking the powershell.exe binary through interfaces to PowerShell's underlying System.Management.Automation assembly exposed through the .NET framework and Windows Common Language Interface (CLI). (Citation: Sixdub PowerPick Jan 2016)(Citation: SilentBreak Offensive PS Dec 2015) (Citation: Microsoft PSfromCsharp APR 2014)

## Detection
If proper execution policy is set, adversaries will likely be able to define their own execution policy if they obtain administrator or system access, either through the Registry or at the command line. This change in policy on a system may be a way to detect malicious use of PowerShell. If PowerShell is not used in an environment, then simply looking for PowerShell execution may detect malicious activity.

Monitor for loading and/or execution of artifacts associated with PowerShell specific assemblies, such as System.Management.Automation.dll (especially to unusual process names/locations). (Citation: Sixdub PowerPick Jan 2016)(Citation: SilentBreak Offensive PS Dec 2015)

It is also beneficial to turn on PowerShell logging to gain increased fidelity in what occurs during execution (which is applied to .NET invocations). (Citation: Malware Archaeology PowerShell Cheat Sheet) PowerShell 5.0 introduced enhanced logging capabilities, and some of those features have since been added to PowerShell 4.0. Earlier versions of PowerShell do not have many logging features. (Citation: FireEye PowerShell Logging 2016) An organization can gather PowerShell execution details in a data analytic platform to supplement it with other data.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1086)
- [TechNet PowerShell](https://technet.microsoft.com/en-us/scriptcenter/dd742419.aspx)
- [Powersploit](https://github.com/mattifestation/PowerSploit)
- [Github PSAttack](https://github.com/jaredhaight/PSAttack)
- [Sixdub PowerPick Jan 2016](http://www.sixdub.net/?p=367)
- [SilentBreak Offensive PS Dec 2015](https://silentbreaksecurity.com/powershell-jobs-without-powershell-exe/)
- [Microsoft PSfromCsharp APR 2014](https://blogs.msdn.microsoft.com/kebab/2014/04/28/executing-powershell-scripts-from-c/)
- [Malware Archaeology PowerShell Cheat Sheet](http://www.malwarearchaeology.com/s/Windows-PowerShell-Logging-Cheat-Sheet-ver-June-2016-v2.pdf)
- [FireEye PowerShell Logging 2016](https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html)
