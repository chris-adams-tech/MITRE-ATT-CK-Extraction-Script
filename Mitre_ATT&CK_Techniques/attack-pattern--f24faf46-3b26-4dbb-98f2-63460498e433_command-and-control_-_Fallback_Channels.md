---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--f24faf46-3b26-4dbb-98f2-63460498e433
mitre_attack_url: https://attack.mitre.org/techniques/T1008
name: Fallback Channels
platforms:
- Linux
- Windows
- macOS
tactics:
- command-and-control
title: command-and-control - Fallback Channels
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1008](https://attack.mitre.org/techniques/T1008) |

# Fallback Channels (attack-pattern--f24faf46-3b26-4dbb-98f2-63460498e433)

## Description
Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inaccessible in order to maintain reliable command and control and to avoid data transfer thresholds.

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1008)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
