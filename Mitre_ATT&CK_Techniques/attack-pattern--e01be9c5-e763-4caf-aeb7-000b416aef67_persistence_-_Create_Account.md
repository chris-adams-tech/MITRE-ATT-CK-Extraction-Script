---
contributors:
- Microsoft Threat Intelligence Center (MSTIC)
- Praetorian
- Austin Clark, @c2defense
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'User Account: User Account Creation'
id: attack-pattern--e01be9c5-e763-4caf-aeb7-000b416aef67
mitre_attack_url: https://attack.mitre.org/techniques/T1136
name: Create Account
platforms:
- Windows
- IaaS
- Linux
- macOS
- Network
- Containers
- SaaS
- Office Suite
- Identity Provider
tactics:
- persistence
title: persistence - Create Account
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, IaaS, Linux, macOS, Network, Containers, SaaS, Office Suite, Identity Provider |
| **Data Sources** | Process: Process Creation, Command: Command Execution, User Account: User Account Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1136](https://attack.mitre.org/techniques/T1136) |

# Create Account (attack-pattern--e01be9c5-e763-4caf-aeb7-000b416aef67)

## Description
Adversaries may create an account to maintain access to victim systems.(Citation: Symantec WastedLocker June 2020) With a sufficient level of access, creating such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

Accounts may be created on the local system or within a domain or cloud tenant. In cloud environments, adversaries may create accounts that only have access to specific services, which can reduce the chance of detection.

## Detection
Monitor for processes and command-line parameters associated with account creation, such as <code>net user</code> or <code>useradd</code>. Collect data on account creation within a network. Event ID 4720 is generated when a user account is created on a Windows system and domain controller. (Citation: Microsoft User Creation Event) Perform regular audits of domain and local system accounts to detect suspicious accounts that may have been created by an adversary.

Collect usage logs from cloud administrator accounts to identify unusual activity in the creation of new accounts and assignment of roles to those accounts. Monitor for accounts assigned to admin roles that go over a certain threshold of known admins.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1136)
- [Microsoft User Creation Event](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720)
- [Symantec WastedLocker June 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
