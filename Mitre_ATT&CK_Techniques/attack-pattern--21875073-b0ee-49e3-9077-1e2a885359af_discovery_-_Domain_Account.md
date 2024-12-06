---
contributors:
- ExtraHop
- Miriam Wiesner, @miriamxyra, Microsoft Security
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Process: OS API Execution'
- 'Network Traffic: Network Traffic Content'
- 'Group: Group Enumeration'
id: attack-pattern--21875073-b0ee-49e3-9077-1e2a885359af
mitre_attack_url: https://attack.mitre.org/techniques/T1087/002
name: Domain Account
platforms:
- Linux
- macOS
- Windows
tactics:
- discovery
title: discovery - Domain Account
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution, Process: OS API Execution, Network Traffic: Network Traffic Content, Group: Group Enumeration |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1087/002](https://attack.mitre.org/techniques/T1087/002) |

# Domain Account (attack-pattern--21875073-b0ee-49e3-9077-1e2a885359af)

## Description
Adversaries may attempt to get a listing of domain accounts. This information can help adversaries determine which domain accounts exist to aid in follow-on behavior such as targeting specific accounts which possess particular privileges.

Commands such as <code>net user /domain</code> and <code>net group /domain</code> of the [Net](https://attack.mitre.org/software/S0039) utility, <code>dscacheutil -q group</code> on macOS, and <code>ldapsearch</code> on Linux can list domain users and groups. [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlets including <code>Get-ADUser</code> and <code>Get-ADGroupMember</code> may enumerate members of Active Directory groups.(Citation: CrowdStrike StellarParticle January 2022)  

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).


## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1087/002)
- [CrowdStrike StellarParticle January 2022](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
