---
contributors:
- Suzy Schapperle - Microsoft Azure Red Team
- Praetorian
- Thanabodi Phrakhun, I-SECURE
- Arun Seelagan, CISA
data_sources:
- 'Cloud Service: Cloud Service Enumeration'
- 'Logon Session: Logon Session Creation'
id: attack-pattern--e24fcba8-2557-4442-a139-1ee2f2e784db
mitre_attack_url: https://attack.mitre.org/techniques/T1526
name: Cloud Service Discovery
platforms:
- SaaS
- IaaS
- Office Suite
- Identity Provider
tactics:
- discovery
title: discovery - Cloud Service Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | SaaS, IaaS, Office Suite, Identity Provider |
| **Data Sources** | Cloud Service: Cloud Service Enumeration, Logon Session: Logon Session Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1526](https://attack.mitre.org/techniques/T1526) |

# Cloud Service Discovery (attack-pattern--e24fcba8-2557-4442-a139-1ee2f2e784db)

## Description
An adversary may attempt to enumerate the cloud services running on a system after gaining access. These methods can differ from platform-as-a-service (PaaS), to infrastructure-as-a-service (IaaS), or software-as-a-service (SaaS). Many services exist throughout the various cloud providers and can include Continuous Integration and Continuous Delivery (CI/CD), Lambda Functions, Entra ID, etc. They may also include security services, such as AWS GuardDuty and Microsoft Defender for Cloud, and logging services, such as AWS CloudTrail and Google Cloud Audit Logs.

Adversaries may attempt to discover information about the services enabled throughout the environment. Azure tools and APIs, such as the Microsoft Graph API and Azure Resource Manager API, can enumerate resources and services, including applications, management groups, resources and policy definitions, and their relationships that are accessible by an identity.(Citation: Azure - Resource Manager API)(Citation: Azure AD Graph API)

For example, Stormspotter is an open source tool for enumerating and constructing a graph for Azure resources and services, and Pacu is an open source AWS exploitation framework that supports several methods for discovering cloud services.(Citation: Azure - Stormspotter)(Citation: GitHub Pacu)

Adversaries may use the information gained to shape follow-on behaviors, such as targeting data or credentials from enumerated services or evading identified defenses through [Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001) or [Disable or Modify Cloud Logs](https://attack.mitre.org/techniques/T1562/008).

## Detection
Cloud service discovery techniques will likely occur throughout an operation where an adversary is targeting cloud-based systems and services. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities based on the information obtained.

Normal, benign system and network events that look like cloud service discovery may be uncommon, depending on the environment and how they are used. Monitor cloud service usage for anomalous behavior that may indicate adversarial presence within the environment.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1526)
- [Azure AD Graph API](https://docs.microsoft.com/en-us/previous-versions/azure/ad/graph/howto/azure-ad-graph-api-operations-overview)
- [Azure - Resource Manager API](https://docs.microsoft.com/en-us/rest/api/resources/)
- [Azure - Stormspotter](https://github.com/Azure/Stormspotter)
- [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
