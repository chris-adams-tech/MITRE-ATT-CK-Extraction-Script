---
contributors:
- Praetorian
- Darin Smith, Cisco
- ExtraHop
- Gabriel Currie
data_sources:
- 'Cloud Storage: Cloud Storage Modification'
- 'Snapshot: Snapshot Creation'
- 'Snapshot: Snapshot Modification'
- 'Cloud Storage: Cloud Storage Metadata'
- 'Snapshot: Snapshot Metadata'
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Content'
- 'Cloud Storage: Cloud Storage Creation'
id: attack-pattern--d4bdbdea-eaec-4071-b4f9-5105e12ea4b6
mitre_attack_url: https://attack.mitre.org/techniques/T1537
name: Transfer Data to Cloud Account
platforms:
- IaaS
- SaaS
- Office Suite
tactics:
- exfiltration
title: exfiltration - Transfer Data to Cloud Account
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | IaaS, SaaS, Office Suite |
| **Data Sources** | Cloud Storage: Cloud Storage Modification, Snapshot: Snapshot Creation, Snapshot: Snapshot Modification, Cloud Storage: Cloud Storage Metadata, Snapshot: Snapshot Metadata, Application Log: Application Log Content, Network Traffic: Network Traffic Content, Cloud Storage: Cloud Storage Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1537](https://attack.mitre.org/techniques/T1537) |

# Transfer Data to Cloud Account (attack-pattern--d4bdbdea-eaec-4071-b4f9-5105e12ea4b6)

## Description
Adversaries may exfiltrate data by transferring the data, including through sharing/syncing and creating backups of cloud environments, to another cloud account they control on the same service.

A defender who is monitoring for large transfers to outside the cloud environment through normal file transfers or over command and control channels may not be watching for data transfers to another account within the same cloud provider. Such transfers may utilize existing cloud provider APIs and the internal address space of the cloud provider to blend into normal traffic or avoid data transfers over external network interfaces.(Citation: TLDRSec AWS Attacks)

Adversaries may also use cloud-native mechanisms to share victim data with adversary-controlled cloud accounts, such as creating anonymous file sharing links or, in Azure, a shared access signature (SAS) URI.(Citation: Microsoft Azure Storage Shared Access Signature)

Incidents have been observed where adversaries have created backups of cloud instances and transferred them to separate accounts.(Citation: DOJ GRU Indictment Jul 2018) 

## Detection
Monitor account activity for attempts to share data, snapshots, or backups with untrusted or unusual accounts on the same cloud service provider. Monitor for anomalous file transfer activity between accounts and to untrusted VPCs. 

In AWS, sharing an Elastic Block Store (EBS) snapshot, either with specified users or publicly, generates a ModifySnapshotAttribute event in CloudTrail logs.(Citation: AWS EBS Snapshot Sharing) Similarly, in Azure, creating a Shared Access Signature (SAS) URI for a Virtual Hard Disk (VHS) snapshot generates a "Get Snapshot SAS URL" event in Activity Logs.(Citation: Azure Blob Snapshots)(Citation: Azure Shared Access Signature)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1537)
- [AWS EBS Snapshot Sharing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html)
- [TLDRSec AWS Attacks](https://tldrsec.com/p/blog-lesser-known-aws-attacks)
- [Azure Shared Access Signature](https://docs.microsoft.com/en-us/rest/api/storageservices/delegate-access-with-shared-access-signature)
- [Azure Blob Snapshots](https://docs.microsoft.com/en-us/azure/storage/blobs/snapshots-overview)
- [Microsoft Azure Storage Shared Access Signature](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
- [DOJ GRU Indictment Jul 2018](https://www.justice.gov/file/1080281/download)
