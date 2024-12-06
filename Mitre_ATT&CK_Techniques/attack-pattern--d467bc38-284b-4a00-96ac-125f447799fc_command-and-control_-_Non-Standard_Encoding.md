---
data_sources:
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--d467bc38-284b-4a00-96ac-125f447799fc
mitre_attack_url: https://attack.mitre.org/techniques/T1132/002
name: Non-Standard Encoding
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Non-Standard Encoding
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1132/002](https://attack.mitre.org/techniques/T1132/002) |

# Non-Standard Encoding (attack-pattern--d467bc38-284b-4a00-96ac-125f447799fc)

## Description
Adversaries may encode data with a non-standard data encoding system to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a non-standard data encoding system that diverges from existing protocol specifications. Non-standard data encoding schemes may be based on or related to standard data encoding schemes, such as a modified Base64 encoding for the message body of an HTTP request.(Citation: Wikipedia Binary-to-text Encoding) (Citation: Wikipedia Character Encoding) 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1132/002)
- [Wikipedia Binary-to-text Encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding)
- [Wikipedia Character Encoding](https://en.wikipedia.org/wiki/Character_encoding)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
