---
contributors:
- Madhukar Raina (Senior Security Researcher - Hack The Box, UK)
data_sources:
- 'User Account: User Account Modification'
id: attack-pattern--3e6831b2-bf4c-4ae6-b328-2e7c6633b291
mitre_attack_url: https://attack.mitre.org/techniques/T1098/007
name: Additional Local or Domain Groups
platforms:
- Windows
- macOS
- Linux
tactics:
- persistence
- privilege-escalation
title: persistence - Additional Local or Domain Groups
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | User Account: User Account Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1098/007](https://attack.mitre.org/techniques/T1098/007) |

# Additional Local or Domain Groups (attack-pattern--3e6831b2-bf4c-4ae6-b328-2e7c6633b291)

## Description
An adversary may add additional local or domain groups to an adversary-controlled account to maintain persistent access to a system or domain.

On Windows, accounts may use the `net localgroup` and `net group` commands to add existing users to local and domain groups.(Citation: Microsoft Net Localgroup)(Citation: Microsoft Net Group) On Linux, adversaries may use the `usermod` command for the same purpose.(Citation: Linux Usermod)

For example, accounts may be added to the local administrators group on Windows devices to maintain elevated privileges. They may also be added to the Remote Desktop Users group, which allows them to leverage [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001) to log into the endpoints in the future.(Citation: Microsoft RDP Logons) On Linux, accounts may be added to the sudoers group, allowing them to persistently leverage [Sudo and Sudo Caching](https://attack.mitre.org/techniques/T1548/003) for elevated privileges. 

In Windows environments, machine accounts may also be added to domain groups. This allows the local SYSTEM account to gain privileges on the domain.(Citation: RootDSE AD Detection 2022)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1098/007)
- [Linux Usermod](https://www.man7.org/linux/man-pages/man8/usermod.8.html)
- [Microsoft Net Group](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc754051(v=ws.11))
- [Microsoft Net Localgroup](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc725622(v=ws.11))
- [Microsoft RDP Logons](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/allow-log-on-through-remote-desktop-services)
- [RootDSE AD Detection 2022](https://rootdse.org/posts/monitoring-realtime-activedirectory-domain-scenarios)
