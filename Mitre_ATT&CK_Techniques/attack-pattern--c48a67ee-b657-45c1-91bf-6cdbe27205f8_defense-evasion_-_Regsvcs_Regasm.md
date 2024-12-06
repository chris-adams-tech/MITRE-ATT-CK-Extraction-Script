---
contributors:
- Casey Smith
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--c48a67ee-b657-45c1-91bf-6cdbe27205f8
mitre_attack_url: https://attack.mitre.org/techniques/T1218/009
name: Regsvcs/Regasm
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Regsvcs/Regasm
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/009](https://attack.mitre.org/techniques/T1218/009) |

# Regsvcs/Regasm (attack-pattern--c48a67ee-b657-45c1-91bf-6cdbe27205f8)

## Description
Adversaries may abuse Regsvcs and Regasm to proxy execution of code through a trusted Windows utility. Regsvcs and Regasm are Windows command-line utilities that are used to register .NET [Component Object Model](https://attack.mitre.org/techniques/T1559/001) (COM) assemblies. Both are binaries that may be digitally signed by Microsoft. (Citation: MSDN Regsvcs) (Citation: MSDN Regasm)

Both utilities may be used to bypass application control through use of attributes within the binary to specify code that should be run before registration or unregistration: <code>[ComRegisterFunction]</code> or <code>[ComUnregisterFunction]</code> respectively. The code with the registration and unregistration attributes will be executed even if the process is run under insufficient privileges and fails to execute. (Citation: LOLBAS Regsvcs)(Citation: LOLBAS Regasm)

## Detection
Use process monitoring to monitor the execution and arguments of Regsvcs.exe and Regasm.exe. Compare recent invocations of Regsvcs.exe and Regasm.exe with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. Command arguments used before and after Regsvcs.exe or Regasm.exe invocation may also be useful in determining the origin and purpose of the binary being executed.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/009)
- [MSDN Regsvcs](https://msdn.microsoft.com/en-us/library/04za0hca.aspx)
- [MSDN Regasm](https://msdn.microsoft.com/en-us/library/tzat5yw6.aspx)
- [LOLBAS Regsvcs](https://lolbas-project.github.io/lolbas/Binaries/Regsvcs/)
- [LOLBAS Regasm](https://lolbas-project.github.io/lolbas/Binaries/Regasm/)
