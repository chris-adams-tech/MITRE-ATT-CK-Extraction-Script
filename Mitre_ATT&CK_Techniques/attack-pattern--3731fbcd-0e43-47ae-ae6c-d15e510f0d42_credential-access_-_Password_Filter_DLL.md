---
contributors:
- Vincent Le Toux
data_sources:
- 'Windows Registry: Windows Registry Key Modification'
- 'File: File Creation'
- 'Module: Module Load'
id: attack-pattern--3731fbcd-0e43-47ae-ae6c-d15e510f0d42
mitre_attack_url: https://attack.mitre.org/techniques/T1556/002
name: Password Filter DLL
platforms:
- Windows
tactics:
- credential-access
- defense-evasion
- persistence
title: credential-access - Password Filter DLL
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, defense-evasion, persistence |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Modification, File: File Creation, Module: Module Load |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1556/002](https://attack.mitre.org/techniques/T1556/002) |

# Password Filter DLL (attack-pattern--3731fbcd-0e43-47ae-ae6c-d15e510f0d42)

## Description
Adversaries may register malicious password filter dynamic link libraries (DLLs) into the authentication process to acquire user credentials as they are validated. 

Windows password filters are password policy enforcement mechanisms for both domain and local accounts. Filters are implemented as DLLs containing a method to validate potential passwords against password policies. Filter DLLs can be positioned on local computers for local accounts and/or domain controllers for domain accounts. Before registering new passwords in the Security Accounts Manager (SAM), the Local Security Authority (LSA) requests validation from each registered filter. Any potential changes cannot take effect until every registered filter acknowledges validation. 

Adversaries can register malicious password filters to harvest credentials from local computers and/or entire domains. To perform proper validation, filters must receive plain-text credentials from the LSA. A malicious password filter would receive these plain-text credentials every time a password request is made.(Citation: Carnal Ownage Password Filters Sept 2013)

## Detection
Monitor for new, unfamiliar DLL files written to a domain controller and/or local computer. Monitor for changes to Registry entries for password filters (ex: <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages</code>) and correlate then investigate the DLL files these files reference.

Password filters will also show up as an autorun and loaded DLL in lsass.exe.(Citation: Clymb3r Function Hook Passwords Sept 2013)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1556/002)
- [Clymb3r Function Hook Passwords Sept 2013](https://clymb3r.wordpress.com/2013/09/15/intercepting-password-changes-with-function-hooking/)
- [Carnal Ownage Password Filters Sept 2013](http://carnal0wnage.attackresearch.com/2013/09/stealing-passwords-every-time-they.html)
