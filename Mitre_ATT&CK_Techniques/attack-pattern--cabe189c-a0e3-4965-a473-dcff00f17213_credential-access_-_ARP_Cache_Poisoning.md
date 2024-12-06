---
contributors:
- Jon Sternstein, Stern Security
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--cabe189c-a0e3-4965-a473-dcff00f17213
mitre_attack_url: https://attack.mitre.org/techniques/T1557/002
name: ARP Cache Poisoning
platforms:
- Linux
- Windows
- macOS
tactics:
- credential-access
- collection
title: credential-access - ARP Cache Poisoning
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, collection |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1557/002](https://attack.mitre.org/techniques/T1557/002) |

# ARP Cache Poisoning (attack-pattern--cabe189c-a0e3-4965-a473-dcff00f17213)

## Description
Adversaries may poison Address Resolution Protocol (ARP) caches to position themselves between the communication of two or more networked devices. This activity may be used to enable follow-on behaviors such as [Network Sniffing](https://attack.mitre.org/techniques/T1040) or [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002).

The ARP protocol is used to resolve IPv4 addresses to link layer addresses, such as a media access control (MAC) address.(Citation: RFC826 ARP) Devices in a local network segment communicate with each other by using link layer addresses. If a networked device does not have the link layer address of a particular networked device, it may send out a broadcast ARP request to the local network to translate the IP address to a MAC address. The device with the associated IP address directly replies with its MAC address. The networked device that made the ARP request will then use as well as store that information in its ARP cache.

An adversary may passively wait for an ARP request to poison the ARP cache of the requesting device. The adversary may reply with their MAC address, thus deceiving the victim by making them believe that they are communicating with the intended networked device. For the adversary to poison the ARP cache, their reply must be faster than the one made by the legitimate IP address owner. Adversaries may also send a gratuitous ARP reply that maliciously announces the ownership of a particular IP address to all the devices in the local network segment.

The ARP protocol is stateless and does not require authentication. Therefore, devices may wrongly add or update the MAC address of the IP address in their ARP cache.(Citation: Sans ARP Spoofing Aug 2003)(Citation: Cylance Cleaver)

Adversaries may use ARP cache poisoning as a means to intercept network traffic. This activity may be used to collect and/or relay data such as credentials, especially those sent over an insecure, unencrypted protocol.(Citation: Sans ARP Spoofing Aug 2003)


## Detection
Monitor network traffic for unusual ARP traffic, gratuitous ARP replies may be suspicious. 

Consider collecting changes to ARP caches across endpoints for signs of ARP poisoning. For example, if multiple IP addresses map to a single MAC address, this could be an indicator that the ARP cache has been poisoned.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1557/002)
- [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)
- [RFC826 ARP](https://tools.ietf.org/html/rfc826)
- [Sans ARP Spoofing Aug 2003](https://pen-testing.sans.org/resources/papers/gcih/real-world-arp-spoofing-105411)
