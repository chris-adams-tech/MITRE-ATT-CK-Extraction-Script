---
contributors:
- Ryan Becwar
id: attack-pattern--f72eb8a8-cd4c-461d-a814-3f862befbf00
mitre_attack_url: https://attack.mitre.org/techniques/T1094
name: Custom Command and Control Protocol
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Custom Command and Control Protocol
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1094](https://attack.mitre.org/techniques/T1094) |

# Custom Command and Control Protocol (attack-pattern--f72eb8a8-cd4c-461d-a814-3f862befbf00)

## Description
Adversaries may communicate using a custom command and control protocol instead of encapsulating commands/data in an existing [Application Layer Protocol](https://attack.mitre.org/techniques/T1071). Implementations include mimicking well-known protocols or developing custom protocols (including raw sockets) on top of fundamental protocols provided by TCP/IP/another standard network stack.

## Detection
Analyze network traffic for ICMP messages or other protocols that contain abnormal data or are not normally seen within or exiting the network.

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2)

Monitor and investigate API calls to functions associated with enabling and/or utilizing alternative communication channels.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1094)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
