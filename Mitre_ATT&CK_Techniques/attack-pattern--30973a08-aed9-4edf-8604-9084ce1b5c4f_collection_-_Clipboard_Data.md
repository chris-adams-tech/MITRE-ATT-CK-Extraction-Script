---
data_sources:
- 'Process: OS API Execution'
- 'Command: Command Execution'
id: attack-pattern--30973a08-aed9-4edf-8604-9084ce1b5c4f
mitre_attack_url: https://attack.mitre.org/techniques/T1115
name: Clipboard Data
platforms:
- Linux
- Windows
- macOS
tactics:
- collection
title: collection - Clipboard Data
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Process: OS API Execution, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1115](https://attack.mitre.org/techniques/T1115) |

# Clipboard Data (attack-pattern--30973a08-aed9-4edf-8604-9084ce1b5c4f)

## Description
Adversaries may collect data stored in the clipboard from users copying information within or between applications. 

For example, on Windows adversaries can access clipboard data by using <code>clip.exe</code> or <code>Get-Clipboard</code>.(Citation: MSDN Clipboard)(Citation: clip_win_server)(Citation: CISA_AA21_200B) Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002)).(Citation: mining_ruby_reversinglabs)

macOS and Linux also have commands, such as <code>pbpaste</code>, to grab clipboard contents.(Citation: Operating with EmPyre)

## Detection
Access to the clipboard is a legitimate function of many applications on an operating system. If an organization chooses to monitor for this behavior, then the data will likely need to be correlated against other suspicious or non-user-driven activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1115)
- [CISA_AA21_200B](https://www.cisa.gov/uscert/ncas/alerts/aa21-200b)
- [mining_ruby_reversinglabs](https://blog.reversinglabs.com/blog/mining-for-malicious-ruby-gems)
- [clip_win_server](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/clip)
- [MSDN Clipboard](https://msdn.microsoft.com/en-us/library/ms649012)
- [Operating with EmPyre](https://medium.com/rvrsh3ll/operating-with-empyre-ea764eda3363)
