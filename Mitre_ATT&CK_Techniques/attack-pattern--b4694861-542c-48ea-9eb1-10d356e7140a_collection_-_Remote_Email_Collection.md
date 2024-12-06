---
contributors:
- Arun Seelagan, CISA
data_sources:
- 'Application Log: Application Log Content'
- 'Logon Session: Logon Session Creation'
- 'Command: Command Execution'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--b4694861-542c-48ea-9eb1-10d356e7140a
mitre_attack_url: https://attack.mitre.org/techniques/T1114/002
name: Remote Email Collection
platforms:
- Windows
- Office Suite
tactics:
- collection
title: collection - Remote Email Collection
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | Application Log: Application Log Content, Logon Session: Logon Session Creation, Command: Command Execution, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1114/002](https://attack.mitre.org/techniques/T1114/002) |

# Remote Email Collection (attack-pattern--b4694861-542c-48ea-9eb1-10d356e7140a)

## Description
Adversaries may target an Exchange server, Office 365, or Google Workspace to collect sensitive information. Adversaries may leverage a user's credentials and interact directly with the Exchange server to acquire information from within a network. Adversaries may also access externally facing Exchange services, Office 365, or Google Workspace to access email using credentials or access tokens. Tools such as [MailSniper](https://attack.mitre.org/software/S0413) can be used to automate searches for specific keywords.

## Detection
Monitor for unusual login activity from unknown or abnormal locations, especially for privileged accounts (ex: Exchange administrator account).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1114/002)
