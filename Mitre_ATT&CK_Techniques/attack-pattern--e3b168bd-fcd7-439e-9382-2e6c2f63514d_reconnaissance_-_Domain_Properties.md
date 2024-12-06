---
contributors:
- "Jannie Li, Microsoft Threat Intelligence\u202FCenter\u202F(MSTIC)"
id: attack-pattern--e3b168bd-fcd7-439e-9382-2e6c2f63514d
mitre_attack_url: https://attack.mitre.org/techniques/T1590/001
name: Domain Properties
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Domain Properties
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1590/001](https://attack.mitre.org/techniques/T1590/001) |

# Domain Properties (attack-pattern--e3b168bd-fcd7-439e-9382-2e6c2f63514d)

## Description
Adversaries may gather information about the victim's network domain(s) that can be used during targeting. Information about domains and their properties may include a variety of details, including what domain(s) the victim owns as well as administrative data (ex: name, registrar, etc.) and more directly actionable information such as contacts (email addresses and phone numbers), business addresses, and name servers.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about victim domains and their properties may also be exposed to adversaries via online or other accessible data sets (ex: [WHOIS](https://attack.mitre.org/techniques/T1596/002)).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Where third-party cloud providers are in use, this information may also be exposed through publicly available API endpoints, such as GetUserRealm and autodiscover in Office 365 environments.(Citation: Azure Active Directory Reconnaisance)(Citation: Office 265 Azure Domain Availability) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596), [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593), or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566)).

## Detection
Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders.

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1590/001)
- [Circl Passive DNS](https://www.circl.lu/services/passive-dns/)
- [Azure Active Directory Reconnaisance](https://o365blog.com/post/just-looking/)
- [DNS Dumpster](https://dnsdumpster.com/)
- [Office 265 Azure Domain Availability](https://docs.microsoft.com/en-us/archive/blogs/tip_of_the_day/cloud-tip-of-the-day-advanced-way-to-check-domain-availability-for-office-365-and-azure)
- [WHOIS](https://www.whois.net/)
