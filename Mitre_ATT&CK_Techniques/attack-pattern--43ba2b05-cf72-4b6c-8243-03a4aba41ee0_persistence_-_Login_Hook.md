---
data_sources:
- 'File: File Creation'
- 'File: File Modification'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--43ba2b05-cf72-4b6c-8243-03a4aba41ee0
mitre_attack_url: https://attack.mitre.org/techniques/T1037/002
name: Login Hook
platforms:
- macOS
tactics:
- persistence
- privilege-escalation
title: persistence - Login Hook
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS |
| **Data Sources** | File: File Creation, File: File Modification, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1037/002](https://attack.mitre.org/techniques/T1037/002) |

# Login Hook (attack-pattern--43ba2b05-cf72-4b6c-8243-03a4aba41ee0)

## Description
Adversaries may use a Login Hook to establish persistence executed upon user logon. A login hook is a plist file that points to a specific script to execute with root privileges upon user logon. The plist file is located in the <code>/Library/Preferences/com.apple.loginwindow.plist</code> file and can be modified using the <code>defaults</code> command-line utility. This behavior is the same for logout hooks where a script can be executed upon user logout. All hooks require administrator permissions to modify or create hooks.(Citation: Login Scripts Apple Dev)(Citation: LoginWindowScripts Apple Dev) 

Adversaries can add or insert a path to a malicious script in the <code>com.apple.loginwindow.plist</code> file, using the <code>LoginHook</code> or <code>LogoutHook</code> key-value pair. The malicious script is executed upon the next user login. If a login hook already exists, adversaries can add additional commands to an existing login hook. There can be only one login and logout hook on a system at a time.(Citation: S1 macOs Persistence)(Citation: Wardle Persistence Chapter)

**Note:** Login hooks were deprecated in 10.11 version of macOS in favor of [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) and [Launch Agent](https://attack.mitre.org/techniques/T1543/001) 

## Detection
Monitor logon scripts for unusual access by abnormal users or at abnormal times. Look for files added or modified by unusual accounts outside of normal administration duties. Monitor running process for actions that could be indicative of abnormal programs or executables running upon logon.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1037/002)
- [Login Scripts Apple Dev](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CustomLogin.html)
- [LoginWindowScripts Apple Dev](https://developer.apple.com/documentation/devicemanagement/loginwindowscripts)
- [Wardle Persistence Chapter](https://taomm.org/PDFs/vol1/CH%200x02%20Persistence.pdf)
- [S1 macOs Persistence](https://www.sentinelone.com/blog/how-malware-persists-on-macos/)
