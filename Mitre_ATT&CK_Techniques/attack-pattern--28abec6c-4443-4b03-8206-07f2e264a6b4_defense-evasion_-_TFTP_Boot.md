---
data_sources:
- 'Command: Command Execution'
- 'Network Traffic: Network Connection Creation'
- 'Firmware: Firmware Modification'
id: attack-pattern--28abec6c-4443-4b03-8206-07f2e264a6b4
mitre_attack_url: https://attack.mitre.org/techniques/T1542/005
name: TFTP Boot
platforms:
- Network
tactics:
- defense-evasion
- persistence
title: defense-evasion - TFTP Boot
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence |
| **Platforms** | Network |
| **Data Sources** | Command: Command Execution, Network Traffic: Network Connection Creation, Firmware: Firmware Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1542/005](https://attack.mitre.org/techniques/T1542/005) |

# TFTP Boot (attack-pattern--28abec6c-4443-4b03-8206-07f2e264a6b4)

## Description
Adversaries may abuse netbooting to load an unauthorized network device operating system from a Trivial File Transfer Protocol (TFTP) server. TFTP boot (netbooting) is commonly used by network administrators to load configuration-controlled network device images from a centralized management server. Netbooting is one option in the boot sequence and can be used to centralize, manage, and control device images.

Adversaries may manipulate the configuration on the network device specifying use of a malicious TFTP server, which may be used in conjunction with [Modify System Image](https://attack.mitre.org/techniques/T1601) to load a modified image on device startup or reset. The unauthorized image allows adversaries to modify device configuration, add malicious capabilities to the device, and introduce backdoors to maintain control of the network device while minimizing detection through use of a standard functionality. This technique is similar to [ROMMONkit](https://attack.mitre.org/techniques/T1542/004) and may result in the network device running a modified image. (Citation: Cisco Blog Legacy Device Attacks)

## Detection
Consider comparing a copy of the network device configuration and system image against a known-good version to discover unauthorized changes to system boot, startup configuration, or the running OS. (Citation: Cisco IOS Software Integrity Assurance - Secure Boot) (Citation: Cisco IOS Software Integrity Assurance - Image File Verification)The same process can be accomplished through a comparison of the run-time memory, though this is non-trivial and may require assistance from the vendor.  (Citation: Cisco IOS Software Integrity Assurance - Run-Time Memory Verification)

Review command history in either the console or as part of the running memory to determine if unauthorized or suspicious commands were used to modify device configuration. (Citation: Cisco IOS Software Integrity Assurance - Command History) Check boot information including system uptime, image booted, and startup configuration to determine if results are consistent with expected behavior in the environment. (Citation: Cisco IOS Software Integrity Assurance - Boot Information) Monitor unusual connections or connection attempts to the device that may specifically target TFTP or other file-sharing protocols.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1542/005)
- [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
- [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)
- [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)
- [Cisco IOS Software Integrity Assurance - Run-Time Memory Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#13)
- [Cisco IOS Software Integrity Assurance - Command History](https://tools.cisco.com/security/center/resources/integrity_assurance.html#23)
- [Cisco IOS Software Integrity Assurance - Boot Information](https://tools.cisco.com/security/center/resources/integrity_assurance.html#26)
