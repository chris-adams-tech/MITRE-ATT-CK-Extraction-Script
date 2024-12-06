---
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--a9d4b653-6915-42af-98b2-5758c4ceee56
mitre_attack_url: https://attack.mitre.org/techniques/T1059/004
name: Unix Shell
platforms:
- macOS
- Linux
- Network
tactics:
- execution
title: execution - Unix Shell
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | macOS, Linux, Network |
| **Data Sources** | Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/004](https://attack.mitre.org/techniques/T1059/004) |

# Unix Shell (attack-pattern--a9d4b653-6915-42af-98b2-5758c4ceee56)

## Description
Adversaries may abuse Unix shell commands and scripts for execution. Unix shells are the primary command prompt on Linux and macOS systems, though many variations of the Unix shell exist (e.g. sh, bash, zsh, etc.) depending on the specific OS or distribution.(Citation: DieNet Bash)(Citation: Apple ZShell) Unix shells can control every aspect of a system, with certain commands requiring elevated privileges.

Unix shells also support scripts that enable sequential execution of commands as well as other typical programming operations such as conditionals and loops. Common uses of shell scripts include long or repetitive tasks, or the need to run the same set of commands on multiple systems.

Adversaries may abuse Unix shells to execute various commands or payloads. Interactive shells may be accessed through command and control channels or during lateral movement such as with [SSH](https://attack.mitre.org/techniques/T1021/004). Adversaries may also leverage shell scripts to deliver and execute multiple commands on victims or as part of payloads used for persistence.

## Detection
Unix shell usage may be common on administrator, developer, or power user systems, depending on job function. If scripting is restricted for normal users, then any attempt to enable scripts running on a system would be considered suspicious. If scripts are not commonly used on a system, but enabled, scripts running out of cycle from patching or other administrator functions are suspicious. Scripts should be captured from the file system when possible to determine their actions and intent.

Scripts are likely to perform actions with various effects on a system that may generate events, depending on the types of monitoring used. Monitor processes and command-line arguments for script execution and subsequent behavior. Actions may be related to network and system information discovery, collection, or other scriptable post-compromise behaviors and could be used as indicators of detection leading back to the source script. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/004)
- [Apple ZShell](https://support.apple.com/HT208050)
- [DieNet Bash](https://linux.die.net/man/1/bash)
