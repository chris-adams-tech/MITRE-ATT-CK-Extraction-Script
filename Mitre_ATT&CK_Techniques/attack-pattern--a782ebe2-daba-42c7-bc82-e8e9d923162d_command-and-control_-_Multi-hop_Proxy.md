---
contributors:
- Eduardo Chavarro Ovalle
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--a782ebe2-daba-42c7-bc82-e8e9d923162d
mitre_attack_url: https://attack.mitre.org/techniques/T1090/003
name: Multi-hop Proxy
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- command-and-control
title: command-and-control - Multi-hop Proxy
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1090/003](https://attack.mitre.org/techniques/T1090/003) |

# Multi-hop Proxy (attack-pattern--a782ebe2-daba-42c7-bc82-e8e9d923162d)

## Description
Adversaries may chain together multiple proxies to disguise the source of malicious traffic. Typically, a defender will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not be able to identify any previous proxies before the last-hop proxy. This technique makes identifying the original source of the malicious traffic even more difficult by requiring the defender to trace malicious traffic through several proxies to identify its source.

For example, adversaries may construct or use onion routing networks – such as the publicly available [Tor](https://attack.mitre.org/software/S0183) network – to transport encrypted C2 traffic through a compromised population, allowing communication with any device within the network.(Citation: Onion Routing) Adversaries may also use operational relay box (ORB) networks composed of virtual private servers (VPS), Internet of Things (IoT) devices, smart devices, and end-of-life routers to obfuscate their operations. (Citation: ORB Mandiant) 

In the case of network infrastructure, it is possible for an adversary to leverage multiple compromised devices to create a multi-hop proxy chain (i.e., [Network Devices](https://attack.mitre.org/techniques/T1584/008)). By leveraging [Patch System Image](https://attack.mitre.org/techniques/T1601/001) on routers, adversaries can add custom code to the affected network devices that will implement onion routing between those nodes. This method is dependent upon the [Network Boundary Bridging](https://attack.mitre.org/techniques/T1599) method allowing the adversaries to cross the protected network boundary of the Internet perimeter and into the organization’s Wide-Area Network (WAN).  Protocols such as ICMP may be used as a transport.  

Similarly, adversaries may abuse peer-to-peer (P2P) and blockchain-oriented infrastructure to implement routing between a decentralized network of peers.(Citation: NGLite Trojan)

## Detection
When observing use of Multi-hop proxies, network data from the actual command and control servers could allow correlating incoming and outgoing flows to trace malicious traffic back to its source. Multi-hop proxies can also be detected by alerting on traffic to known anonymity networks (such as [Tor](https://attack.mitre.org/software/S0183)) or known adversary infrastructure that uses this technique.

In context of network devices, monitor traffic for encrypted communications from the Internet that is addressed to border routers.  Compare this traffic with the configuration to determine whether it matches with any configured site-to-site Virtual Private Network (VPN) connections the device was intended to have. Monitor traffic for encrypted communications originating from potentially breached routers that is addressed to other routers within the organization.  Compare the source and destination with the configuration of the device to determine if these channels are an authorized Virtual Private Network (VPN) connections or other encrypted modes of communication. Monitor ICMP traffic from the Internet that is addressed to border routers and is encrypted.  Few if any legitimate use cases exist for sending encrypted data to a network device via ICMP.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1090/003)
- [ORB Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-orb-networks)
- [NGLite Trojan](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/)
- [Onion Routing](https://en.wikipedia.org/wiki/Onion_routing)
