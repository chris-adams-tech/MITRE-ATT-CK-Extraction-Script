---
contributors:
- David Tayouri
data_sources:
- 'Network Share: Network Share Access'
- 'Command: Command Execution'
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
- 'File: File Access'
id: attack-pattern--ae676644-d2d2-41b7-af7e-9bed1b55898c
mitre_attack_url: https://attack.mitre.org/techniques/T1039
name: Data from Network Shared Drive
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
title: collection - Data from Network Shared Drive
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Share: Network Share Access, Command: Command Execution, Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow, File: File Access |
| **System Requirements** | Privileges to access network shared drive |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1039](https://attack.mitre.org/techniques/T1039) |

# Data from Network Shared Drive (attack-pattern--ae676644-d2d2-41b7-af7e-9bed1b55898c)

## Description
Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [cmd](https://attack.mitre.org/software/S0106) may be used to gather information.

## Detection
Monitor processes and command-line arguments for actions that could be taken to collect files from a network share. Remote access tools with built-in features may interact directly with the Windows API to gather data. Data may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1039)
