---
contributors:
- Ziv Kaspersky, Cymptom
- Alexandros Pappas
data_sources:
- 'Module: Module Load'
- 'Network Traffic: Network Connection Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--365be77f-fc0e-42ee-bac8-4faf806d9336
mitre_attack_url: https://attack.mitre.org/techniques/T1218/007
name: Msiexec
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Msiexec
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Module: Module Load, Network Traffic: Network Connection Creation, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/007](https://attack.mitre.org/techniques/T1218/007) |

# Msiexec (attack-pattern--365be77f-fc0e-42ee-bac8-4faf806d9336)

## Description
Adversaries may abuse msiexec.exe to proxy execution of malicious payloads. Msiexec.exe is the command-line utility for the Windows Installer and is thus commonly associated with executing installation packages (.msi).(Citation: Microsoft msiexec) The Msiexec.exe binary may also be digitally signed by Microsoft.

Adversaries may abuse msiexec.exe to launch local or network accessible MSI files. Msiexec.exe can also execute DLLs.(Citation: LOLBAS Msiexec)(Citation: TrendMicro Msiexec Feb 2018) Since it may be signed and native on Windows systems, msiexec.exe can be used to bypass application control solutions that do not account for its potential abuse. Msiexec.exe execution may also be elevated to SYSTEM privileges if the <code>AlwaysInstallElevated</code> policy is enabled.(Citation: Microsoft AlwaysInstallElevated 2018)

## Detection
Use process monitoring to monitor the execution and arguments of msiexec.exe. Compare recent invocations of msiexec.exe with prior history of known good arguments and executed MSI files or DLLs to determine anomalous and potentially adversarial activity. Command arguments used before and after the invocation of msiexec.exe may also be useful in determining the origin and purpose of the MSI files or DLLs being executed.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/007)
- [TrendMicro Msiexec Feb 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/attack-using-windows-installer-msiexec-exe-leads-lokibot/)
- [LOLBAS Msiexec](https://lolbas-project.github.io/lolbas/Binaries/Msiexec/)
- [Microsoft msiexec](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec)
- [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)
