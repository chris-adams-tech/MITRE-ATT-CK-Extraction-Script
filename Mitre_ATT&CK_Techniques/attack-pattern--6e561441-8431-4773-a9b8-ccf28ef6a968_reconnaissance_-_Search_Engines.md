---
id: attack-pattern--6e561441-8431-4773-a9b8-ccf28ef6a968
mitre_attack_url: https://attack.mitre.org/techniques/T1593/002
name: Search Engines
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Search Engines
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1593/002](https://attack.mitre.org/techniques/T1593/002) |

# Search Engines (attack-pattern--6e561441-8431-4773-a9b8-ccf28ef6a968)

## Description
Adversaries may use search engines to collect information about victims that can be used during targeting. Search engine services typical crawl online sites to index context and may provide users with specialized syntax to search for specific keywords or specific types of content (i.e. filetypes).(Citation: SecurityTrails Google Hacking)(Citation: ExploitDB GoogleHacking)

Adversaries may craft various search engine queries depending on what information they seek to gather. Threat actors may use search engines to harvest general information about victims, as well as use specialized queries to look for spillages/leaks of sensitive information such as network details or credentials. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Valid Accounts](https://attack.mitre.org/techniques/T1078) or [Phishing](https://attack.mitre.org/techniques/T1566)).

## Detection
Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders.

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1593/002)
- [SecurityTrails Google Hacking](https://www.recordedfuture.com/threat-intelligence-101/threat-analysis-techniques/google-dorks)
- [ExploitDB GoogleHacking](https://www.exploit-db.com/google-hacking-database)
