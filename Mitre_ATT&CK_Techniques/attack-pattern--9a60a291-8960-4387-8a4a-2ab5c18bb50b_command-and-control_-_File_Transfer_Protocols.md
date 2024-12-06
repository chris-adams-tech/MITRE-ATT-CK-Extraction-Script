---
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--9a60a291-8960-4387-8a4a-2ab5c18bb50b
mitre_attack_url: https://attack.mitre.org/techniques/T1071/002
name: File Transfer Protocols
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- command-and-control
title: command-and-control - File Transfer Protocols
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1071/002](https://attack.mitre.org/techniques/T1071/002) |

# File Transfer Protocols (attack-pattern--9a60a291-8960-4387-8a4a-2ab5c18bb50b)

## Description
Adversaries may communicate using application layer protocols associated with transferring files to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Protocols such as SMB(Citation: US-CERT TA18-074A), FTP(Citation: ESET Machete July 2019), FTPS, and TFTP that transfer files may be very common in environments.  Packets produced from these protocols may have many fields and headers in which data can be concealed. Data could also be concealed within the transferred files. An adversary may abuse these protocols to communicate with systems under their control within a victim network while also mimicking normal, expected traffic. 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect application layer protocols that do not follow the expected protocol for the port that is being used.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1071/002)
- [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
- [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)
