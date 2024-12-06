---
contributors:
- Dor Edry, Microsoft
data_sources:
- 'Internet Scan: Response Content'
id: attack-pattern--ae797531-3219-49a4-bccf-324ad7a4c7b2
mitre_attack_url: https://attack.mitre.org/techniques/T1584/006
name: Web Services
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Web Services
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1584/006](https://attack.mitre.org/techniques/T1584/006) |

# Web Services (attack-pattern--ae797531-3219-49a4-bccf-324ad7a4c7b2)

## Description
Adversaries may compromise access to third-party web services that can be used during targeting. A variety of popular websites exist for legitimate users to register for web-based services, such as GitHub, Twitter, Dropbox, Google, SendGrid, etc. Adversaries may try to take ownership of a legitimate user's access to a web service and use that web service as infrastructure in support of cyber operations. Such web services can be abused during later stages of the adversary lifecycle, such as during Command and Control ([Web Service](https://attack.mitre.org/techniques/T1102)), [Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567), or [Phishing](https://attack.mitre.org/techniques/T1566).(Citation: Recorded Future Turla Infra 2020) Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. By utilizing a web service, particularly when access is stolen from legitimate users, adversaries can make it difficult to physically tie back operations to them. Additionally, leveraging compromised web-based email services may allow adversaries to leverage the trust associated with legitimate domains.

## Detection
Once adversaries leverage the abused web service as infrastructure (ex: for command and control), it may be possible to look for unique characteristics associated with adversary software, if known.(Citation: ThreatConnect Infrastructure Dec 2020)

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control ([Web Service](https://attack.mitre.org/techniques/T1102)) or [Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1584/006)
- [Recorded Future Turla Infra 2020](https://www.recordedfuture.com/research/turla-apt-infrastructure)
- [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
