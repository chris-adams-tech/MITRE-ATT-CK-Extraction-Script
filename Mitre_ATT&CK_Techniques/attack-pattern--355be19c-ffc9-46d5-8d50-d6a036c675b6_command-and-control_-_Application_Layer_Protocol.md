---
contributors:
- Duane Michael
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--355be19c-ffc9-46d5-8d50-d6a036c675b6
mitre_attack_url: https://attack.mitre.org/techniques/T1071
name: Application Layer Protocol
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- command-and-control
title: command-and-control - Application Layer Protocol
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1071](https://attack.mitre.org/techniques/T1071) |

# Application Layer Protocol (attack-pattern--355be19c-ffc9-46d5-8d50-d6a036c675b6)

## Description
Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are SMB, SSH, or RDP.(Citation: Mandiant APT29 Eye Spy Email Nov 22) 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect application layer protocols that do not follow the expected protocol standards regarding syntax, structure, or any other variable adversaries could leverage to conceal data.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1071)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
- [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
