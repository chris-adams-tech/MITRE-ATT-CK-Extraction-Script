---
data_sources:
- 'Firmware: Firmware Modification'
id: attack-pattern--f5bb433e-bdf6-4781-84bc-35e97e43be89
mitre_attack_url: https://attack.mitre.org/techniques/T1495
name: Firmware Corruption
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- impact
title: impact - Firmware Corruption
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Firmware: Firmware Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1495](https://attack.mitre.org/techniques/T1495) |

# Firmware Corruption (attack-pattern--f5bb433e-bdf6-4781-84bc-35e97e43be89)

## Description
Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached to a system in order to render them inoperable or unable to boot, thus denying the availability to use the devices and/or the system.(Citation: Symantec Chernobyl W95.CIH) Firmware is software that is loaded and executed from non-volatile memory on hardware devices in order to initialize and manage device functionality. These devices may include the motherboard, hard drive, or video cards.

In general, adversaries may manipulate, overwrite, or corrupt firmware in order to deny the use of the system or devices. For example, corruption of firmware responsible for loading the operating system for network devices may render the network devices inoperable.(Citation: dhs_threat_to_net_devices)(Citation: cisa_malware_orgs_ukraine) Depending on the device, this attack may also result in [Data Destruction](https://attack.mitre.org/techniques/T1485). 

## Detection
System firmware manipulation may be detected.(Citation: MITRE Trustworthy Firmware Measurement) Log attempts to read/write to BIOS and compare against known patching behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1495)
- [cisa_malware_orgs_ukraine](https://www.cisa.gov/uscert/ncas/alerts/aa22-057a)
- [dhs_threat_to_net_devices](https://cyber.dhs.gov/assets/report/ar-16-20173.pdf)
- [MITRE Trustworthy Firmware Measurement](http://www.mitre.org/publications/project-stories/going-deep-into-the-bios-with-mitre-firmware-security-research)
- [Symantec Chernobyl W95.CIH](https://web.archive.org/web/20190508170055/https://www.symantec.com/security-center/writeup/2000-122010-2655-99)
