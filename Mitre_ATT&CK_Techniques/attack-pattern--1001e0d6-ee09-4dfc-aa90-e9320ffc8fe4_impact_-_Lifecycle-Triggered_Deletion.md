---
data_sources:
- 'Cloud Storage: Cloud Storage Modification'
id: attack-pattern--1001e0d6-ee09-4dfc-aa90-e9320ffc8fe4
mitre_attack_url: https://attack.mitre.org/techniques/T1485/001
name: Lifecycle-Triggered Deletion
platforms:
- IaaS
tactics:
- impact
title: impact - Lifecycle-Triggered Deletion
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | IaaS |
| **Data Sources** | Cloud Storage: Cloud Storage Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1485/001](https://attack.mitre.org/techniques/T1485/001) |

# Lifecycle-Triggered Deletion (attack-pattern--1001e0d6-ee09-4dfc-aa90-e9320ffc8fe4)

## Description
Adversaries may modify the lifecycle policies of a cloud storage bucket to destroy all objects stored within.  

Cloud storage buckets often allow users to set lifecycle policies to automate the migration, archival, or deletion of objects after a set period of time.(Citation: AWS Storage Lifecycles)(Citation: GCP Storage Lifecycles)(Citation: Azure Storage Lifecycles) If a threat actor has sufficient permissions to modify these policies, they may be able to delete all objects at once. 

For example, in AWS environments, an adversary with the `PutLifecycleConfiguration` permission may use the `PutBucketLifecycle` API call to apply a lifecycle policy to an S3 bucket that deletes all objects in the bucket after one day.(Citation: Palo Alto Cloud Ransomware) In addition to destroying data for purposes of extortion and [Financial Theft](https://attack.mitre.org/techniques/T1657), adversaries may also perform this action on buckets storing cloud logs for [Indicator Removal](https://attack.mitre.org/techniques/T1070).(Citation: Datadog S3 Lifecycle CloudTrail Logs)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1485/001)
- [AWS Storage Lifecycles](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [GCP Storage Lifecycles](https://cloud.google.com/storage/docs/lifecycle)
- [Azure Storage Lifecycles](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure?tabs=azure-portal)
- [Palo Alto Cloud Ransomware](https://www.paloaltonetworks.com/blog/prisma-cloud/ransomware-data-protection-cloud/)
- [Datadog S3 Lifecycle CloudTrail Logs](https://stratus-red-team.cloud/attack-techniques/AWS/aws.defense-evasion.cloudtrail-lifecycle-rule/)
