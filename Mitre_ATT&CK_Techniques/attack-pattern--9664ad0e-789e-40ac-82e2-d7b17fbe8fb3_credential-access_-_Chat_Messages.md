---
contributors:
- Douglas Weir
data_sources:
- 'Application Log: Application Log Content'
id: attack-pattern--9664ad0e-789e-40ac-82e2-d7b17fbe8fb3
mitre_attack_url: https://attack.mitre.org/techniques/T1552/008
name: Chat Messages
platforms:
- SaaS
- Office Suite
tactics:
- credential-access
title: credential-access - Chat Messages
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | SaaS, Office Suite |
| **Data Sources** | Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1552/008](https://attack.mitre.org/techniques/T1552/008) |

# Chat Messages (attack-pattern--9664ad0e-789e-40ac-82e2-d7b17fbe8fb3)

## Description
Adversaries may directly collect unsecured credentials stored or passed through user communication services. Credentials may be sent and stored in user chat communication applications such as email, chat services like Slack or Teams, collaboration tools like Jira or Trello, and any other services that support user communication. Users may share various forms of credentials (such as usernames and passwords, API keys, or authentication tokens) on private or public corporate internal communications channels.

Rather than accessing the stored chat logs (i.e., [Credentials In Files](https://attack.mitre.org/techniques/T1552/001)), adversaries may directly access credentials within these services on the user endpoint, through servers hosting the services, or through administrator portals for cloud hosted services. Adversaries may also compromise integration tools like Slack Workflows to automatically search through messages to extract user credentials. These credentials may then be abused to perform follow-on activities such as lateral movement or privilege escalation (Citation: Slack Security Risks).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1552/008)
- [Slack Security Risks](https://www.nightfall.ai/blog/saas-slack-security-risks-2020)
