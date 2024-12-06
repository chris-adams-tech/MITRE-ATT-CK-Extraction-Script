---
data_sources:
- 'Logon Session: Logon Session Creation'
id: attack-pattern--8861073d-d1b8-4941-82ce-dce621d398f0
mitre_attack_url: https://attack.mitre.org/techniques/T1021/007
name: Cloud Services
platforms:
- SaaS
- IaaS
- Office Suite
- Identity Provider
tactics:
- lateral-movement
title: lateral-movement - Cloud Services
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | SaaS, IaaS, Office Suite, Identity Provider |
| **Data Sources** | Logon Session: Logon Session Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1021/007](https://attack.mitre.org/techniques/T1021/007) |

# Cloud Services (attack-pattern--8861073d-d1b8-4941-82ce-dce621d398f0)

## Description
Adversaries may log into accessible cloud services within a compromised environment using [Valid Accounts](https://attack.mitre.org/techniques/T1078) that are synchronized with or federated to on-premises user identities. The adversary may then perform management actions or access cloud-hosted resources as the logged-on user. 

Many enterprises federate centrally managed user identities to cloud services, allowing users to login with their domain credentials in order to access the cloud control plane. Similarly, adversaries may connect to available cloud services through the web console or through the cloud command line interface (CLI) (e.g., [Cloud API](https://attack.mitre.org/techniques/T1059/009)), using commands such as <code>Connect-AZAccount</code> for Azure PowerShell, <code>Connect-MgGraph</code> for Microsoft Graph PowerShell, and <code>gcloud auth login</code> for the Google Cloud CLI.

In some cases, adversaries may be able to authenticate to these services via [Application Access Token](https://attack.mitre.org/techniques/T1550/001) instead of a username and password. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1021/007)
