---
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--8868cb5b-d575-4a60-acb2-07d37389a2fd
mitre_attack_url: https://attack.mitre.org/techniques/T1205/001
name: Port Knocking
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- defense-evasion
- persistence
- command-and-control
title: defense-evasion - Port Knocking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence, command-and-control |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Flow |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1205/001](https://attack.mitre.org/techniques/T1205/001) |

# Port Knocking (attack-pattern--8868cb5b-d575-4a60-acb2-07d37389a2fd)

## Description
Adversaries may use port knocking to hide open ports used for persistence or command and control. To enable a port, an adversary sends a series of attempted connections to a predefined sequence of closed ports. After the sequence is completed, opening a port is often accomplished by the host based firewall, but could also be implemented by custom software.

This technique has been observed both for the dynamic opening of a listening port as well as the initiating of a connection to a listening server on a different system.

The observation of the signal packets to trigger the communication can be conducted through different methods. One means, originally implemented by Cd00r (Citation: Hartrell cd00r 2002), is to use the libpcap libraries to sniff for the packets in question. Another method leverages raw sockets, which enables the malware to use ports that are already open for use by other programs.

## Detection
Record network packets sent to and from the system, looking for extraneous packets that do not belong to established flows.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1205/001)
- [Hartrell cd00r 2002](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)
