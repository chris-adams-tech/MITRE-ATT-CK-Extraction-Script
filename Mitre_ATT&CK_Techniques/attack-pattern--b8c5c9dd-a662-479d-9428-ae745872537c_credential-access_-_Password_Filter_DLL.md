---
contributors:
- Vincent Le Toux
id: attack-pattern--b8c5c9dd-a662-479d-9428-ae745872537c
mitre_attack_url: https://attack.mitre.org/techniques/T1174
name: Password Filter DLL
platforms:
- Windows
tactics:
- credential-access
title: credential-access - Password Filter DLL
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1174](https://attack.mitre.org/techniques/T1174) |

# Password Filter DLL (attack-pattern--b8c5c9dd-a662-479d-9428-ae745872537c)

## Description
Windows password filters are password policy enforcement mechanisms for both domain and local accounts. Filters are implemented as dynamic link libraries (DLLs) containing a method to validate potential passwords against password policies. Filter DLLs can be positioned on local computers for local accounts and/or domain controllers for domain accounts.

Before registering new passwords in the Security Accounts Manager (SAM), the Local Security Authority (LSA) requests validation from each registered filter. Any potential changes cannot take effect until every registered filter acknowledges validation.

Adversaries can register malicious password filters to harvest credentials from local computers and/or entire domains. To perform proper validation, filters must receive plain-text credentials from the LSA. A malicious password filter would receive these plain-text credentials every time a password request is made. (Citation: Carnal Ownage Password Filters Sept 2013)

## Detection
Monitor for change notifications to and from unfamiliar password filters.

Newly installed password filters will not take effect until after a system reboot.

Password filters will show up as an autorun and loaded DLL in lsass.exe. (Citation: Clymb3r Function Hook Passwords Sept 2013)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1174)
- [Carnal Ownage Password Filters Sept 2013](http://carnal0wnage.attackresearch.com/2013/09/stealing-passwords-every-time-they.html)
- [Clymb3r Function Hook Passwords Sept 2013](https://clymb3r.wordpress.com/2013/09/15/intercepting-password-changes-with-function-hooking/)
