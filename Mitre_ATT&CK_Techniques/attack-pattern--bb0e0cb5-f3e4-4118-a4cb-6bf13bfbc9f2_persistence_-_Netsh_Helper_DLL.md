---
contributors:
- Matthew Demaske, Adaptforward
id: attack-pattern--bb0e0cb5-f3e4-4118-a4cb-6bf13bfbc9f2
mitre_attack_url: https://attack.mitre.org/techniques/T1128
name: Netsh Helper DLL
platforms:
- Windows
tactics:
- persistence
title: persistence - Netsh Helper DLL
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **System Requirements** | {{LinkByID|S0108}} |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1128](https://attack.mitre.org/techniques/T1128) |

# Netsh Helper DLL (attack-pattern--bb0e0cb5-f3e4-4118-a4cb-6bf13bfbc9f2)

## Description
Netsh.exe (also referred to as Netshell) is a command-line scripting utility used to interact with the network configuration of a system. It contains functionality to add helper DLLs for extending functionality of the utility. (Citation: TechNet Netsh) The paths to registered netsh.exe helper DLLs are entered into the Windows Registry at <code>HKLM\SOFTWARE\Microsoft\Netsh</code>.

Adversaries can use netsh.exe with helper DLLs to proxy execution of arbitrary code in a persistent manner when netsh.exe is executed automatically with another Persistence technique or if other persistent software is present on the system that executes netsh.exe as part of its normal functionality. Examples include some VPN software that invoke netsh.exe. (Citation: Demaske Netsh Persistence)

Proof of concept code exists to load Cobalt Strike's payload using netsh.exe helper DLLs. (Citation: Github Netsh Helper CS Beacon)

## Detection
It is likely unusual for netsh.exe to have any child processes in most environments. Monitor process executions and investigate any child processes spawned by netsh.exe for malicious behavior. Monitor the <code>HKLM\SOFTWARE\Microsoft\Netsh</code> registry key for any new or suspicious entries that do not correlate with known system files or benign software. (Citation: Demaske Netsh Persistence)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1128)
- [TechNet Netsh](https://technet.microsoft.com/library/bb490939.aspx)
- [Demaske Netsh Persistence](https://htmlpreview.github.io/?https://github.com/MatthewDemaske/blogbackup/blob/master/netshell.html)
- [Github Netsh Helper CS Beacon](https://github.com/outflankbv/NetshHelperBeacon)
