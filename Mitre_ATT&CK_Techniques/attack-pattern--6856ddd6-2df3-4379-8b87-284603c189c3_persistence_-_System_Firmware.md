---
contributors:
- Ryan Becwar
- McAfee
id: attack-pattern--6856ddd6-2df3-4379-8b87-284603c189c3
mitre_attack_url: https://attack.mitre.org/techniques/T1019
name: System Firmware
platforms:
- Windows
tactics:
- persistence
title: persistence - System Firmware
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1019](https://attack.mitre.org/techniques/T1019) |

# System Firmware (attack-pattern--6856ddd6-2df3-4379-8b87-284603c189c3)

## Description
The BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) or Extensible Firmware Interface (EFI) are examples of system firmware that operate as the software interface between the operating system and hardware of a computer. (Citation: Wikipedia BIOS) (Citation: Wikipedia UEFI) (Citation: About UEFI)

System firmware like BIOS and (U)EFI underly the functionality of a computer and may be modified by an adversary to perform or assist in malicious activity. Capabilities exist to overwrite the system firmware, which may give sophisticated adversaries a means to install malicious firmware updates as a means of persistence on a system that may be difficult to detect.

## Detection
System firmware manipulation may be detected. (Citation: MITRE Trustworthy Firmware Measurement) Dump and inspect BIOS images on vulnerable systems and compare against known good images. (Citation: MITRE Copernicus) Analyze differences to determine if malicious changes have occurred. Log attempts to read/write to BIOS and compare against known patching behavior.

Likewise, EFI modules can be collected and compared against a known-clean list of EFI executable binaries to detect potentially malicious modules. The CHIPSEC framework can be used for analysis to determine if firmware modifications have been performed. (Citation: McAfee CHIPSEC Blog) (Citation: Github CHIPSEC) (Citation: Intel HackingTeam UEFI Rootkit)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1019)
- [capec](https://capec.mitre.org/data/definitions/532.html)
- [Wikipedia BIOS](https://en.wikipedia.org/wiki/BIOS)
- [Wikipedia UEFI](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface)
- [About UEFI](http://www.uefi.org/about)
- [MITRE Trustworthy Firmware Measurement](http://www.mitre.org/publications/project-stories/going-deep-into-the-bios-with-mitre-firmware-security-research)
- [MITRE Copernicus](http://www.mitre.org/capabilities/cybersecurity/overview/cybersecurity-blog/copernicus-question-your-assumptions-about)
- [McAfee CHIPSEC Blog](https://securingtomorrow.mcafee.com/business/chipsec-support-vault-7-disclosure-scanning/)
- [Github CHIPSEC](https://github.com/chipsec/chipsec)
- [Intel HackingTeam UEFI Rootkit](http://www.intelsecurity.com/advanced-threat-research/content/data/HT-UEFI-rootkit.html)
