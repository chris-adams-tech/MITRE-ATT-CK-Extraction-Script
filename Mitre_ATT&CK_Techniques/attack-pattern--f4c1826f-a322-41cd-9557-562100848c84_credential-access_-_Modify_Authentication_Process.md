---
contributors:
- Chris Ross @xorrior
data_sources:
- 'Application Log: Application Log Content'
- 'Process: Process Access'
- 'Logon Session: Logon Session Creation'
- 'Active Directory: Active Directory Object Modification'
- 'User Account: User Account Authentication'
- 'Process: OS API Execution'
- 'Windows Registry: Windows Registry Key Creation'
- 'File: File Creation'
- 'User Account: User Account Modification'
- 'File: File Modification'
- 'Module: Module Load'
- 'Cloud Service: Cloud Service Modification'
- 'Windows Registry: Windows Registry Key Modification'
id: attack-pattern--f4c1826f-a322-41cd-9557-562100848c84
mitre_attack_url: https://attack.mitre.org/techniques/T1556
name: Modify Authentication Process
platforms:
- Windows
- Linux
- macOS
- Network
- IaaS
- SaaS
- Office Suite
- Identity Provider
tactics:
- credential-access
- defense-evasion
- persistence
title: credential-access - Modify Authentication Process
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, defense-evasion, persistence |
| **Platforms** | Windows, Linux, macOS, Network, IaaS, SaaS, Office Suite, Identity Provider |
| **Data Sources** | Application Log: Application Log Content, Process: Process Access, Logon Session: Logon Session Creation, Active Directory: Active Directory Object Modification, User Account: User Account Authentication, Process: OS API Execution, Windows Registry: Windows Registry Key Creation, File: File Creation, User Account: User Account Modification, File: File Modification, Module: Module Load, Cloud Service: Cloud Service Modification, Windows Registry: Windows Registry Key Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1556](https://attack.mitre.org/techniques/T1556) |

# Modify Authentication Process (attack-pattern--f4c1826f-a322-41cd-9557-562100848c84)

## Description
Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise unwarranted access to accounts. The authentication process is handled by mechanisms, such as the Local Security Authentication Server (LSASS) process and the Security Accounts Manager (SAM) on Windows, pluggable authentication modules (PAM) on Unix-based systems, and authorization plugins on MacOS systems, responsible for gathering, storing, and validating credentials. By modifying an authentication process, an adversary may be able to authenticate to a service or system without using [Valid Accounts](https://attack.mitre.org/techniques/T1078).

Adversaries may maliciously modify a part of this process to either reveal credentials or bypass authentication mechanisms. Compromised credentials or access may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access and remote desktop.

## Detection
Monitor for new, unfamiliar DLL files written to a domain controller and/or local computer. Monitor for changes to Registry entries for password filters (ex: <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages</code>) and correlate then investigate the DLL files these files reference. 

Password filters will also show up as an autorun and loaded DLL in lsass.exe.(Citation: Clymb3r Function Hook Passwords Sept 2013)

Monitor for calls to <code>OpenProcess</code> that can be used to manipulate lsass.exe running on a domain controller as well as for malicious modifications to functions exported from authentication-related system DLLs (such as cryptdll.dll and samsrv.dll).(Citation: Dell Skeleton) 

Monitor PAM configuration and module paths (ex: <code>/etc/pam.d/</code>) for changes. Use system-integrity tools such as AIDE and monitoring tools such as auditd to monitor PAM files.

Monitor for suspicious additions to the /Library/Security/SecurityAgentPlugins directory.(Citation: Xorrior Authorization Plugins)

Configure robust, consistent account activity audit policies across the enterprise and with externally accessible services. (Citation: TechNet Audit Policy) Look for suspicious account behavior across systems that share accounts, either user, admin, or service accounts. Examples: one account logged into multiple systems simultaneously; multiple accounts logged into the same machine simultaneously; accounts logged in at odd times or outside of business hours. Activity may be from interactive login sessions or process ownership from accounts being used to execute binaries on a remote system as a particular account. Correlate other security systems with login information (e.g., a user has an active login session but has not entered the building or does not have VPN access).

Monitor property changes in Group Policy that manage authentication mechanisms (i.e. [Group Policy Modification](https://attack.mitre.org/techniques/T1484/001)). The <code>Store passwords using reversible encryption</code> configuration should be set to Disabled. Additionally, monitor and/or block suspicious command/script execution of <code>-AllowReversiblePasswordEncryption $true</code>, <code>Set-ADUser</code> and <code>Set-ADAccountControl</code>. Finally, monitor Fine-Grained Password Policies and regularly audit user accounts and group settings.(Citation: dump_pwd_dcsync)


## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1556)
- [Clymb3r Function Hook Passwords Sept 2013](https://clymb3r.wordpress.com/2013/09/15/intercepting-password-changes-with-function-hooking/)
- [Xorrior Authorization Plugins](https://xorrior.com/persistent-credential-theft/)
- [Dell Skeleton](https://www.secureworks.com/research/skeleton-key-malware-analysis)
- [dump_pwd_dcsync](https://adsecurity.org/?p=2053)
- [TechNet Audit Policy](https://technet.microsoft.com/en-us/library/dn487457.aspx)
