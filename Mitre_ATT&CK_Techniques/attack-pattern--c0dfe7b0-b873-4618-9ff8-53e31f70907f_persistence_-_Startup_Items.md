---
data_sources:
- 'Command: Command Execution'
- 'File: File Creation'
- 'Process: Process Creation'
- 'File: File Modification'
id: attack-pattern--c0dfe7b0-b873-4618-9ff8-53e31f70907f
mitre_attack_url: https://attack.mitre.org/techniques/T1037/005
name: Startup Items
platforms:
- macOS
tactics:
- persistence
- privilege-escalation
title: persistence - Startup Items
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS |
| **Data Sources** | Command: Command Execution, File: File Creation, Process: Process Creation, File: File Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1037/005](https://attack.mitre.org/techniques/T1037/005) |

# Startup Items (attack-pattern--c0dfe7b0-b873-4618-9ff8-53e31f70907f)

## Description
Adversaries may use startup items automatically executed at boot initialization to establish persistence. Startup items execute during the final phase of the boot process and contain shell scripts or other executable files along with configuration information used by the system to determine the execution order for all startup items.(Citation: Startup Items)

This is technically a deprecated technology (superseded by [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)), and thus the appropriate folder, <code>/Library/StartupItems</code> isn’t guaranteed to exist on the system by default, but does appear to exist by default on macOS Sierra. A startup item is a directory whose executable and configuration property list (plist), <code>StartupParameters.plist</code>, reside in the top-level directory. 

An adversary can create the appropriate folders/files in the StartupItems directory to register their own persistence mechanism.(Citation: Methods of Mac Malware Persistence) Additionally, since StartupItems run during the bootup phase of macOS, they will run as the elevated root user.

## Detection
The <code>/Library/StartupItems</code> folder can be monitored for changes. Similarly, the programs that are actually executed from this mechanism should be checked against a whitelist.

Monitor processes that are executed during the bootup process to check for unusual or unknown applications and behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1037/005)
- [Startup Items](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
