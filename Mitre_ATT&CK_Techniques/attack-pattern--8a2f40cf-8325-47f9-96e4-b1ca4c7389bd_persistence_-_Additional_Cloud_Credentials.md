---
contributors:
- Expel
- Oleg Kolesnikov, Securonix
- "Jannie Li, Microsoft Threat Intelligence\u202FCenter\u202F(MSTIC)"
- Zur Ulianitzky, XM Cyber
- Alex Soler, AttackIQ
- Dylan Silva, AWS Security
- Arad Inbar, Fidelis Security
- Arun Seelagan, CISA
data_sources:
- 'User Account: User Account Modification'
- 'Active Directory: Active Directory Object Creation'
- 'Active Directory: Active Directory Object Modification'
id: attack-pattern--8a2f40cf-8325-47f9-96e4-b1ca4c7389bd
mitre_attack_url: https://attack.mitre.org/techniques/T1098/001
name: Additional Cloud Credentials
platforms:
- IaaS
- SaaS
- Identity Provider
tactics:
- persistence
- privilege-escalation
title: persistence - Additional Cloud Credentials
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | IaaS, SaaS, Identity Provider |
| **Data Sources** | User Account: User Account Modification, Active Directory: Active Directory Object Creation, Active Directory: Active Directory Object Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1098/001](https://attack.mitre.org/techniques/T1098/001) |

# Additional Cloud Credentials (attack-pattern--8a2f40cf-8325-47f9-96e4-b1ca4c7389bd)

## Description
Adversaries may add adversary-controlled credentials to a cloud account to maintain persistent access to victim accounts and instances within the environment.

For example, adversaries may add credentials for Service Principals and Applications in addition to existing legitimate credentials in Azure / Entra ID.(Citation: Microsoft SolarWinds Customer Guidance)(Citation: Blue Cloud of Death)(Citation: Blue Cloud of Death Video) These credentials include both x509 keys and passwords.(Citation: Microsoft SolarWinds Customer Guidance) With sufficient permissions, there are a variety of ways to add credentials including the Azure Portal, Azure command line interface, and Azure or Az PowerShell modules.(Citation: Demystifying Azure AD Service Principals)

In infrastructure-as-a-service (IaaS) environments, after gaining access through [Cloud Accounts](https://attack.mitre.org/techniques/T1078/004), adversaries may generate or import their own SSH keys using either the <code>CreateKeyPair</code> or <code>ImportKeyPair</code> API in AWS or the <code>gcloud compute os-login ssh-keys add</code> command in GCP.(Citation: GCP SSH Key Add) This allows persistent access to instances within the cloud environment without further usage of the compromised cloud accounts.(Citation: Expel IO Evil in AWS)(Citation: Expel Behind the Scenes)

Adversaries may also use the <code>CreateAccessKey</code> API in AWS or the <code>gcloud iam service-accounts keys create</code> command in GCP to add access keys to an account. Alternatively, they may use the <code>CreateLoginProfile</code> API in AWS to add a password that can be used to log into the AWS Management Console for [Cloud Service Dashboard](https://attack.mitre.org/techniques/T1538).(Citation: Permiso Scattered Spider 2023)(Citation: Lacework AI Resource Hijacking 2024) If the target account has different permissions from the requesting account, the adversary may also be able to escalate their privileges in the environment (i.e. [Cloud Accounts](https://attack.mitre.org/techniques/T1078/004)).(Citation: Rhino Security Labs AWS Privilege Escalation)(Citation: Sysdig ScarletEel 2.0) For example, in Entra ID environments, an adversary with the Application Administrator role can add a new set of credentials to their application's service principal. In doing so the adversary would be able to access the service principal’s roles and permissions, which may be different from those of the Application Administrator.(Citation: SpecterOps Azure Privilege Escalation) 

In AWS environments, adversaries with the appropriate permissions may also use the `sts:GetFederationToken` API call to create a temporary set of credentials to [Forge Web Credentials](https://attack.mitre.org/techniques/T1606) tied to the permissions of the original user account. These temporary credentials may remain valid for the duration of their lifetime even if the original account’s API credentials are deactivated.
(Citation: Crowdstrike AWS User Federation Persistence)

In Entra ID environments with the app password feature enabled, adversaries may be able to add an app password to a user account.(Citation: Mandiant APT42 Operations 2024) As app passwords are intended to be used with legacy devices that do not support multi-factor authentication (MFA), adding an app password can allow an adversary to bypass MFA requirements. Additionally, app passwords may remain valid even if the user’s primary password is reset.(Citation: Microsoft Entra ID App Passwords)

## Detection
Monitor Azure Activity Logs for Service Principal and Application modifications. Monitor for the usage of APIs that create or import SSH keys, particularly by unexpected users or accounts such as the root account.

Monitor for use of credentials at unusual times or to unusual systems or services. This may also correlate with other suspicious activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1098/001)
- [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)
- [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)
- [SpecterOps Azure Privilege Escalation](https://posts.specterops.io/azure-privilege-escalation-via-service-principal-abuse-210ae2be2a5)
- [Demystifying Azure AD Service Principals](https://nedinthecloud.com/2019/07/16/demystifying-azure-ad-service-principals/)
- [Lacework AI Resource Hijacking 2024](https://www.lacework.com/blog/detecting-ai-resource-hijacking-with-composite-alerts)
- [GCP SSH Key Add](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/add)
- [Permiso Scattered Spider 2023](https://permiso.io/blog/lucr-3-scattered-spider-getting-saas-y-in-the-cloud)
- [Blue Cloud of Death Video](https://www.youtube.com/watch?v=wQ1CuAPnrLM&feature=youtu.be&t=2815)
- [Blue Cloud of Death](https://speakerdeck.com/tweekfawkes/blue-cloud-of-death-red-teaming-azure-1)
- [Microsoft Entra ID App Passwords](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-app-passwords)
- [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)
- [Mandiant APT42 Operations 2024](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
- [Expel Behind the Scenes](https://expel.io/blog/behind-the-scenes-expel-soc-alert-aws/)
- [Sysdig ScarletEel 2.0](https://sysdig.com/blog/scarleteel-2-0/)
- [Rhino Security Labs AWS Privilege Escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
