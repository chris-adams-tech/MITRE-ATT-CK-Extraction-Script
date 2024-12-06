---
contributors:
- Jeremy Galloway
data_sources:
- 'Domain Name: Active DNS'
- 'Domain Name: Passive DNS'
id: attack-pattern--c2f59d25-87fe-44aa-8f83-e8e59d077bf5
mitre_attack_url: https://attack.mitre.org/techniques/T1584/002
name: DNS Server
platforms:
- PRE
tactics:
- resource-development
title: resource-development - DNS Server
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Domain Name: Active DNS, Domain Name: Passive DNS |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1584/002](https://attack.mitre.org/techniques/T1584/002) |

# DNS Server (attack-pattern--c2f59d25-87fe-44aa-8f83-e8e59d077bf5)

## Description
Adversaries may compromise third-party DNS servers that can be used during targeting. During post-compromise activity, adversaries may utilize DNS traffic for various tasks, including for Command and Control (ex: [Application Layer Protocol](https://attack.mitre.org/techniques/T1071)). Instead of setting up their own DNS servers, adversaries may compromise third-party DNS servers in support of operations.

By compromising DNS servers, adversaries can alter DNS records. Such control can allow for redirection of an organization's traffic, facilitating Collection and Credential Access efforts for the adversary.(Citation: Talos DNSpionage Nov 2018)(Citation: FireEye DNS Hijack 2019)  Additionally, adversaries may leverage such control in conjunction with [Digital Certificates](https://attack.mitre.org/techniques/T1588/004) to redirect traffic to adversary-controlled infrastructure, mimicking normal trusted network communications.(Citation: FireEye DNS Hijack 2019)(Citation: Crowdstrike DNS Hijack 2019) Adversaries may also be able to silently create subdomains pointed at malicious servers without tipping off the actual owner of the DNS server.(Citation: CiscoAngler)(Citation: Proofpoint Domain Shadowing)

## Detection
Consider monitoring for anomalous resolution changes for domain addresses. Efforts may need to be tailored to specific domains of interest as benign resolution changes are a common occurrence on the internet.

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1584/002)
- [FireEye DNS Hijack 2019](https://www.fireeye.com/blog/threat-research/2019/01/global-dns-hijacking-campaign-dns-record-manipulation-at-scale.html)
- [Crowdstrike DNS Hijack 2019](https://www.crowdstrike.com/blog/widespread-dns-hijacking-activity-targets-multiple-sectors/)
- [Talos DNSpionage Nov 2018](https://blog.talosintelligence.com/2018/11/dnspionage-campaign-targets-middle-east.html)
- [CiscoAngler](https://blogs.cisco.com/security/talos/angler-domain-shadowing)
- [Proofpoint Domain Shadowing](https://www.proofpoint.com/us/threat-insight/post/The-Shadow-Knows)
