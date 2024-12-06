---
contributors:
- Netskope
- Praetorian
- AppOmni
- Arun Seelagan, CISA
data_sources:
- 'Cloud Service: Cloud Service Metadata'
- 'Cloud Storage: Cloud Storage Access'
id: attack-pattern--3298ce88-1628-43b1-87d9-0b5336b193d7
mitre_attack_url: https://attack.mitre.org/techniques/T1530
name: Data from Cloud Storage
platforms:
- IaaS
- SaaS
- Office Suite
tactics:
- collection
title: collection - Data from Cloud Storage
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | IaaS, SaaS, Office Suite |
| **Data Sources** | Cloud Service: Cloud Service Metadata, Cloud Storage: Cloud Storage Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1530](https://attack.mitre.org/techniques/T1530) |

# Data from Cloud Storage (attack-pattern--3298ce88-1628-43b1-87d9-0b5336b193d7)

## Description
Adversaries may access data from cloud storage.

Many IaaS providers offer solutions for online data object storage such as Amazon S3, Azure Storage, and Google Cloud Storage. Similarly, SaaS enterprise platforms such as Office 365 and Google Workspace provide cloud-based document storage to users through services such as OneDrive and Google Drive, while SaaS application providers such as Slack, Confluence, Salesforce, and Dropbox may provide cloud storage solutions as a peripheral or primary use case of their platform. 

In some cases, as with IaaS-based cloud storage, there exists no overarching application (such as SQL or Elasticsearch) with which to interact with the stored objects: instead, data from these solutions is retrieved directly though the [Cloud API](https://attack.mitre.org/techniques/T1059/009). In SaaS applications, adversaries may be able to collect this data directly from APIs or backend cloud storage objects, rather than through their front-end application or interface (i.e., [Data from Information Repositories](https://attack.mitre.org/techniques/T1213)). 

Adversaries may collect sensitive data from these cloud storage solutions. Providers typically offer security guides to help end users configure systems, though misconfigurations are a common problem.(Citation: Amazon S3 Security, 2019)(Citation: Microsoft Azure Storage Security, 2019)(Citation: Google Cloud Storage Best Practices, 2019) There have been numerous incidents where cloud storage has been improperly secured, typically by unintentionally allowing public access to unauthenticated users, overly-broad access by all users, or even access for any anonymous person outside the control of the Identity Access Management system without even needing basic user permissions.

This open access may expose various types of sensitive data, such as credit cards, personally identifiable information, or medical records.(Citation: Trend Micro S3 Exposed PII, 2017)(Citation: Wired Magecart S3 Buckets, 2019)(Citation: HIPAA Journal S3 Breach, 2017)(Citation: Rclone-mega-extortion_05_2021)

Adversaries may also obtain then abuse leaked credentials from source repositories, logs, or other means as a way to gain access to cloud storage objects.

## Detection
Monitor for unusual queries to the cloud provider's storage service. Activity originating from unexpected sources may indicate improper permissions are set that is allowing access to data. Additionally, detecting failed attempts by a user for a certain object, followed by escalation of privileges by the same user, and access to the same object may be an indication of suspicious activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1530)
- [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)
- [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)
- [Wired Magecart S3 Buckets, 2019](https://www.wired.com/story/magecart-amazon-cloud-hacks/)
- [Google Cloud Storage Best Practices, 2019](https://cloud.google.com/storage/docs/best-practices)
- [HIPAA Journal S3 Breach, 2017](https://www.hipaajournal.com/47gb-medical-records-unsecured-amazon-s3-bucket/)
- [Rclone-mega-extortion_05_2021](https://redcanary.com/blog/rclone-mega-extortion/)
- [Trend Micro S3 Exposed PII, 2017](https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/a-misconfigured-amazon-s3-exposed-almost-50-thousand-pii-in-australia)
