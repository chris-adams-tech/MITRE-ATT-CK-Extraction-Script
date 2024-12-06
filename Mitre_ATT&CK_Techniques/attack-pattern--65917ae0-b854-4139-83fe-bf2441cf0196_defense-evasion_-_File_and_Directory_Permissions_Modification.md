---
contributors:
- CrowdStrike Falcon OverWatch
- Jan Miller, CrowdStrike
data_sources:
- 'Process: Process Creation'
- 'Active Directory: Active Directory Object Modification'
- 'Command: Command Execution'
- 'File: File Metadata'
id: attack-pattern--65917ae0-b854-4139-83fe-bf2441cf0196
mitre_attack_url: https://attack.mitre.org/techniques/T1222
name: File and Directory Permissions Modification
platforms:
- Linux
- Windows
- macOS
tactics:
- defense-evasion
title: defense-evasion - File and Directory Permissions Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Process: Process Creation, Active Directory: Active Directory Object Modification, Command: Command Execution, File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1222](https://attack.mitre.org/techniques/T1222) |

# File and Directory Permissions Modification (attack-pattern--65917ae0-b854-4139-83fe-bf2441cf0196)

## Description
Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Modifications may include changing specific access rights, which may require taking ownership of a file or directory and/or elevated permissions depending on the file or directory’s existing permissions. This may enable malicious activity such as modifying, replacing, or deleting specific files or directories. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [Accessibility Features](https://attack.mitre.org/techniques/T1546/008), [Boot or Logon Initialization Scripts](https://attack.mitre.org/techniques/T1037), [Unix Shell Configuration Modification](https://attack.mitre.org/techniques/T1546/004), or tainting/hijacking other instrumental binary/configuration files via [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574).

Adversaries may also change permissions of symbolic links. For example, malware (particularly ransomware) may modify symbolic links and associated settings to enable access to files from local shortcuts with remote paths.(Citation: new_rust_based_ransomware)(Citation: bad_luck_blackcat)(Citation: falconoverwatch_blackcat_attack)(Citation: blackmatter_blackcat)(Citation: fsutil_behavior) 

## Detection
Monitor and investigate attempts to modify ACLs and file/directory ownership. Many of the commands used to modify ACLs and file/directory ownership are built-in system utilities and may generate a high false positive alert rate, so compare against baseline knowledge for how systems are typically used and correlate modification events with other indications of malicious activity where possible.

Consider enabling file/directory permission change auditing on folders containing key binary/configuration files. For example, Windows Security Log events (Event ID 4670) are created when DACLs are modified.(Citation: EventTracker File Permissions Feb 2014)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1222)
- [falconoverwatch_blackcat_attack](https://www.crowdstrike.com/blog/falcon-overwatch-contributes-to-blackcat-protection/)
- [Hybrid Analysis Icacls1 June 2018](https://www.hybrid-analysis.com/sample/ef0d2628823e8e0a0de3b08b8eacaf41cf284c086a948bdfd67f4e4373c14e4d?environmentId=100)
- [Hybrid Analysis Icacls2 May 2018](https://www.hybrid-analysis.com/sample/22dab012c3e20e3d9291bce14a2bfc448036d3b966c6e78167f4626f5f9e38d6?environmentId=110)
- [bad_luck_blackcat](https://go.kaspersky.com/rs/802-IJN-240/images/TR_BlackCat_Report.pdf)
- [fsutil_behavior](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-behavior)
- [EventTracker File Permissions Feb 2014](https://www.eventtracker.com/tech-articles/monitoring-file-permission-changes-windows-security-log/)
- [blackmatter_blackcat](https://blog.talosintelligence.com/2022/03/from-blackmatter-to-blackcat-analyzing.html)
- [new_rust_based_ransomware](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/noberus-blackcat-alphv-rust-ransomware)
