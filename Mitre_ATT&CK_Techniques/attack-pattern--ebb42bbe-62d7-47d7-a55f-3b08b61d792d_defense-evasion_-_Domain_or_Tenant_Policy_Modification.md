---
contributors:
- Obsidian Security
data_sources:
- 'Active Directory: Active Directory Object Deletion'
- 'Active Directory: Active Directory Object Creation'
- 'Command: Command Execution'
- 'Active Directory: Active Directory Object Modification'
- 'Application Log: Application Log Content'
id: attack-pattern--ebb42bbe-62d7-47d7-a55f-3b08b61d792d
mitre_attack_url: https://attack.mitre.org/techniques/T1484
name: Domain or Tenant Policy Modification
platforms:
- Windows
- Identity Provider
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Domain or Tenant Policy Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows, Identity Provider |
| **Data Sources** | Active Directory: Active Directory Object Deletion, Active Directory: Active Directory Object Creation, Command: Command Execution, Active Directory: Active Directory Object Modification, Application Log: Application Log Content |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1484](https://attack.mitre.org/techniques/T1484) |

# Domain or Tenant Policy Modification (attack-pattern--ebb42bbe-62d7-47d7-a55f-3b08b61d792d)

## Description
Adversaries may modify the configuration settings of a domain or identity tenant to evade defenses and/or escalate privileges in centrally managed environments. Such services provide a centralized means of managing identity resources such as devices and accounts, and often include configuration settings that may apply between domains or tenants such as trust relationships, identity syncing, or identity federation.

Modifications to domain or tenant settings may include altering domain Group Policy Objects (GPOs) in Microsoft Active Directory (AD) or changing trust settings for domains, including federation trusts relationships between domains or tenants.

With sufficient permissions, adversaries can modify domain or tenant policy settings. Since configuration settings for these services apply to a large number of identity resources, there are a great number of potential attacks malicious outcomes that can stem from this abuse. Examples of such abuse include:  

* modifying GPOs to push a malicious [Scheduled Task](https://attack.mitre.org/techniques/T1053/005) to computers throughout the domain environment(Citation: ADSecurity GPO Persistence 2016)(Citation: Wald0 Guide to GPOs)(Citation: Harmj0y Abusing GPO Permissions)
* modifying domain trusts to include an adversary-controlled domain, allowing adversaries to  forge access tokens that will subsequently be accepted by victim domain resources(Citation: Microsoft - Customer Guidance on Recent Nation-State Cyber Attacks)
* changing configuration settings within the AD environment to implement a [Rogue Domain Controller](https://attack.mitre.org/techniques/T1207).
* adding new, adversary-controlled federated identity providers to identity tenants, allowing adversaries to authenticate as any user managed by the victim tenant (Citation: Okta Cross-Tenant Impersonation 2023)

Adversaries may temporarily modify domain or tenant policy, carry out a malicious action(s), and then revert the change to remove suspicious indicators.

## Detection
It may be possible to detect domain policy modifications using Windows event logs. Group policy modifications, for example, may be logged under a variety of Windows event IDs for modifying, creating, undeleting, moving, and deleting directory service objects (Event ID 5136, 5137, 5138, 5139, 5141 respectively). Monitor for modifications to domain trust settings, such as when a user or application modifies the federation settings on the domain or updates domain authentication from Managed to Federated via ActionTypes <code>Set federation settings on domain</code> and <code>Set domain authentication</code>.(Citation: Microsoft - Azure Sentinel ADFSDomainTrustMods)(Citation: Microsoft 365 Defender Solorigate) This may also include monitoring for Event ID 307 which can be correlated to relevant Event ID 510 with the same Instance ID for change details.(Citation: Sygnia Golden SAML)(Citation: CISA SolarWinds Cloud Detection)

Consider monitoring for commands/cmdlets and command-line arguments that may be leveraged to modify domain policy settings.(Citation: Microsoft - Update or Repair Federated domain) Some domain policy modifications, such as changes to federation settings, are likely to be rare.(Citation: Microsoft 365 Defender Solorigate)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1484)
- [CISA SolarWinds Cloud Detection](https://us-cert.cisa.gov/ncas/alerts/aa21-008a)
- [ADSecurity GPO Persistence 2016](https://adsecurity.org/?p=2716)
- [Microsoft 365 Defender Solorigate](https://www.microsoft.com/security/blog/2020/12/28/using-microsoft-365-defender-to-coordinate-protection-against-solorigate/)
- [Microsoft - Azure Sentinel ADFSDomainTrustMods](https://github.com/Azure/Azure-Sentinel/blob/master/Detections/AuditLogs/ADFSDomainTrustMods.yaml)
- [Microsoft - Update or Repair Federated domain](https://docs.microsoft.com/en-us/office365/troubleshoot/active-directory/update-federated-domain-office-365)
- [Microsoft - Customer Guidance on Recent Nation-State Cyber Attacks](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)
- [Okta Cross-Tenant Impersonation 2023](https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection)
- [Wald0 Guide to GPOs](https://wald0.com/?p=179)
- [Harmj0y Abusing GPO Permissions](https://blog.harmj0y.net/redteaming/abusing-gpo-permissions/)
- [Sygnia Golden SAML](https://www.sygnia.co/golden-saml-advisory)
