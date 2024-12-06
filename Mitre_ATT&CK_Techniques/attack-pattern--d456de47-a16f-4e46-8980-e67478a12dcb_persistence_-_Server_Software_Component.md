---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Application Log: Application Log Content'
- 'File: File Modification'
- 'File: File Creation'
- 'Process: Process Creation'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--d456de47-a16f-4e46-8980-e67478a12dcb
mitre_attack_url: https://attack.mitre.org/techniques/T1505
name: Server Software Component
platforms:
- Windows
- Linux
- macOS
- Network
tactics:
- persistence
title: persistence - Server Software Component
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, Linux, macOS, Network |
| **Data Sources** | Network Traffic: Network Traffic Flow, Application Log: Application Log Content, File: File Modification, File: File Creation, Process: Process Creation, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1505](https://attack.mitre.org/techniques/T1505) |

# Server Software Component (attack-pattern--d456de47-a16f-4e46-8980-e67478a12dcb)

## Description
Adversaries may abuse legitimate extensible development features of servers to establish persistent access to systems. Enterprise server applications may include features that allow developers to write and install software or scripts to extend the functionality of the main application. Adversaries may install malicious components to extend and abuse server applications.(Citation: volexity_0day_sophos_FW)

## Detection
Consider monitoring application logs for abnormal behavior that may indicate suspicious installation of application software components. Consider monitoring file locations associated with the installation of new application software components such as paths from which applications typically load such extensible components.

Process monitoring may be used to detect servers components that perform suspicious actions such as running cmd.exe or accessing files. Log authentication attempts to the server and any unusual traffic patterns to or from the server and internal network. (Citation: US-CERT Alert TA15-314A Web Shells) 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1505)
- [volexity_0day_sophos_FW](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)
- [US-CERT Alert TA15-314A Web Shells](https://www.us-cert.gov/ncas/alerts/TA15-314A)
