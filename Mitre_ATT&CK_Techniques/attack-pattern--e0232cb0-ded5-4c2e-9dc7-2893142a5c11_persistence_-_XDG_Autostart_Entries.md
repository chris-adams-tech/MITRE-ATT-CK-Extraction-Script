---
contributors:
- Tony Lambert, Red Canary
data_sources:
- 'File: File Creation'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'File: File Modification'
id: attack-pattern--e0232cb0-ded5-4c2e-9dc7-2893142a5c11
mitre_attack_url: https://attack.mitre.org/techniques/T1547/013
name: XDG Autostart Entries
platforms:
- Linux
tactics:
- persistence
- privilege-escalation
title: persistence - XDG Autostart Entries
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Linux |
| **Data Sources** | File: File Creation, Command: Command Execution, Process: Process Creation, File: File Modification |
| **Permissions Required** | User, root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/013](https://attack.mitre.org/techniques/T1547/013) |

# XDG Autostart Entries (attack-pattern--e0232cb0-ded5-4c2e-9dc7-2893142a5c11)

## Description
Adversaries may add or modify XDG Autostart Entries to execute malicious programs or commands when a user’s desktop environment is loaded at login. XDG Autostart entries are available for any XDG-compliant Linux system. XDG Autostart entries use Desktop Entry files (`.desktop`) to configure the user’s desktop environment upon user login. These configuration files determine what applications launch upon user login, define associated applications to open specific file types, and define applications used to open removable media.(Citation: Free Desktop Application Autostart Feb 2006)(Citation: Free Desktop Entry Keys)

Adversaries may abuse this feature to establish persistence by adding a path to a malicious binary or command to the `Exec` directive in the `.desktop` configuration file. When the user’s desktop environment is loaded at user login, the `.desktop` files located in the XDG Autostart directories are automatically executed. System-wide Autostart entries are located in the `/etc/xdg/autostart` directory while the user entries are located in the `~/.config/autostart` directory.

Adversaries may combine this technique with [Masquerading](https://attack.mitre.org/techniques/T1036) to blend malicious Autostart entries with legitimate programs.(Citation: Red Canary Netwire Linux 2022)

## Detection
Malicious XDG autostart entries may be detected by auditing file creation and modification events within the <code>/etc/xdg/autostart</code> and <code>~/.config/autostart</code> directories. Depending on individual configurations, defenders may need to query the environment variables <code>$XDG_CONFIG_HOME</code> or <code>$XDG_CONFIG_DIRS</code> to determine the paths of Autostart entries. Autostart entry files not associated with legitimate packages may be considered suspicious. Suspicious entries can also be identified by comparing entries to a trusted system baseline.
 
Suspicious processes or scripts spawned in this manner will have a parent process of the desktop component implementing the XDG specification and will execute as the logged on user.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/013)
- [Free Desktop Application Autostart Feb 2006](https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html)
- [Free Desktop Entry Keys](https://specifications.freedesktop.org/desktop-entry-spec/1.2/ar01s06.html)
- [Red Canary Netwire Linux 2022](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
