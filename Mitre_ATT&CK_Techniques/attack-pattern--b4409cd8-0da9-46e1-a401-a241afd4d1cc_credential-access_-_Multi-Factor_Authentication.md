---
contributors:
- Liran Ravich, CardinalOps
- Muhammad Moiz Arshad, @5T34L7H
- Arun Seelagan, CISA
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Application Log: Application Log Content'
- 'Active Directory: Active Directory Object Modification'
- 'User Account: User Account Authentication'
- 'User Account: User Account Modification'
id: attack-pattern--b4409cd8-0da9-46e1-a401-a241afd4d1cc
mitre_attack_url: https://attack.mitre.org/techniques/T1556/006
name: Multi-Factor Authentication
platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Office Suite
- Identity Provider
tactics:
- credential-access
- defense-evasion
- persistence
title: credential-access - Multi-Factor Authentication
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, defense-evasion, persistence |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Office Suite, Identity Provider |
| **Data Sources** | Logon Session: Logon Session Creation, Application Log: Application Log Content, Active Directory: Active Directory Object Modification, User Account: User Account Authentication, User Account: User Account Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1556/006](https://attack.mitre.org/techniques/T1556/006) |

# Multi-Factor Authentication (attack-pattern--b4409cd8-0da9-46e1-a401-a241afd4d1cc)

## Description
Adversaries may disable or modify multi-factor authentication (MFA) mechanisms to enable persistent access to compromised accounts.

Once adversaries have gained access to a network by either compromising an account lacking MFA or by employing an MFA bypass method such as [Multi-Factor Authentication Request Generation](https://attack.mitre.org/techniques/T1621), adversaries may leverage their access to modify or completely disable MFA defenses. This can be accomplished by abusing legitimate features, such as excluding users from Azure AD Conditional Access Policies, registering a new yet vulnerable/adversary-controlled MFA method, or by manually patching MFA programs and configuration files to bypass expected functionality.(Citation: Mandiant APT42)(Citation: Azure AD Conditional Access Exclusions)

For example, modifying the Windows hosts file (`C:\windows\system32\drivers\etc\hosts`) to redirect MFA calls to localhost instead of an MFA server may cause the MFA process to fail. If a "fail open" policy is in place, any otherwise successful authentication attempt may be granted access without enforcing MFA. (Citation: Russians Exploit Default MFA Protocol - CISA March 2022) 

Depending on the scope, goals, and privileges of the adversary, MFA defenses may be disabled for individual accounts or for all accounts tied to a larger group, such as all domain accounts in a victim's network environment.(Citation: Russians Exploit Default MFA Protocol - CISA March 2022) 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1556/006)
- [Russians Exploit Default MFA Protocol - CISA March 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)
- [Mandiant APT42](https://www.mandiant.com/media/17826)
- [Azure AD Conditional Access Exclusions](https://docs.microsoft.com/en-us/azure/active-directory/governance/conditional-access-exclusion)
