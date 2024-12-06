---
id: attack-pattern--9e80ddfb-ce32-4961-a778-ca6a10cfae72
mitre_attack_url: https://attack.mitre.org/techniques/T1169
name: Sudo
platforms:
- Linux
- macOS
tactics:
- privilege-escalation
title: privilege-escalation - Sudo
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation |
| **Platforms** | Linux, macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1169](https://attack.mitre.org/techniques/T1169) |

# Sudo (attack-pattern--9e80ddfb-ce32-4961-a778-ca6a10cfae72)

## Description
The sudoers file, <code>/etc/sudoers</code>, describes which users can run which commands and from which terminals. This also describes which commands users can run as other users or groups. This provides the idea of least privilege such that users are running in their lowest possible permissions for most of the time and only elevate to other users or permissions as needed, typically by prompting for a password. However, the sudoers file can also specify when to not prompt users for passwords with a line like <code>user1 ALL=(ALL) NOPASSWD: ALL</code> (Citation: OSX.Dok Malware). 

Adversaries can take advantage of these configurations to execute commands as other users or spawn processes with higher privileges. You must have elevated privileges to edit this file though.

## Detection
On Linux, auditd can alert every time a user's actual ID and effective ID are different (this is what happens when you sudo).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1169)
- [OSX.Dok Malware](https://blog.malwarebytes.com/threat-analysis/2017/04/new-osx-dok-malware-intercepts-web-traffic/)
