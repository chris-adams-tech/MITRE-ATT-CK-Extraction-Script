---
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Module: Module Load'
id: attack-pattern--6e3bd510-6b33-41a4-af80-2d80f3ee0071
mitre_attack_url: https://attack.mitre.org/techniques/T1218/008
name: Odbcconf
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Odbcconf
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation, Module: Module Load |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/008](https://attack.mitre.org/techniques/T1218/008) |

# Odbcconf (attack-pattern--6e3bd510-6b33-41a4-af80-2d80f3ee0071)

## Description
Adversaries may abuse odbcconf.exe to proxy execution of malicious payloads. Odbcconf.exe is a Windows utility that allows you to configure Open Database Connectivity (ODBC) drivers and data source names.(Citation: Microsoft odbcconf.exe) The Odbcconf.exe binary may be digitally signed by Microsoft.

Adversaries may abuse odbcconf.exe to bypass application control solutions that do not account for its potential abuse. Similar to [Regsvr32](https://attack.mitre.org/techniques/T1218/010), odbcconf.exe has a <code>REGSVR</code> flag that can be misused to execute DLLs (ex: <code>odbcconf.exe /S /A &lbrace;REGSVR "C:\Users\Public\file.dll"&rbrace;</code>). (Citation: LOLBAS Odbcconf)(Citation: TrendMicro Squiblydoo Aug 2017)(Citation: TrendMicro Cobalt Group Nov 2017) 


## Detection
Use process monitoring to monitor the execution and arguments of odbcconf.exe. Compare recent invocations of odbcconf.exe with prior history of known good arguments and loaded DLLs to determine anomalous and potentially adversarial activity. Command arguments used before and after the invocation of odbcconf.exe may also be useful in determining the origin and purpose of the DLL being loaded.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/008)
- [Microsoft odbcconf.exe](https://docs.microsoft.com/en-us/sql/odbc/odbcconf-exe?view=sql-server-2017)
- [LOLBAS Odbcconf](https://lolbas-project.github.io/lolbas/Binaries/Odbcconf/)
- [TrendMicro Squiblydoo Aug 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/backdoor-carrying-emails-set-sights-on-russian-speaking-businesses/)
- [TrendMicro Cobalt Group Nov 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/cobalt-spam-runs-use-macros-cve-2017-8759-exploit/)
