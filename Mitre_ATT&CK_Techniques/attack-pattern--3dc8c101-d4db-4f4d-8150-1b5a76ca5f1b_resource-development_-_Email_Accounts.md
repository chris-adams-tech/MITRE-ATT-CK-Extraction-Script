---
contributors:
- Tristan Bennett, Seamless Intelligence
- Bryan Onel
id: attack-pattern--3dc8c101-d4db-4f4d-8150-1b5a76ca5f1b
mitre_attack_url: https://attack.mitre.org/techniques/T1586/002
name: Email Accounts
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Email Accounts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1586/002](https://attack.mitre.org/techniques/T1586/002) |

# Email Accounts (attack-pattern--3dc8c101-d4db-4f4d-8150-1b5a76ca5f1b)

## Description
Adversaries may compromise email accounts that can be used during targeting. Adversaries can use compromised email accounts to further their operations, such as leveraging them to conduct [Phishing for Information](https://attack.mitre.org/techniques/T1598), [Phishing](https://attack.mitre.org/techniques/T1566), or large-scale spam email campaigns. Utilizing an existing persona with a compromised email account may engender a level of trust in a potential victim if they have a relationship with, or knowledge of, the compromised persona. Compromised email accounts can also be used in the acquisition of infrastructure (ex: [Domains](https://attack.mitre.org/techniques/T1583/001)).

A variety of methods exist for compromising email accounts, such as gathering credentials via [Phishing for Information](https://attack.mitre.org/techniques/T1598), purchasing credentials from third-party sites, brute forcing credentials (ex: password reuse from breach credential dumps), or paying employees, suppliers or business partners for access to credentials.(Citation: AnonHBGary)(Citation: Microsoft DEV-0537) Prior to compromising email accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation. Adversaries may target compromising well-known email accounts or domains from which malicious spam or [Phishing](https://attack.mitre.org/techniques/T1566) emails may evade reputation-based email filtering rules.

Adversaries can use a compromised email account to hijack existing email threads with targets of interest.

## Detection
Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access (ex: [Phishing](https://attack.mitre.org/techniques/T1566)).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1586/002)
- [AnonHBGary](https://arstechnica.com/tech-policy/2011/02/anonymous-speaks-the-inside-story-of-the-hbgary-hack/)
- [Microsoft DEV-0537](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
