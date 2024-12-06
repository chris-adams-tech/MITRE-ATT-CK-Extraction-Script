---
contributors:
- "Jannie Li, Microsoft Threat Intelligence\u202FCenter\u202F(MSTIC)"
- Praetorian
- Tim MalcomVetter
- Wojciech Lesicki
- Arad Inbar, Fidelis Security
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Active Directory: Active Directory Object Modification'
- 'File: File Modification'
- 'Group: Group Modification'
- 'User Account: User Account Modification'
id: attack-pattern--a10641f4-87b4-45a3-a906-92a149cb2c27
mitre_attack_url: https://attack.mitre.org/techniques/T1098
name: Account Manipulation
platforms:
- Windows
- IaaS
- Linux
- macOS
- SaaS
- Network
- Containers
- Office Suite
- Identity Provider
tactics:
- persistence
- privilege-escalation
title: persistence - Account Manipulation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows, IaaS, Linux, macOS, SaaS, Network, Containers, Office Suite, Identity Provider |
| **Data Sources** | Command: Command Execution, Process: Process Creation, Active Directory: Active Directory Object Modification, File: File Modification, Group: Group Modification, User Account: User Account Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1098](https://attack.mitre.org/techniques/T1098) |

# Account Manipulation (attack-pattern--a10641f4-87b4-45a3-a906-92a149cb2c27)

## Description
Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials or permission groups.(Citation: FireEye SMOKEDHAM June 2021) These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve the life of compromised credentials. 

In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged [Valid Accounts](https://attack.mitre.org/techniques/T1078).

## Detection
Collect events that correlate with changes to account objects and/or permissions on systems and the domain, such as event IDs 4738, 4728 and 4670.(Citation: Microsoft User Modified Event)(Citation: Microsoft Security Event 4670)(Citation: Microsoft Security Event 4670) Monitor for modification of accounts in correlation with other suspicious activity. Changes may occur at unusual times or from unusual systems. Especially flag events where the subject and target accounts differ(Citation: InsiderThreat ChangeNTLM July 2017) or that include additional flags such as changing a password without knowledge of the old password.(Citation: GitHub Mimikatz Issue 92 June 2017)

Monitor for use of credentials at unusual times or to unusual systems or services. This may also correlate with other suspicious activity.

Monitor for unusual permissions changes that may indicate excessively broad permissions being granted to compromised accounts. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged [Valid Accounts](https://attack.mitre.org/techniques/T1078)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1098)
- [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
- [Microsoft Security Event 4670](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4670)
- [Microsoft User Modified Event](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738)
- [InsiderThreat ChangeNTLM July 2017](https://blog.stealthbits.com/manipulating-user-passwords-with-mimikatz-SetNTLM-ChangeNTLM)
- [GitHub Mimikatz Issue 92 June 2017](https://github.com/gentilkiwi/mimikatz/issues/92)
