---
data_sources:
- 'Command: Command Execution'
id: attack-pattern--818302b2-d640-477b-bf88-873120ce85c4
mitre_attack_url: https://attack.mitre.org/techniques/T1059/008
name: Network Device CLI
platforms:
- Network
tactics:
- execution
title: execution - Network Device CLI
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Network |
| **Data Sources** | Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/008](https://attack.mitre.org/techniques/T1059/008) |

# Network Device CLI (attack-pattern--818302b2-d640-477b-bf88-873120ce85c4)

## Description
Adversaries may abuse scripting or built-in command line interpreters (CLI) on network devices to execute malicious command and payloads. The CLI is the primary means through which users and administrators interact with the device in order to view system information, modify device operations, or perform diagnostic and administrative functions. CLIs typically contain various permission levels required for different commands. 

Scripting interpreters automate tasks and extend functionality beyond the command set included in the network OS. The CLI and scripting interpreter are accessible through a direct console connection, or through remote means, such as telnet or [SSH](https://attack.mitre.org/techniques/T1021/004).

Adversaries can use the network CLI to change how network devices behave and operate. The CLI may be used to manipulate traffic flows to intercept or manipulate data, modify startup configuration parameters to load malicious system software, or to disable security features or logging to avoid detection.(Citation: Cisco Synful Knock Evolution)

## Detection
Consider reviewing command history in either the console or as part of the running memory to determine if unauthorized or suspicious commands were used to modify device configuration.(Citation: Cisco IOS Software Integrity Assurance - Command History)

Consider comparing a copy of the network device configuration against a known-good version to discover unauthorized changes to the command interpreter. The same process can be accomplished through a comparison of the run-time memory, though this is non-trivial and may require assistance from the vendor.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/008)
- [Cisco IOS Software Integrity Assurance - Command History](https://tools.cisco.com/security/center/resources/integrity_assurance.html#23)
- [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
