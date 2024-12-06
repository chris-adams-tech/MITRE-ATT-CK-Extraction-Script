---
contributors:
- William Cain
- Austin Clark, @c2defense
data_sources:
- 'Process: OS API Execution'
- 'Script: Script Execution'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'File: File Access'
id: attack-pattern--3c4a2599-71ee-4405-ba1e-0e28414b4bc5
mitre_attack_url: https://attack.mitre.org/techniques/T1005
name: Data from Local System
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- collection
title: collection - Data from Local System
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Process: OS API Execution, Script: Script Execution, Command: Command Execution, Process: Process Creation, File: File Access |
| **System Requirements** | Privileges to access certain files and directories |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1005](https://attack.mitre.org/techniques/T1005) |

# Data from Local System (attack-pattern--3c4a2599-71ee-4405-ba1e-0e28414b4bc5)

## Description
Adversaries may search local system sources, such as file systems and configuration files or local databases, to find files of interest and sensitive data prior to Exfiltration.

Adversaries may do this using a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), such as [cmd](https://attack.mitre.org/software/S0106) as well as a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008), which have functionality to interact with the file system to gather information.(Citation: show_run_config_cmd_cisco) Adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on the local system.


## Detection
Monitor processes and command-line arguments for actions that could be taken to collect files from a system. Remote access tools with built-in features may interact directly with the Windows API to gather data. Further, [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands may also be used to collect files such as configuration files with built-in features native to the network device platform.(Citation: Mandiant APT41 Global Intrusion )(Citation: US-CERT-TA18-106A) Monitor CLI activity for unexpected or unauthorized use commands being run by non-standard users from non-standard locations. Data may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

For network infrastructure devices, collect AAA logging to monitor `show` commands that view configuration files. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1005)
- [show_run_config_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_protocols_through_showmon.html#wp2760878733)
- [Mandiant APT41 Global Intrusion ](https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
