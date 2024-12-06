---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
- 'Command: Command Execution'
- 'File: File Access'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--79a4052e-1a89-4b09-aea6-51f1d11fe19c
mitre_attack_url: https://attack.mitre.org/techniques/T1048/001
name: Exfiltration Over Symmetric Encrypted Non-C2 Protocol
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Exfiltration Over Symmetric Encrypted Non-C2 Protocol
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content, Command: Command Execution, File: File Access, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1048/001](https://attack.mitre.org/techniques/T1048/001) |

# Exfiltration Over Symmetric Encrypted Non-C2 Protocol (attack-pattern--79a4052e-1a89-4b09-aea6-51f1d11fe19c)

## Description
Adversaries may steal data by exfiltrating it over a symmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Symmetric encryption algorithms are those that use shared or the same keys/secrets on each end of the channel. This requires an exchange or pre-arranged agreement/possession of the value used to encrypt and decrypt data. 

Network protocols that use asymmetric encryption often utilize symmetric encryption once keys are exchanged, but adversaries may opt to manually share keys and implement symmetric cryptographic algorithms (ex: RC4, AES) vice using mechanisms that are baked into a protocol. This may result in multiple layers of encryption (in protocols that are natively encrypted such as HTTPS) or encryption in protocols that not typically encrypted (such as HTTP or FTP). 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious.(Citation: University of Birmingham C2) 

Artifacts and evidence of symmetric key exchange may be recoverable by analyzing network traffic or looking for hard-coded values within malware. If recovered, these keys can be used to decrypt network data from command and control channels. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1048/001)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
