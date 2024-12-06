---
contributors:
- Chris Roffe
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--7bd9c723-2f78-4309-82c5-47cad406572b
mitre_attack_url: https://attack.mitre.org/techniques/T1568
name: Dynamic Resolution
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Dynamic Resolution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1568](https://attack.mitre.org/techniques/T1568) |

# Dynamic Resolution (attack-pattern--7bd9c723-2f78-4309-82c5-47cad406572b)

## Description
Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. These calculations can be used to dynamically adjust parameters such as the domain name, IP address, or port number the malware uses for command and control.

Adversaries may use dynamic resolution for the purpose of [Fallback Channels](https://attack.mitre.org/techniques/T1008). When contact is lost with the primary command and control server malware may employ dynamic resolution as a means to reestablishing command and control.(Citation: Talos CCleanup 2017)(Citation: FireEye POSHSPY April 2017)(Citation: ESET Sednit 2017 Activity)

## Detection
Detecting dynamically generated C2 can be challenging due to the number of different algorithms, constantly evolving malware families, and the increasing complexity of the algorithms. There are multiple approaches to detecting a pseudo-randomly generated domain name, including using frequency analysis, Markov chains, entropy, proportion of dictionary words, ratio of vowels to other characters, and more (Citation: Data Driven Security DGA). CDN domains may trigger these detections due to the format of their domain names. In addition to detecting algorithm generated domains based on the name, another more general approach for detecting a suspicious domain is to check for recently registered names or for rarely visited domains.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1568)
- [Talos CCleanup 2017](http://blog.talosintelligence.com/2017/09/avast-distributes-malware.html)
- [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
- [ESET Sednit 2017 Activity](https://www.welivesecurity.com/2017/12/21/sednit-update-fancy-bear-spent-year/)
- [Data Driven Security DGA](https://datadrivensecurity.info/blog/posts/2014/Oct/dga-part2/)
