---
contributors:
- "Jannie Li, Microsoft Threat Intelligence\u202FCenter\u202F(MSTIC)"
id: attack-pattern--0ff59227-8aa8-4c09-bf1f-925605bd07ea
mitre_attack_url: https://attack.mitre.org/techniques/T1590/002
name: DNS
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - DNS
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1590/002](https://attack.mitre.org/techniques/T1590/002) |

# DNS (attack-pattern--0ff59227-8aa8-4c09-bf1f-925605bd07ea)

## Description
Adversaries may gather information about the victim's DNS that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts. DNS MX, TXT, and SPF records may also reveal the use of third party cloud and SaaS providers, such as Office 365, G Suite, Salesforce, or Zendesk.(Citation: Sean Metcalf Twitter DNS Records)

Adversaries may gather this information in various ways, such as querying or otherwise collecting details via [DNS/Passive DNS](https://attack.mitre.org/techniques/T1596/001). DNS information may also be exposed to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596), [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593), or [Active Scanning](https://attack.mitre.org/techniques/T1595)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

Adversaries may also use DNS zone transfer (DNS query type AXFR) to collect all records from a misconfigured DNS server.(Citation: Trails-DNS)(Citation: DNS-CISA)(Citation: Alexa-dns)

## Detection
Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders.

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1590/002)
- [Circl Passive DNS](https://www.circl.lu/services/passive-dns/)
- [DNS-CISA](https://www.cisa.gov/news-events/alerts/2015/04/13/dns-zone-transfer-axfr-requests-may-leak-domain-information)
- [DNS Dumpster](https://dnsdumpster.com/)
- [Alexa-dns](https://en.internetwache.org/scanning-alexas-top-1m-for-axfr-29-03-2015/)
- [Sean Metcalf Twitter DNS Records](https://x.com/PyroTek3/status/1126487227712921600)
- [Trails-DNS](https://web.archive.org/web/20180615055527/https://securitytrails.com/blog/russian-tlds)
