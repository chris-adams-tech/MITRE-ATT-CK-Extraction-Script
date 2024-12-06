---
contributors:
- Jon Sternstein, Stern Security
data_sources:
- 'User Account: User Account Authentication'
- 'Logon Session: Logon Session Creation'
- 'Logon Session: Logon Session Metadata'
id: attack-pattern--c3d4bdd9-2cfe-4a80-9d0c-07a29ecdce8f
mitre_attack_url: https://attack.mitre.org/techniques/T1078/002
name: Domain Accounts
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
- persistence
- privilege-escalation
- initial-access
title: defense-evasion - Domain Accounts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence, privilege-escalation, initial-access |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | User Account: User Account Authentication, Logon Session: Logon Session Creation, Logon Session: Logon Session Metadata |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1078/002](https://attack.mitre.org/techniques/T1078/002) |

# Domain Accounts (attack-pattern--c3d4bdd9-2cfe-4a80-9d0c-07a29ecdce8f)

## Description
Adversaries may obtain and abuse credentials of a domain account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion.(Citation: TechNet Credential Theft) Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover users, administrators, and services.(Citation: Microsoft AD Accounts)

Adversaries may compromise domain accounts, some with a high level of privileges, through various means such as [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) or password reuse, allowing access to privileged resources of the domain.

## Detection
Configure robust, consistent account activity audit policies across the enterprise and with externally accessible services.(Citation: TechNet Audit Policy) Look for suspicious account behavior across systems that share accounts, either user, admin, or service accounts. Examples: one account logged into multiple systems simultaneously; multiple accounts logged into the same machine simultaneously; accounts logged in at odd times or outside of business hours. Activity may be from interactive login sessions or process ownership from accounts being used to execute binaries on a remote system as a particular account. Correlate other security systems with login information (e.g., a user has an active login session but has not entered the building or does not have VPN access).

On Linux, check logs and other artifacts created by use of domain authentication services, such as the System Security Services Daemon (sssd).(Citation: Ubuntu SSSD Docs) 

Perform regular audits of domain accounts to detect accounts that may have been created by an adversary for persistence.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1078/002)
- [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)
- [TechNet Audit Policy](https://technet.microsoft.com/en-us/library/dn487457.aspx)
- [Microsoft AD Accounts](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-accounts)
- [Ubuntu SSSD Docs](https://ubuntu.com/server/docs/service-sssd)
