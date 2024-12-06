---
contributors:
- William Cain
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
- 'Command: Command Execution'
- 'Network Traffic: Network Traffic Flow'
- 'File: File Access'
- 'Application Log: Application Log Content'
id: attack-pattern--40597f16-0963-4249-bf4c-ac93b7fb9807
mitre_attack_url: https://attack.mitre.org/techniques/T1567
name: Exfiltration Over Web Service
platforms:
- Linux
- macOS
- Windows
- SaaS
- Office Suite
tactics:
- exfiltration
title: exfiltration - Exfiltration Over Web Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows, SaaS, Office Suite |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation, Command: Command Execution, Network Traffic: Network Traffic Flow, File: File Access, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1567](https://attack.mitre.org/techniques/T1567) |

# Exfiltration Over Web Service (attack-pattern--40597f16-0963-4249-bf4c-ac93b7fb9807)

## Description
Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. User behavior monitoring may help to detect abnormal patterns of activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1567)
