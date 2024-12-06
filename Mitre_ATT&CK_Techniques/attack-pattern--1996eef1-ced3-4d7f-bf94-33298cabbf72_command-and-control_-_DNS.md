---
contributors:
- Jan Petrov, Citi
- Chris Heald
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--1996eef1-ced3-4d7f-bf94-33298cabbf72
mitre_attack_url: https://attack.mitre.org/techniques/T1071/004
name: DNS
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- command-and-control
title: command-and-control - DNS
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1071/004](https://attack.mitre.org/techniques/T1071/004) |

# DNS (attack-pattern--1996eef1-ced3-4d7f-bf94-33298cabbf72)

## Description
Adversaries may communicate using the Domain Name System (DNS) application layer protocol to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

The DNS protocol serves an administrative function in computer networking and thus may be very common in environments. DNS traffic may also be allowed even before network authentication is completed. DNS packets contain many fields and headers in which data can be concealed. Often known as DNS tunneling, adversaries may abuse DNS to communicate with systems under their control within a victim network while also mimicking normal, expected traffic.(Citation: PAN DNS Tunneling)(Citation: Medium DnsTunneling) 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect application layer protocols that do not follow the expected protocol standards regarding syntax, structure, or any other variable adversaries could leverage to conceal data.(Citation: University of Birmingham C2)

Monitor for DNS traffic to/from known-bad or suspicious domains.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1071/004)
- [Medium DnsTunneling](https://medium.com/@galolbardes/learn-how-easy-is-to-bypass-firewalls-using-dns-tunneling-and-also-how-to-block-it-3ed652f4a000)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
- [PAN DNS Tunneling](https://www.paloaltonetworks.com/cyberpedia/what-is-dns-tunneling)
