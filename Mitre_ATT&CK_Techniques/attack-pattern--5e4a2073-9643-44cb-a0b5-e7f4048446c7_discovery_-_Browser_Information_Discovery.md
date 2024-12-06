---
contributors:
- Mike Kemmerer
- Manikantan Srinivasan, NEC Corporation India
- Yinon Engelsman, Talon Cyber Security
- Yonatan Gotlib, Talon Cyber Security
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'File: File Access'
id: attack-pattern--5e4a2073-9643-44cb-a0b5-e7f4048446c7
mitre_attack_url: https://attack.mitre.org/techniques/T1217
name: Browser Information Discovery
platforms:
- Linux
- Windows
- macOS
tactics:
- discovery
title: discovery - Browser Information Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Process: Process Creation, Command: Command Execution, File: File Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1217](https://attack.mitre.org/techniques/T1217) |

# Browser Information Discovery (attack-pattern--5e4a2073-9643-44cb-a0b5-e7f4048446c7)

## Description
Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure.(Citation: Kaspersky Autofill)

Browser information may also highlight additional targets after an adversary has access to valid credentials, especially [Credentials In Files](https://attack.mitre.org/techniques/T1552/001) associated with logins cached by a browser.

Specific storage locations vary based on platform and/or application, but browser information is typically stored in local files and databases (e.g., `%APPDATA%/Google/Chrome`).(Citation: Chrome Roaming Profiles)

## Detection
Monitor processes and command-line arguments for actions that could be taken to gather browser bookmark information. Remote access tools with built-in features may interact directly using APIs to gather information. Information may also be acquired through system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Collection and Exfiltration, based on the information obtained.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1217)
- [Chrome Roaming Profiles](https://support.google.com/chrome/a/answer/7349337)
- [Kaspersky Autofill](https://www.kaspersky.com/blog/browser-data-theft/27871/)
