---
id: attack-pattern--4b74a1d4-b0e9-4ef1-93f1-14ecc6e2f5b5
mitre_attack_url: https://attack.mitre.org/techniques/T1032
name: Standard Cryptographic Protocol
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Standard Cryptographic Protocol
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1032](https://attack.mitre.org/techniques/T1032) |

# Standard Cryptographic Protocol (attack-pattern--4b74a1d4-b0e9-4ef1-93f1-14ecc6e2f5b5)

## Description
Adversaries may explicitly employ a known encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if necessary secret keys are encoded and/or generated within malware samples/configuration files.

## Detection
SSL/TLS inspection is one way of detecting command and control traffic within some encrypted communication channels. (Citation: SANS Decrypting SSL) SSL/TLS inspection does come with certain risks that should be considered before implementing to avoid potential security issues such as incomplete certificate validation. (Citation: SEI SSL Inspection Risks)

If malware uses encryption with symmetric keys, it may be possible to obtain the algorithm and key from samples and use them to decode network traffic to detect malware communications signatures. (Citation: Fidelis DarkComet)

In general, analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1032)
- [SANS Decrypting SSL](http://www.sans.org/reading-room/whitepapers/analyst/finding-hidden-threats-decrypting-ssl-34840)
- [SEI SSL Inspection Risks](https://insights.sei.cmu.edu/cert/2015/03/the-risks-of-ssl-inspection.html)
- [Fidelis DarkComet](https://www.fidelissecurity.com/sites/default/files/FTA_1018_looking_at_the_sky_for_a_dark_comet.pdf)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
