---
data_sources:
- 'File: File Modification'
- 'Process: Process Creation'
- 'Scheduled Job: Scheduled Job Creation'
- 'Command: Command Execution'
id: attack-pattern--2acf44aa-542f-4366-b4eb-55ef5747759c
mitre_attack_url: https://attack.mitre.org/techniques/T1053/003
name: Cron
platforms:
- Linux
- macOS
tactics:
- execution
- persistence
- privilege-escalation
title: execution - Cron
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, persistence, privilege-escalation |
| **Platforms** | Linux, macOS |
| **Data Sources** | File: File Modification, Process: Process Creation, Scheduled Job: Scheduled Job Creation, Command: Command Execution |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1053/003](https://attack.mitre.org/techniques/T1053/003) |

# Cron (attack-pattern--2acf44aa-542f-4366-b4eb-55ef5747759c)

## Description
Adversaries may abuse the <code>cron</code> utility to perform task scheduling for initial or recurring execution of malicious code.(Citation: 20 macOS Common Tools and Techniques) The <code>cron</code> utility is a time-based job scheduler for Unix-like operating systems.  The <code> crontab</code> file contains the schedule of cron entries to be run and the specified times for execution. Any <code>crontab</code> files are stored in operating system-specific file paths.

An adversary may use <code>cron</code> in Linux or Unix environments to execute programs at system startup or on a scheduled basis for [Persistence](https://attack.mitre.org/tactics/TA0003). 

## Detection
Monitor scheduled task creation from common utilities using command-line invocation. Legitimate scheduled tasks may be created during installation of new software or through system administration functions. Look for changes to tasks that do not correlate with known software, patch cycles, etc.  

Suspicious program execution through scheduled tasks may show up as outlier processes that have not been seen before when compared against historical data. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1053/003)
- [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
