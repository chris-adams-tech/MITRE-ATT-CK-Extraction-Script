---
contributors:
- Mayuresh Dani, Qualys
- Praetorian
- Ross Brittain
data_sources:
- 'Script: Script Execution'
- 'Process: Process Creation'
- 'Process: Process Metadata'
- 'Command: Command Execution'
- 'Module: Module Load'
id: attack-pattern--970a3432-3237-47ad-bcca-7d8cbb217736
mitre_attack_url: https://attack.mitre.org/techniques/T1059/001
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
| **Data Sources** | Script: Script Execution, Process: Process Creation, Process: Process Metadata, Command: Command Execution, Module: Module Load |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/001](https://attack.mitre.org/techniques/T1059/001) |

# PowerShell (attack-pattern--970a3432-3237-47ad-bcca-7d8cbb217736)

## Description
Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system.(Citation: TechNet PowerShell) Adversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code. Examples include the <code>Start-Process</code> cmdlet which can be used to run an executable and the <code>Invoke-Command</code> cmdlet which runs a command locally or on a remote computer (though administrator permissions are required to use PowerShell to connect to remote systems).

PowerShell may also be used to download and run executables from the Internet, which can be executed from disk or in memory without touching disk.

A number of PowerShell-based offensive testing tools are available, including [Empire](https://attack.mitre.org/software/S0363),  [PowerSploit](https://attack.mitre.org/software/S0194), [PoshC2](https://attack.mitre.org/software/S0378), and PSAttack.(Citation: Github PSAttack)

PowerShell commands/scripts can also be executed without directly invoking the <code>powershell.exe</code> binary through interfaces to PowerShell's underlying <code>System.Management.Automation</code> assembly DLL exposed through the .NET framework and Windows Common Language Interface (CLI).(Citation: Sixdub PowerPick Jan 2016)(Citation: SilentBreak Offensive PS Dec 2015)(Citation: Microsoft PSfromCsharp APR 2014)

## Detection
If proper execution policy is set, adversaries will likely be able to define their own execution policy if they obtain administrator or system access, either through the Registry or at the command line. This change in policy on a system may be a way to detect malicious use of PowerShell. If PowerShell is not used in an environment, then simply looking for PowerShell execution may detect malicious activity.

Monitor for loading and/or execution of artifacts associated with PowerShell specific assemblies, such as System.Management.Automation.dll (especially to unusual process names/locations).(Citation: Sixdub PowerPick Jan 2016)(Citation: SilentBreak Offensive PS Dec 2015)

It is also beneficial to turn on PowerShell logging to gain increased fidelity in what occurs during execution (which is applied to .NET invocations). (Citation: Malware Archaeology PowerShell Cheat Sheet) PowerShell 5.0 introduced enhanced logging capabilities, and some of those features have since been added to PowerShell 4.0. Earlier versions of PowerShell do not have many logging features.(Citation: FireEye PowerShell Logging 2016) An organization can gather PowerShell execution details in a data analytic platform to supplement it with other data.

Consider monitoring for Windows event ID (EID) 400, which shows the version of PowerShell executing in the <code>EngineVersion</code> field (which may also be relevant to detecting a potential [Downgrade Attack](https://attack.mitre.org/techniques/T1562/010)) as well as if PowerShell is running locally or remotely in the <code>HostName</code> field. Furthermore, EID 400 may indicate the start time and EID 403 indicates the end time of a PowerShell session.(Citation: inv_ps_attacks)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/001)
- [Microsoft PSfromCsharp APR 2014](https://blogs.msdn.microsoft.com/kebab/2014/04/28/executing-powershell-scripts-from-c/)
- [SilentBreak Offensive PS Dec 2015](https://web.archive.org/web/20190508170150/https://silentbreaksecurity.com/powershell-jobs-without-powershell-exe/)
- [FireEye PowerShell Logging 2016](https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html)
- [Github PSAttack](https://github.com/Exploit-install/PSAttack-1)
- [inv_ps_attacks](https://powershellmagazine.com/2014/07/16/investigating-powershell-attacks/)
- [Malware Archaeology PowerShell Cheat Sheet](http://www.malwarearchaeology.com/s/Windows-PowerShell-Logging-Cheat-Sheet-ver-June-2016-v2.pdf)
- [TechNet PowerShell](https://technet.microsoft.com/en-us/scriptcenter/dd742419.aspx)
- [Sixdub PowerPick Jan 2016](https://web.archive.org/web/20160327101330/http://www.sixdub.net/?p=367)
