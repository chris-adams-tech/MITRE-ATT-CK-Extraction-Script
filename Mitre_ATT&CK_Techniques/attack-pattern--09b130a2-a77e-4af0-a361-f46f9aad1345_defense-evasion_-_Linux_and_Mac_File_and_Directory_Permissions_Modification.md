---
data_sources:
- 'Process: Process Creation'
- 'File: File Metadata'
- 'Command: Command Execution'
id: attack-pattern--09b130a2-a77e-4af0-a361-f46f9aad1345
mitre_attack_url: https://attack.mitre.org/techniques/T1222/002
name: Linux and Mac File and Directory Permissions Modification
platforms:
- macOS
- Linux
tactics:
- defense-evasion
title: defense-evasion - Linux and Mac File and Directory Permissions Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Linux |
| **Data Sources** | Process: Process Creation, File: File Metadata, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1222/002](https://attack.mitre.org/techniques/T1222/002) |

# Linux and Mac File and Directory Permissions Modification (attack-pattern--09b130a2-a77e-4af0-a361-f46f9aad1345)

## Description
Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Most Linux and Linux-based platforms provide a standard set of permission groups (user, group, and other) and a standard set of permissions (read, write, and execute) that are applied to each group. While nuances of each platform’s permissions implementation may vary, most of the platforms provide two primary commands used to manipulate file and directory ACLs: <code>chown</code> (short for change owner), and <code>chmod</code> (short for change mode).

Adversarial may use these commands to make themselves the owner of files and directories or change the mode if current permissions allow it. They could subsequently lock others out of the file. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [Unix Shell Configuration Modification](https://attack.mitre.org/techniques/T1546/004) or tainting/hijacking other instrumental binary/configuration files via [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574).(Citation: 20 macOS Common Tools and Techniques) 

## Detection
Monitor and investigate attempts to modify ACLs and file/directory ownership. Many of the commands used to modify ACLs and file/directory ownership are built-in system utilities and may generate a high false positive alert rate, so compare against baseline knowledge for how systems are typically used and correlate modification events with other indications of malicious activity where possible. Commonly abused command arguments include <code>chmod +x</code>, <code>chmod -R 755</code>, and <code>chmod 777</code>.(Citation: 20 macOS Common Tools and Techniques) 

Consider enabling file/directory permission change auditing on folders containing key binary/configuration files.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1222/002)
- [Hybrid Analysis Icacls1 June 2018](https://www.hybrid-analysis.com/sample/ef0d2628823e8e0a0de3b08b8eacaf41cf284c086a948bdfd67f4e4373c14e4d?environmentId=100)
- [Hybrid Analysis Icacls2 May 2018](https://www.hybrid-analysis.com/sample/22dab012c3e20e3d9291bce14a2bfc448036d3b966c6e78167f4626f5f9e38d6?environmentId=110)
- [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
