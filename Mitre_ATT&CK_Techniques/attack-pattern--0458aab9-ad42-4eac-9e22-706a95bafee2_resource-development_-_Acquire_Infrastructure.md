---
contributors:
- Shailesh Tiwary (Indian Army)
- Menachem Goldstein
data_sources:
- 'Internet Scan: Response Metadata'
- 'Internet Scan: Response Content'
- 'Domain Name: Active DNS'
- 'Domain Name: Passive DNS'
- 'Domain Name: Domain Registration'
id: attack-pattern--0458aab9-ad42-4eac-9e22-706a95bafee2
mitre_attack_url: https://attack.mitre.org/techniques/T1583
name: Acquire Infrastructure
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Acquire Infrastructure
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Metadata, Internet Scan: Response Content, Domain Name: Active DNS, Domain Name: Passive DNS, Domain Name: Domain Registration |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1583](https://attack.mitre.org/techniques/T1583) |

# Acquire Infrastructure (attack-pattern--0458aab9-ad42-4eac-9e22-706a95bafee2)

## Description
Adversaries may buy, lease, rent, or obtain infrastructure that can be used during targeting. A wide variety of infrastructure exists for hosting and orchestrating adversary operations. Infrastructure solutions include physical or cloud servers, domains, and third-party web services.(Citation: TrendmicroHideoutsLease) Some infrastructure providers offer free trial periods, enabling infrastructure acquisition at limited to no cost.(Citation: Free Trial PurpleUrchin) Additionally, botnets are available for rent or purchase.

Use of these infrastructure solutions allows adversaries to stage, launch, and execute operations. Solutions may help adversary operations blend in with traffic that is seen as normal, such as contacting third-party web services or acquiring infrastructure to support [Proxy](https://attack.mitre.org/techniques/T1090), including from residential proxy services.(Citation: amnesty_nso_pegasus)(Citation: FBI Proxies Credential Stuffing)(Citation: Mandiant APT29 Microsoft 365 2022) Depending on the implementation, adversaries may use infrastructure that makes it difficult to physically tie back to them as well as utilize infrastructure that can be rapidly provisioned, modified, and shut down.

## Detection
Consider use of services that may aid in tracking of newly acquired infrastructure, such as WHOIS databases for domain registration information. 

Once adversaries have provisioned infrastructure (ex: a server for use in command and control), internet scans may help proactively discover adversary acquired infrastructure. Consider looking for identifiable patterns such as services listening, certificates in use, SSL/TLS negotiation features, or other response artifacts associated with adversary C2 software.(Citation: ThreatConnect Infrastructure Dec 2020)(Citation: Mandiant SCANdalous Jul 2020)(Citation: Koczwara Beacon Hunting Sep 2021)

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1583)
- [amnesty_nso_pegasus](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/)
- [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)
- [FBI Proxies Credential Stuffing](https://www.ic3.gov/Media/News/2022/220818.pdf)
- [Free Trial PurpleUrchin](https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/)
- [Koczwara Beacon Hunting Sep 2021](https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2)
- [TrendmicroHideoutsLease](https://documents.trendmicro.com/assets/wp/wp-criminal-hideouts-for-lease.pdf)
- [Mandiant SCANdalous Jul 2020](https://www.mandiant.com/resources/scandalous-external-detection-using-network-scan-data-and-automation)
- [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
