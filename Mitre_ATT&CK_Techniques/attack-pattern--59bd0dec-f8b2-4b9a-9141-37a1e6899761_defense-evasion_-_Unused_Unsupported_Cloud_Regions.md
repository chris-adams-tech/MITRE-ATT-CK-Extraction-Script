---
contributors:
- Netskope
data_sources:
- 'Instance: Instance Creation'
- 'Instance: Instance Metadata'
id: attack-pattern--59bd0dec-f8b2-4b9a-9141-37a1e6899761
mitre_attack_url: https://attack.mitre.org/techniques/T1535
name: Unused/Unsupported Cloud Regions
platforms:
- IaaS
tactics:
- defense-evasion
title: defense-evasion - Unused/Unsupported Cloud Regions
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | IaaS |
| **Data Sources** | Instance: Instance Creation, Instance: Instance Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1535](https://attack.mitre.org/techniques/T1535) |

# Unused/Unsupported Cloud Regions (attack-pattern--59bd0dec-f8b2-4b9a-9141-37a1e6899761)

## Description
Adversaries may create cloud instances in unused geographic service regions in order to evade detection. Access is usually obtained through compromising accounts used to manage cloud infrastructure.

Cloud service providers often provide infrastructure throughout the world in order to improve performance, provide redundancy, and allow customers to meet compliance requirements. Oftentimes, a customer will only use a subset of the available regions and may not actively monitor other regions. If an adversary creates resources in an unused region, they may be able to operate undetected.

A variation on this behavior takes advantage of differences in functionality across cloud regions. An adversary could utilize regions which do not support advanced detection services in order to avoid detection of their activity.

An example of adversary use of unused AWS regions is to mine cryptocurrency through [Resource Hijacking](https://attack.mitre.org/techniques/T1496), which can cost organizations substantial amounts of money over time depending on the processing power used.(Citation: CloudSploit - Unused AWS Regions)

## Detection
Monitor system logs to review activities occurring across all cloud environments and regions. Configure alerting to notify of activity in normally unused regions or if the number of instances active in a region goes above a certain threshold.(Citation: CloudSploit - Unused AWS Regions)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1535)
- [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)
