---
id: attack-pattern--810d8072-afb6-4a56-9ee7-86379ac4a6f3
mitre_attack_url: https://attack.mitre.org/techniques/T1584/005
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
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1584/005](https://attack.mitre.org/techniques/T1584/005) |

# Botnet (attack-pattern--810d8072-afb6-4a56-9ee7-86379ac4a6f3)

## Description
Adversaries may compromise numerous third-party systems to form a botnet that can be used during targeting. A botnet is a network of compromised systems that can be instructed to perform coordinated tasks.(Citation: Norton Botnet) Instead of purchasing/renting a botnet from a booter/stresser service, adversaries may build their own botnet by compromising numerous third-party systems.(Citation: Imperva DDoS for Hire) Adversaries may also conduct a takeover of an existing botnet, such as redirecting bots to adversary-controlled C2 servers.(Citation: Dell Dridex Oct 2015) With a botnet at their disposal, adversaries may perform follow-on activity such as large-scale [Phishing](https://attack.mitre.org/techniques/T1566) or Distributed Denial of Service (DDoS).

## Detection
Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during [Phishing](https://attack.mitre.org/techniques/T1566), [Endpoint Denial of Service](https://attack.mitre.org/techniques/T1499), or [Network Denial of Service](https://attack.mitre.org/techniques/T1498).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1584/005)
- [Dell Dridex Oct 2015](https://www.secureworks.com/research/dridex-bugat-v5-botnet-takeover-operation)
- [Imperva DDoS for Hire](https://www.imperva.com/learn/ddos/booters-stressers-ddosers/)
- [Norton Botnet](https://us.norton.com/internetsecurity-malware-what-is-a-botnet.html)
