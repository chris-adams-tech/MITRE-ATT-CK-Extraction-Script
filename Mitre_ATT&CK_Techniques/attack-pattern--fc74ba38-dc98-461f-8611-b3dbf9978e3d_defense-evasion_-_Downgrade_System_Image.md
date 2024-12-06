---
data_sources:
- 'File: File Modification'
id: attack-pattern--fc74ba38-dc98-461f-8611-b3dbf9978e3d
mitre_attack_url: https://attack.mitre.org/techniques/T1601/002
name: Downgrade System Image
platforms:
- Network
tactics:
- defense-evasion
title: defense-evasion - Downgrade System Image
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Network |
| **Data Sources** | File: File Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1601/002](https://attack.mitre.org/techniques/T1601/002) |

# Downgrade System Image (attack-pattern--fc74ba38-dc98-461f-8611-b3dbf9978e3d)

## Description
Adversaries may install an older version of the operating system of a network device to weaken security.  Older operating system versions on network devices often have weaker encryption ciphers and, in general, fewer/less updated defensive features. (Citation: Cisco Synful Knock Evolution)

On embedded devices, downgrading the version typically only requires replacing the operating system file in storage.  With most embedded devices, this can be achieved by downloading a copy of the desired version of the operating system file and reconfiguring the device to boot from that file on next system restart.  The adversary could then restart the device to implement the change immediately or they could wait until the next time the system restarts.

Downgrading the system image to an older versions may allow an adversary to evade defenses by enabling behaviors such as [Weaken Encryption](https://attack.mitre.org/techniques/T1600).  Downgrading of a system image can be done on its own, or it can be used in conjunction with [Patch System Image](https://attack.mitre.org/techniques/T1601/001).  

## Detection
Many embedded network devices provide a command to print the version of the currently running operating system.  Use this command to query the operating system for its version number and compare it to what is expected for the device in question.  Because image downgrade may be used in conjunction with [Patch System Image](https://attack.mitre.org/techniques/T1601/001), it may be appropriate to also verify the integrity of the vendor provided operating system image file. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1601/002)
- [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
