---
contributors:
- Travis Smith, Tripwire
- Casey Smith
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--2cd950a6-16c4-404a-aa01-044322395107
mitre_attack_url: https://attack.mitre.org/techniques/T1218/004
name: InstallUtil
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - InstallUtil
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/004](https://attack.mitre.org/techniques/T1218/004) |

# InstallUtil (attack-pattern--2cd950a6-16c4-404a-aa01-044322395107)

## Description
Adversaries may use InstallUtil to proxy execution of code through a trusted Windows utility. InstallUtil is a command-line utility that allows for installation and uninstallation of resources by executing specific installer components specified in .NET binaries. (Citation: MSDN InstallUtil) The InstallUtil binary may also be digitally signed by Microsoft and located in the .NET directories on a Windows system: <code>C:\Windows\Microsoft.NET\Framework\v<version>\InstallUtil.exe</code> and <code>C:\Windows\Microsoft.NET\Framework64\v<version>\InstallUtil.exe</code>.

InstallUtil may also be used to bypass application control through use of attributes within the binary that execute the class decorated with the attribute <code>[System.ComponentModel.RunInstaller(true)]</code>. (Citation: LOLBAS Installutil)

## Detection
Use process monitoring to monitor the execution and arguments of InstallUtil.exe. Compare recent invocations of InstallUtil.exe with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. Command arguments used before and after the InstallUtil.exe invocation may also be useful in determining the origin and purpose of the binary being executed.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/004)
- [MSDN InstallUtil](https://msdn.microsoft.com/en-us/library/50614e95.aspx)
- [LOLBAS Installutil](https://lolbas-project.github.io/lolbas/Binaries/Installutil/)
