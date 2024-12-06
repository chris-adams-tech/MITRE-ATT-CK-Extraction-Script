---
contributors:
- Regina Elwell
- Isif Ibrahima, Mandiant
data_sources:
- 'Cloud Storage: Cloud Storage Access'
- 'Cloud Storage: Cloud Storage Enumeration'
id: attack-pattern--8565825b-21c8-4518-b75e-cbc4c717a156
mitre_attack_url: https://attack.mitre.org/techniques/T1619
name: Cloud Storage Object Discovery
platforms:
- IaaS
tactics:
- discovery
title: discovery - Cloud Storage Object Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | IaaS |
| **Data Sources** | Cloud Storage: Cloud Storage Access, Cloud Storage: Cloud Storage Enumeration |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1619](https://attack.mitre.org/techniques/T1619) |

# Cloud Storage Object Discovery (attack-pattern--8565825b-21c8-4518-b75e-cbc4c717a156)

## Description
Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) on a local host, after identifying available storage services (i.e. [Cloud Infrastructure Discovery](https://attack.mitre.org/techniques/T1580)) adversaries may access the contents/objects stored in cloud infrastructure.

Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS (Citation: ListObjectsV2) and List Blobs in Azure(Citation: List Blobs) .

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Collection and Exfiltration, based on the information obtained. 
Monitor cloud logs for API calls used for file or object enumeration for unusual activity. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1619)
- [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
- [List Blobs](https://docs.microsoft.com/en-us/rest/api/storageservices/list-blobs)
