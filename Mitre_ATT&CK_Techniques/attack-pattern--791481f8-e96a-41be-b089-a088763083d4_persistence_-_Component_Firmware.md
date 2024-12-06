---
data_sources:
- 'Firmware: Firmware Modification'
- 'Process: OS API Execution'
- 'Driver: Driver Metadata'
id: attack-pattern--791481f8-e96a-41be-b089-a088763083d4
mitre_attack_url: https://attack.mitre.org/techniques/T1542/002
name: Component Firmware
platforms:
- Windows
- Linux
- macOS
tactics:
- persistence
- defense-evasion
title: persistence - Component Firmware
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, defense-evasion |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Firmware: Firmware Modification, Process: OS API Execution, Driver: Driver Metadata |
| **Permissions Required** | SYSTEM |
| **System Requirements** | Ability to update component device firmware from the host operating system. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1542/002](https://attack.mitre.org/techniques/T1542/002) |

# Component Firmware (attack-pattern--791481f8-e96a-41be-b089-a088763083d4)

## Description
Adversaries may modify component firmware to persist on systems. Some adversaries may employ sophisticated means to compromise computer components and install malicious firmware that will execute adversary code outside of the operating system and main system firmware or BIOS. This technique may be similar to [System Firmware](https://attack.mitre.org/techniques/T1542/001) but conducted upon other system components/devices that may not have the same capability or level of integrity checking.

Malicious component firmware could provide both a persistent level of access to systems despite potential typical failures to maintain access and hard disk re-images, as well as a way to evade host software-based defenses and integrity checks.

## Detection
Data and telemetry from use of device drivers (i.e. processes and API calls) and/or provided by SMART (Self-Monitoring, Analysis and Reporting Technology) disk monitoring may reveal malicious manipulations of components.(Citation: SanDisk SMART)(Citation: SmartMontools) Otherwise, this technique may be difficult to detect since malicious activity is taking place on system components possibly outside the purview of OS security and integrity mechanisms.

Disk check and forensic utilities may reveal indicators of malicious firmware such as strings, unexpected disk partition table entries, or blocks of otherwise unusual memory that warrant deeper investigation.(Citation: ITWorld Hard Disk Health Dec 2014) Also consider comparing components, including hashes of component firmware and behavior, against known good images.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1542/002)
- [SmartMontools](https://www.smartmontools.org/)
- [ITWorld Hard Disk Health Dec 2014](https://www.itworld.com/article/2853992/3-tools-to-check-your-hard-drives-health-and-make-sure-its-not-already-dying-on-you.html)
