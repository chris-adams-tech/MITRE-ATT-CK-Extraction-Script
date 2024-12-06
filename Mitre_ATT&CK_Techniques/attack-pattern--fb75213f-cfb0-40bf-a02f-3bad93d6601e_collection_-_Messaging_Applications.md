---
contributors:
- Menachem Goldstein
- Obsidian Security
data_sources:
- 'Application Log: Application Log Content'
id: attack-pattern--fb75213f-cfb0-40bf-a02f-3bad93d6601e
mitre_attack_url: https://attack.mitre.org/techniques/T1213/005
name: Messaging Applications
platforms:
- SaaS
- Office Suite
tactics:
- collection
title: collection - Messaging Applications
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | SaaS, Office Suite |
| **Data Sources** | Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1213/005](https://attack.mitre.org/techniques/T1213/005) |

# Messaging Applications (attack-pattern--fb75213f-cfb0-40bf-a02f-3bad93d6601e)

## Description
Adversaries may leverage chat and messaging applications, such as Microsoft Teams, Google Chat, and Slack, to mine valuable information.  

The following is a brief list of example information that may hold potential value to an adversary and may also be found on messaging applications: 

* Testing / development credentials (i.e., [Chat Messages](https://attack.mitre.org/techniques/T1552/008)) 
* Source code snippets 
* Links to network shares and other internal resources 
* Proprietary data(Citation: Guardian Grand Theft Auto Leak 2022)
* Discussions about ongoing incident response efforts(Citation: SC Magazine Ragnar Locker 2021)(Citation: Microsoft DEV-0537)

In addition to exfiltrating data from messaging applications, adversaries may leverage data from chat messages in order to improve their targeting - for example, by learning more about an environment or evading ongoing incident response efforts.(Citation: Sentinel Labs NullBulge 2024)(Citation: Permiso Scattered Spider 2023)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1213/005)
- [Sentinel Labs NullBulge 2024](https://www.sentinelone.com/labs/nullbulge-threat-actor-masquerades-as-hacktivist-group-rebelling-against-ai/)
- [Permiso Scattered Spider 2023](https://permiso.io/blog/lucr-3-scattered-spider-getting-saas-y-in-the-cloud)
- [SC Magazine Ragnar Locker 2021](https://www.scmagazine.com/analysis/ragnar-locker-reminds-breach-victims-it-can-read-the-on-network-incident-response-chat-rooms)
- [Guardian Grand Theft Auto Leak 2022](https://www.theguardian.com/games/2022/sep/19/grand-theft-auto-6-leak-who-hacked-rockstar-and-what-was-stolen)
- [Microsoft DEV-0537](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
