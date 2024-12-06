---
id: attack-pattern--2ba5aa71-9d15-4b22-b726-56af06d9ad2f
mitre_attack_url: https://attack.mitre.org/techniques/T1165
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
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1165](https://attack.mitre.org/techniques/T1165) |

# Startup Items (attack-pattern--2ba5aa71-9d15-4b22-b726-56af06d9ad2f)

## Description
Per Apple’s documentation, startup items execute during the final phase of the boot process and contain shell scripts or other executable files along with configuration information used by the system to determine the execution order for all startup items (Citation: Startup Items). This is technically a deprecated version (superseded by Launch Daemons), and thus the appropriate folder, <code>/Library/StartupItems</code> isn’t guaranteed to exist on the system by default, but does appear to exist by default on macOS Sierra. A startup item is a directory whose executable and configuration property list (plist), <code>StartupParameters.plist</code>, reside in the top-level directory. 

An adversary can create the appropriate folders/files in the StartupItems directory to register their own persistence mechanism (Citation: Methods of Mac Malware Persistence). Additionally, since StartupItems run during the bootup phase of macOS, they will run as root. If an adversary is able to modify an existing Startup Item, then they will be able to Privilege Escalate as well.

## Detection
The <code>/Library/StartupItems</code> folder can be monitored for changes. Similarly, the programs that are actually executed from this mechanism should be checked against a whitelist. Monitor processes that are executed during the bootup process to check for unusual or unknown applications and behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1165)
- [Startup Items](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
