---
contributors:
- William Cain
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Command: Command Execution'
- 'File: File Access'
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--8e350c1d-ac79-4b5c-bd4e-7476d7e84ec5
mitre_attack_url: https://attack.mitre.org/techniques/T1048/002
name: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Command: Command Execution, File: File Access, Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1048/002](https://attack.mitre.org/techniques/T1048/002) |

# Exfiltration Over Asymmetric Encrypted Non-C2 Protocol (attack-pattern--8e350c1d-ac79-4b5c-bd4e-7476d7e84ec5)

## Description
Adversaries may steal data by exfiltrating it over an asymmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Asymmetric encryption algorithms are those that use different keys on each end of the channel. Also known as public-key cryptography, this requires pairs of cryptographic keys that can encrypt/decrypt data from the corresponding key. Each end of the communication channels requires a private key (only in the procession of that entity) and the public key of the other entity. The public keys of each entity are exchanged before encrypted communications begin. 

Network protocols that use asymmetric encryption (such as HTTPS/TLS/SSL) often utilize symmetric encryption once keys are exchanged. Adversaries may opt to use these encrypted mechanisms that are baked into a protocol. 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious.(Citation: University of Birmingham C2) 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1048/002)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
