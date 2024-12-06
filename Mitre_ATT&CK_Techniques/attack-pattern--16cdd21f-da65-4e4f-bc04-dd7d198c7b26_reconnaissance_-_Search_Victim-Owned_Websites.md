---
contributors:
- James P Callahan, Professional Paranoid
data_sources:
- 'Application Log: Application Log Content'
id: attack-pattern--16cdd21f-da65-4e4f-bc04-dd7d198c7b26
mitre_attack_url: https://attack.mitre.org/techniques/T1594
name: Search Victim-Owned Websites
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Search Victim-Owned Websites
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **Data Sources** | Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1594](https://attack.mitre.org/techniques/T1594) |

# Search Victim-Owned Websites (attack-pattern--16cdd21f-da65-4e4f-bc04-dd7d198c7b26)

## Description
Adversaries may search websites owned by the victim for information that can be used during targeting. Victim-owned websites may contain a variety of details, including names of departments/divisions, physical locations, and data about key employees such as names, roles, and contact info (ex: [Email Addresses](https://attack.mitre.org/techniques/T1589/002)). These sites may also have details highlighting business operations and relationships.(Citation: Comparitech Leak)

Adversaries may search victim-owned websites to gather actionable information. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Trusted Relationship](https://attack.mitre.org/techniques/T1199) or [Phishing](https://attack.mitre.org/techniques/T1566)).

In addition to manually browsing the website, adversaries may attempt to identify hidden directories or files that could contain additional sensitive information or vulnerable functionality. They may do this through automated activities such as [Wordlist Scanning](https://attack.mitre.org/techniques/T1595/003), as well as by leveraging files such as sitemap.xml and robots.txt.(Citation: Perez Sitemap XML 2023)(Citation: Register Robots TXT 2015) 

## Detection
Monitor for suspicious network traffic that could be indicative of adversary reconnaissance, such as rapid successions of requests indicative of web crawling and/or large quantities of requests originating from a single source (especially if the source is known to be associated with an adversary). Analyzing web metadata may also reveal artifacts that can be attributed to potentially malicious activity, such as referer or user-agent string HTTP/S fields.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1594)
- [Perez Sitemap XML 2023](https://medium.com/@adimenia/how-attackers-can-misuse-sitemaps-to-enumerate-users-and-discover-sensitive-information-361a5065857a)
- [Comparitech Leak](https://www.comparitech.com/blog/vpn-privacy/350-million-customer-records-exposed-online/)
- [Register Robots TXT 2015](https://www.theregister.com/2015/05/19/robotstxt/)
