---
data_sources:
- 'Firewall: Firewall Rule Modification'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
- 'Firewall: Firewall Disable'
id: attack-pattern--5372c5fe-f424-4def-bcd5-d3a8e770f07b
mitre_attack_url: https://attack.mitre.org/techniques/T1562/004
name: Disable or Modify System Firewall
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- defense-evasion
title: defense-evasion - Disable or Modify System Firewall
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Firewall: Firewall Rule Modification, Windows Registry: Windows Registry Key Modification, Command: Command Execution, Firewall: Firewall Disable |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/004](https://attack.mitre.org/techniques/T1562/004) |

# Disable or Modify System Firewall (attack-pattern--5372c5fe-f424-4def-bcd5-d3a8e770f07b)

## Description
Adversaries may disable or modify system firewalls in order to bypass controls limiting network usage. Changes could be disabling the entire mechanism as well as adding, deleting, or modifying particular rules. This can be done numerous ways depending on the operating system, including via command-line, editing Windows Registry keys, and Windows Control Panel.

Modifying or disabling a system firewall may enable adversary C2 communications, lateral movement, and/or data exfiltration that would otherwise not be allowed. For example, adversaries may add a new firewall rule for a well-known protocol (such as RDP) using a non-traditional and potentially less securitized port (i.e. [Non-Standard Port](https://attack.mitre.org/techniques/T1571)).(Citation: change_rdp_port_conti)

Adversaries may also modify host networking settings that indirectly manipulate system firewalls, such as interface bandwidth or network connection request thresholds.(Citation: Huntress BlackCat) Settings related to enabling abuse of various [Remote Services](https://attack.mitre.org/techniques/T1021) may also indirectly modify firewall rules.

## Detection
Monitor processes and command-line arguments to see if firewalls are disabled or modified. Monitor Registry edits to keys that manage firewalls.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/004)
- [Huntress BlackCat](https://www.huntress.com/blog/blackcat-ransomware-affiliate-ttps)
- [change_rdp_port_conti](https://x.com/TheDFIRReport/status/1498657772254240768)
