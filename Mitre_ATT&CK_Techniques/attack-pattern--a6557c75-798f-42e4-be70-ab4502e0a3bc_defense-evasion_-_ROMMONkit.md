---
data_sources:
- 'Firmware: Firmware Modification'
id: attack-pattern--a6557c75-798f-42e4-be70-ab4502e0a3bc
mitre_attack_url: https://attack.mitre.org/techniques/T1542/004
name: ROMMONkit
platforms:
- Network
tactics:
- defense-evasion
- persistence
title: defense-evasion - ROMMONkit
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence |
| **Platforms** | Network |
| **Data Sources** | Firmware: Firmware Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1542/004](https://attack.mitre.org/techniques/T1542/004) |

# ROMMONkit (attack-pattern--a6557c75-798f-42e4-be70-ab4502e0a3bc)

## Description
Adversaries may abuse the ROM Monitor (ROMMON) by loading an unauthorized firmware with adversary code to provide persistent access and manipulate device behavior that is difficult to detect. (Citation: Cisco Synful Knock Evolution)(Citation: Cisco Blog Legacy Device Attacks)


ROMMON is a Cisco network device firmware that functions as a boot loader, boot image, or boot helper to initialize hardware and software when the platform is powered on or reset. Similar to [TFTP Boot](https://attack.mitre.org/techniques/T1542/005), an adversary may upgrade the ROMMON image locally or remotely (for example, through TFTP) with adversary code and restart the device in order to overwrite the existing ROMMON image. This provides adversaries with the means to update the ROMMON to gain persistence on a system in a way that may be difficult to detect.

## Detection
There are no documented means for defenders to validate the operation of the ROMMON outside of vendor support. If a network device is suspected of being compromised, contact the vendor to assist in further investigation.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1542/004)
- [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
- [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
