---
contributors:
- Yossi Weizman, Azure Defender Research Team
- Vishwas Manral, McAfee
- Praetorian
data_sources:
- 'Image: Image Metadata'
- 'Image: Image Creation'
- 'Image: Image Modification'
id: attack-pattern--4fd8a28b-4b3a-4cd6-a8cf-85ba5f824a7f
mitre_attack_url: https://attack.mitre.org/techniques/T1525
name: Implant Internal Image
platforms:
- IaaS
- Containers
tactics:
- persistence
title: persistence - Implant Internal Image
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | IaaS, Containers |
| **Data Sources** | Image: Image Metadata, Image: Image Creation, Image: Image Modification |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1525](https://attack.mitre.org/techniques/T1525) |

# Implant Internal Image (attack-pattern--4fd8a28b-4b3a-4cd6-a8cf-85ba5f824a7f)

## Description
Adversaries may implant cloud or container images with malicious code to establish persistence after gaining access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike [Upload Malware](https://attack.mitre.org/techniques/T1608/001), this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed to always use the latest image.(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)

A tool has been developed to facilitate planting backdoors in cloud container images.(Citation: Rhino Labs Cloud Backdoor September 2019) If an adversary has access to a compromised AWS instance, and permissions to list the available container images, they may implant a backdoor such as a [Web Shell](https://attack.mitre.org/techniques/T1505/003).(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)

## Detection
Monitor interactions with images and containers by users to identify ones that are added or modified anomalously.

In containerized environments, changes may be detectable by monitoring the Docker daemon logs or setting up and monitoring Kubernetes audit logs depending on registry configuration. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1525)
- [Rhino Labs Cloud Image Backdoor Technique Sept 2019](https://rhinosecuritylabs.com/aws/cloud-container-attack-tool/)
- [Rhino Labs Cloud Backdoor September 2019](https://github.com/RhinoSecurityLabs/ccat)
