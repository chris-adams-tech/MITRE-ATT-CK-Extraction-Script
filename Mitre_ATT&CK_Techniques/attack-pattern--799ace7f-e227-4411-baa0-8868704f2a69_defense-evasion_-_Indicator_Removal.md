---
contributors:
- Brad Geesaman, @bradgeesaman
- Ed Williams, Trustwave, SpiderLabs
- Blake Strom, Microsoft 365 Defender
data_sources:
- 'Scheduled Job: Scheduled Job Modification'
- 'File: File Modification'
- 'Firewall: Firewall Rule Modification'
- 'User Account: User Account Authentication'
- 'File: File Metadata'
- 'User Account: User Account Deletion'
- 'Process: OS API Execution'
- 'Application Log: Application Log Content'
- 'Command: Command Execution'
- 'File: File Deletion'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Network Traffic: Network Traffic Content'
- 'Windows Registry: Windows Registry Key Deletion'
id: attack-pattern--799ace7f-e227-4411-baa0-8868704f2a69
mitre_attack_url: https://attack.mitre.org/techniques/T1070
name: Indicator Removal
platforms:
- Linux
- macOS
- Windows
- Containers
- Network
- Office Suite
tactics:
- defense-evasion
title: defense-evasion - Indicator Removal
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, Containers, Network, Office Suite |
| **Data Sources** | Scheduled Job: Scheduled Job Modification, File: File Modification, Firewall: Firewall Rule Modification, User Account: User Account Authentication, File: File Metadata, User Account: User Account Deletion, Process: OS API Execution, Application Log: Application Log Content, Command: Command Execution, File: File Deletion, Process: Process Creation, Windows Registry: Windows Registry Key Modification, Network Traffic: Network Traffic Content, Windows Registry: Windows Registry Key Deletion |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1070](https://attack.mitre.org/techniques/T1070) |

# Indicator Removal (attack-pattern--799ace7f-e227-4411-baa0-8868704f2a69)

## Description
Adversaries may delete or modify artifacts generated within systems to remove evidence of their presence or hinder defenses. Various artifacts may be created by an adversary or something that can be attributed to an adversary’s actions. Typically these artifacts are used as defensive indicators related to monitored events, such as strings from downloaded files, logs that are generated from user actions, and other data analyzed by defenders. Location, format, and type of artifact (such as command or login history) are often specific to each platform.

Removal of these indicators may interfere with event collection, reporting, or other processes used to detect intrusion activity. This may compromise the integrity of security solutions by causing notable events to go unreported. This activity may also impede forensic analysis and incident response, due to lack of sufficient data to determine what occurred.

## Detection
File system monitoring may be used to detect improper deletion or modification of indicator files.  Events not stored on the file system may require different detection mechanisms.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1070)
