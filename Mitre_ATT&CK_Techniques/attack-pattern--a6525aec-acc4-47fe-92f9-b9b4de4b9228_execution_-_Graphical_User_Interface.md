---
id: attack-pattern--a6525aec-acc4-47fe-92f9-b9b4de4b9228
mitre_attack_url: https://attack.mitre.org/techniques/T1061
name: Graphical User Interface
platforms:
- Linux
- macOS
- Windows
tactics:
- execution
title: execution - Graphical User Interface
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Linux, macOS, Windows |
| **Permissions Required** | User, Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1061](https://attack.mitre.org/techniques/T1061) |

# Graphical User Interface (attack-pattern--a6525aec-acc4-47fe-92f9-b9b4de4b9228)

## Description
**This technique has been deprecated. Please use [Remote Services](https://attack.mitre.org/techniques/T1021) where appropriate.**

The Graphical User Interfaces (GUI) is a common way to interact with an operating system. Adversaries may use a system's GUI during an operation, commonly through a remote interactive session such as [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1076), instead of through a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), to search for information and execute files via mouse double-click events, the Windows Run command (Citation: Wikipedia Run Command), or other potentially difficult to monitor interactions.

## Detection
Detection of execution through the GUI will likely lead to significant false positives. Other factors should be considered to detect misuse of services that can lead to adversaries gaining access to systems through interactive remote sessions. 

Unknown or unusual process launches outside of normal behavior on a particular system occurring through remote interactive sessions are suspicious. Collect and audit security logs that may indicate access to and use of Legitimate Credentials to access remote systems within the network.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1061)
- [Wikipedia Run Command](https://en.wikipedia.org/wiki/Run_command)
