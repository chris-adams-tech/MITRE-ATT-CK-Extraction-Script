---
data_sources:
- 'Internet Scan: Response Content'
id: attack-pattern--506f6f49-7045-4156-9007-7474cb44ad6d
mitre_attack_url: https://attack.mitre.org/techniques/T1608/002
name: Upload Tool
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Upload Tool
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1608/002](https://attack.mitre.org/techniques/T1608/002) |

# Upload Tool (attack-pattern--506f6f49-7045-4156-9007-7474cb44ad6d)

## Description
Adversaries may upload tools to third-party or adversary controlled infrastructure to make it accessible during targeting. Tools can be open or closed source, free or commercial. Tools can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: [PsExec](https://attack.mitre.org/software/S0029)). Adversaries may upload tools to support their operations, such as making a tool available to a victim network to enable [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105) by placing it on an Internet accessible web server.

Tools may be placed on infrastructure that was previously purchased/rented by the adversary ([Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)) or was otherwise compromised by them ([Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)).(Citation: Dell TG-3390) Tools can also be staged on web services, such as an adversary controlled GitHub repo, or on Platform-as-a-Service offerings that enable users to easily provision applications.(Citation: Dragos Heroku Watering Hole)(Citation: Malwarebytes Heroku Skimmers)(Citation: Intezer App Service Phishing)

Adversaries can avoid the need to upload a tool by having compromised victim machines download the tool directly from a third-party hosting location (ex: a non-adversary controlled GitHub repo), including the original hosting site of the tool.

## Detection
If infrastructure or patterns in tooling have been previously identified, internet scanning may uncover when an adversary has staged tools to make them accessible for targeting.

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on post-compromise phases of the adversary lifecycle, such as [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1608/002)
- [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
- [Malwarebytes Heroku Skimmers](https://www.malwarebytes.com/blog/news/2019/12/theres-an-app-for-that-web-skimmers-found-on-paas-heroku)
- [Dragos Heroku Watering Hole](https://www.dragos.com/blog/industry-news/a-new-water-watering-hole/)
- [Intezer App Service Phishing](https://www.intezer.com/blog/malware-analysis/kud-i-enter-your-server-new-vulnerabilities-in-microsoft-azure/)
