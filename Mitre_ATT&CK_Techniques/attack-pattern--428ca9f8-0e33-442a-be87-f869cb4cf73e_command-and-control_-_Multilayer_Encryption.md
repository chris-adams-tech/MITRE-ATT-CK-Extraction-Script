---
id: attack-pattern--428ca9f8-0e33-442a-be87-f869cb4cf73e
mitre_attack_url: https://attack.mitre.org/techniques/T1079
name: Multilayer Encryption
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Multilayer Encryption
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1079](https://attack.mitre.org/techniques/T1079) |

# Multilayer Encryption (attack-pattern--428ca9f8-0e33-442a-be87-f869cb4cf73e)

## Description
An adversary performs C2 communications using multiple layers of encryption, typically (but not exclusively) tunneling a custom encryption scheme within a protocol encryption scheme such as HTTPS or SMTPS.

## Detection
If malware uses [Standard Cryptographic Protocol](https://attack.mitre.org/techniques/T1032), SSL/TLS inspection can be used to detect command and control traffic within some encrypted communication channels. (Citation: SANS Decrypting SSL) SSL/TLS inspection does come with certain risks that should be considered before implementing to avoid potential security issues such as incomplete certificate validation. (Citation: SEI SSL Inspection Risks) After SSL/TLS inspection, additional cryptographic analysis may be needed to analyze the second layer of encryption.

With [Custom Cryptographic Protocol](https://attack.mitre.org/techniques/T1024), if malware uses encryption with symmetric keys, it may be possible to obtain the algorithm and key from samples and use them to decode network traffic to detect malware communications signatures. (Citation: Fidelis DarkComet)

In general, analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1079)
- [SANS Decrypting SSL](http://www.sans.org/reading-room/whitepapers/analyst/finding-hidden-threats-decrypting-ssl-34840)
- [SEI SSL Inspection Risks](https://insights.sei.cmu.edu/cert/2015/03/the-risks-of-ssl-inspection.html)
- [Fidelis DarkComet](https://www.fidelissecurity.com/sites/default/files/FTA_1018_looking_at_the_sky_for_a_dark_comet.pdf)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
