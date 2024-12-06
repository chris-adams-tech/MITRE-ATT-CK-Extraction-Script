---
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Process: Process Access'
- 'File: File Modification'
- 'Process: OS API Execution'
id: attack-pattern--d4b96d2c-1032-4b22-9235-2b5b649d0605
mitre_attack_url: https://attack.mitre.org/techniques/T1556/001
name: Domain Controller Authentication
platforms:
- Windows
tactics:
- credential-access
- defense-evasion
- persistence
title: credential-access - Domain Controller Authentication
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, defense-evasion, persistence |
| **Platforms** | Windows |
| **Data Sources** | Logon Session: Logon Session Creation, Process: Process Access, File: File Modification, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1556/001](https://attack.mitre.org/techniques/T1556/001) |

# Domain Controller Authentication (attack-pattern--d4b96d2c-1032-4b22-9235-2b5b649d0605)

## Description
Adversaries may patch the authentication process on a domain controller to bypass the typical authentication mechanisms and enable access to accounts. 

Malware may be used to inject false credentials into the authentication process on a domain controller with the intent of creating a backdoor used to access any user’s account and/or credentials (ex: [Skeleton Key](https://attack.mitre.org/software/S0007)). Skeleton key works through a patch on an enterprise domain controller authentication process (LSASS) with credentials that adversaries may use to bypass the standard authentication system. Once patched, an adversary can use the injected password to successfully authenticate as any domain user account (until the the skeleton key is erased from memory by a reboot of the domain controller). Authenticated access may enable unfettered access to hosts and/or resources within single-factor authentication environments.(Citation: Dell Skeleton)

## Detection
Monitor for calls to <code>OpenProcess</code> that can be used to manipulate lsass.exe running on a domain controller as well as for malicious modifications to functions exported from authentication-related system DLLs (such as cryptdll.dll and samsrv.dll).(Citation: Dell Skeleton)

Configure robust, consistent account activity audit policies across the enterprise and with externally accessible services.(Citation: TechNet Audit Policy) Look for suspicious account behavior across systems that share accounts, either user, admin, or service accounts. Examples: one account logged into multiple systems simultaneously; multiple accounts logged into the same machine simultaneously; accounts logged in at odd times or outside of business hours. Activity may be from interactive login sessions or process ownership from accounts being used to execute binaries on a remote system as a particular account. Correlate other security systems with login information (e.g. a user has an active login session but has not entered the building or does not have VPN access). 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1556/001)
- [Dell Skeleton](https://www.secureworks.com/research/skeleton-key-malware-analysis)
- [TechNet Audit Policy](https://technet.microsoft.com/en-us/library/dn487457.aspx)
