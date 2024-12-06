---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'File: File Creation'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--718cb208-6446-4572-a2f0-9c799c60091e
mitre_attack_url: https://attack.mitre.org/techniques/T1496/002
name: Bandwidth Hijacking
platforms:
- Linux
- Windows
- macOS
- IaaS
- Containers
tactics:
- impact
title: impact - Bandwidth Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, Windows, macOS, IaaS, Containers |
| **Data Sources** | Network Traffic: Network Traffic Flow, File: File Creation, Command: Command Execution, Process: Process Creation, Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1496/002](https://attack.mitre.org/techniques/T1496/002) |

# Bandwidth Hijacking (attack-pattern--718cb208-6446-4572-a2f0-9c799c60091e)

## Description
Adversaries may leverage the network bandwidth resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. 

Adversaries may also use malware that leverages a system's network bandwidth as part of a botnet in order to facilitate [Network Denial of Service](https://attack.mitre.org/techniques/T1498) campaigns and/or to seed malicious torrents.(Citation: GoBotKR) Alternatively, they may engage in proxyjacking by selling use of the victims' network bandwidth and IP address to proxyware services.(Citation: Sysdig Proxyjacking) Finally, they may engage in internet-wide scanning in order to identify additional targets for compromise.(Citation: Unit 42 Leaked Environment Variables 2024)

In addition to incurring potential financial costs or availability disruptions, this technique may cause reputational damage if a victim’s bandwidth is used for illegal activities.(Citation: Sysdig Proxyjacking)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1496/002)
- [Sysdig Proxyjacking](https://sysdig.com/blog/proxyjacking-attackers-log4j-exploited/)
- [Unit 42 Leaked Environment Variables 2024](https://unit42.paloaltonetworks.com/large-scale-cloud-extortion-operation/)
- [GoBotKR](https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/)
