---
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--be055942-6e63-49d7-9fa1-9cb7d8a8f3f4
mitre_attack_url: https://attack.mitre.org/techniques/T1102/002
name: Bidirectional Communication
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Bidirectional Communication
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Flow |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1102/002](https://attack.mitre.org/techniques/T1102/002) |

# Bidirectional Communication (attack-pattern--be055942-6e63-49d7-9fa1-9cb7d8a8f3f4)

## Description
Adversaries may use an existing, legitimate external Web service as a means for sending commands to and receiving output from a compromised system over the Web service channel. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those infected systems can then send the output from those commands back over that Web service channel. The return traffic may occur in a variety of ways, depending on the Web service being utilized. For example, the return traffic may take the form of the compromised system posting a comment on a forum, issuing a pull request to development project, updating a document hosted on a Web service, or by sending a Tweet. 

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection. 

## Detection
Host data that can relate unknown or suspicious process activity using a network connection is important to supplement any existing indicators of compromise based on malware command and control signatures and infrastructure or the presence of strong encryption. Packet capture analysis will require SSL/TLS inspection if data is encrypted. Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). User behavior monitoring may help to detect abnormal patterns of activity.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1102/002)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
