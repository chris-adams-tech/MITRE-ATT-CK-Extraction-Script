---
contributors:
- Praetorian
data_sources:
- 'User Account: User Account Authentication'
id: attack-pattern--19bf235b-8620-4997-b5b4-94e0659ed7c3
mitre_attack_url: https://attack.mitre.org/techniques/T1552/005
name: Cloud Instance Metadata API
platforms:
- IaaS
tactics:
- credential-access
title: credential-access - Cloud Instance Metadata API
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | IaaS |
| **Data Sources** | User Account: User Account Authentication |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1552/005](https://attack.mitre.org/techniques/T1552/005) |

# Cloud Instance Metadata API (attack-pattern--19bf235b-8620-4997-b5b4-94e0659ed7c3)

## Description
Adversaries may attempt to access the Cloud Instance Metadata API to collect credentials and other sensitive data.

Most cloud service providers support a Cloud Instance Metadata API which is a service provided to running virtual instances that allows applications to access information about the running virtual instance. Available information generally includes name, security group, and additional metadata including sensitive data such as credentials and UserData scripts that may contain additional secrets. The Instance Metadata API is provided as a convenience to assist in managing applications and is accessible by anyone who can access the instance.(Citation: AWS Instance Metadata API) A cloud metadata API has been used in at least one high profile compromise.(Citation: Krebs Capital One August 2019)

If adversaries have a presence on the running virtual instance, they may query the Instance Metadata API directly to identify credentials that grant access to additional resources. Additionally, adversaries may exploit a Server-Side Request Forgery (SSRF) vulnerability in a public facing web proxy that allows them to gain access to the sensitive information via a request to the Instance Metadata API.(Citation: RedLock Instance Metadata API 2018)

The de facto standard across cloud service providers is to host the Instance Metadata API at <code>http[:]//169.254.169.254</code>.


## Detection
Monitor access to the Instance Metadata API and look for anomalous queries.

It may be possible to detect adversary use of credentials they have obtained such as in [Valid Accounts](https://attack.mitre.org/techniques/T1078).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1552/005)
- [AWS Instance Metadata API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)
- [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)
- [Krebs Capital One August 2019](https://krebsonsecurity.com/2019/08/what-we-can-learn-from-the-capital-one-hack/)
