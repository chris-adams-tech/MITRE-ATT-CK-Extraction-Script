---
contributors:
- Casey Smith
- Matthew Demaske, Adaptforward
data_sources:
- 'Command: Command Execution'
- 'Module: Module Load'
- 'Process: Process Metadata'
- 'Process: Process Creation'
id: attack-pattern--ff25900d-76d5-449b-a351-8824e62fc81b
mitre_attack_url: https://attack.mitre.org/techniques/T1127
name: Trusted Developer Utilities Proxy Execution
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Trusted Developer Utilities Proxy Execution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Module: Module Load, Process: Process Metadata, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1127](https://attack.mitre.org/techniques/T1127) |

# Trusted Developer Utilities Proxy Execution (attack-pattern--ff25900d-76d5-449b-a351-8824e62fc81b)

## Description
Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads. There are many utilities used for software development related tasks that can be used to execute code in various forms to assist in development, debugging, and reverse engineering.(Citation: engima0x3 DNX Bypass)(Citation: engima0x3 RCSI Bypass)(Citation: Exploit Monday WinDbg)(Citation: LOLBAS Tracker) These utilities may often be signed with legitimate certificates that allow them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application control solutions.

## Detection
Monitor for abnormal presence of these or other utilities that enable proxy execution that are typically used for development, debugging, and reverse engineering on a system that is not used for these purposes may be suspicious.

Use process monitoring to monitor the execution and arguments of from developer utilities that may be abused. Compare recent invocations of those binaries with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. It is likely that these utilities will be used by software developers or for other software development related tasks, so if it exists and is used outside of that context, then the event may be suspicious. Command arguments used before and after invocation of the utilities may also be useful in determining the origin and purpose of the binary being executed.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1127)
- [Exploit Monday WinDbg](http://www.exploit-monday.com/2016/08/windbg-cdb-shellcode-runner.html)
- [LOLBAS Tracker](https://lolbas-project.github.io/lolbas/OtherMSBinaries/Tracker/)
- [engima0x3 RCSI Bypass](https://enigma0x3.net/2016/11/21/bypassing-application-whitelisting-by-using-rcsi-exe/)
- [engima0x3 DNX Bypass](https://enigma0x3.net/2016/11/17/bypassing-application-whitelisting-by-using-dnx-exe/)
