---
contributors:
- Arun Seelagan, CISA
data_sources:
- 'Instance: Instance Creation'
- 'Instance: Instance Metadata'
id: attack-pattern--cf1c2504-433f-4c4e-a1f8-91de45a0318c
mitre_attack_url: https://attack.mitre.org/techniques/T1578/002
name: Create Cloud Instance
platforms:
- IaaS
tactics:
- defense-evasion
title: defense-evasion - Create Cloud Instance
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | IaaS |
| **Data Sources** | Instance: Instance Creation, Instance: Instance Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1578/002](https://attack.mitre.org/techniques/T1578/002) |

# Create Cloud Instance (attack-pattern--cf1c2504-433f-4c4e-a1f8-91de45a0318c)

## Description
An adversary may create a new instance or virtual machine (VM) within the compute service of a cloud account to evade defenses. Creating a new instance may allow an adversary to bypass firewall rules and permissions that exist on instances currently residing within an account. An adversary may [Create Snapshot](https://attack.mitre.org/techniques/T1578/001) of one or more volumes in an account, create a new instance, mount the snapshots, and then apply a less restrictive security policy to collect [Data from Local System](https://attack.mitre.org/techniques/T1005) or for [Remote Data Staging](https://attack.mitre.org/techniques/T1074/002).(Citation: Mandiant M-Trends 2020)

Creating a new instance may also allow an adversary to carry out malicious activity within an environment without affecting the execution of current running instances.

## Detection
The creation of a new instance or VM is a common part of operations within many cloud environments. Events should then not be viewed in isolation, but as part of a chain of behavior that could lead to other activities. For example, the creation of an instance by a new user account or the unexpected creation of one or more snapshots followed by the creation of an instance may indicate suspicious activity.

In AWS, CloudTrail logs capture the creation of an instance in the <code>RunInstances</code> event, and in Azure the creation of a VM may be captured in Azure activity logs.(Citation: AWS CloudTrail Search)(Citation: Azure Activity Logs) Google's Admin Activity audit logs within their Cloud Audit logs can be used to detect the usage of <code>gcloud compute instances create</code> to create a VM.(Citation: Cloud Audit Logs)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1578/002)
- [AWS CloudTrail Search](https://aws.amazon.com/premiumsupport/knowledge-center/cloudtrail-search-api-calls/)
- [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit#admin-activity)
- [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
- [Azure Activity Logs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/view-activity-logs)
