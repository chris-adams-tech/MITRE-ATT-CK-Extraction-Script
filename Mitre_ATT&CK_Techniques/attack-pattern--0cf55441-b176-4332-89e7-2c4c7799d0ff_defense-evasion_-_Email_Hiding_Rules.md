---
contributors:
  - Dor Edry, Microsoft
  - Liran Ravich, CardinalOps
data_sources:
  - "Command: Command Execution"
  - "Application Log: Application Log Content"
  - "File: File Modification"
id: attack-pattern--0cf55441-b176-4332-89e7-2c4c7799d0ff
mitre_attack_url: https://attack.mitre.org/techniques/T1564/008
name: Email Hiding Rules
platforms:
  - Windows
  - Linux
  - macOS
  - Office Suite
tactics:
  - defense-evasion
title: T1564.008 - defense-evasion - Email Hiding Rules
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, Linux, macOS, Office Suite |
| **Data Sources** | Command: Command Execution, Application Log: Application Log Content, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1564/008](https://attack.mitre.org/techniques/T1564/008) |

# Email Hiding Rules (attack-pattern--0cf55441-b176-4332-89e7-2c4c7799d0ff)

## Description
Adversaries may use email rules to hide inbound emails in a compromised user's mailbox. Many email clients allow users to create inbox rules for various email functions, including moving emails to other folders, marking emails as read, or deleting emails. Rules may be created or modified within email clients or through external features such as the <code>New-InboxRule</code> or <code>Set-InboxRule</code> [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlets on Windows systems.(Citation: Microsoft Inbox Rules)(Citation: MacOS Email Rules)(Citation: Microsoft New-InboxRule)(Citation: Microsoft Set-InboxRule)

Adversaries may utilize email rules within a compromised user's mailbox to delete and/or move emails to less noticeable folders. Adversaries may do this to hide security alerts, C2 communication, or responses to [Internal Spearphishing](https://attack.mitre.org/techniques/T1534) emails sent from the compromised account.

Any user or administrator within the organization (or adversary with valid credentials) may be able to create rules to automatically move or delete emails. These rules can be abused to impair/delay detection had the email content been immediately seen by a user or defender. Malicious rules commonly filter out emails based on key words (such as <code>malware</code>, <code>suspicious</code>, <code>phish</code>, and <code>hack</code>) found in message bodies and subject lines. (Citation: Microsoft Cloud App Security)

In some environments, administrators may be able to enable email rules that operate organization-wide rather than on individual inboxes. For example, Microsoft Exchange supports transport rules that evaluate all mail an organization receives against user-specified conditions, then performs a user-specified action on mail that adheres to those conditions.(Citation: Microsoft Mail Flow Rules 2023) Adversaries that abuse such features may be able to automatically modify or delete all emails related to specific topics (such as internal security incident notifications).

## Detection
Monitor email clients and applications for suspicious activity, such as missing messages or abnormal configuration and/or log entries.

On Windows systems, monitor for creation of suspicious inbox rules through the use of the <code>New-InboxRule</code> and <code>Set-InboxRule</code> PowerShell cmdlets.(Citation: Microsoft BEC Campaign) On MacOS systems, monitor for modifications to the <code>RulesActiveState.plist</code>, <code>SyncedRules.plist</code>, <code>UnsyncedRules.plist</code>, and <code>MessageRules.plist</code> files.(Citation: MacOS Email Rules)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1564/008)
- [MacOS Email Rules](https://support.apple.com/guide/mail/use-rules-to-manage-emails-you-receive-mlhlp1017/mac)
- [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)
- [Microsoft Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/mail-flow-rules)
- [Microsoft Inbox Rules](https://support.microsoft.com/en-us/office/manage-email-messages-by-using-rules-c24f5dea-9465-4df4-ad17-a50704d66c59)
- [Microsoft New-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/new-inboxrule?view=exchange-ps)
- [Microsoft Set-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/set-inboxrule?view=exchange-ps)
- [Microsoft Cloud App Security](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/rule-your-inbox-with-microsoft-cloud-app-security/ba-p/299154)
