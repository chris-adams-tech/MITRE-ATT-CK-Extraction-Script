---
data_sources:
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--eec23884-3fa1-4d8a-ac50-6f104d51e235
mitre_attack_url: https://attack.mitre.org/techniques/T1001/002
name: Steganography
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Steganography
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1001/002](https://attack.mitre.org/techniques/T1001/002) |

# Steganography (attack-pattern--eec23884-3fa1-4d8a-ac50-6f104d51e235)

## Description
Adversaries may use steganographic techniques to hide command and control traffic to make detection efforts more difficult. Steganographic techniques can be used to hide data in digital messages that are transferred between systems. This hidden information can be used for command and control of compromised systems. In some cases, the passing of files embedded using steganography, such as image or document files, can be used for command and control. 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1001/002)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
