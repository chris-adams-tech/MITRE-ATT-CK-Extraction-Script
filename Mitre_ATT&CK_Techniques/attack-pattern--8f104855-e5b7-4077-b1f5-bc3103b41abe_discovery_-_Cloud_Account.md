---
contributors:
- Praetorian
data_sources:
- 'Command: Command Execution'
id: attack-pattern--8f104855-e5b7-4077-b1f5-bc3103b41abe
mitre_attack_url: https://attack.mitre.org/techniques/T1087/004
name: Cloud Account
platforms:
- SaaS
- IaaS
- Office Suite
- Identity Provider
tactics:
- discovery
title: discovery - Cloud Account
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | SaaS, IaaS, Office Suite, Identity Provider |
| **Data Sources** | Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1087/004](https://attack.mitre.org/techniques/T1087/004) |

# Cloud Account (attack-pattern--8f104855-e5b7-4077-b1f5-bc3103b41abe)

## Description
Adversaries may attempt to get a listing of cloud accounts. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of resources within a cloud service provider or SaaS application.

With authenticated access there are several tools that can be used to find accounts. The <code>Get-MsolRoleMember</code> PowerShell cmdlet can be used to obtain account names given a role or permissions group in Office 365.(Citation: Microsoft msolrolemember)(Citation: GitHub Raindance) The Azure CLI (AZ CLI) also provides an interface to obtain user accounts with authenticated access to a domain. The command <code>az ad user list</code> will list all users within a domain.(Citation: Microsoft AZ CLI)(Citation: Black Hills Red Teaming MS AD Azure, 2018) 

The AWS command <code>aws iam list-users</code> may be used to obtain a list of users in the current account while <code>aws iam list-roles</code> can obtain IAM roles that have a specified path prefix.(Citation: AWS List Roles)(Citation: AWS List Users) In GCP, <code>gcloud iam service-accounts list</code> and <code>gcloud projects get-iam-policy</code> may be used to obtain a listing of service accounts and users in a project.(Citation: Google Cloud - IAM Servie Accounts List API)

## Detection
Monitor processes, command-line arguments, and logs for actions that could be taken to gather information about cloud accounts, including the use of calls to cloud APIs that perform account discovery.

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment, and also to an extent in normal network operations. Therefore discovery data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1087/004)
- [AWS List Roles](https://docs.aws.amazon.com/cli/latest/reference/iam/list-roles.html)
- [AWS List Users](https://docs.aws.amazon.com/cli/latest/reference/iam/list-users.html)
- [Black Hills Red Teaming MS AD Azure, 2018](https://www.blackhillsinfosec.com/red-teaming-microsoft-part-1-active-directory-leaks-via-azure/)
- [Google Cloud - IAM Servie Accounts List API](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list)
- [Microsoft AZ CLI](https://docs.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)
- [Microsoft msolrolemember](https://docs.microsoft.com/en-us/powershell/module/msonline/get-msolrolemember?view=azureadps-1.0)
- [GitHub Raindance](https://github.com/True-Demon/raindance)
