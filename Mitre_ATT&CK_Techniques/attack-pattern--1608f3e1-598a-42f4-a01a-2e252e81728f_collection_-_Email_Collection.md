---
contributors:
- Swetha Prabakaran, Microsoft Threat Intelligence Center (MSTIC)
- Menachem Goldstein
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Connection Creation'
- 'File: File Access'
- 'Command: Command Execution'
id: attack-pattern--1608f3e1-598a-42f4-a01a-2e252e81728f
mitre_attack_url: https://attack.mitre.org/techniques/T1114
name: Email Collection
platforms:
- Windows
- macOS
- Linux
- Office Suite
tactics:
- collection
title: collection - Email Collection
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Windows, macOS, Linux, Office Suite |
| **Data Sources** | Logon Session: Logon Session Creation, Application Log: Application Log Content, Network Traffic: Network Connection Creation, File: File Access, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1114](https://attack.mitre.org/techniques/T1114) |

# Email Collection (attack-pattern--1608f3e1-598a-42f4-a01a-2e252e81728f)

## Description
Adversaries may target user email to collect sensitive information. Emails may contain sensitive data, including trade secrets or personal information, that can prove valuable to adversaries. Emails may also contain details of ongoing incident response operations, which may allow adversaries to adjust their techniques in order to maintain persistence or evade defenses.(Citation: TrustedSec OOB Communications)(Citation: CISA AA20-352A 2021) Adversaries can collect or forward email from mail servers or clients. 

## Detection
There are likely a variety of ways an adversary could collect email from a target, each with a different mechanism for detection.

File access of local system email files for Exfiltration, unusual processes connecting to an email server within a network, or unusual access patterns or authentication attempts on a public-facing webmail server may all be indicators of malicious activity.

Monitor processes and command-line arguments for actions that could be taken to gather local email files. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

Detection is challenging because all messages forwarded because of an auto-forwarding rule have the same presentation as a manually forwarded message. It is also possible for the user to not be aware of the addition of such an auto-forwarding rule and not suspect that their account has been compromised; email-forwarding rules alone will not affect the normal usage patterns or operations of the email account.

Auto-forwarded messages generally contain specific detectable artifacts that may be present in the header; such artifacts would be platform-specific. Examples include <code>X-MS-Exchange-Organization-AutoForwarded</code> set to true, <code>X-MailFwdBy</code> and <code>X-Forwarded-To</code>. The <code>forwardingSMTPAddress</code> parameter used in a forwarding process that is managed by administrators and not by user actions. All messages for the mailbox are forwarded to the specified SMTP address. However, unlike typical client-side rules, the message does not appear as forwarded in the mailbox; it appears as if it were sent directly to the specified destination mailbox.(Citation: Microsoft Tim McMichael Exchange Mail Forwarding 2) High volumes of emails that bear the <code>X-MS-Exchange-Organization-AutoForwarded</code> header (indicating auto-forwarding) without a corresponding number of emails that match the appearance of a forwarded message may indicate that further investigation is needed at the administrator level rather than user-level.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1114)
- [CISA AA20-352A 2021](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a)
- [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)
- [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)
