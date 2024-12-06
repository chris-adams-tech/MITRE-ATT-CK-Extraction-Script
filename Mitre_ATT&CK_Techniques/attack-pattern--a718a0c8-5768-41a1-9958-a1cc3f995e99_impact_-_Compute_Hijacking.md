---
data_sources:
- 'Command: Command Execution'
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
- 'Sensor Health: Host Status'
- 'Process: Process Creation'
- 'File: File Creation'
id: attack-pattern--a718a0c8-5768-41a1-9958-a1cc3f995e99
mitre_attack_url: https://attack.mitre.org/techniques/T1496/001
name: Compute Hijacking
platforms:
- Windows
- IaaS
- Linux
- macOS
- Containers
tactics:
- impact
title: impact - Compute Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, IaaS, Linux, macOS, Containers |
| **Data Sources** | Command: Command Execution, Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow, Sensor Health: Host Status, Process: Process Creation, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1496/001](https://attack.mitre.org/techniques/T1496/001) |

# Compute Hijacking (attack-pattern--a718a0c8-5768-41a1-9958-a1cc3f995e99)

## Description
Adversaries may leverage the compute resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. 

One common purpose for [Compute Hijacking](https://attack.mitre.org/techniques/T1496/001) is to validate transactions of cryptocurrency networks and earn virtual currency. Adversaries may consume enough system resources to negatively impact and/or cause affected machines to become unresponsive.(Citation: Kaspersky Lazarus Under The Hood Blog 2017) Servers and cloud-based systems are common targets because of the high potential for available resources, but user endpoint systems may also be compromised and used for [Compute Hijacking](https://attack.mitre.org/techniques/T1496/001) and cryptocurrency mining.(Citation: CloudSploit - Unused AWS Regions) Containerized environments may also be targeted due to the ease of deployment via exposed APIs and the potential for scaling mining activities by deploying or compromising multiple containers within an environment or cluster.(Citation: Unit 42 Hildegard Malware)(Citation: Trend Micro Exposed Docker APIs)

Additionally, some cryptocurrency mining malware identify then kill off processes for competing malware to ensure it’s not competing for resources.(Citation: Trend Micro War of Crypto Miners)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1496/001)
- [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)
- [Kaspersky Lazarus Under The Hood Blog 2017](https://securelist.com/lazarus-under-the-hood/77908/)
- [Trend Micro Exposed Docker APIs](https://www.trendmicro.com/en_us/research/19/e/infected-cryptocurrency-mining-containers-target-docker-hosts-with-exposed-apis-use-shodan-to-find-additional-victims.html)
- [Trend Micro War of Crypto Miners](https://www.trendmicro.com/en_us/research/20/i/war-of-linux-cryptocurrency-miners-a-battle-for-resources.html)
