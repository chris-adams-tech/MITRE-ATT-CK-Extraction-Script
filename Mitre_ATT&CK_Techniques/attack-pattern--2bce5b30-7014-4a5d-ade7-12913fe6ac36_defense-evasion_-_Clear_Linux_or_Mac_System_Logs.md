---
data_sources:
- 'File: File Deletion'
- 'File: File Modification'
- 'Command: Command Execution'
id: attack-pattern--2bce5b30-7014-4a5d-ade7-12913fe6ac36
mitre_attack_url: https://attack.mitre.org/techniques/T1070/002
name: Clear Linux or Mac System Logs
platforms:
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - Clear Linux or Mac System Logs
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS |
| **Data Sources** | File: File Deletion, File: File Modification, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1070/002](https://attack.mitre.org/techniques/T1070/002) |

# Clear Linux or Mac System Logs (attack-pattern--2bce5b30-7014-4a5d-ade7-12913fe6ac36)

## Description
Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the <code>/var/log/</code> directory. Subfolders in this directory categorize logs by their related functions, such as:(Citation: Linux Logs)

* <code>/var/log/messages:</code>: General and system-related messages
* <code>/var/log/secure</code> or <code>/var/log/auth.log</code>: Authentication logs
* <code>/var/log/utmp</code> or <code>/var/log/wtmp</code>: Login records
* <code>/var/log/kern.log</code>: Kernel logs
* <code>/var/log/cron.log</code>: Crond logs
* <code>/var/log/maillog</code>: Mail server logs
* <code>/var/log/httpd/</code>: Web server access and error logs


## Detection
File system monitoring may be used to detect improper deletion or modification of indicator files. Also monitor for suspicious processes interacting with log files.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1070/002)
- [Linux Logs](https://www.eurovps.com/blog/important-linux-log-files-you-must-be-monitoring/)
