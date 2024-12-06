---
data_sources:
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--04fd5427-79c7-44ea-ae13-11b24778ff1c
mitre_attack_url: https://attack.mitre.org/techniques/T1132/001
name: Standard Encoding
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Standard Encoding
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1132/001](https://attack.mitre.org/techniques/T1132/001) |

# Standard Encoding (attack-pattern--04fd5427-79c7-44ea-ae13-11b24778ff1c)

## Description
Adversaries may encode data with a standard data encoding system to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system that adheres to existing protocol specifications. Common data encoding schemes include ASCII, Unicode, hexadecimal, Base64, and MIME.(Citation: Wikipedia Binary-to-text Encoding)(Citation: Wikipedia Character Encoding) Some data encoding systems may also result in data compression, such as gzip.

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1132/001)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
- [Wikipedia Binary-to-text Encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding)
- [Wikipedia Character Encoding](https://en.wikipedia.org/wiki/Character_encoding)
