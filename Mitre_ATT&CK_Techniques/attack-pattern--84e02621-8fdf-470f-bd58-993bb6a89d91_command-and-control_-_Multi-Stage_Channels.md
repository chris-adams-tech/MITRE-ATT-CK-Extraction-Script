---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--84e02621-8fdf-470f-bd58-993bb6a89d91
mitre_attack_url: https://attack.mitre.org/techniques/T1104
name: Multi-Stage Channels
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Multi-Stage Channels
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1104](https://attack.mitre.org/techniques/T1104) |

# Multi-Stage Channels (attack-pattern--84e02621-8fdf-470f-bd58-993bb6a89d91)

## Description
Adversaries may create multiple stages for command and control that are employed under different conditions or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.

Remote access tools will call back to the first-stage command and control server for instructions. The first stage may have automated capabilities to collect basic host information, update tools, and upload additional files. A second remote access tool (RAT) could be uploaded at that point to redirect the host to the second-stage command and control server. The second stage will likely be more fully featured and allow the adversary to interact with the system through a reverse shell and additional RAT features.

The different stages will likely be hosted separately with no overlapping infrastructure. The loader may also have backup first-stage callbacks or [Fallback Channels](https://attack.mitre.org/techniques/T1008) in case the original first-stage communication path is discovered and blocked.

## Detection
Host data that can relate unknown or suspicious process activity using a network connection is important to supplement any existing indicators of compromise based on malware command and control signatures and infrastructure. Relating subsequent actions that may result from Discovery of the system and network information or Lateral Movement to the originating process may also yield useful data.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1104)
