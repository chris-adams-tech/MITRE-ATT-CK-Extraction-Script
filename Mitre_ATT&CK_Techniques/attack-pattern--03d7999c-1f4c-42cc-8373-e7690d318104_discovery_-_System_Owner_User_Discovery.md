---
contributors:
- Austin Clark, @c2defense
data_sources:
- 'Active Directory: Active Directory Object Access'
- 'Process: OS API Execution'
- 'Command: Command Execution'
- 'Network Traffic: Network Traffic Content'
- 'Process: Process Creation'
- 'Network Traffic: Network Traffic Flow'
- 'Windows Registry: Windows Registry Key Access'
- 'File: File Access'
- 'Process: Process Access'
id: attack-pattern--03d7999c-1f4c-42cc-8373-e7690d318104
mitre_attack_url: https://attack.mitre.org/techniques/T1033
name: System Owner/User Discovery
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- discovery
title: discovery - System Owner/User Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Active Directory: Active Directory Object Access, Process: OS API Execution, Command: Command Execution, Network Traffic: Network Traffic Content, Process: Process Creation, Network Traffic: Network Traffic Flow, Windows Registry: Windows Registry Key Access, File: File Access, Process: Process Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1033](https://attack.mitre.org/techniques/T1033) |

# System Owner/User Discovery (attack-pattern--03d7999c-1f4c-42cc-8373-e7690d318104)

## Description
Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from [System Owner/User Discovery](https://attack.mitre.org/techniques/T1033) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Various utilities and commands may acquire this information, including <code>whoami</code>. In macOS and Linux, the currently logged in user can be identified with <code>w</code> and <code>who</code>. On macOS the <code>dscl . list /Users | grep -v '_'</code> command can also be used to enumerate user accounts. Environment variables, such as <code>%USERNAME%</code> and <code>$USER</code>, may also be used to access this information.

On network devices, [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `show users` and `show ssh` can be used to display users currently logged into the device.(Citation: show_ssh_users_cmd_cisco)(Citation: US-CERT TA18-106A Network Infrastructure Devices 2018)

## Detection
`System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

For network infrastructure devices, collect AAA logging to monitor `show` commands being run by non-standard users from non-standard locations.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1033)
- [show_ssh_users_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s5.html)
- [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)
