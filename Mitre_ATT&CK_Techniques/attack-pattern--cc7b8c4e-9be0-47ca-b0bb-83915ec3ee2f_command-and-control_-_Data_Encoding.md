---
contributors:
- Itzik Kotler, SafeBreach
data_sources:
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--cc7b8c4e-9be0-47ca-b0bb-83915ec3ee2f
mitre_attack_url: https://attack.mitre.org/techniques/T1132
name: Data Encoding
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Data Encoding
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1132](https://attack.mitre.org/techniques/T1132) |

# Data Encoding (attack-pattern--cc7b8c4e-9be0-47ca-b0bb-83915ec3ee2f)

## Description
Adversaries may encode data to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system. Use of data encoding may adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64, MIME, or other binary-to-text and character encoding systems.(Citation: Wikipedia Binary-to-text Encoding) (Citation: Wikipedia Character Encoding) Some data encoding systems may also result in data compression, such as gzip.

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1132)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
- [Wikipedia Binary-to-text Encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding)
- [Wikipedia Character Encoding](https://en.wikipedia.org/wiki/Character_encoding)
