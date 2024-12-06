---
contributors:
- '@ionstorm'
- Carrie Roberts, @OrOneEqualsOne
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--c92e3d68-2349-49e4-a341-7edca2deff96
mitre_attack_url: https://attack.mitre.org/techniques/T1127/001
name: MSBuild
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - MSBuild
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation |
| **System Requirements** | .NET Framework version 4 or higher |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1127/001](https://attack.mitre.org/techniques/T1127/001) |

# MSBuild (attack-pattern--c92e3d68-2349-49e4-a341-7edca2deff96)

## Description
Adversaries may use MSBuild to proxy execution of code through a trusted Windows utility. MSBuild.exe (Microsoft Build Engine) is a software build platform used by Visual Studio. It handles XML formatted project files that define requirements for loading and building various platforms and configurations.(Citation: MSDN MSBuild)

Adversaries can abuse MSBuild to proxy execution of malicious code. The inline task capability of MSBuild that was introduced in .NET version 4 allows for C# or Visual Basic code to be inserted into an XML project file.(Citation: MSDN MSBuild)(Citation: Microsoft MSBuild Inline Tasks 2017) MSBuild will compile and execute the inline task. MSBuild.exe is a signed Microsoft binary, so when it is used this way it can execute arbitrary code and bypass application control defenses that are configured to allow MSBuild.exe execution.(Citation: LOLBAS Msbuild)

## Detection
Use process monitoring to monitor the execution and arguments of MSBuild.exe. Compare recent invocations of those binaries with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. Command arguments used before and after invocation of the utilities may also be useful in determining the origin and purpose of the binary being executed.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1127/001)
- [LOLBAS Msbuild](https://lolbas-project.github.io/lolbas/Binaries/Msbuild/)
- [Microsoft MSBuild Inline Tasks 2017](https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-inline-tasks?view=vs-2019#code-element)
- [MSDN MSBuild](https://msdn.microsoft.com/library/dd393574.aspx)
