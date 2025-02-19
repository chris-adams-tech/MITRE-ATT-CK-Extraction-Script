---
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--69b8fd78-40e8-4600-ae4d-662c9d7afdb3
mitre_attack_url: https://attack.mitre.org/techniques/T1090/002
name: External Proxy
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- command-and-control
title: command-and-control - External Proxy
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1090/002](https://attack.mitre.org/techniques/T1090/002) |

# External Proxy (attack-pattern--69b8fd78-40e8-4600-ae4d-662c9d7afdb3)

## Description
Adversaries may use an external proxy to act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040), ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command and control communications, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths to avoid suspicion.

External connection proxies are used to mask the destination of C2 traffic and are typically implemented with port redirectors. Compromised systems outside of the victim environment may be used for these purposes, as well as purchased infrastructure such as cloud-based resources or virtual private servers. Proxies may be chosen based on the low likelihood that a connection to them from a compromised system would be investigated. Victim systems would communicate directly with the external proxy on the Internet and then the proxy would forward communications to the C2 server.

## Detection
Analyze network data for uncommon data flows, such as a client sending significantly more data than it receives from an external server. Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1090/002)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
- [Trend Micro APT Attack Tools](http://blog.trendmicro.com/trendlabs-security-intelligence/in-depth-look-apt-attack-tools-of-the-trade/)
