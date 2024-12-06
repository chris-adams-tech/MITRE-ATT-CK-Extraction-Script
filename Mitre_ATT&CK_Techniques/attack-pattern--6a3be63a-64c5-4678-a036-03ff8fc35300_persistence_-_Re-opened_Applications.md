---
id: attack-pattern--6a3be63a-64c5-4678-a036-03ff8fc35300
mitre_attack_url: https://attack.mitre.org/techniques/T1164
name: Re-opened Applications
platforms:
- macOS
tactics:
- persistence
title: persistence - Re-opened Applications
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1164](https://attack.mitre.org/techniques/T1164) |

# Re-opened Applications (attack-pattern--6a3be63a-64c5-4678-a036-03ff8fc35300)

## Description
Starting in Mac OS X 10.7 (Lion), users can specify certain applications to be re-opened when a user reboots their machine. While this is usually done via a Graphical User Interface (GUI) on an app-by-app basis, there are property list files (plist) that contain this information as well located at <code>~/Library/Preferences/com.apple.loginwindow.plist</code> and <code>~/Library/Preferences/ByHost/com.apple.loginwindow.* .plist</code>. 

An adversary can modify one of these files directly to include a link to their malicious executable to provide a persistence mechanism each time the user reboots their machine (Citation: Methods of Mac Malware Persistence).

## Detection
Monitoring the specific plist files associated with reopening applications can indicate when an application has registered itself to be reopened.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1164)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
