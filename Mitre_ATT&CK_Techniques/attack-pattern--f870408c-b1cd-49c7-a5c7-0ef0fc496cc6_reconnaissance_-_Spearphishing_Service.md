---
contributors:
- Robert Simmons, @MalwareUtkonos
data_sources:
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--f870408c-b1cd-49c7-a5c7-0ef0fc496cc6
mitre_attack_url: https://attack.mitre.org/techniques/T1598/001
name: Spearphishing Service
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Spearphishing Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **Data Sources** | Application Log: Application Log Content, Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1598/001](https://attack.mitre.org/techniques/T1598/001) |

# Spearphishing Service (attack-pattern--f870408c-b1cd-49c7-a5c7-0ef0fc496cc6)

## Description
Adversaries may send spearphishing messages via third-party services to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries send messages through various social media services, personal webmail, and other non-enterprise controlled services.(Citation: ThreatPost Social Media Phishing) These services are more likely to have a less-strict security policy than an enterprise. As with most kinds of spearphishing, the goal is to generate rapport with the target or get the target's interest in some way. Adversaries may create fake social media accounts and message employees for potential job opportunities. Doing so allows a plausible reason for asking about services, policies, and information about their environment. Adversaries may also use information from previous reconnaissance efforts (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)) to craft persuasive and believable lures.

## Detection
Monitor social media traffic for suspicious activity, including messages requesting information as well as abnormal file or data transfers (especially those involving unknown, or otherwise suspicious accounts).

Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders.

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1598/001)
- [ThreatPost Social Media Phishing](https://threatpost.com/facebook-launching-pad-phishing-attacks/160351/)
