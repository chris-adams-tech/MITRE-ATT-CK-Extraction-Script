---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--4ffc1794-ec3b-45be-9e52-42dbcb2af2de
mitre_attack_url: https://attack.mitre.org/techniques/T1599/001
name: Network Address Translation Traversal
platforms:
- Network
tactics:
- defense-evasion
title: defense-evasion - Network Address Translation Traversal
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Network |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1599/001](https://attack.mitre.org/techniques/T1599/001) |

# Network Address Translation Traversal (attack-pattern--4ffc1794-ec3b-45be-9e52-42dbcb2af2de)

## Description
Adversaries may bridge network boundaries by modifying a network device’s Network Address Translation (NAT) configuration. Malicious modifications to NAT may enable an adversary to bypass restrictions on traffic routing that otherwise separate trusted and untrusted networks.

Network devices such as routers and firewalls that connect multiple networks together may implement NAT during the process of passing packets between networks. When performing NAT, the network device will rewrite the source and/or destination addresses of the IP address header. Some network designs require NAT for the packets to cross the border device.  A typical example of this is environments where internal networks make use of non-Internet routable addresses.(Citation: RFC1918)

When an adversary gains control of a network boundary device, they can either leverage existing NAT configurations to send traffic between two separated networks, or they can implement NAT configurations of their own design.  In the case of network designs that require NAT to function, this enables the adversary to overcome inherent routing limitations that would normally prevent them from accessing protected systems behind the border device.  In the case of network designs that do not require NAT, address translation can be used by adversaries to obscure their activities, as changing the addresses of packets that traverse a network boundary device can make monitoring data transmissions more challenging for defenders.  

Adversaries may use [Patch System Image](https://attack.mitre.org/techniques/T1601/001) to change the operating system of a network device, implementing their own custom NAT mechanisms to further obscure their activities

## Detection
Consider monitoring network traffic on both interfaces of border network devices.  Compare packets transmitted by the device between networks to look for signs of NAT being implemented.  Packets which have their IP addresses changed should still have the same size and contents in the data encapsulated beyond Layer 3.  In some cases, Port Address Translation (PAT) may also be used by an adversary.

Monitor the border network device’s configuration to determine if any unintended NAT rules have been added without authorization.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1599/001)
- [RFC1918](https://tools.ietf.org/html/rfc1918)
