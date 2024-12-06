---
data_sources:
- 'Application Log: Application Log Content'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--a9e2cea0-c805-4bf8-9e31-f5f0513a3634
mitre_attack_url: https://attack.mitre.org/techniques/T1137/003
name: Outlook Forms
platforms:
- Windows
- Office Suite
tactics:
- persistence
title: persistence - Outlook Forms
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | Application Log: Application Log Content, Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1137/003](https://attack.mitre.org/techniques/T1137/003) |

# Outlook Forms (attack-pattern--a9e2cea0-c805-4bf8-9e31-f5f0513a3634)

## Description
Adversaries may abuse Microsoft Outlook forms to obtain persistence on a compromised system. Outlook forms are used as templates for presentation and functionality in Outlook messages. Custom Outlook forms can be created that will execute code when a specifically crafted email is sent by an adversary utilizing the same custom Outlook form.(Citation: SensePost Outlook Forms)

Once malicious forms have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious forms will execute when an adversary sends a specifically crafted email to the user.(Citation: SensePost Outlook Forms)

## Detection
Microsoft has released a PowerShell script to safely gather mail forwarding rules and custom forms in your mail environment as well as steps to interpret the output.(Citation: Microsoft Detect Outlook Forms) SensePost, whose tool [Ruler](https://attack.mitre.org/software/S0358) can be used to carry out malicious rules, forms, and Home Page attacks, has released a tool to detect Ruler usage.(Citation: SensePost NotRuler)

Collect process execution information including process IDs (PID) and parent process IDs (PPID) and look for abnormal chains of activity resulting from Office processes. Non-standard process execution trees may also indicate suspicious or malicious behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1137/003)
- [Microsoft Detect Outlook Forms](https://docs.microsoft.com/en-us/office365/securitycompliance/detect-and-remediate-outlook-rules-forms-attack)
- [SensePost NotRuler](https://github.com/sensepost/notruler)
- [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)
