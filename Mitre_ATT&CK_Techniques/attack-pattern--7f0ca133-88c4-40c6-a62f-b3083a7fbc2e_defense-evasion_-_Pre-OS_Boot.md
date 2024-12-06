---
data_sources:
- 'Drive: Drive Modification'
- 'Network Traffic: Network Connection Creation'
- 'Process: OS API Execution'
- 'Driver: Driver Metadata'
- 'Command: Command Execution'
- 'Firmware: Firmware Modification'
id: attack-pattern--7f0ca133-88c4-40c6-a62f-b3083a7fbc2e
mitre_attack_url: https://attack.mitre.org/techniques/T1542
name: Pre-OS Boot
platforms:
- Linux
- Windows
- Network
- macOS
tactics:
- defense-evasion
- persistence
title: defense-evasion - Pre-OS Boot
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence |
| **Platforms** | Linux, Windows, Network, macOS |
| **Data Sources** | Drive: Drive Modification, Network Traffic: Network Connection Creation, Process: OS API Execution, Driver: Driver Metadata, Command: Command Execution, Firmware: Firmware Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1542](https://attack.mitre.org/techniques/T1542) |

# Pre-OS Boot (attack-pattern--7f0ca133-88c4-40c6-a62f-b3083a7fbc2e)

## Description
Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system. During the booting process of a computer, firmware and various startup services are loaded before the operating system. These programs control flow of execution before the operating system takes control.(Citation: Wikipedia Booting)

Adversaries may overwrite data in boot drivers or firmware such as BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) to persist on systems at a layer below the operating system. This can be particularly difficult to detect as malware at this level will not be detected by host software-based defenses.

## Detection
Perform integrity checking on pre-OS boot mechanisms that can be manipulated for malicious purposes. Take snapshots of boot records and firmware and compare against known good images. Log changes to boot records, BIOS, and EFI, which can be performed by API calls, and compare against known good behavior and patching.

Disk check, forensic utilities, and data from device drivers (i.e. processes and API calls) may reveal anomalies that warrant deeper investigation.(Citation: ITWorld Hard Disk Health Dec 2014)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1542)
- [ITWorld Hard Disk Health Dec 2014](https://www.itworld.com/article/2853992/3-tools-to-check-your-hard-drives-health-and-make-sure-its-not-already-dying-on-you.html)
- [Wikipedia Booting](https://en.wikipedia.org/wiki/Booting)
