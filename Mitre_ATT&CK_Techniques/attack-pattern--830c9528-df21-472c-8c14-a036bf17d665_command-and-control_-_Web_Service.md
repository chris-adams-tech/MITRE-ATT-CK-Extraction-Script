---
contributors:
- Anastasios Pingios
- Sarathkumar Rajendran, Microsoft Defender365
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--830c9528-df21-472c-8c14-a036bf17d665
mitre_attack_url: https://attack.mitre.org/techniques/T1102
name: Web Service
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Web Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1102](https://attack.mitre.org/techniques/T1102) |

# Web Service (attack-pattern--830c9528-df21-472c-8c14-a036bf17d665)

## Description
Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites, cloud services, and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google, Microsoft, or Twitter, makes it easier for adversaries to hide in expected noise.(Citation: Broadcom BirdyClient Microsoft Graph API 2024) Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

## Detection
Host data that can relate unknown or suspicious process activity using a network connection is important to supplement any existing indicators of compromise based on malware command and control signatures and infrastructure or the presence of strong encryption. Packet capture analysis will require SSL/TLS inspection if data is encrypted. Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). User behavior monitoring may help to detect abnormal patterns of activity.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1102)
- [Broadcom BirdyClient Microsoft Graph API 2024](https://www.broadcom.com/support/security-center/protection-bulletin/birdyclient-malware-leverages-microsoft-graph-api-for-c-c-communication)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
