---
contributors:
- Microsoft Detection and Response Team (DART)
- Mike Burns, Mandiant
- "Jannie Li, Microsoft Threat Intelligence\u202FCenter\u202F(MSTIC)"
- Arad Inbar, Fidelis Security
- Nilesh Dherange (Gurucul)
- Naveen Vijayaraghavan
data_sources:
- 'Group: Group Modification'
- 'Application Log: Application Log Content'
- 'User Account: User Account Modification'
id: attack-pattern--e74de37c-a829-446c-937d-56a44f0e9306
mitre_attack_url: https://attack.mitre.org/techniques/T1098/002
name: Additional Email Delegate Permissions
platforms:
- Windows
- Office Suite
tactics:
- persistence
- privilege-escalation
title: persistence - Additional Email Delegate Permissions
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | Group: Group Modification, Application Log: Application Log Content, User Account: User Account Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1098/002](https://attack.mitre.org/techniques/T1098/002) |

# Additional Email Delegate Permissions (attack-pattern--e74de37c-a829-446c-937d-56a44f0e9306)

## Description
Adversaries may grant additional permission levels to maintain persistent access to an adversary-controlled email account. 

For example, the <code>Add-MailboxPermission</code> [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlet, available in on-premises Exchange and in the cloud-based service Office 365, adds permissions to a mailbox.(Citation: Microsoft - Add-MailboxPermission)(Citation: FireEye APT35 2018)(Citation: Crowdstrike Hiding in Plain Sight 2018) In Google Workspace, delegation can be enabled via the Google Admin console and users can delegate accounts via their Gmail settings.(Citation: Gmail Delegation)(Citation: Google Ensuring Your Information is Safe) 

Adversaries may also assign mailbox folder permissions through individual folder permissions or roles. In Office 365 environments, adversaries may assign the Default or Anonymous user permissions or roles to the Top of Information Store (root), Inbox, or other mailbox folders. By assigning one or both user permissions to a folder, the adversary can utilize any other account in the tenant to maintain persistence to the target user’s mail folders.(Citation: Mandiant Defend UNC2452 White Paper)

This may be used in persistent threat incidents as well as BEC (Business Email Compromise) incidents where an adversary can add [Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003) to the accounts they wish to compromise. This may further enable use of additional techniques for gaining access to systems. For example, compromised business accounts are often used to send messages to other accounts in the network of the target business while creating inbox rules (ex: [Internal Spearphishing](https://attack.mitre.org/techniques/T1534)), so the messages evade spam/phishing detection mechanisms.(Citation: Bienstock, D. - Defending O365 - 2019)

## Detection
Monitor for unusual Exchange and Office 365 email account permissions changes that may indicate excessively broad permissions being granted to compromised accounts.

Enable the UpdateFolderPermissions action for all logon types. The mailbox audit log will forward folder permission modification events to the Unified Audit Log. Create rules to alert on ModifyFolderPermissions operations where the Anonymous or Default user is assigned permissions other than None. 

A larger than normal volume of emails sent from an account and similar phishing emails sent from  real accounts within a network may be a sign that an account was compromised and attempts to leverage access with modified email permissions is occurring.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1098/002)
- [Bienstock, D. - Defending O365 - 2019](https://www.slideshare.net/DouglasBienstock/shmoocon-2019-becs-and-beyond-investigating-and-defending-office-365)
- [Crowdstrike Hiding in Plain Sight 2018](https://www.crowdstrike.com/blog/hiding-in-plain-sight-using-the-office-365-activities-api-to-investigate-business-email-compromises/)
- [Google Ensuring Your Information is Safe](https://googleblog.blogspot.com/2011/06/ensuring-your-information-is-safe.html)
- [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)
- [FireEye APT35 2018](https://www.fireeye.com/content/dam/collateral/en/mtrends-2018.pdf)
- [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)
- [Microsoft - Add-MailboxPermission](https://docs.microsoft.com/en-us/powershell/module/exchange/mailboxes/add-mailboxpermission?view=exchange-ps)
