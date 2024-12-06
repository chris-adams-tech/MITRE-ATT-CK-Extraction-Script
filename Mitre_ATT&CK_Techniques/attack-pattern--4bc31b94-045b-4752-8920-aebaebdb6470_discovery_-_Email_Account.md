---
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--4bc31b94-045b-4752-8920-aebaebdb6470
mitre_attack_url: https://attack.mitre.org/techniques/T1087/003
name: Email Account
platforms:
- Windows
- Office Suite
tactics:
- discovery
title: discovery - Email Account
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1087/003](https://attack.mitre.org/techniques/T1087/003) |

# Email Account (attack-pattern--4bc31b94-045b-4752-8920-aebaebdb6470)

## Description
Adversaries may attempt to get a listing of email addresses and accounts. Adversaries may try to dump Exchange address lists such as global address lists (GALs).(Citation: Microsoft Exchange Address Lists)

In on-premises Exchange and Exchange Online, the <code>Get-GlobalAddressList</code> PowerShell cmdlet can be used to obtain email addresses and accounts from a domain using an authenticated session.(Citation: Microsoft getglobaladdresslist)(Citation: Black Hills Attacking Exchange MailSniper, 2016)

In Google Workspace, the GAL is shared with Microsoft Outlook users through the Google Workspace Sync for Microsoft Outlook (GWSMO) service. Additionally, the Google Workspace Directory allows for users to get a listing of other users within the organization.(Citation: Google Workspace Global Access List)

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1087/003)
- [Black Hills Attacking Exchange MailSniper, 2016](https://www.blackhillsinfosec.com/attacking-exchange-with-mailsniper/)
- [Google Workspace Global Access List](https://support.google.com/a/answer/166870?hl=en)
- [Microsoft Exchange Address Lists](https://docs.microsoft.com/en-us/exchange/email-addresses-and-address-books/address-lists/address-lists?view=exchserver-2019)
- [Microsoft getglobaladdresslist](https://docs.microsoft.com/en-us/powershell/module/exchange/email-addresses-and-address-books/get-globaladdresslist)
