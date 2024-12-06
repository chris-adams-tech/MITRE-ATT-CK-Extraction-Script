---
id: attack-pattern--b53dbcc6-147d-48bb-9df4-bcb8bb808ff6
mitre_attack_url: https://attack.mitre.org/techniques/T1154
name: Trap
platforms:
- Linux
- macOS
tactics:
- execution
- persistence
title: execution - Trap
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, persistence |
| **Platforms** | Linux, macOS |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1154](https://attack.mitre.org/techniques/T1154) |

# Trap (attack-pattern--b53dbcc6-147d-48bb-9df4-bcb8bb808ff6)

## Description
The <code>trap</code> command allows programs and shells to specify commands that will be executed upon receiving interrupt signals. A common situation is a script allowing for graceful termination and handling of common  keyboard interrupts like <code>ctrl+c</code> and <code>ctrl+d</code>. Adversaries can use this to register code to be executed when the shell encounters specific interrupts either to gain execution or as a persistence mechanism. Trap commands are of the following format <code>trap 'command list' signals</code> where "command list" will be executed when "signals" are received.(Citation: Trap Manual)(Citation: Cyberciti Trap Statements)

## Detection
Trap commands must be registered for the shell or programs, so they appear in files. Monitoring files for suspicious or overly broad trap commands can narrow down suspicious behavior during an investigation. Monitor for suspicious processes executed through trap interrupts.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1154)
- [Trap Manual](https://ss64.com/bash/trap.html)
- [Cyberciti Trap Statements](https://bash.cyberciti.biz/guide/Trap_statement)
