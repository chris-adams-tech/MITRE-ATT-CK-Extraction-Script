---
id: attack-pattern--31225cd3-cd46-4575-b287-c2c14011c074
mitre_attack_url: https://attack.mitre.org/techniques/T1583/005
name: Botnet
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Botnet
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1583/005](https://attack.mitre.org/techniques/T1583/005) |

# Botnet (attack-pattern--31225cd3-cd46-4575-b287-c2c14011c074)

## Description
Adversaries may buy, lease, or rent a network of compromised systems that can be used during targeting. A botnet is a network of compromised systems that can be instructed to perform coordinated tasks.(Citation: Norton Botnet) Adversaries may purchase a subscription to use an existing botnet from a booter/stresser service. With a botnet at their disposal, adversaries may perform follow-on activity such as large-scale [Phishing](https://attack.mitre.org/techniques/T1566) or Distributed Denial of Service (DDoS).(Citation: Imperva DDoS for Hire)(Citation: Krebs-Anna)(Citation: Krebs-Bazaar)(Citation: Krebs-Booter)

## Detection
Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during [Phishing](https://attack.mitre.org/techniques/T1566), [Endpoint Denial of Service](https://attack.mitre.org/techniques/T1499), or [Network Denial of Service](https://attack.mitre.org/techniques/T1498).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1583/005)
- [Norton Botnet](https://us.norton.com/internetsecurity-malware-what-is-a-botnet.html)
- [Imperva DDoS for Hire](https://www.imperva.com/learn/ddos/booters-stressers-ddosers/)
- [Krebs-Anna](https://krebsonsecurity.com/2017/01/who-is-anna-senpai-the-mirai-worm-author/)
- [Krebs-Bazaar](https://krebsonsecurity.com/2016/10/hackforums-shutters-booter-service-bazaar/)
- [Krebs-Booter](https://krebsonsecurity.com/2016/10/are-the-days-of-booter-services-numbered/)
