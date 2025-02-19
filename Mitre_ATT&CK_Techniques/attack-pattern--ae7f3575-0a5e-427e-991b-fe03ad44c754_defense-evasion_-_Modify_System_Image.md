---
data_sources:
- 'File: File Modification'
id: attack-pattern--ae7f3575-0a5e-427e-991b-fe03ad44c754
mitre_attack_url: https://attack.mitre.org/techniques/T1601
name: Modify System Image
platforms:
- Network
tactics:
- defense-evasion
title: defense-evasion - Modify System Image
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Network |
| **Data Sources** | File: File Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1601](https://attack.mitre.org/techniques/T1601) |

# Modify System Image (attack-pattern--ae7f3575-0a5e-427e-991b-fe03ad44c754)

## Description
Adversaries may make changes to the operating system of embedded network devices to weaken defenses and provide new capabilities for themselves.  On such devices, the operating systems are typically monolithic and most of the device functionality and capabilities are contained within a single file.

To change the operating system, the adversary typically only needs to affect this one file, replacing or modifying it.  This can either be done live in memory during system runtime for immediate effect, or in storage to implement the change on the next boot of the network device.

## Detection
Most embedded network devices provide a command to print the version of the currently running operating system.  Use this command to query the operating system for its version number and compare it to what is expected for the device in question.  Because this method may be used in conjunction with [Patch System Image](https://attack.mitre.org/techniques/T1601/001), it may be appropriate to also verify the integrity of the vendor provided operating system image file. 

Compare the checksum of the operating system file with the checksum of a known good copy from a trusted source.  Some embedded network device platforms may have the capability to calculate the checksum of the file, while others may not.  Even for those platforms that have the capability, it is recommended to download a copy of the file to a trusted computer to calculate the checksum with software that is not compromised.  (Citation: Cisco IOS Software Integrity Assurance - Image File Verification)

Many vendors of embedded network devices can provide advanced debugging support that will allow them to work with device owners to validate the integrity of the operating system running in memory.  If a compromise of the operating system is suspected, contact the vendor technical support and seek such services for a more thorough inspection of the current running system.  (Citation: Cisco IOS Software Integrity Assurance - Run-Time Memory Verification)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1601)
- [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)
- [Cisco IOS Software Integrity Assurance - Run-Time Memory Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#13)
