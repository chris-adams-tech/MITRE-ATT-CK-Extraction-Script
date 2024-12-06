---
contributors:
- Walker Johnson
data_sources:
- 'Command: Command Execution'
- 'File: File Deletion'
id: attack-pattern--d63a3fb8-9452-4e9d-a60a-54be68d5998c
mitre_attack_url: https://attack.mitre.org/techniques/T1070/004
name: File Deletion
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - File Deletion
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Command: Command Execution, File: File Deletion |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1070/004](https://attack.mitre.org/techniques/T1070/004) |

# File Deletion (attack-pattern--d63a3fb8-9452-4e9d-a60a-54be68d5998c)

## Description
Adversaries may delete files left behind by the actions of their intrusion activity. Malware, tools, or other non-native files dropped or created on a system by an adversary (ex: [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) may leave traces to indicate to what was done within a network and how. Removal of these files can occur during an intrusion, or as part of a post-intrusion process to minimize the adversary's footprint.

There are tools available from the host operating system to perform cleanup, but adversaries may use other tools as well.(Citation: Microsoft SDelete July 2016) Examples of built-in [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) functions include <code>del</code> on Windows and <code>rm</code> or <code>unlink</code> on Linux and macOS.

## Detection
It may be uncommon for events related to benign command-line functions such as DEL or third-party utilities or tools to be found in an environment, depending on the user base and how systems are typically used. Monitoring for command-line deletion functions to correlate with binaries or other files that an adversary may drop and remove may lead to detection of malicious activity. Another good practice is monitoring for known deletion and secure deletion tools that are not already on systems within an enterprise network that an adversary could introduce. Some monitoring tools may collect command-line arguments, but may not capture DEL commands since DEL is a native function within cmd.exe.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1070/004)
- [Microsoft SDelete July 2016](https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete)
