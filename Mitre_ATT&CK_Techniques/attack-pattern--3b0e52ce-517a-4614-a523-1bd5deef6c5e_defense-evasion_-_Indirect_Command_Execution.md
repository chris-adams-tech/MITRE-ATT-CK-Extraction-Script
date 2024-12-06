---
contributors:
- Matthew Demaske, Adaptforward
- Liran Ravich, CardinalOps
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--3b0e52ce-517a-4614-a523-1bd5deef6c5e
mitre_attack_url: https://attack.mitre.org/techniques/T1202
name: Indirect Command Execution
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Indirect Command Execution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1202](https://attack.mitre.org/techniques/T1202) |

# Indirect Command Execution (attack-pattern--3b0e52ce-517a-4614-a523-1bd5deef6c5e)

## Description
Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit the use of command-line interpreters. Various Windows utilities may be used to execute commands, possibly without invoking [cmd](https://attack.mitre.org/software/S0106). For example, [Forfiles](https://attack.mitre.org/software/S0193), the Program Compatibility Assistant (pcalua.exe), components of the Windows Subsystem for Linux (WSL), Scriptrunner.exe, as well as other utilities may invoke the execution of programs and commands from a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), Run window, or via scripts.(Citation: VectorSec ForFiles Aug 2017)(Citation: Evi1cg Forfiles Nov 2017)(Citation: Secure Team - Scriptrunner.exe)(Citation: SS64)(Citation: Bleeping Computer - Scriptrunner.exe)

Adversaries may abuse these features for [Defense Evasion](https://attack.mitre.org/tactics/TA0005), specifically to perform arbitrary execution while subverting detections and/or mitigation controls (such as Group Policy) that limit/prevent the usage of [cmd](https://attack.mitre.org/software/S0106) or file extensions more commonly associated with malicious payloads.

## Detection
Monitor and analyze logs from host-based detection mechanisms, such as Sysmon, for events such as process creations that include or are resulting from parameters associated with invoking programs/commands/files and/or spawning child processes/network connections. (Citation: RSA Forfiles Aug 2017)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1202)
- [Bleeping Computer - Scriptrunner.exe](https://www.bleepingcomputer.com/news/security/hackers-abuse-windows-error-reporting-tool-to-deploy-malware/)
- [Evi1cg Forfiles Nov 2017](https://x.com/Evi1cg/status/935027922397573120)
- [RSA Forfiles Aug 2017](https://community.rsa.com/community/products/netwitness/blog/2017/08/14/are-you-looking-out-for-forfilesexe-if-you-are-watching-for-cmdexe)
- [Secure Team - Scriptrunner.exe](https://secureteam.co.uk/2023/01/08/windows-error-reporting-tool-abused-to-load-malware/)
- [SS64](https://ss64.com/nt/scriptrunner.html)
- [VectorSec ForFiles Aug 2017](https://x.com/vector_sec/status/896049052642533376)
