---
contributors:
- Casey Smith
- Travis Smith, Tripwire
id: attack-pattern--f792d02f-813d-402b-86a5-ab98cb391d3b
mitre_attack_url: https://attack.mitre.org/techniques/T1118
name: InstallUtil
platforms:
- Windows
tactics:
- defense-evasion
- execution
title: defense-evasion - InstallUtil
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, execution |
| **Platforms** | Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1118](https://attack.mitre.org/techniques/T1118) |

# InstallUtil (attack-pattern--f792d02f-813d-402b-86a5-ab98cb391d3b)

## Description
InstallUtil is a command-line utility that allows for installation and uninstallation of resources by executing specific installer components specified in .NET binaries. (Citation: MSDN InstallUtil) InstallUtil is located in the .NET directories on a Windows system: <code>C:\Windows\Microsoft.NET\Framework\v<version>\InstallUtil.exe</code> and <code>C:\Windows\Microsoft.NET\Framework64\v<version>\InstallUtil.exe</code>. InstallUtil.exe is digitally signed by Microsoft.

Adversaries may use InstallUtil to proxy execution of code through a trusted Windows utility. InstallUtil may also be used to bypass process whitelisting through use of attributes within the binary that execute the class decorated with the attribute <code>[System.ComponentModel.RunInstaller(true)]</code>. (Citation: LOLBAS Installutil)

## Detection
Use process monitoring to monitor the execution and arguments of InstallUtil.exe. Compare recent invocations of InstallUtil.exe with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. Command arguments used before and after the InstallUtil.exe invocation may also be useful in determining the origin and purpose of the binary being executed.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1118)
- [MSDN InstallUtil](https://msdn.microsoft.com/en-us/library/50614e95.aspx)
- [LOLBAS Installutil](https://lolbas-project.github.io/lolbas/Binaries/Installutil/)
