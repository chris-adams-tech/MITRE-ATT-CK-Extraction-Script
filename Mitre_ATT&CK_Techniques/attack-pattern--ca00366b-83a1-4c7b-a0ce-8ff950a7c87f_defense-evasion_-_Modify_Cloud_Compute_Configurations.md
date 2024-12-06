---
contributors:
- Blake Strom, Microsoft Threat Intelligence
- Amir Gharib, Microsoft Threat Intelligence
data_sources:
- 'Cloud Service: Cloud Service Modification'
id: attack-pattern--ca00366b-83a1-4c7b-a0ce-8ff950a7c87f
mitre_attack_url: https://attack.mitre.org/techniques/T1578/005
name: Modify Cloud Compute Configurations
platforms:
- IaaS
tactics:
- defense-evasion
title: defense-evasion - Modify Cloud Compute Configurations
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | IaaS |
| **Data Sources** | Cloud Service: Cloud Service Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1578/005](https://attack.mitre.org/techniques/T1578/005) |

# Modify Cloud Compute Configurations (attack-pattern--ca00366b-83a1-4c7b-a0ce-8ff950a7c87f)

## Description
Adversaries may modify settings that directly affect the size, locations, and resources available to cloud compute infrastructure in order to evade defenses. These settings may include service quotas, subscription associations, tenant-wide policies, or other configurations that impact available compute. Such modifications may allow adversaries to abuse the victim’s compute resources to achieve their goals, potentially without affecting the execution of running instances and/or revealing their activities to the victim.

For example, cloud providers often limit customer usage of compute resources via quotas. Customers may request adjustments to these quotas to support increased computing needs, though these adjustments may require approval from the cloud provider. Adversaries who compromise a cloud environment may similarly request quota adjustments in order to support their activities, such as enabling additional [Resource Hijacking](https://attack.mitre.org/techniques/T1496) without raising suspicion by using up a victim’s entire quota.(Citation: Microsoft Cryptojacking 2023) Adversaries may also increase allowed resource usage by modifying any tenant-wide policies that limit the sizes of deployed virtual machines.(Citation: Microsoft Azure Policy)

Adversaries may also modify settings that affect where cloud resources can be deployed, such as enabling [Unused/Unsupported Cloud Regions](https://attack.mitre.org/techniques/T1535). 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1578/005)
- [Microsoft Cryptojacking 2023](https://www.microsoft.com/en-us/security/blog/2023/07/25/cryptojacking-understanding-and-defending-against-cloud-compute-resource-abuse/)
- [Microsoft Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies#compute)
