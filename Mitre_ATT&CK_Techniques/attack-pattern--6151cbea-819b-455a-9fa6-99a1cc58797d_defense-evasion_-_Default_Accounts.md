---
data_sources:
- 'Logon Session: Logon Session Creation'
- 'User Account: User Account Authentication'
id: attack-pattern--6151cbea-819b-455a-9fa6-99a1cc58797d
mitre_attack_url: https://attack.mitre.org/techniques/T1078/001
name: Default Accounts
platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Containers
- Network
- Office Suite
- Identity Provider
tactics:
- defense-evasion
- persistence
- privilege-escalation
- initial-access
title: defense-evasion - Default Accounts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence, privilege-escalation, initial-access |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Containers, Network, Office Suite, Identity Provider |
| **Data Sources** | Logon Session: Logon Session Creation, User Account: User Account Authentication |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1078/001](https://attack.mitre.org/techniques/T1078/001) |

# Default Accounts (attack-pattern--6151cbea-819b-455a-9fa6-99a1cc58797d)

## Description
Adversaries may obtain and abuse credentials of a default account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Default accounts are those that are built-into an OS, such as the Guest or Administrator accounts on Windows systems. Default accounts also include default factory/provider set accounts on other types of systems, software, or devices, including the root user account in AWS and the default service account in Kubernetes.(Citation: Microsoft Local Accounts Feb 2019)(Citation: AWS Root User)(Citation: Threat Matrix for Kubernetes)

Default accounts are not limited to client machines, rather also include accounts that are preset for equipment such as network devices and computer applications whether they are internal, open source, or commercial. Appliances that come preset with a username and password combination pose a serious threat to organizations that do not change it post installation, as they are easy targets for an adversary. Similarly, adversaries may also utilize publicly disclosed or stolen [Private Keys](https://attack.mitre.org/techniques/T1552/004) or credential materials to legitimately connect to remote environments via [Remote Services](https://attack.mitre.org/techniques/T1021).(Citation: Metasploit SSH Module)

## Detection
Monitor whether default accounts have been activated or logged into. These audits should also include checks on any appliances and applications for default credentials or SSH keys, and if any are discovered, they should be updated immediately.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1078/001)
- [AWS Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)
- [Microsoft Local Accounts Feb 2019](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts)
- [Metasploit SSH Module](https://github.com/rapid7/metasploit-framework/tree/master/modules/exploits/linux/ssh)
- [Threat Matrix for Kubernetes](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)
