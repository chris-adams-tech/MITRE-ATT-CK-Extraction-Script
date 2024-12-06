---
data_sources:
- 'Process: Process Creation'
- 'User Account: User Account Modification'
- 'Command: Command Execution'
- 'Process: OS API Execution'
- 'File: File Modification'
- 'Process: Process Metadata'
- 'File: File Metadata'
- 'Windows Registry: Windows Registry Key Modification'
id: attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b
mitre_attack_url: https://attack.mitre.org/techniques/T1548
name: Abuse Elevation Control Mechanism
platforms:
- Linux
- macOS
- Windows
- IaaS
- Office Suite
- Identity Provider
tactics:
- privilege-escalation
- defense-evasion
title: privilege-escalation - Abuse Elevation Control Mechanism
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, defense-evasion |
| **Platforms** | Linux, macOS, Windows, IaaS, Office Suite, Identity Provider |
| **Data Sources** | Process: Process Creation, User Account: User Account Modification, Command: Command Execution, Process: OS API Execution, File: File Modification, Process: Process Metadata, File: File Metadata, Windows Registry: Windows Registry Key Modification |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1548](https://attack.mitre.org/techniques/T1548) |

# Abuse Elevation Control Mechanism (attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b)

## Description
Adversaries may circumvent mechanisms designed to control elevate privileges to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher risk.(Citation: TechNet How UAC Works)(Citation: sudo man page 2018) An adversary can perform several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system.(Citation: OSX Keydnap malware)(Citation: Fortinet Fareit)

## Detection
Monitor the file system for files that have the setuid or setgid bits set. Also look for any process API calls for behavior that may be indicative of [Process Injection](https://attack.mitre.org/techniques/T1055) and unusual loaded DLLs through [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001), which indicate attempts to gain access to higher privileged processes. On Linux, auditd can alert every time a user's actual ID and effective ID are different (this is what happens when you sudo).

Consider monitoring for <code>/usr/libexec/security_authtrampoline</code> executions which may indicate that AuthorizationExecuteWithPrivileges is being executed. MacOS system logs may also indicate when AuthorizationExecuteWithPrivileges is being called. Monitoring OS API callbacks for the execution can also be a way to detect this behavior but requires specialized security tooling.

On Linux, auditd can alert every time a user's actual ID and effective ID are different (this is what happens when you sudo). This technique is abusing normal functionality in macOS and Linux systems, but sudo has the ability to log all input and output based on the <code>LOG_INPUT</code> and <code>LOG_OUTPUT</code> directives in the <code>/etc/sudoers</code> file.

There are many ways to perform UAC bypasses when a user is in the local administrator group on a system, so it may be difficult to target detection on all variations. Efforts should likely be placed on mitigation and collecting enough information on process launches and actions that could be performed before and after a UAC bypass is performed. Some UAC bypass methods rely on modifying specific, user-accessible Registry settings. Analysts should monitor Registry settings for unauthorized changes.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1548)
- [TechNet How UAC Works](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/how-user-account-control-works)
- [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
- [Fortinet Fareit](https://blog.fortinet.com/2016/12/16/malicious-macro-bypasses-uac-to-elevate-privilege-for-fareit-malware)
- [sudo man page 2018](https://www.sudo.ws/)
