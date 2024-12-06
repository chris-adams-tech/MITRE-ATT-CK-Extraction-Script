---
contributors:
- Praetorian
- Microsoft Threat Intelligence Center (MSTIC)
- Arun Seelagan, CISA
data_sources:
- 'User Account: User Account Creation'
id: attack-pattern--a009cb25-4801-4116-9105-80a91cf15c1b
mitre_attack_url: https://attack.mitre.org/techniques/T1136/003
name: Cloud Account
platforms:
- IaaS
- SaaS
- Office Suite
- Identity Provider
tactics:
- persistence
title: persistence - Cloud Account
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | IaaS, SaaS, Office Suite, Identity Provider |
| **Data Sources** | User Account: User Account Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1136/003](https://attack.mitre.org/techniques/T1136/003) |

# Cloud Account (attack-pattern--a009cb25-4801-4116-9105-80a91cf15c1b)

## Description
Adversaries may create a cloud account to maintain access to victim systems. With a sufficient level of access, such accounts may be used to establish secondary credentialed access that does not require persistent remote access tools to be deployed on the system.(Citation: Microsoft O365 Admin Roles)(Citation: Microsoft Support O365 Add Another Admin, October 2019)(Citation: AWS Create IAM User)(Citation: GCP Create Cloud Identity Users)(Citation: Microsoft Azure AD Users)

In addition to user accounts, cloud accounts may be associated with services. Cloud providers handle the concept of service accounts in different ways. In Azure, service accounts include service principals and managed identities, which can be linked to various resources such as OAuth applications, serverless functions, and virtual machines in order to grant those resources permissions to perform various activities in the environment.(Citation: Microsoft Entra ID Service Principals) In GCP, service accounts can also be linked to specific resources, as well as be impersonated by other accounts for [Temporary Elevated Cloud Access](https://attack.mitre.org/techniques/T1548/005).(Citation: GCP Service Accounts) While AWS has no specific concept of service accounts, resources can be directly granted permission to assume roles.(Citation: AWS Instance Profiles)(Citation: AWS Lambda Execution Role)

Adversaries may create accounts that only have access to specific cloud services, which can reduce the chance of detection.

Once an adversary has created a cloud account, they can then manipulate that account to ensure persistence and allow access to additional resources - for example, by adding [Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001) or assigning [Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003).

## Detection
Collect usage logs from cloud user and administrator accounts to identify unusual activity in the creation of new accounts and assignment of roles to those accounts. Monitor for accounts assigned to admin roles that go over a certain threshold of known admins.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1136/003)
- [Microsoft O365 Admin Roles](https://docs.microsoft.com/en-us/office365/admin/add-users/about-admin-roles?view=o365-worldwide)
- [AWS Create IAM User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
- [AWS Lambda Execution Role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)
- [AWS Instance Profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)
- [GCP Create Cloud Identity Users](https://support.google.com/cloudidentity/answer/7332836?hl=en&ref_topic=7558554)
- [GCP Service Accounts](https://cloud.google.com/iam/docs/service-account-overview)
- [Microsoft Azure AD Users](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/add-users-azure-active-directory)
- [Microsoft Entra ID Service Principals](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals?tabs=browser)
- [Microsoft Support O365 Add Another Admin, October 2019](https://support.office.com/en-us/article/add-another-admin-f693489f-9f55-4bd0-a637-a81ce93de22d)
