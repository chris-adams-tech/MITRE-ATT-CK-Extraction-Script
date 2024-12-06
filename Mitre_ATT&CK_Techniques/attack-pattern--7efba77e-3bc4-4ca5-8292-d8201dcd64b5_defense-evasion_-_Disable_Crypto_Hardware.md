---
data_sources:
- 'File: File Modification'
id: attack-pattern--7efba77e-3bc4-4ca5-8292-d8201dcd64b5
mitre_attack_url: https://attack.mitre.org/techniques/T1600/002
name: Disable Crypto Hardware
platforms:
- Network
tactics:
- defense-evasion
title: defense-evasion - Disable Crypto Hardware
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Network |
| **Data Sources** | File: File Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1600/002](https://attack.mitre.org/techniques/T1600/002) |

# Disable Crypto Hardware (attack-pattern--7efba77e-3bc4-4ca5-8292-d8201dcd64b5)

## Description
Adversaries disable a network device’s dedicated hardware encryption, which may enable them to leverage weaknesses in software encryption in order to reduce the effort involved in collecting, manipulating, and exfiltrating transmitted data.

Many network devices such as routers, switches, and firewalls, perform encryption on network traffic to secure transmission across networks. Often, these devices are equipped with special, dedicated encryption hardware to greatly increase the speed of the encryption process as well as to prevent malicious tampering. When an adversary takes control of such a device, they may disable the dedicated hardware, for example, through use of [Modify System Image](https://attack.mitre.org/techniques/T1601), forcing the use of software to perform encryption on general processors. This is typically used in conjunction with attacks to weaken the strength of the cipher in software (e.g., [Reduce Key Space](https://attack.mitre.org/techniques/T1600/001)). (Citation: Cisco Blog Legacy Device Attacks)

## Detection
There is no documented method for defenders to directly identify behaviors that disable cryptographic hardware. Detection efforts may be focused on closely related adversary behaviors, such as [Modify System Image](https://attack.mitre.org/techniques/T1601) and [Network Device CLI](https://attack.mitre.org/techniques/T1059/008). Some detection methods require vendor support to aid in investigation.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1600/002)
- [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
