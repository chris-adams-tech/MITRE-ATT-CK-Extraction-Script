---
id: attack-pattern--bbe5b322-e2af-4a5e-9625-a4e62bf84ed3
mitre_attack_url: https://attack.mitre.org/techniques/T1593/001
name: Social Media
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Social Media
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1593/001](https://attack.mitre.org/techniques/T1593/001) |

# Social Media (attack-pattern--bbe5b322-e2af-4a5e-9625-a4e62bf84ed3)

## Description
Adversaries may search social media for information about victims that can be used during targeting. Social media sites may contain various information about a victim organization, such as business announcements as well as information about the roles, locations, and interests of staff.

Adversaries may search in different social media sites depending on what information they seek to gather. Threat actors may passively harvest data from these sites, as well as use information gathered to create fake profiles/groups to elicit victim’s into revealing specific information (i.e. [Spearphishing Service](https://attack.mitre.org/techniques/T1598/001)).(Citation: Cyware Social Media) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Spearphishing via Service](https://attack.mitre.org/techniques/T1566/003)).

## Detection
Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders.

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1593/001)
- [Cyware Social Media](https://cyware.com/news/how-hackers-exploit-social-media-to-break-into-your-company-88e8da8e)
