---
contributors:
- Center for Threat-Informed Defense (CTID)
- Vishwas Manral, McAfee
data_sources:
- 'Application Log: Application Log Content'
- 'Command: Command Execution'
- 'Image: Image Creation'
- 'Container: Container Start'
- 'Container: Container Creation'
- 'Instance: Instance Start'
- 'Instance: Instance Creation'
id: attack-pattern--b0c74ef9-c61e-4986-88cb-78da98a355ec
mitre_attack_url: https://attack.mitre.org/techniques/T1204/003
name: Malicious Image
platforms:
- IaaS
- Containers
tactics:
- execution
title: execution - Malicious Image
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | IaaS, Containers |
| **Data Sources** | Application Log: Application Log Content, Command: Command Execution, Image: Image Creation, Container: Container Start, Container: Container Creation, Instance: Instance Start, Instance: Instance Creation |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1204/003](https://attack.mitre.org/techniques/T1204/003) |

# Malicious Image (attack-pattern--b0c74ef9-c61e-4986-88cb-78da98a355ec)

## Description
Adversaries may rely on a user running a malicious image to facilitate execution. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be backdoored. Backdoored images may be uploaded to a public repository via [Upload Malware](https://attack.mitre.org/techniques/T1608/001), and users may then download and deploy an instance or container from the image without realizing the image is malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that executes cryptocurrency mining, in the instance or container.(Citation: Summit Route Malicious AMIs)

Adversaries may also name images a certain way to increase the chance of users mistakenly deploying an instance or container from the image (ex: [Match Legitimate Name or Location](https://attack.mitre.org/techniques/T1036/005)).(Citation: Aqua Security Cloud Native Threat Report June 2021)

## Detection
Monitor the local image registry to make sure malicious images are not added. Track the deployment of new containers, especially from newly built images. Monitor the behavior of containers within the environment to detect anomalous behavior or malicious activity after users deploy from malicious images.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1204/003)
- [Summit Route Malicious AMIs](https://summitroute.com/blog/2018/09/24/investigating_malicious_amis/)
- [Aqua Security Cloud Native Threat Report June 2021](https://info.aquasec.com/hubfs/Threat%20reports/AquaSecurity_Cloud_Native_Threat_Report_2021.pdf?utm_campaign=WP%20-%20Jun2021%20Nautilus%202021%20Threat%20Research%20Report&utm_medium=email&_hsmi=132931006&_hsenc=p2ANqtz-_8oopT5Uhqab8B7kE0l3iFo1koirxtyfTehxF7N-EdGYrwk30gfiwp5SiNlW3G0TNKZxUcDkYOtwQ9S6nNVNyEO-Dgrw&utm_content=132931006&utm_source=hs_automation)
