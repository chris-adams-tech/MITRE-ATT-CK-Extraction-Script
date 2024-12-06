---
id: attack-pattern--b9f5dbe2-4c55-4fc5-af2e-d42c1d182ec4
mitre_attack_url: https://attack.mitre.org/techniques/T1002
name: Data Compressed
platforms:
- Linux
- Windows
- macOS
tactics:
- exfiltration
title: exfiltration - Data Compressed
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, Windows, macOS |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1002](https://attack.mitre.org/techniques/T1002) |

# Data Compressed (attack-pattern--b9f5dbe2-4c55-4fc5-af2e-d42c1d182ec4)

## Description
An adversary may compress data (e.g., sensitive documents) that is collected prior to exfiltration in order to make it portable and minimize the amount of data sent over the network. The compression is done separately from the exfiltration channel and is performed using a custom program or algorithm, or a more common compression library or utility such as 7zip, RAR, ZIP, or zlib.

## Detection
Compression software and compressed files can be detected in many ways. Common utilities that may be present on the system or brought in by an adversary may be detectable through process monitoring and monitoring for command-line arguments for known compression utilities. This may yield a significant amount of benign events, depending on how systems in the environment are typically used.

If the communications channel is unencrypted, compressed files can be detected in transit during exfiltration with a network intrusion detection or data loss prevention system analyzing file headers. (Citation: Wikipedia File Header Signatures)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1002)
- [Wikipedia File Header Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
