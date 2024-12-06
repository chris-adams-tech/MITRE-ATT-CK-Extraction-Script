---
contributors:
- Microsoft Threat Intelligence Center (MSTIC)
- Alex Parsons, Crowdstrike
- Chris Romano, Crowdstrike
- Wojciech Lesicki
- "Pi\xE0 Consigny, Tenable"
- "Cl\xE9ment Notin, Tenable"
- Praetorian
- Alex Soler, AttackIQ
- Arad Inbar, Fidelis Security
- Arun Seelagan, CISA
data_sources:
- 'User Account: User Account Modification'
id: attack-pattern--2dbbdcd5-92cf-44c0-aea2-fe24783a6bc3
mitre_attack_url: https://attack.mitre.org/techniques/T1098/003
name: Additional Cloud Roles
platforms:
- IaaS
- SaaS
- Office Suite
- Identity Provider
tactics:
- persistence
- privilege-escalation
title: persistence - Additional Cloud Roles
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | IaaS, SaaS, Office Suite, Identity Provider |
| **Data Sources** | User Account: User Account Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1098/003](https://attack.mitre.org/techniques/T1098/003) |

# Additional Cloud Roles (attack-pattern--2dbbdcd5-92cf-44c0-aea2-fe24783a6bc3)

## Description
An adversary may add additional roles or permissions to an adversary-controlled cloud account to maintain persistent access to a tenant. For example, adversaries may update IAM policies in cloud-based environments or add a new global administrator in Office 365 environments.(Citation: AWS IAM Policies and Permissions)(Citation: Google Cloud IAM Policies)(Citation: Microsoft Support O365 Add Another Admin, October 2019)(Citation: Microsoft O365 Admin Roles) With sufficient permissions, a compromised account can gain almost unlimited access to data and settings (including the ability to reset the passwords of other admins).(Citation: Expel AWS Attacker)
(Citation: Microsoft O365 Admin Roles) 

This account modification may immediately follow [Create Account](https://attack.mitre.org/techniques/T1136) or other malicious account activity. Adversaries may also modify existing [Valid Accounts](https://attack.mitre.org/techniques/T1078) that they have compromised. This could lead to privilege escalation, particularly if the roles added allow for lateral movement to additional accounts.

For example, in AWS environments, an adversary with appropriate permissions may be able to use the <code>CreatePolicyVersion</code> API to define a new version of an IAM policy or the <code>AttachUserPolicy</code> API to attach an IAM policy with additional or distinct permissions to a compromised user account.(Citation: Rhino Security Labs AWS Privilege Escalation)

In some cases, adversaries may add roles to adversary-controlled accounts outside the victim cloud tenant. This allows these external accounts to perform actions inside the victim tenant without requiring the adversary to [Create Account](https://attack.mitre.org/techniques/T1136) or modify a victim-owned account.(Citation: Invictus IR DangerDev 2024)

## Detection
Collect activity logs from IAM services and cloud administrator accounts to identify unusual activity in the assignment of roles to those accounts. Monitor for accounts assigned to admin roles that go over a certain threshold of known admins. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1098/003)
- [Expel AWS Attacker](https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/)
- [Microsoft O365 Admin Roles](https://docs.microsoft.com/en-us/office365/admin/add-users/about-admin-roles?view=o365-worldwide)
- [AWS IAM Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Google Cloud IAM Policies](https://cloud.google.com/iam/docs/policies)
- [Invictus IR DangerDev 2024](https://www.invictus-ir.com/news/the-curious-case-of-dangerdev-protonmail-me)
- [Microsoft Support O365 Add Another Admin, October 2019](https://support.office.com/en-us/article/add-another-admin-f693489f-9f55-4bd0-a637-a81ce93de22d)
- [Rhino Security Labs AWS Privilege Escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
