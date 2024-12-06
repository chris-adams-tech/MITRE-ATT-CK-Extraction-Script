---
data_sources:
- 'File: File Modification'
id: attack-pattern--3a40f208-a9c1-4efa-a598-4003c3681fb8
mitre_attack_url: https://attack.mitre.org/techniques/T1600/001
name: Reduce Key Space
platforms:
- Network
tactics:
- defense-evasion
title: defense-evasion - Reduce Key Space
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Network |
| **Data Sources** | File: File Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1600/001](https://attack.mitre.org/techniques/T1600/001) |

# Reduce Key Space (attack-pattern--3a40f208-a9c1-4efa-a598-4003c3681fb8)

## Description
Adversaries may reduce the level of effort required to decrypt data transmitted over the network by reducing the cipher strength of encrypted communications.(Citation: Cisco Synful Knock Evolution)

Adversaries can weaken the encryption software on a compromised network device by reducing the key size used by the software to convert plaintext to ciphertext (e.g., from hundreds or thousands of bytes to just a couple of bytes). As a result, adversaries dramatically reduce the amount of effort needed to decrypt the protected information without the key.

Adversaries may modify the key size used and other encryption parameters using specialized commands in a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) introduced to the system through [Modify System Image](https://attack.mitre.org/techniques/T1601) to change the configuration of the device. (Citation: Cisco Blog Legacy Device Attacks)

## Detection
There is no documented method for defenders to directly identify behaviors that reduce encryption key space. Detection efforts may be focused on closely related adversary behaviors, such as [Modify System Image](https://attack.mitre.org/techniques/T1601) and [Network Device CLI](https://attack.mitre.org/techniques/T1059/008). Some detection methods require vendor support to aid in investigation.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1600/001)
- [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
- [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
