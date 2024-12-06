---
contributors:
- Dor Edry, Microsoft
data_sources:
- 'Internet Scan: Response Content'
id: attack-pattern--88d31120-5bc7-4ce3-a9c0-7cf147be8e54
mitre_attack_url: https://attack.mitre.org/techniques/T1583/006
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
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1583/006](https://attack.mitre.org/techniques/T1583/006) |

# Web Services (attack-pattern--88d31120-5bc7-4ce3-a9c0-7cf147be8e54)

## Description
Adversaries may register for web services that can be used during targeting. A variety of popular websites exist for adversaries to register for a web-based service that can be abused during later stages of the adversary lifecycle, such as during Command and Control ([Web Service](https://attack.mitre.org/techniques/T1102)), [Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567), or [Phishing](https://attack.mitre.org/techniques/T1566). Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise.(Citation: FireEye APT29) By utilizing a web service, adversaries can make it difficult to physically tie back operations to them.

## Detection
Once adversaries leverage the web service as infrastructure (ex: for command and control), it may be possible to look for unique characteristics associated with adversary software, if known.(Citation: ThreatConnect Infrastructure Dec 2020)

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control ([Web Service](https://attack.mitre.org/techniques/T1102)) or [Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1583/006)
- [FireEye APT29](https://www2.fireeye.com/rs/848-DID-242/images/rpt-apt29-hammertoss.pdf)
- [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
