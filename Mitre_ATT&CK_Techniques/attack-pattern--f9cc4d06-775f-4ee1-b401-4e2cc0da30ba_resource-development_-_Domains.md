---
contributors:
- Jeremy Galloway
data_sources:
- 'Domain Name: Passive DNS'
- 'Domain Name: Domain Registration'
- 'Domain Name: Active DNS'
id: attack-pattern--f9cc4d06-775f-4ee1-b401-4e2cc0da30ba
mitre_attack_url: https://attack.mitre.org/techniques/T1584/001
name: Domains
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Domains
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Domain Name: Passive DNS, Domain Name: Domain Registration, Domain Name: Active DNS |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1584/001](https://attack.mitre.org/techniques/T1584/001) |

# Domains (attack-pattern--f9cc4d06-775f-4ee1-b401-4e2cc0da30ba)

## Description
Adversaries may hijack domains and/or subdomains that can be used during targeting. Domain registration hijacking is the act of changing the registration of a domain name without the permission of the original registrant.(Citation: ICANNDomainNameHijacking) Adversaries may gain access to an email account for the person listed as the owner of the domain. The adversary can then claim that they forgot their password in order to make changes to the domain registration. Other possibilities include social engineering a domain registration help desk to gain access to an account, taking advantage of renewal process gaps, or compromising a cloud service that enables managing domains (e.g., AWS Route53).(Citation: Krebs DNS Hijack 2019)

Subdomain hijacking can occur when organizations have DNS entries that point to non-existent or deprovisioned resources. In such cases, an adversary may take control of a subdomain to conduct operations with the benefit of the trust associated with that domain.(Citation: Microsoft Sub Takeover 2020)

Adversaries who compromise a domain may also engage in domain shadowing by creating malicious subdomains under their control while keeping any existing DNS records. As service will not be disrupted, the malicious subdomains may go unnoticed for long periods of time.(Citation: Palo Alto Unit 42 Domain Shadowing 2022)

## Detection
Consider monitoring for anomalous changes to domain registrant information and/or domain resolution information that may indicate the compromise of a domain. Efforts may need to be tailored to specific domains of interest as benign registration and resolution changes are a common occurrence on the internet.

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1584/001)
- [Krebs DNS Hijack 2019](https://krebsonsecurity.com/2019/02/a-deep-dive-on-the-recent-widespread-dns-hijacking-attacks/)
- [ICANNDomainNameHijacking](https://www.icann.org/groups/ssac/documents/sac-007-en)
- [Palo Alto Unit 42 Domain Shadowing 2022](https://unit42.paloaltonetworks.com/domain-shadowing/)
- [Microsoft Sub Takeover 2020](https://docs.microsoft.com/en-us/azure/security/fundamentals/subdomain-takeover)
