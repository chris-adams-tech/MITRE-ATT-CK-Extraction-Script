---
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--348f1eef-964b-4eb6-bb53-69b3dcb0c643
mitre_attack_url: https://attack.mitre.org/techniques/T1120
name: Peripheral Device Discovery
platforms:
- Windows
- macOS
- Linux
tactics:
- discovery
title: discovery - Peripheral Device Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Process: OS API Execution, Process: Process Creation, Command: Command Execution |
| **Permissions Required** | User, Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1120](https://attack.mitre.org/techniques/T1120) |

# Peripheral Device Discovery (attack-pattern--348f1eef-964b-4eb6-bb53-69b3dcb0c643)

## Description
Adversaries may attempt to gather information about attached peripheral devices and components connected to a computer system.(Citation: Peripheral Discovery Linux)(Citation: Peripheral Discovery macOS) Peripheral devices could include auxiliary resources that support a variety of functionalities such as keyboards, printers, cameras, smart card readers, or removable storage. The information may be used to enhance their awareness of the system and network environment or may be used for further actions.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1120)
- [Peripheral Discovery Linux](https://linuxhint.com/list-usb-devices-linux/)
- [Peripheral Discovery macOS](https://ss64.com/osx/system_profiler.html)
