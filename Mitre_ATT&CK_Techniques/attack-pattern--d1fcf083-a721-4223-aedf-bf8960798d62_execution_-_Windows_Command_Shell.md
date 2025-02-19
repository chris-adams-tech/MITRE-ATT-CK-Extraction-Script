---
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--d1fcf083-a721-4223-aedf-bf8960798d62
mitre_attack_url: https://attack.mitre.org/techniques/T1059/003
name: Windows Command Shell
platforms:
- Windows
tactics:
- execution
title: execution - Windows Command Shell
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/003](https://attack.mitre.org/techniques/T1059/003) |

# Windows Command Shell (attack-pattern--d1fcf083-a721-4223-aedf-bf8960798d62)

## Description
Adversaries may abuse the Windows command shell for execution. The Windows command shell ([cmd](https://attack.mitre.org/software/S0106)) is the primary command prompt on Windows systems. The Windows command prompt can be used to control almost any aspect of a system, with various permission levels required for different subsets of commands. The command prompt can be invoked remotely via [Remote Services](https://attack.mitre.org/techniques/T1021) such as [SSH](https://attack.mitre.org/techniques/T1021/004).(Citation: SSH in Windows)

Batch files (ex: .bat or .cmd) also provide the shell with a list of sequential commands to run, as well as normal scripting operations such as conditionals and loops. Common uses of batch files include long or repetitive tasks, or the need to run the same set of commands on multiple systems.

Adversaries may leverage [cmd](https://attack.mitre.org/software/S0106) to execute various commands and payloads. Common uses include [cmd](https://attack.mitre.org/software/S0106) to execute a single command, or abusing [cmd](https://attack.mitre.org/software/S0106) interactively with input and output forwarded over a command and control channel.

## Detection
Usage of the Windows command shell may be common on administrator, developer, or power user systems depending on job function. If scripting is restricted for normal users, then any attempt to enable scripts running on a system would be considered suspicious. If scripts are not commonly used on a system, but enabled, scripts running out of cycle from patching or other administrator functions are suspicious. Scripts should be captured from the file system when possible to determine their actions and intent.

Scripts are likely to perform actions with various effects on a system that may generate events, depending on the types of monitoring used. Monitor processes and command-line arguments for script execution and subsequent behavior. Actions may be related to network and system information Discovery, Collection, or other scriptable post-compromise behaviors and could be used as indicators of detection leading back to the source script.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/003)
- [SSH in Windows](https://docs.microsoft.com/en-us/windows/terminal/tutorials/ssh)
