---
contributors:
- Francesco Bigarella
id: attack-pattern--926d8cfd-1d0d-4da2-ab49-3ca10ec3f3b5
mitre_attack_url: https://attack.mitre.org/techniques/T1585/003
name: Cloud Accounts
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Cloud Accounts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1585/003](https://attack.mitre.org/techniques/T1585/003) |

# Cloud Accounts (attack-pattern--926d8cfd-1d0d-4da2-ab49-3ca10ec3f3b5)

## Description
Adversaries may create accounts with cloud providers that can be used during targeting. Adversaries can use cloud accounts to further their operations, including leveraging cloud storage services such as Dropbox, MEGA, Microsoft OneDrive, or AWS S3 buckets for [Exfiltration to Cloud Storage](https://attack.mitre.org/techniques/T1567/002) or to [Upload Tool](https://attack.mitre.org/techniques/T1608/002)s. Cloud accounts can also be used in the acquisition of infrastructure, such as [Virtual Private Server](https://attack.mitre.org/techniques/T1583/003)s or [Serverless](https://attack.mitre.org/techniques/T1583/007) infrastructure. Establishing cloud accounts may allow adversaries to develop sophisticated capabilities without managing their own servers.(Citation: Awake Security C2 Cloud)

Creating [Cloud Accounts](https://attack.mitre.org/techniques/T1585/003) may also require adversaries to establish [Email Accounts](https://attack.mitre.org/techniques/T1585/002) to register with the cloud provider. 

## Detection
Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during exfiltration (ex: [Transfer Data to Cloud Account](https://attack.mitre.org/techniques/T1537)).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1585/003)
- [Awake Security C2 Cloud](https://awakesecurity.com/blog/threat-hunting-series-detecting-command-control-in-the-cloud/)
