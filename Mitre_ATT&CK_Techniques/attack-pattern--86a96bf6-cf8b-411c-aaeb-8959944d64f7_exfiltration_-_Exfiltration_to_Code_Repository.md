---
data_sources:
- 'Command: Command Execution'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
- 'File: File Access'
id: attack-pattern--86a96bf6-cf8b-411c-aaeb-8959944d64f7
mitre_attack_url: https://attack.mitre.org/techniques/T1567/001
name: Exfiltration to Code Repository
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Exfiltration to Code Repository
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Command: Command Execution, Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow, File: File Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1567/001](https://attack.mitre.org/techniques/T1567/001) |

# Exfiltration to Code Repository (attack-pattern--86a96bf6-cf8b-411c-aaeb-8959944d64f7)

## Description
Adversaries may exfiltrate data to a code repository rather than over their primary command and control channel. Code repositories are often accessible via an API (ex: https://api.github.com). Access to these APIs are often over HTTPS, which gives the adversary an additional level of protection.

Exfiltration to a code repository can also provide a significant amount of cover to the adversary if it is a popular service already used by hosts within the network. 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server) to code repositories. Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. User behavior monitoring may help to detect abnormal patterns of activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1567/001)
