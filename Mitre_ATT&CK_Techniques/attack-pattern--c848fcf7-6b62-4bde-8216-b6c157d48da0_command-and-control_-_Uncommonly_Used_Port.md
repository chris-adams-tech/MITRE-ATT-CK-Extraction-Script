---
id: attack-pattern--c848fcf7-6b62-4bde-8216-b6c157d48da0
mitre_attack_url: https://attack.mitre.org/techniques/T1065
name: Uncommonly Used Port
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Uncommonly Used Port
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1065](https://attack.mitre.org/techniques/T1065) |

# Uncommonly Used Port (attack-pattern--c848fcf7-6b62-4bde-8216-b6c157d48da0)

## Description
Adversaries may conduct C2 communications over a non-standard port to bypass proxies and firewalls that have been improperly configured.

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1065)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
