---
contributors:
- Domenico Mazzaferro Palmeri
- Sofia Sanchez Margolles
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--241f9ea8-f6ae-4f38-92f5-cef5b7e539dd
mitre_attack_url: https://attack.mitre.org/techniques/T1071/005
name: Publish/Subscribe Protocols
platforms:
- macOS
- Linux
- Windows
- Network
tactics:
- command-and-control
title: command-and-control - Publish/Subscribe Protocols
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | macOS, Linux, Windows, Network |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1071/005](https://attack.mitre.org/techniques/T1071/005) |

# Publish/Subscribe Protocols (attack-pattern--241f9ea8-f6ae-4f38-92f5-cef5b7e539dd)

## Description
Adversaries may communicate using publish/subscribe (pub/sub) application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Protocols such as <code>MQTT</code>, <code>XMPP</code>, <code>AMQP</code>, and <code>STOMP</code> use a publish/subscribe design, with message distribution managed by a centralized broker.(Citation: wailing crab sub/pub)(Citation: Mandiant APT1 Appendix) Publishers categorize their messages by topics, while subscribers receive messages according to their subscribed topics.(Citation: wailing crab sub/pub) An adversary may abuse publish/subscribe protocols to communicate with systems under their control from behind a message broker while also mimicking normal, expected traffic.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1071/005)
- [wailing crab sub/pub](https://securityintelligence.com/x-force/wailingcrab-malware-misues-mqtt-messaging-protocol/)
- [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
