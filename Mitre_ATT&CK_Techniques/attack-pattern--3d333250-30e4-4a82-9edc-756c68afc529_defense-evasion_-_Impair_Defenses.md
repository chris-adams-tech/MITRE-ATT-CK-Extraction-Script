---
contributors:
- "Jamie Williams (U \u03C9 U), PANW Unit 42"
- Liran Ravich, CardinalOps
data_sources:
- 'File: File Modification'
- 'Cloud Service: Cloud Service Disable'
- 'Firewall: Firewall Rule Modification'
- 'Command: Command Execution'
- 'Script: Script Execution'
- 'Process: Process Modification'
- 'Windows Registry: Windows Registry Key Deletion'
- 'Process: Process Termination'
- 'Service: Service Metadata'
- 'Cloud Service: Cloud Service Modification'
- 'User Account: User Account Modification'
- 'File: File Deletion'
- 'Sensor Health: Host Status'
- 'Process: OS API Execution'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Driver: Driver Load'
- 'Firewall: Firewall Disable'
id: attack-pattern--3d333250-30e4-4a82-9edc-756c68afc529
mitre_attack_url: https://attack.mitre.org/techniques/T1562
name: Impair Defenses
platforms:
- Windows
- IaaS
- Linux
- macOS
- Containers
- Network
- Identity Provider
- Office Suite
tactics:
- defense-evasion
title: defense-evasion - Impair Defenses
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, IaaS, Linux, macOS, Containers, Network, Identity Provider, Office Suite |
| **Data Sources** | File: File Modification, Cloud Service: Cloud Service Disable, Firewall: Firewall Rule Modification, Command: Command Execution, Script: Script Execution, Process: Process Modification, Windows Registry: Windows Registry Key Deletion, Process: Process Termination, Service: Service Metadata, Cloud Service: Cloud Service Modification, User Account: User Account Modification, File: File Deletion, Sensor Health: Host Status, Process: OS API Execution, Process: Process Creation, Windows Registry: Windows Registry Key Modification, Driver: Driver Load, Firewall: Firewall Disable |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562](https://attack.mitre.org/techniques/T1562) |

# Impair Defenses (attack-pattern--3d333250-30e4-4a82-9edc-756c68afc529)

## Description
Adversaries may maliciously modify components of a victim environment in order to hinder or disable defensive mechanisms. This not only involves impairing preventative defenses, such as firewalls and anti-virus, but also detection capabilities that defenders can use to audit activity and identify malicious behavior. This may also span both native defenses as well as supplemental capabilities installed by users and administrators.

Adversaries may also impair routine operations that contribute to defensive hygiene, such as blocking users from logging out, preventing a system from shutting down, or disabling or modifying the update process. Adversaries could also target event aggregation and analysis mechanisms, or otherwise disrupt these procedures by altering other system components. These restrictions can further enable malicious operations as well as the continued propagation of incidents.(Citation: Google Cloud Mandiant UNC3886 2024)(Citation: Emotet shutdown)



## Detection
Monitor processes and command-line arguments to see if security tools or logging services are killed or stop running. Monitor Registry edits for modifications to services and startup programs that correspond to security tools.  Lack of log events may be suspicious.

Monitor environment variables and APIs that can be leveraged to disable security measures.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562)
- [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Emotet shutdown](https://thedfirreport.com/2022/11/28/emotet-strikes-again-lnk-file-leads-to-domain-wide-ransomware/)
