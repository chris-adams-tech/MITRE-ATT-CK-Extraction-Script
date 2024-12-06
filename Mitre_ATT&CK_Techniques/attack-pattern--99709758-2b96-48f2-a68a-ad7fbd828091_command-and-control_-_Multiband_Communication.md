---
id: attack-pattern--99709758-2b96-48f2-a68a-ad7fbd828091
mitre_attack_url: https://attack.mitre.org/techniques/T1026
name: Multiband Communication
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Multiband Communication
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1026](https://attack.mitre.org/techniques/T1026) |

# Multiband Communication (attack-pattern--99709758-2b96-48f2-a68a-ad7fbd828091)

## Description
**This technique has been deprecated and should no longer be used.**

Some adversaries may split communications between different protocols. There could be one protocol for inbound command and control and another for outbound data, allowing it to bypass certain firewall restrictions. The split could also be random to simply avoid data threshold alerts on any one communication.

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2) Correlating alerts between multiple communication channels can further help identify command-and-control behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1026)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
