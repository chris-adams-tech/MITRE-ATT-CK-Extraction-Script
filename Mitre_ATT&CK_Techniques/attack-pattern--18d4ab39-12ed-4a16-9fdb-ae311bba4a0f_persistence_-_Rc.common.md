---
id: attack-pattern--18d4ab39-12ed-4a16-9fdb-ae311bba4a0f
mitre_attack_url: https://attack.mitre.org/techniques/T1163
name: Rc.common
platforms:
- macOS
tactics:
- persistence
title: persistence - Rc.common
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | macOS |
| **Permissions Required** | root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1163](https://attack.mitre.org/techniques/T1163) |

# Rc.common (attack-pattern--18d4ab39-12ed-4a16-9fdb-ae311bba4a0f)

## Description
During the boot process, macOS executes <code>source /etc/rc.common</code>, which is a shell script containing various utility functions. This file also defines routines for processing command-line arguments and for gathering system settings, and is thus recommended to include in the start of Startup Item Scripts (Citation: Startup Items). In macOS and OS X, this is now a deprecated technique in favor of launch agents and launch daemons, but is currently still used.

Adversaries can use the rc.common file as a way to hide code for persistence that will execute on each reboot as the root user (Citation: Methods of Mac Malware Persistence).

## Detection
The <code>/etc/rc.common</code> file can be monitored to detect changes from the company policy. Monitor process execution resulting from the rc.common script for unusual or unknown applications or behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1163)
- [Startup Items](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
