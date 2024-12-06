---
data_sources:
- 'File: File Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'File: File Modification'
id: attack-pattern--63220765-d418-44de-8fae-694b3912317d
mitre_attack_url: https://attack.mitre.org/techniques/T1546/005
name: Trap
platforms:
- macOS
- Linux
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Trap
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | macOS, Linux |
| **Data Sources** | File: File Creation, Process: Process Creation, Command: Command Execution, File: File Modification |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/005](https://attack.mitre.org/techniques/T1546/005) |

# Trap (attack-pattern--63220765-d418-44de-8fae-694b3912317d)

## Description
Adversaries may establish persistence by executing malicious content triggered by an interrupt signal. The <code>trap</code> command allows programs and shells to specify commands that will be executed upon receiving interrupt signals. A common situation is a script allowing for graceful termination and handling of common keyboard interrupts like <code>ctrl+c</code> and <code>ctrl+d</code>.

Adversaries can use this to register code to be executed when the shell encounters specific interrupts as a persistence mechanism. Trap commands are of the following format <code>trap 'command list' signals</code> where "command list" will be executed when "signals" are received.(Citation: Trap Manual)(Citation: Cyberciti Trap Statements)

## Detection
Trap commands must be registered for the shell or programs, so they appear in files. Monitoring files for suspicious or overly broad trap commands can narrow down suspicious behavior during an investigation. Monitor for suspicious processes executed through trap interrupts.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/005)
- [Trap Manual](https://ss64.com/bash/trap.html)
- [Cyberciti Trap Statements](https://bash.cyberciti.biz/guide/Trap_statement)
