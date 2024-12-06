---
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--e0033c16-a07e-48aa-8204-7c3ca669998c
mitre_attack_url: https://attack.mitre.org/techniques/T1563/002
name: RDP Hijacking
platforms:
- Windows
tactics:
- lateral-movement
title: lateral-movement - RDP Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows |
| **Data Sources** | Logon Session: Logon Session Creation, Process: Process Creation, Command: Command Execution, Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1563/002](https://attack.mitre.org/techniques/T1563/002) |

# RDP Hijacking (attack-pattern--e0033c16-a07e-48aa-8204-7c3ca669998c)

## Description
Adversaries may hijack a legitimate user’s remote desktop session to move laterally within an environment. Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).(Citation: TechNet Remote Desktop Services)

Adversaries may perform RDP session hijacking which involves stealing a legitimate user's remote session. Typically, a user is notified when someone else is trying to steal their session. With System permissions and using Terminal Services Console, `c:\windows\system32\tscon.exe [session number to be stolen]`, an adversary can hijack a session without the need for credentials or prompts to the user.(Citation: RDP Hijacking Korznikov) This can be done remotely or locally and with active or disconnected sessions.(Citation: RDP Hijacking Medium) It can also lead to [Remote System Discovery](https://attack.mitre.org/techniques/T1018) and Privilege Escalation by stealing a Domain Admin or higher privileged account session. All of this can be done by using native Windows commands, but it has also been added as a feature in red teaming tools.(Citation: Kali Redsnarf)

## Detection
Consider monitoring processes for `tscon.exe` usage and monitor service creation that uses `cmd.exe /k` or `cmd.exe /c` in its arguments to detect RDP session hijacking.

Use of RDP may be legitimate, depending on the network environment and how it is used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior with RDP.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1563/002)
- [RDP Hijacking Medium](https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6)
- [RDP Hijacking Korznikov](http://www.korznikov.com/2017/03/0-day-or-feature-privilege-escalation.html)
- [TechNet Remote Desktop Services](https://technet.microsoft.com/en-us/windowsserver/ee236407.aspx)
- [Kali Redsnarf](https://github.com/nccgroup/redsnarf)
