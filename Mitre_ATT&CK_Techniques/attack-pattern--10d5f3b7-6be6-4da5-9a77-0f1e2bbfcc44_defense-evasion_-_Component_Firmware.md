---
id: attack-pattern--10d5f3b7-6be6-4da5-9a77-0f1e2bbfcc44
mitre_attack_url: https://attack.mitre.org/techniques/T1109
name: Component Firmware
platforms:
- Windows
tactics:
- defense-evasion
- persistence
title: defense-evasion - Component Firmware
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence |
| **Platforms** | Windows |
| **Permissions Required** | SYSTEM |
| **System Requirements** | Ability to update component device firmware from the host operating system. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1109](https://attack.mitre.org/techniques/T1109) |

# Component Firmware (attack-pattern--10d5f3b7-6be6-4da5-9a77-0f1e2bbfcc44)

## Description
Some adversaries may employ sophisticated means to compromise computer components and install malicious firmware that will execute adversary code outside of the operating system and main system firmware or BIOS. This technique may be similar to [System Firmware](https://attack.mitre.org/techniques/T1019) but conducted upon other system components that may not have the same capability or level of integrity checking. Malicious device firmware could provide both a persistent level of access to systems despite potential typical failures to maintain access and hard disk re-images, as well as a way to evade host software-based defenses and integrity checks.

## Detection
Data and telemetry from use of device drivers (i.e. processes and API calls) and/or provided by SMART (Self-Monitoring, Analysis and Reporting Technology) (Citation: SanDisk SMART) (Citation: SmartMontools) disk monitoring may reveal malicious manipulations of components. Otherwise, this technique may be difficult to detect since malicious activity is taking place on system components possibly outside the purview of OS security and integrity mechanisms.

Disk check and forensic utilities (Citation: ITWorld Hard Disk Health Dec 2014) may reveal indicators of malicious firmware such as strings, unexpected disk partition table entries, or blocks of otherwise unusual memory that warrant deeper investigation. Also consider comparing components, including hashes of component firmware and behavior, against known good images.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1109)
- [SmartMontools](https://www.smartmontools.org/)
- [ITWorld Hard Disk Health Dec 2014](https://www.itworld.com/article/2853992/3-tools-to-check-your-hard-drives-health-and-make-sure-its-not-already-dying-on-you.html)
