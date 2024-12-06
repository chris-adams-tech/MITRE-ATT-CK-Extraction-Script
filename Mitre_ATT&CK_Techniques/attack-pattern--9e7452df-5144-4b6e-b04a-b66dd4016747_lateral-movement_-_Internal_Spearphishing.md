---
contributors:
- Tim MalcomVetter
- Swetha Prabakaran, Microsoft Threat Intelligence Center (MSTIC)
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
- 'Application Log: Application Log Content'
id: attack-pattern--9e7452df-5144-4b6e-b04a-b66dd4016747
mitre_attack_url: https://attack.mitre.org/techniques/T1534
name: Internal Spearphishing
platforms:
- Windows
- macOS
- Linux
- SaaS
- Office Suite
tactics:
- lateral-movement
title: lateral-movement - Internal Spearphishing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows, macOS, Linux, SaaS, Office Suite |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1534](https://attack.mitre.org/techniques/T1534) |

# Internal Spearphishing (attack-pattern--9e7452df-5144-4b6e-b04a-b66dd4016747)

## Description
After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing to gain access to additional information or compromise other users within the same organization. Internal spearphishing is multi-staged campaign where a legitimate account is initially compromised either by controlling the user's device or by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating [Impersonation](https://attack.mitre.org/techniques/T1656).(Citation: Trend Micro - Int SP)

For example, adversaries may leverage [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001) or [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002) as part of internal spearphishing to deliver a payload or redirect to an external site to capture credentials through [Input Capture](https://attack.mitre.org/techniques/T1056) on sites that mimic login interfaces.

Adversaries may also leverage internal chat apps, such as Microsoft Teams, to spread malicious content or engage users in attempts to capture sensitive information and/or credentials.(Citation: Int SP - chat apps)

## Detection
Network intrusion detection systems and email gateways usually do not scan internal email, but an organization can leverage the journaling-based solution which sends a copy of emails to a security service for offline analysis or incorporate service-integrated solutions using on-premise or API-based integrations to help detect internal spearphishing campaigns.(Citation: Trend Micro When Phishing Starts from the Inside 2017)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1534)
- [Trend Micro When Phishing Starts from the Inside 2017](https://blog.trendmicro.com/phishing-starts-inside/)
- [Int SP - chat apps](https://www.microsoft.com/en-us/security/blog/2023/08/02/midnight-blizzard-conducts-targeted-social-engineering-over-microsoft-teams/)
- [Trend Micro - Int SP](https://www.trendmicro.com/en_us/research.html)
