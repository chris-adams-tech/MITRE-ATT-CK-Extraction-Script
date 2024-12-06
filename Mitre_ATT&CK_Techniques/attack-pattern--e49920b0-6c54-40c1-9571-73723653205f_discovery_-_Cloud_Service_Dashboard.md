---
contributors:
- Praetorian
- Obsidian Security
data_sources:
- 'Logon Session: Logon Session Creation'
- 'User Account: User Account Authentication'
id: attack-pattern--e49920b0-6c54-40c1-9571-73723653205f
mitre_attack_url: https://attack.mitre.org/techniques/T1538
name: Cloud Service Dashboard
platforms:
- IaaS
- SaaS
- Office Suite
- Identity Provider
tactics:
- discovery
title: discovery - Cloud Service Dashboard
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | IaaS, SaaS, Office Suite, Identity Provider |
| **Data Sources** | Logon Session: Logon Session Creation, User Account: User Account Authentication |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1538](https://attack.mitre.org/techniques/T1538) |

# Cloud Service Dashboard (attack-pattern--e49920b0-6c54-40c1-9571-73723653205f)

## Description
An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, findings of potential security risks, and to run additional queries, such as finding public IP addresses and open ports.(Citation: Google Command Center Dashboard)

Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical dashboard than an API. This allows the adversary to gain information without making any API requests.

## Detection
Monitor account activity logs to see actions performed and activity associated with the cloud service management console. Some cloud providers, such as AWS, provide distinct log events for login attempts to the management console.(Citation: AWS Console Sign-in Events)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1538)
- [AWS Console Sign-in Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html)
- [Google Command Center Dashboard](https://cloud.google.com/security-command-center/docs/quickstart-scc-dashboard)
