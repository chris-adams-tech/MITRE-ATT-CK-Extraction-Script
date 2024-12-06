---
data_sources:
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--24bfaeba-cb0d-4525-b3dc-507c77ecec41
mitre_attack_url: https://attack.mitre.org/techniques/T1573/001
name: Symmetric Cryptography
platforms:
- Linux
- Windows
- macOS
- Network
tactics:
- command-and-control
title: command-and-control - Symmetric Cryptography
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, Windows, macOS, Network |
| **Data Sources** | Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1573/001](https://attack.mitre.org/techniques/T1573/001) |

# Symmetric Cryptography (attack-pattern--24bfaeba-cb0d-4525-b3dc-507c77ecec41)

## Description
Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Symmetric encryption algorithms use the same key for plaintext encryption and ciphertext decryption. Common symmetric encryption algorithms include AES, DES, 3DES, Blowfish, and RC4.

## Detection
With symmetric encryption, it may be possible to obtain the algorithm and key from samples and use them to decode network traffic to detect malware communications signatures.

In general, analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1573/001)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
