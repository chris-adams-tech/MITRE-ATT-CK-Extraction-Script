---
data_sources:
- 'Command: Command Execution'
- 'File: File Modification'
id: attack-pattern--e5cc9e7a-e61a-46a1-b869-55fb6eab058e
mitre_attack_url: https://attack.mitre.org/techniques/T1547/007
name: Re-opened Applications
platforms:
- macOS
tactics:
- persistence
- privilege-escalation
title: persistence - Re-opened Applications
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS |
| **Data Sources** | Command: Command Execution, File: File Modification |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/007](https://attack.mitre.org/techniques/T1547/007) |

# Re-opened Applications (attack-pattern--e5cc9e7a-e61a-46a1-b869-55fb6eab058e)

## Description
Adversaries may modify plist files to automatically run an application when a user logs in. When a user logs out or restarts via the macOS Graphical User Interface (GUI), a prompt is provided to the user with a checkbox to "Reopen windows when logging back in".(Citation: Re-Open windows on Mac) When selected, all applications currently open are added to a property list file named <code>com.apple.loginwindow.[UUID].plist</code> within the <code>~/Library/Preferences/ByHost</code> directory.(Citation: Methods of Mac Malware Persistence)(Citation: Wardle Persistence Chapter) Applications listed in this file are automatically reopened upon the user’s next logon.

Adversaries can establish [Persistence](https://attack.mitre.org/tactics/TA0003) by adding a malicious application path to the <code>com.apple.loginwindow.[UUID].plist</code> file to execute payloads when a user logs in.

## Detection
Monitoring the specific plist files associated with reopening applications can indicate when an application has registered itself to be reopened.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/007)
- [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [Wardle Persistence Chapter](https://taomm.org/PDFs/vol1/CH%200x02%20Persistence.pdf)
