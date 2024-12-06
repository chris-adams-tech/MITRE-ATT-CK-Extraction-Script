---
contributors:
- James Emery-Callcott, Emerging Threats Team, Proofpoint
data_sources:
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--c325b232-d5bc-4dde-a3ec-71f3db9e8adc
mitre_attack_url: https://attack.mitre.org/techniques/T1001/003
name: Protocol or Service Impersonation
platforms:
- Linux
- Windows
- macOS
tactics:
- command-and-control
title: command-and-control - Protocol or Service Impersonation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1001/003](https://attack.mitre.org/techniques/T1001/003) |

# Protocol or Service Impersonation (attack-pattern--c325b232-d5bc-4dde-a3ec-71f3db9e8adc)

## Description
Adversaries may impersonate legitimate protocols or web service traffic to disguise command and control activity and thwart analysis efforts. By impersonating legitimate protocols or web services, adversaries can make their command and control traffic blend in with legitimate network traffic.  

Adversaries may impersonate a fake SSL/TLS handshake to make it look like subsequent traffic is SSL/TLS encrypted, potentially interfering with some security tooling, or to make the traffic look like it is related with a trusted entity. 

Adversaries may also leverage legitimate protocols to impersonate expected web traffic or trusted services. For example, adversaries may manipulate HTTP headers, URI endpoints, SSL certificates, and transmitted data to disguise C2 communications or mimic legitimate services such as Gmail, Google Drive, and Yahoo Messenger.(Citation: ESET Okrum July 2019)(Citation: Malleable-C2-U42)

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1001/003)
- [Malleable-C2-U42](https://unit42.paloaltonetworks.com/cobalt-strike-malleable-c2-profile/)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
- [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
