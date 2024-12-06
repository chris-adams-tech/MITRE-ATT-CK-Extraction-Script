---
id: attack-pattern--45d84c8b-c1e2-474d-a14d-69b5de0a2bc0
mitre_attack_url: https://attack.mitre.org/techniques/T1153
name: Source
platforms:
- Linux
- macOS
tactics:
- execution
title: execution - Source
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Linux, macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1153](https://attack.mitre.org/techniques/T1153) |

# Source (attack-pattern--45d84c8b-c1e2-474d-a14d-69b5de0a2bc0)

## Description
**This technique has been deprecated and should no longer be used.**

The <code>source</code> command loads functions into the current shell or executes files in the current context. This built-in command can be run in two different ways <code>source /path/to/filename [arguments]</code> or <code>.**This technique has been deprecated and should no longer be used.** /path/to/filename [arguments]</code>. Take note of the space after the ".". Without a space, a new shell is created that runs the program instead of running the program within the current context. This is often used to make certain features or functions available to a shell or to update a specific shell's environment.(Citation: Source Manual)

Adversaries can abuse this functionality to execute programs. The file executed with this technique does not need to be marked executable beforehand.

## Detection
Monitor for command shell execution of source and subsequent processes that are started as a result of being executed by a source command. Adversaries must also drop a file to disk in order to execute it with source, and these files can also detected by file monitoring.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1153)
- [Source Manual](https://ss64.com/bash/source.html)
