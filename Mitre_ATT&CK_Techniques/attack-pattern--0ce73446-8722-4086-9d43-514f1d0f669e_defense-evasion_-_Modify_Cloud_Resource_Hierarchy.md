---
data_sources:
  - "Cloud Service: Cloud Service Modification"
id: attack-pattern--0ce73446-8722-4086-9d43-514f1d0f669e
mitre_attack_url: https://attack.mitre.org/techniques/T1666
name: Modify Cloud Resource Hierarchy
platforms:
  - IaaS
tactics:
  - defense-evasion
title: T1666 - defense-evasion - Modify Cloud Resource Hierarchy
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | IaaS |
| **Data Sources** | Cloud Service: Cloud Service Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1666](https://attack.mitre.org/techniques/T1666) |

# Modify Cloud Resource Hierarchy (attack-pattern--0ce73446-8722-4086-9d43-514f1d0f669e)

## Description
Adversaries may attempt to modify hierarchical structures in infrastructure-as-a-service (IaaS) environments in order to evade defenses.  

IaaS environments often group resources into a hierarchy, enabling improved resource management and application of policies to relevant groups. Hierarchical structures differ among cloud providers. For example, in AWS environments, multiple accounts can be grouped under a single organization, while in Azure environments, multiple subscriptions can be grouped under a single management group.(Citation: AWS Organizations)(Citation: Microsoft Azure Resources)

Adversaries may add, delete, or otherwise modify resource groups within an IaaS hierarchy. For example, in Azure environments, an adversary who has gained access to a Global Administrator account may create new subscriptions in which to deploy resources. They may also engage in subscription hijacking by transferring an existing pay-as-you-go subscription from a victim tenant to an adversary-controlled tenant. This will allow the adversary to use the victim’s compute resources without generating logs on the victim tenant.(Citation: Microsoft Peach Sandstorm 2023)(Citation: Microsoft Subscription Hijacking 2022)

In AWS environments, adversaries with appropriate permissions in a given account may call the `LeaveOrganization` API, causing the account to be severed from the AWS Organization to which it was tied and removing any Service Control Policies, guardrails, or restrictions imposed upon it by its former Organization. Alternatively, adversaries may call the `CreateAccount` API in order to create a new account within an AWS Organization. This account will use the same payment methods registered to the payment account but may not be subject to existing detections or Service Control Policies.(Citation: AWS RE:Inforce Threat Detection 2024)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1666)
- [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)
- [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)
- [Microsoft Subscription Hijacking 2022](https://techcommunity.microsoft.com/t5/microsoft-365-defender-blog/hunt-for-compromised-azure-subscriptions-using-microsoft/ba-p/3607121)
- [Microsoft Azure Resources](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources)
- [Microsoft Peach Sandstorm 2023](https://www.microsoft.com/en-us/security/blog/2023/09/14/peach-sandstorm-password-spray-campaigns-enable-intelligence-collection-at-high-value-targets/)
