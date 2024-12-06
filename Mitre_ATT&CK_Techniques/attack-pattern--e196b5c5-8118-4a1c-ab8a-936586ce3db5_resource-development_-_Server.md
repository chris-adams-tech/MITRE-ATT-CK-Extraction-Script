---
contributors:
- Dor Edry, Microsoft
data_sources:
- 'Internet Scan: Response Content'
- 'Internet Scan: Response Metadata'
id: attack-pattern--e196b5c5-8118-4a1c-ab8a-936586ce3db5
mitre_attack_url: https://attack.mitre.org/techniques/T1584/004
name: Server
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Server
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Content, Internet Scan: Response Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1584/004](https://attack.mitre.org/techniques/T1584/004) |

# Server (attack-pattern--e196b5c5-8118-4a1c-ab8a-936586ce3db5)

## Description
Adversaries may compromise third-party servers that can be used during targeting. Use of servers allows an adversary to stage, launch, and execute an operation. During post-compromise activity, adversaries may utilize servers for various tasks, including for Command and Control.(Citation: TrendMicro EarthLusca 2022) Instead of purchasing a [Server](https://attack.mitre.org/techniques/T1583/004) or [Virtual Private Server](https://attack.mitre.org/techniques/T1583/003), adversaries may compromise third-party servers in support of operations.

Adversaries may also compromise web servers to support watering hole operations, as in [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), or email servers to support [Phishing](https://attack.mitre.org/techniques/T1566) operations.

## Detection
Once adversaries have provisioned software on a compromised server (ex: for use as a command and control server), internet scans may reveal servers that adversaries have compromised. Consider looking for identifiable patterns such as services listening, certificates in use, SSL/TLS negotiation features, or other response artifacts associated with adversary C2 software.(Citation: ThreatConnect Infrastructure Dec 2020)(Citation: Mandiant SCANdalous Jul 2020)(Citation: Koczwara Beacon Hunting Sep 2021)

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1584/004)
- [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [Koczwara Beacon Hunting Sep 2021](https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2)
- [Mandiant SCANdalous Jul 2020](https://www.mandiant.com/resources/scandalous-external-detection-using-network-scan-data-and-automation)
- [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
