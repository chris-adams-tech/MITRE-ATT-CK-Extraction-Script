---
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'User Account: User Account Creation'
id: attack-pattern--7610cada-1499-41a4-b3dd-46467b68d177
mitre_attack_url: https://attack.mitre.org/techniques/T1136/002
name: Domain Account
platforms:
- Windows
- macOS
- Linux
tactics:
- persistence
title: persistence - Domain Account
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Process: Process Creation, Command: Command Execution, User Account: User Account Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1136/002](https://attack.mitre.org/techniques/T1136/002) |

# Domain Account (attack-pattern--7610cada-1499-41a4-b3dd-46467b68d177)

## Description
Adversaries may create a domain account to maintain access to victim systems. Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover user, administrator, and service accounts. With a sufficient level of access, the <code>net user /add /domain</code> command can be used to create a domain account.(Citation: Savill 1999)

Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

## Detection
Monitor for processes and command-line parameters associated with domain account creation, such as <code>net user /add /domain</code>. Collect data on account creation within a network. Event ID 4720 is generated when a user account is created on a Windows domain controller. (Citation: Microsoft User Creation Event) Perform regular audits of domain accounts to detect suspicious accounts that may have been created by an adversary.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1136/002)
- [Microsoft User Creation Event](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720)
- [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
