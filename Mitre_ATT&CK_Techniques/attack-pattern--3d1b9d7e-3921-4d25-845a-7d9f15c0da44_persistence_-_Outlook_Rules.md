---
contributors:
- Microsoft Security
data_sources:
- 'Process: Process Creation'
- 'Application Log: Application Log Content'
- 'Command: Command Execution'
id: attack-pattern--3d1b9d7e-3921-4d25-845a-7d9f15c0da44
mitre_attack_url: https://attack.mitre.org/techniques/T1137/005
name: Outlook Rules
platforms:
- Windows
- Office Suite
tactics:
- persistence
title: persistence - Outlook Rules
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | Process: Process Creation, Application Log: Application Log Content, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1137/005](https://attack.mitre.org/techniques/T1137/005) |

# Outlook Rules (attack-pattern--3d1b9d7e-3921-4d25-845a-7d9f15c0da44)

## Description
Adversaries may abuse Microsoft Outlook rules to obtain persistence on a compromised system. Outlook rules allow a user to define automated behavior to manage email messages. A benign rule might, for example, automatically move an email to a particular folder in Outlook if it contains specific words from a specific sender. Malicious Outlook rules can be created that can trigger code execution when an adversary sends a specifically crafted email to that user.(Citation: SilentBreak Outlook Rules)

Once malicious rules have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious rules will execute when an adversary sends a specifically crafted email to the user.(Citation: SilentBreak Outlook Rules)

## Detection
Microsoft has released a PowerShell script to safely gather mail forwarding rules and custom forms in your mail environment as well as steps to interpret the output.(Citation: Microsoft Detect Outlook Forms) This PowerShell script is ineffective in gathering rules with modified `PRPR_RULE_MSG_NAME` and `PR_RULE_MSG_PROVIDER` properties caused by adversaries using a Microsoft Exchange Server Messaging API Editor (MAPI Editor), so only examination with the Exchange Administration tool MFCMapi can reveal these mail forwarding rules.(Citation: Pfammatter - Hidden Inbox Rules) SensePost, whose tool [Ruler](https://attack.mitre.org/software/S0358) can be used to carry out malicious rules, forms, and Home Page attacks, has released a tool to detect Ruler usage.(Citation: SensePost NotRuler)

Collect process execution information including process IDs (PID) and parent process IDs (PPID) and look for abnormal chains of activity resulting from Office processes. Non-standard process execution trees may also indicate suspicious or malicious behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1137/005)
- [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)
- [Microsoft Detect Outlook Forms](https://docs.microsoft.com/en-us/office365/securitycompliance/detect-and-remediate-outlook-rules-forms-attack)
- [SilentBreak Outlook Rules](https://silentbreaksecurity.com/malicious-outlook-rules/)
- [SensePost NotRuler](https://github.com/sensepost/notruler)
