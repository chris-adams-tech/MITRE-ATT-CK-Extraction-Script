---
contributors:
- Ryan Becwar
- Duane Michael
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--c21d5a77-d422-4a69-acd7-2c53c1faa34b
mitre_attack_url: https://attack.mitre.org/techniques/T1095
name: Non-Application Layer Protocol
platforms:
- Windows
- Linux
- macOS
- Network
tactics:
- command-and-control
title: command-and-control - Non-Application Layer Protocol
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Windows, Linux, macOS, Network |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1095](https://attack.mitre.org/techniques/T1095) |

# Non-Application Layer Protocol (attack-pattern--c21d5a77-d422-4a69-acd7-2c53c1faa34b)

## Description
Adversaries may use an OSI non-application layer protocol for communication between host and C2 server or among infected hosts within a network. The list of possible protocols is extensive.(Citation: Wikipedia OSI) Specific examples include use of network layer protocols, such as the Internet Control Message Protocol (ICMP), transport layer protocols, such as the User Datagram Protocol (UDP), session layer protocols, such as Socket Secure (SOCKS), as well as redirected/tunneled protocols, such as Serial over LAN (SOL).

ICMP communication between hosts is one example.(Citation: Cisco Synful Knock Evolution) Because ICMP is part of the Internet Protocol Suite, it is required to be implemented by all IP-compatible hosts.(Citation: Microsoft ICMP) However, it is not as commonly monitored as other Internet Protocols such as TCP or UDP and may be used by adversaries to hide communications.

## Detection
Analyze network traffic for ICMP messages or other protocols that contain abnormal data or are not normally seen within or exiting the network.(Citation: Cisco Blog Legacy Device Attacks)

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used.(Citation: University of Birmingham C2) 

Monitor and investigate API calls to functions associated with enabling and/or utilizing alternative communication channels.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1095)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
- [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
- [Microsoft ICMP](http://support.microsoft.com/KB/170292)
- [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
- [Wikipedia OSI](http://en.wikipedia.org/wiki/List_of_network_protocols_%28OSI_model%29)
