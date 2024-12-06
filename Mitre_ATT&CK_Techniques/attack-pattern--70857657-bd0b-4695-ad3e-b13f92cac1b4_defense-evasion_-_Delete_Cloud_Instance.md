---
contributors:
- Arun Seelagan, CISA
data_sources:
- 'Instance: Instance Metadata'
- 'Instance: Instance Deletion'
id: attack-pattern--70857657-bd0b-4695-ad3e-b13f92cac1b4
mitre_attack_url: https://attack.mitre.org/techniques/T1578/003
name: Delete Cloud Instance
platforms:
- IaaS
tactics:
- defense-evasion
title: defense-evasion - Delete Cloud Instance
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | IaaS |
| **Data Sources** | Instance: Instance Metadata, Instance: Instance Deletion |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1578/003](https://attack.mitre.org/techniques/T1578/003) |

# Delete Cloud Instance (attack-pattern--70857657-bd0b-4695-ad3e-b13f92cac1b4)

## Description
An adversary may delete a cloud instance after they have performed malicious activities in an attempt to evade detection and remove evidence of their presence.  Deleting an instance or virtual machine can remove valuable forensic artifacts and other evidence of suspicious behavior if the instance is not recoverable.

An adversary may also [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and later terminate the instance after achieving their objectives.(Citation: Mandiant M-Trends 2020)

## Detection
The deletion of a new instance or virtual machine is a common part of operations within many cloud environments. Events should then not be viewed in isolation, but as part of a chain of behavior that could lead to other activities. For example, detecting a sequence of events such as the creation of an instance, mounting of a snapshot to that instance, and deletion of that instance by a new user account may indicate suspicious activity.

In AWS, CloudTrail logs capture the deletion of an instance in the <code>TerminateInstances</code> event, and in Azure the deletion of a VM may be captured in Azure activity logs.(Citation: AWS CloudTrail Search)(Citation: Azure Activity Logs) Google's Admin Activity audit logs within their Cloud Audit logs can be used to detect the usage of <code>gcloud compute instances delete</code> to delete a VM.(Citation: Cloud Audit Logs)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1578/003)
- [AWS CloudTrail Search](https://aws.amazon.com/premiumsupport/knowledge-center/cloudtrail-search-api-calls/)
- [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit#admin-activity)
- [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
- [Azure Activity Logs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/view-activity-logs)
