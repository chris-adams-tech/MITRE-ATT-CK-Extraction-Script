---
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Flow'
- 'File: File Access'
- 'Command: Command Execution'
id: attack-pattern--bf1b6176-597c-4600-bfcd-ac989670f96b
mitre_attack_url: https://attack.mitre.org/techniques/T1567/002
name: Exfiltration to Cloud Storage
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Exfiltration to Cloud Storage
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Flow, File: File Access, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1567/002](https://attack.mitre.org/techniques/T1567/002) |

# Exfiltration to Cloud Storage (attack-pattern--bf1b6176-597c-4600-bfcd-ac989670f96b)

## Description
Adversaries may exfiltrate data to a cloud storage service rather than over their primary command and control channel. Cloud storage services allow for the storage, edit, and retrieval of data from a remote cloud storage server over the Internet.

Examples of cloud storage services include Dropbox and Google Docs. Exfiltration to these cloud storage services can provide a significant amount of cover to the adversary if hosts within the network are already communicating with the service. 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server) to known cloud storage services. Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. User behavior monitoring may help to detect abnormal patterns of activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1567/002)
