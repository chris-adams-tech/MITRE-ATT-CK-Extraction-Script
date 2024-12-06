---
contributors:
- Blake Strom, Microsoft 365 Defender
- Praetorian
- Obsidian Security
data_sources:
- 'Command: Command Execution'
- 'Application Log: Application Log Content'
- 'Active Directory: Active Directory Object Modification'
- 'Active Directory: Active Directory Object Creation'
id: attack-pattern--24769ab5-14bd-4f4e-a752-cfb185da53ee
mitre_attack_url: https://attack.mitre.org/techniques/T1484/002
name: Trust Modification
platforms:
- Windows
- Identity Provider
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Trust Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows, Identity Provider |
| **Data Sources** | Command: Command Execution, Application Log: Application Log Content, Active Directory: Active Directory Object Modification, Active Directory: Active Directory Object Creation |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1484/002](https://attack.mitre.org/techniques/T1484/002) |

# Trust Modification (attack-pattern--24769ab5-14bd-4f4e-a752-cfb185da53ee)

## Description
Adversaries may add new domain trusts, modify the properties of existing domain trusts, or otherwise change the configuration of trust relationships between domains and tenants to evade defenses and/or elevate privileges.Trust details, such as whether or not user identities are federated, allow authentication and authorization properties to apply between domains or tenants for the purpose of accessing shared resources.(Citation: Microsoft - Azure AD Federation) These trust objects may include accounts, credentials, and other authentication material applied to servers, tokens, and domains.

Manipulating these trusts may allow an adversary to escalate privileges and/or evade defenses by modifying settings to add objects which they control. For example, in Microsoft Active Directory (AD) environments, this may be used to forge [SAML Tokens](https://attack.mitre.org/techniques/T1606/002) without the need to compromise the signing certificate to forge new credentials. Instead, an adversary can manipulate domain trusts to add their own signing certificate. An adversary may also convert an AD domain to a federated domain using Active Directory Federation Services (AD FS), which may enable malicious trust modifications such as altering the claim issuance rules to log in any valid set of credentials as a specified user.(Citation: AADInternals zure AD Federated Domain) 

An adversary may also add a new federated identity provider to an identity tenant such as Okta or AWS IAM Identity Center, which may enable the adversary to authenticate as any user of the tenant.(Citation: Okta Cross-Tenant Impersonation 2023) This may enable the threat actor to gain broad access into a variety of cloud-based services that leverage the identity tenant. For example, in AWS environments, an adversary that creates a new identity provider for an AWS Organization will be able to federate into all of the AWS Organization member accounts without creating identities for each of the member accounts.(Citation: AWS RE:Inforce Threat Detection 2024)

## Detection
Monitor for modifications to domain trust settings, such as when a user or application modifies the federation settings on the domain or updates domain authentication from Managed to Federated via ActionTypes <code>Set federation settings on domain</code> and <code>Set domain authentication</code>.(Citation: Microsoft - Azure Sentinel ADFSDomainTrustMods) This may also include monitoring for Event ID 307 which can be correlated to relevant Event ID 510 with the same Instance ID for change details.(Citation: Sygnia Golden SAML)(Citation: CISA SolarWinds Cloud Detection)

Monitor for PowerShell commands such as: <code>Update-MSOLFederatedDomain –DomainName: "Federated Domain Name"</code>, or <code>Update-MSOLFederatedDomain –DomainName: "Federated Domain Name" –supportmultipledomain</code>.(Citation: Microsoft - Update or Repair Federated domain)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1484/002)
- [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)
- [CISA SolarWinds Cloud Detection](https://us-cert.cisa.gov/ncas/alerts/aa21-008a)
- [AADInternals zure AD Federated Domain](https://o365blog.com/post/federation-vulnerability/)
- [Microsoft - Azure AD Federation](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-fed)
- [Microsoft - Azure Sentinel ADFSDomainTrustMods](https://github.com/Azure/Azure-Sentinel/blob/master/Detections/AuditLogs/ADFSDomainTrustMods.yaml)
- [Microsoft - Update or Repair Federated domain](https://docs.microsoft.com/en-us/office365/troubleshoot/active-directory/update-federated-domain-office-365)
- [Okta Cross-Tenant Impersonation 2023](https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection)
- [Sygnia Golden SAML](https://www.sygnia.co/golden-saml-advisory)
