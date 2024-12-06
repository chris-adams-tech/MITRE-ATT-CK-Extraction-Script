---
contributors:
- Matthew Demaske, Adaptforward
id: attack-pattern--51dea151-0898-4a45-967c-3ebee0420484
mitre_attack_url: https://attack.mitre.org/techniques/T1076
name: Remote Desktop Protocol
platforms:
- Windows
tactics:
- lateral-movement
title: lateral-movement - Remote Desktop Protocol
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows |
| **Permissions Required** | Remote Desktop Users, User |
| **System Requirements** | RDP service enabled, account in the Remote Desktop Users group. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1076](https://attack.mitre.org/techniques/T1076) |

# Remote Desktop Protocol (attack-pattern--51dea151-0898-4a45-967c-3ebee0420484)

## Description
Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS). (Citation: TechNet Remote Desktop Services) There are other implementations and third-party tools that provide graphical access [Remote Services](https://attack.mitre.org/techniques/T1021) similar to RDS.

Adversaries may connect to a remote system over RDP/RDS to expand access if the service is enabled and allows access to accounts with known credentials. Adversaries will likely use Credential Access techniques to acquire credentials to use with RDP. Adversaries may also use RDP in conjunction with the [Accessibility Features](https://attack.mitre.org/techniques/T1015) technique for Persistence. (Citation: Alperovitch Malware)

Adversaries may also perform RDP session hijacking which involves stealing a legitimate user's remote session. Typically, a user is notified when someone else is trying to steal their session and prompted with a question. With System permissions and using Terminal Services Console, <code>c:\windows\system32\tscon.exe [session number to be stolen]</code>, an adversary can hijack a session without the need for credentials or prompts to the user. (Citation: RDP Hijacking Korznikov) This can be done remotely or locally and with active or disconnected sessions. (Citation: RDP Hijacking Medium) It can also lead to [Remote System Discovery](https://attack.mitre.org/techniques/T1018) and Privilege Escalation by stealing a Domain Admin or higher privileged account session. All of this can be done by using native Windows commands, but it has also been added as a feature in RedSnarf. (Citation: Kali Redsnarf)

## Detection
Use of RDP may be legitimate, depending on the network environment and how it is used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior with RDP. Monitor for user accounts logged into systems they would not normally access or access patterns to multiple systems over a relatively short period of time.

Also, set up process monitoring for <code>tscon.exe</code> usage and monitor service creation that uses <code>cmd.exe /k</code> or <code>cmd.exe /c</code> in its arguments to prevent RDP session hijacking.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1076)
- [capec](https://capec.mitre.org/data/definitions/555.html)
- [TechNet Remote Desktop Services](https://technet.microsoft.com/en-us/windowsserver/ee236407.aspx)
- [Alperovitch Malware](http://blog.crowdstrike.com/adversary-tricks-crowdstrike-treats/)
- [RDP Hijacking Korznikov](http://www.korznikov.com/2017/03/0-day-or-feature-privilege-escalation.html)
- [RDP Hijacking Medium](https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6)
- [Kali Redsnarf](https://github.com/nccgroup/redsnarf)
