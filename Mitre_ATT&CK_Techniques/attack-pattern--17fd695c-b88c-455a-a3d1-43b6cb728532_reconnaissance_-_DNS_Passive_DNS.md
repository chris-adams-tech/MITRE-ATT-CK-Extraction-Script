---
id: attack-pattern--17fd695c-b88c-455a-a3d1-43b6cb728532
mitre_attack_url: https://attack.mitre.org/techniques/T1596/001
name: DNS/Passive DNS
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - DNS/Passive DNS
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1596/001](https://attack.mitre.org/techniques/T1596/001) |

# DNS/Passive DNS (attack-pattern--17fd695c-b88c-455a-a3d1-43b6cb728532)

## Description
Adversaries may search DNS data for information about victims that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts.

Adversaries may search DNS data to gather actionable information. Threat actors can query nameservers for a target organization directly, or search through centralized repositories of logged DNS query responses (known as passive DNS).(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Adversaries may also seek and target DNS misconfigurations/leaks that reveal information about internal networks. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Detection
Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders.

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1596/001)
- [DNS Dumpster](https://dnsdumpster.com/)
- [Circl Passive DNS](https://www.circl.lu/services/passive-dns/)
