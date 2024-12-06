---
data_sources:
- 'Command: Command Execution'
- 'Active Directory: Active Directory Object Modification'
- 'Process: Process Creation'
- 'File: File Metadata'
id: attack-pattern--34e793de-0274-4982-9c1a-246ed1c19dee
mitre_attack_url: https://attack.mitre.org/techniques/T1222/001
name: Windows File and Directory Permissions Modification
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Windows File and Directory Permissions Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Active Directory: Active Directory Object Modification, Process: Process Creation, File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1222/001](https://attack.mitre.org/techniques/T1222/001) |

# Windows File and Directory Permissions Modification (attack-pattern--34e793de-0274-4982-9c1a-246ed1c19dee)

## Description
Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Windows implements file and directory ACLs as Discretionary Access Control Lists (DACLs).(Citation: Microsoft DACL May 2018) Similar to a standard ACL, DACLs identifies the accounts that are allowed or denied access to a securable object. When an attempt is made to access a securable object, the system checks the access control entries in the DACL in order. If a matching entry is found, access to the object is granted. Otherwise, access is denied.(Citation: Microsoft Access Control Lists May 2018)

Adversaries can interact with the DACLs using built-in Windows commands, such as `icacls`, `cacls`, `takeown`, and `attrib`, which can grant adversaries higher permissions on specific files and folders. Further, [PowerShell](https://attack.mitre.org/techniques/T1059/001) provides cmdlets that can be used to retrieve or modify file and directory DACLs. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [Accessibility Features](https://attack.mitre.org/techniques/T1546/008), [Boot or Logon Initialization Scripts](https://attack.mitre.org/techniques/T1037), or tainting/hijacking other instrumental binary/configuration files via [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574).

## Detection
Monitor and investigate attempts to modify DACLs and file/directory ownership. Many of the commands used to modify DACLs and file/directory ownership are built-in system utilities and may generate a high false positive alert rate, so compare against baseline knowledge for how systems are typically used and correlate modification events with other indications of malicious activity where possible.

Consider enabling file/directory permission change auditing on folders containing key binary/configuration files. For example, Windows Security Log events (Event ID 4670) are created when DACLs are modified.(Citation: EventTracker File Permissions Feb 2014)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1222/001)
- [Hybrid Analysis Icacls1 June 2018](https://www.hybrid-analysis.com/sample/ef0d2628823e8e0a0de3b08b8eacaf41cf284c086a948bdfd67f4e4373c14e4d?environmentId=100)
- [Hybrid Analysis Icacls2 May 2018](https://www.hybrid-analysis.com/sample/22dab012c3e20e3d9291bce14a2bfc448036d3b966c6e78167f4626f5f9e38d6?environmentId=110)
- [Microsoft Access Control Lists May 2018](https://docs.microsoft.com/en-us/windows/win32/secauthz/access-control-lists)
- [Microsoft DACL May 2018](https://docs.microsoft.com/windows/desktop/secauthz/dacls-and-aces)
- [EventTracker File Permissions Feb 2014](https://www.eventtracker.com/tech-articles/monitoring-file-permission-changes-windows-security-log/)
