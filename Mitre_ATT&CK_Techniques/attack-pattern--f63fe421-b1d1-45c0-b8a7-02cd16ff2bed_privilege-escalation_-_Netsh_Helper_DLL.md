---
contributors:
- Matthew Demaske, Adaptforward
data_sources:
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Modification'
- 'Module: Module Load'
- 'Process: Process Creation'
id: attack-pattern--f63fe421-b1d1-45c0-b8a7-02cd16ff2bed
mitre_attack_url: https://attack.mitre.org/techniques/T1546/007
name: Netsh Helper DLL
platforms:
- Windows
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Netsh Helper DLL
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Windows Registry: Windows Registry Key Modification, Module: Module Load, Process: Process Creation |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/007](https://attack.mitre.org/techniques/T1546/007) |

# Netsh Helper DLL (attack-pattern--f63fe421-b1d1-45c0-b8a7-02cd16ff2bed)

## Description
Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs. Netsh.exe (also referred to as Netshell) is a command-line scripting utility used to interact with the network configuration of a system. It contains functionality to add helper DLLs for extending functionality of the utility.(Citation: TechNet Netsh) The paths to registered netsh.exe helper DLLs are entered into the Windows Registry at <code>HKLM\SOFTWARE\Microsoft\Netsh</code>.

Adversaries can use netsh.exe helper DLLs to trigger execution of arbitrary code in a persistent manner. This execution would take place anytime netsh.exe is executed, which could happen automatically, with another persistence technique, or if other software (ex: VPN) is present on the system that executes netsh.exe as part of its normal functionality.(Citation: Github Netsh Helper CS Beacon)(Citation: Demaske Netsh Persistence)

## Detection
It is likely unusual for netsh.exe to have any child processes in most environments. Monitor process executions and investigate any child processes spawned by netsh.exe for malicious behavior. Monitor the <code>HKLM\SOFTWARE\Microsoft\Netsh</code> registry key for any new or suspicious entries that do not correlate with known system files or benign software.(Citation: Demaske Netsh Persistence)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/007)
- [Demaske Netsh Persistence](https://htmlpreview.github.io/?https://github.com/MatthewDemaske/blogbackup/blob/master/netshell.html)
- [TechNet Netsh](https://technet.microsoft.com/library/bb490939.aspx)
- [Github Netsh Helper CS Beacon](https://github.com/outflankbv/NetshHelperBeacon)
