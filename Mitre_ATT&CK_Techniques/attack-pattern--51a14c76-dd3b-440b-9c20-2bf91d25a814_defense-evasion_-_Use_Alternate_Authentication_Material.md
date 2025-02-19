---
contributors:
- Blake Strom, Microsoft Threat Intelligence
- Pawel Partyka, Microsoft Threat Intelligence
data_sources:
- 'Application Log: Application Log Content'
- 'Logon Session: Logon Session Creation'
- 'Active Directory: Active Directory Credential Request'
- 'Web Credential: Web Credential Usage'
- 'User Account: User Account Authentication'
id: attack-pattern--51a14c76-dd3b-440b-9c20-2bf91d25a814
mitre_attack_url: https://attack.mitre.org/techniques/T1550
name: Use Alternate Authentication Material
platforms:
- Windows
- SaaS
- IaaS
- Containers
- Identity Provider
- Office Suite
tactics:
- defense-evasion
- lateral-movement
title: defense-evasion - Use Alternate Authentication Material
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, lateral-movement |
| **Platforms** | Windows, SaaS, IaaS, Containers, Identity Provider, Office Suite |
| **Data Sources** | Application Log: Application Log Content, Logon Session: Logon Session Creation, Active Directory: Active Directory Credential Request, Web Credential: Web Credential Usage, User Account: User Account Authentication |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1550](https://attack.mitre.org/techniques/T1550) |

# Use Alternate Authentication Material (attack-pattern--51a14c76-dd3b-440b-9c20-2bf91d25a814)

## Description
Adversaries may use alternate authentication material, such as password hashes, Kerberos tickets, and application access tokens, in order to move laterally within an environment and bypass normal system access controls. 

Authentication processes generally require a valid identity (e.g., username) along with one or more authentication factors (e.g., password, pin, physical smart card, token generator, etc.). Alternate authentication material is legitimately generated by systems after a user or application successfully authenticates by providing a valid identity and the required authentication factor(s). Alternate authentication material may also be generated during the identity creation process.(Citation: NIST Authentication)(Citation: NIST MFA)

Caching alternate authentication material allows the system to verify an identity has successfully authenticated without asking the user to reenter authentication factor(s). Because the alternate authentication must be maintained by the system—either in memory or on disk—it may be at risk of being stolen through [Credential Access](https://attack.mitre.org/tactics/TA0006) techniques. By stealing alternate authentication material, adversaries are able to bypass system access controls and authenticate to systems without knowing the plaintext password or any additional authentication factors.


## Detection
Configure robust, consistent account activity audit policies across the enterprise and with externally accessible services.(Citation: TechNet Audit Policy) Look for suspicious account behavior across systems that share accounts, either user, admin, or service accounts. Examples: one account logged into multiple systems simultaneously; multiple accounts logged into the same machine simultaneously; accounts logged in at odd times or outside of business hours. Activity may be from interactive login sessions or process ownership from accounts being used to execute binaries on a remote system as a particular account. Correlate other security systems with login information (e.g., a user has an active login session but has not entered the building or does not have VPN access).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1550)
- [TechNet Audit Policy](https://technet.microsoft.com/en-us/library/dn487457.aspx)
- [NIST Authentication](https://csrc.nist.gov/glossary/term/authentication)
- [NIST MFA](https://csrc.nist.gov/glossary/term/multi_factor_authentication)
