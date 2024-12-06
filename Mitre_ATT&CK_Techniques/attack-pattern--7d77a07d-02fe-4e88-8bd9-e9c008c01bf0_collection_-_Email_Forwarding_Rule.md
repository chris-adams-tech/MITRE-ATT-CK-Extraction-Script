---
contributors:
- Microsoft Security
- Swetha Prabakaran, Microsoft Threat Intelligence Center (MSTIC)
- Liran Ravich, CardinalOps
- Arun Seelagan, CISA
data_sources:
- 'Command: Command Execution'
- 'Application Log: Application Log Content'
- 'Cloud Service: Cloud Service Metadata'
id: attack-pattern--7d77a07d-02fe-4e88-8bd9-e9c008c01bf0
mitre_attack_url: https://attack.mitre.org/techniques/T1114/003
name: Email Forwarding Rule
platforms:
- Windows
- macOS
- Linux
- Office Suite
tactics:
- collection
title: collection - Email Forwarding Rule
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Windows, macOS, Linux, Office Suite |
| **Data Sources** | Command: Command Execution, Application Log: Application Log Content, Cloud Service: Cloud Service Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1114/003](https://attack.mitre.org/techniques/T1114/003) |

# Email Forwarding Rule (attack-pattern--7d77a07d-02fe-4e88-8bd9-e9c008c01bf0)

## Description
Adversaries may setup email forwarding rules to collect sensitive information. Adversaries may abuse email forwarding rules to monitor the activities of a victim, steal information, and further gain intelligence on the victim or the victim’s organization to use as part of further exploits or operations.(Citation: US-CERT TA18-068A 2018) Furthermore, email forwarding rules can allow adversaries to maintain persistent access to victim's emails even after compromised credentials are reset by administrators.(Citation: Pfammatter - Hidden Inbox Rules) Most email clients allow users to create inbox rules for various email functions, including forwarding to a different recipient. These rules may be created through a local email application, a web interface, or by command-line interface. Messages can be forwarded to internal or external recipients, and there are no restrictions limiting the extent of this rule. Administrators may also create forwarding rules for user accounts with the same considerations and outcomes.(Citation: Microsoft Tim McMichael Exchange Mail Forwarding 2)(Citation: Mac Forwarding Rules)

Any user or administrator within the organization (or adversary with valid credentials) can create rules to automatically forward all received messages to another recipient, forward emails to different locations based on the sender, and more. Adversaries may also hide the rule by making use of the Microsoft Messaging API (MAPI) to modify the rule properties, making it hidden and not visible from Outlook, OWA or most Exchange Administration tools.(Citation: Pfammatter - Hidden Inbox Rules)

In some environments, administrators may be able to enable email forwarding rules that operate organization-wide rather than on individual inboxes. For example, Microsoft Exchange supports transport rules that evaluate all mail an organization receives against user-specified conditions, then performs a user-specified action on mail that adheres to those conditions.(Citation: Microsoft Mail Flow Rules 2023) Adversaries that abuse such features may be able to enable forwarding on all or specific mail an organization receives. 

## Detection
Detection is challenging because all messages forwarded because of an auto-forwarding rule have the same presentation as a manually forwarded message. It is also possible for the user to not be aware of the addition of such an auto-forwarding rule and not suspect that their account has been compromised; email-forwarding rules alone will not affect the normal usage patterns or operations of the email account. This is especially true in cases with hidden auto-forwarding rules. This makes it only possible to reliably detect the existence of a hidden auto-forwarding rule by examining message tracking logs or by using a MAPI editor to notice the modified rule property values.(Citation: Pfammatter - Hidden Inbox Rules)

Auto-forwarded messages generally contain specific detectable artifacts that may be present in the header; such artifacts would be platform-specific. Examples include `X-MS-Exchange-Organization-AutoForwarded` set to true, `X-MailFwdBy` and `X-Forwarded-To`. The `forwardingSMTPAddress` parameter used in a forwarding process that is managed by administrators and not by user actions. All messages for the mailbox are forwarded to the specified SMTP address. However, unlike typical client-side rules, the message does not appear as forwarded in the mailbox; it appears as if it were sent directly to the specified destination mailbox.(Citation: Microsoft Tim McMichael Exchange Mail Forwarding 2) High volumes of emails that bear the `X-MS-Exchange-Organization-AutoForwarded` header (indicating auto-forwarding) without a corresponding number of emails that match the appearance of a forwarded message may indicate that further investigation is needed at the administrator level rather than user-level.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1114/003)
- [Mac Forwarding Rules](https://support.apple.com/guide/mail/reply-to-forward-or-redirect-emails-mlhlp1010/mac)
- [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)
- [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)
- [Microsoft Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/mail-flow-rules)
- [US-CERT TA18-068A 2018](https://www.us-cert.gov/ncas/alerts/TA18-086A)
