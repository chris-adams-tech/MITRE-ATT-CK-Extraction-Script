---
contributors:
- John Lambert, Microsoft Threat Intelligence Center
data_sources:
- 'File: File Modification'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Metadata'
- 'Process: OS API Execution'
- 'Driver: Driver Load'
id: attack-pattern--bb5a00de-e086-4859-a231-fa793f6797e2
mitre_attack_url: https://attack.mitre.org/techniques/T1056
name: Input Capture
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- collection
- credential-access
title: collection - Input Capture
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection, credential-access |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | File: File Modification, Process: Process Creation, Windows Registry: Windows Registry Key Modification, Process: Process Metadata, Process: OS API Execution, Driver: Driver Load |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1056](https://attack.mitre.org/techniques/T1056) |

# Input Capture (attack-pattern--bb5a00de-e086-4859-a231-fa793f6797e2)

## Description
Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [Credential API Hooking](https://attack.mitre.org/techniques/T1056/004)) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. [Web Portal Capture](https://attack.mitre.org/techniques/T1056/003)).

## Detection
Detection may vary depending on how input is captured but may include monitoring for certain Windows API calls (e.g. `SetWindowsHook`, `GetKeyState`, and `GetAsyncKeyState`)(Citation: Adventures of a Keystroke), monitoring for malicious instances of [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), and ensuring no unauthorized drivers or kernel modules that could indicate keylogging or API hooking are present.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1056)
- [Adventures of a Keystroke](http://opensecuritytraining.info/Keylogging_files/The%20Adventures%20of%20a%20Keystroke.pdf)
