---
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Logon Session: Logon Session Metadata'
- 'User Account: User Account Authentication'
id: attack-pattern--fdc47f44-dd32-4b99-af5f-209f556f63c2
mitre_attack_url: https://attack.mitre.org/techniques/T1078/003
name: Local Accounts
platforms:
- Linux
- macOS
- Windows
- Containers
- Network
tactics:
- defense-evasion
- persistence
- privilege-escalation
- initial-access
title: defense-evasion - Local Accounts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence, privilege-escalation, initial-access |
| **Platforms** | Linux, macOS, Windows, Containers, Network |
| **Data Sources** | Logon Session: Logon Session Creation, Logon Session: Logon Session Metadata, User Account: User Account Authentication |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1078/003](https://attack.mitre.org/techniques/T1078/003) |

# Local Accounts (attack-pattern--fdc47f44-dd32-4b99-af5f-209f556f63c2)

## Description
Adversaries may obtain and abuse credentials of a local account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service.

Local Accounts may also be abused to elevate privileges and harvest credentials through [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). Password reuse may allow the abuse of local accounts across a set of machines on a network for the purposes of Privilege Escalation and Lateral Movement. 

## Detection
Perform regular audits of local system accounts to detect accounts that may have been created by an adversary for persistence. Look for suspicious account behavior, such as accounts logged in at odd times or outside of business hours.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1078/003)
