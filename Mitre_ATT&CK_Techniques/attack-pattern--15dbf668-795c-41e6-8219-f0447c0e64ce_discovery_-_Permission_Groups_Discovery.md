---
contributors:
- Daniel Prizmant, Palo Alto Networks
- Yuval Avrahami, Palo Alto Networks
- Microsoft Threat Intelligence Center (MSTIC)
data_sources:
- 'Process: Process Creation'
- 'Group: Group Metadata'
- 'Command: Command Execution'
- 'Application Log: Application Log Content'
- 'Group: Group Enumeration'
id: attack-pattern--15dbf668-795c-41e6-8219-f0447c0e64ce
mitre_attack_url: https://attack.mitre.org/techniques/T1069
name: Permission Groups Discovery
platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Containers
- Office Suite
- Identity Provider
tactics:
- discovery
title: discovery - Permission Groups Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Containers, Office Suite, Identity Provider |
| **Data Sources** | Process: Process Creation, Group: Group Metadata, Command: Command Execution, Application Log: Application Log Content, Group: Group Enumeration |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1069](https://attack.mitre.org/techniques/T1069) |

# Permission Groups Discovery (attack-pattern--15dbf668-795c-41e6-8219-f0447c0e64ce)

## Description
Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.

Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting.(Citation: CrowdStrike BloodHound April 2018)

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001). Monitor container logs for commands and/or API calls related to listing permissions for pods and nodes, such as <code>kubectl auth can-i</code>.(Citation: K8s Authorization Overview)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1069)
- [K8s Authorization Overview](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)
- [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
