---
data_sources:
- 'Module: Module Load'
- 'Process: Process Creation'
- 'Script: Script Execution'
- 'Process: Process Access'
id: attack-pattern--acd0ba37-7ba9-4cc5-ac61-796586cd856d
mitre_attack_url: https://attack.mitre.org/techniques/T1559
name: Inter-Process Communication
platforms:
- Windows
- macOS
- Linux
tactics:
- execution
title: execution - Inter-Process Communication
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Module: Module Load, Process: Process Creation, Script: Script Execution, Process: Process Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1559](https://attack.mitre.org/techniques/T1559) |

# Inter-Process Communication (attack-pattern--acd0ba37-7ba9-4cc5-ac61-796586cd856d)

## Description
Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. 

Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows [Dynamic Data Exchange](https://attack.mitre.org/techniques/T1559/002) or [Component Object Model](https://attack.mitre.org/techniques/T1559/001). Linux environments support several different IPC mechanisms, two of which being sockets and pipes.(Citation: Linux IPC) Higher level execution mediums, such as those of [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)s, may also leverage underlying IPC mechanisms. Adversaries may also use [Remote Services](https://attack.mitre.org/techniques/T1021) such as [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) to facilitate remote IPC execution.(Citation: Fireeye Hunting COM June 2019)

## Detection
Monitor for strings in files/commands, loaded DLLs/libraries, or spawned processes that are associated with abuse of IPC mechanisms.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1559)
- [Fireeye Hunting COM June 2019](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)
- [Linux IPC](https://www.geeksforgeeks.org/inter-process-communication-ipc/#:~:text=Inter%2Dprocess%20communication%20(IPC),of%20co%2Doperation%20between%20them.)
