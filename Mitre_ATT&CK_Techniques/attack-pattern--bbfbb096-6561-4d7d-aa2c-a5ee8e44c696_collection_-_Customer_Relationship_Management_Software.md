---
contributors:
- Centre for Cybersecurity Belgium (CCB)
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Application Log: Application Log Content'
id: attack-pattern--bbfbb096-6561-4d7d-aa2c-a5ee8e44c696
mitre_attack_url: https://attack.mitre.org/techniques/T1213/004
name: Customer Relationship Management Software
platforms:
- SaaS
tactics:
- collection
title: collection - Customer Relationship Management Software
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | SaaS |
| **Data Sources** | Logon Session: Logon Session Creation, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1213/004](https://attack.mitre.org/techniques/T1213/004) |

# Customer Relationship Management Software (attack-pattern--bbfbb096-6561-4d7d-aa2c-a5ee8e44c696)

## Description
Adversaries may leverage Customer Relationship Management (CRM) software to mine valuable information. CRM software is used to assist organizations in tracking and managing customer interactions, as well as storing customer data.

Once adversaries gain access to a victim organization, they may mine CRM software for customer data. This may include personally identifiable information (PII) such as full names, emails, phone numbers, and addresses, as well as additional details such as purchase histories and IT support interactions. By collecting this data, an adversary may be able to send personalized [Phishing](https://attack.mitre.org/techniques/T1566) emails, engage in SIM swapping, or otherwise target the organization’s customers in ways that enable financial gain or the compromise of additional organizations.(Citation: Bleeping Computer US Cellular Hack 2022)(Citation: Bleeping Computer Mint Mobile Hack 2021)(Citation: Bleeping Computer Bank Hack 2020)

CRM software may be hosted on-premises or in the cloud. Information stored in these solutions may vary based on the specific instance or environment. Examples of CRM software include Microsoft Dynamics 365, Salesforce, Zoho, Zendesk, and HubSpot.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1213/004)
- [Bleeping Computer Bank Hack 2020](https://www.bleepingcomputer.com/news/security/customer-owned-bank-informs-100k-of-breach-exposing-account-balance-pii/)
- [Bleeping Computer Mint Mobile Hack 2021](https://www.bleepingcomputer.com/news/security/mint-mobile-hit-by-a-data-breach-after-numbers-ported-data-accessed/)
- [Bleeping Computer US Cellular Hack 2022](https://www.bleepingcomputer.com/news/security/uscellular-discloses-data-breach-after-billing-system-hack/)
