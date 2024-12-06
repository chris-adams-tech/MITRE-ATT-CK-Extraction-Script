---
data_sources:
- 'Internet Scan: Response Content'
- 'Internet Scan: Response Metadata'
id: attack-pattern--79da0971-3147-4af6-a4f5-e8cd447cd795
mitre_attack_url: https://attack.mitre.org/techniques/T1583/003
name: Virtual Private Server
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Virtual Private Server
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Content, Internet Scan: Response Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1583/003](https://attack.mitre.org/techniques/T1583/003) |

# Virtual Private Server (attack-pattern--79da0971-3147-4af6-a4f5-e8cd447cd795)

## Description
Adversaries may rent Virtual Private Servers (VPSs) that can be used during targeting. There exist a variety of cloud service providers that will sell virtual machines/containers as a service. By utilizing a VPS, adversaries can make it difficult to physically tie back operations to them. The use of cloud infrastructure can also make it easier for adversaries to rapidly provision, modify, and shut down their infrastructure.

Acquiring a VPS for use in later stages of the adversary lifecycle, such as Command and Control, can allow adversaries to benefit from the ubiquity and trust associated with higher reputation cloud service providers. Adversaries may also acquire infrastructure from VPS service providers that are known for renting VPSs with minimal registration information, allowing for more anonymous acquisitions of infrastructure.(Citation: TrendmicroHideoutsLease)

## Detection
Once adversaries have provisioned a VPS (ex: for use as a command and control server), internet scans may reveal servers that adversaries have acquired. Consider looking for identifiable patterns such as services listening, certificates in use, SSL/TLS negotiation features, or other response artifacts associated with adversary C2 software.(Citation: ThreatConnect Infrastructure Dec 2020)(Citation: Mandiant SCANdalous Jul 2020)(Citation: Koczwara Beacon Hunting Sep 2021)

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1583/003)
- [Koczwara Beacon Hunting Sep 2021](https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2)
- [TrendmicroHideoutsLease](https://documents.trendmicro.com/assets/wp/wp-criminal-hideouts-for-lease.pdf)
- [Mandiant SCANdalous Jul 2020](https://www.mandiant.com/resources/scandalous-external-detection-using-network-scan-data-and-automation)
- [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
