---
contributors:
- Jeremy Galloway
- Shailesh Tiwary (Indian Army)
- Menachem Goldstein
data_sources:
- 'Internet Scan: Response Content'
- 'Domain Name: Domain Registration'
- 'Domain Name: Active DNS'
- 'Domain Name: Passive DNS'
- 'Internet Scan: Response Metadata'
id: attack-pattern--7e3beebd-8bfe-4e7b-a892-e44ab06a75f9
mitre_attack_url: https://attack.mitre.org/techniques/T1584
name: Compromise Infrastructure
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Compromise Infrastructure
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Content, Domain Name: Domain Registration, Domain Name: Active DNS, Domain Name: Passive DNS, Internet Scan: Response Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1584](https://attack.mitre.org/techniques/T1584) |

# Compromise Infrastructure (attack-pattern--7e3beebd-8bfe-4e7b-a892-e44ab06a75f9)

## Description
Adversaries may compromise third-party infrastructure that can be used during targeting. Infrastructure solutions include physical or cloud servers, domains, network devices, and third-party web and DNS services. Instead of buying, leasing, or renting infrastructure an adversary may compromise infrastructure and use it during other phases of the adversary lifecycle.(Citation: Mandiant APT1)(Citation: ICANNDomainNameHijacking)(Citation: Talos DNSpionage Nov 2018)(Citation: FireEye EPS Awakens Part 2) Additionally, adversaries may compromise numerous machines to form a botnet they can leverage.

Use of compromised infrastructure allows adversaries to stage, launch, and execute operations. Compromised infrastructure can help adversary operations blend in with traffic that is seen as normal, such as contact with high reputation or trusted sites. For example, adversaries may leverage compromised infrastructure (potentially also in conjunction with [Digital Certificates](https://attack.mitre.org/techniques/T1588/004)) to further blend in and support staged information gathering and/or [Phishing](https://attack.mitre.org/techniques/T1566) campaigns.(Citation: FireEye DNS Hijack 2019) Additionally, adversaries may also compromise infrastructure to support [Proxy](https://attack.mitre.org/techniques/T1090) and/or proxyware services.(Citation: amnesty_nso_pegasus)(Citation: Sysdig Proxyjacking)

By using compromised infrastructure, adversaries may make it difficult to tie their actions back to them. Prior to targeting, adversaries may compromise the infrastructure of other adversaries.(Citation: NSA NCSC Turla OilRig)

## Detection
Consider monitoring for anomalous changes to domain registrant information and/or domain resolution information that may indicate the compromise of a domain. Efforts may need to be tailored to specific domains of interest as benign registration and resolution changes are a common occurrence on the internet. 

Once adversaries have provisioned compromised infrastructure (ex: a server for use in command and control), internet scans may help proactively discover compromised infrastructure. Consider looking for identifiable patterns such as services listening, certificates in use, SSL/TLS negotiation features, or other response artifacts associated with adversary C2 software.(Citation: ThreatConnect Infrastructure Dec 2020)(Citation: Mandiant SCANdalous Jul 2020)(Citation: Koczwara Beacon Hunting Sep 2021)

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1584)
- [amnesty_nso_pegasus](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/)
- [Sysdig Proxyjacking](https://sysdig.com/blog/proxyjacking-attackers-log4j-exploited/)
- [FireEye DNS Hijack 2019](https://www.fireeye.com/blog/threat-research/2019/01/global-dns-hijacking-campaign-dns-record-manipulation-at-scale.html)
- [ICANNDomainNameHijacking](https://www.icann.org/groups/ssac/documents/sac-007-en)
- [Koczwara Beacon Hunting Sep 2021](https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2)
- [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Talos DNSpionage Nov 2018](https://blog.talosintelligence.com/2018/11/dnspionage-campaign-targets-middle-east.html)
- [NSA NCSC Turla OilRig](https://media.defense.gov/2019/Oct/18/2002197242/-1/-1/0/NSA_CSA_Turla_20191021%20ver%204%20-%20nsa.gov.pdf)
- [Mandiant SCANdalous Jul 2020](https://www.mandiant.com/resources/scandalous-external-detection-using-network-scan-data-and-automation)
- [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
- [FireEye EPS Awakens Part 2](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)
