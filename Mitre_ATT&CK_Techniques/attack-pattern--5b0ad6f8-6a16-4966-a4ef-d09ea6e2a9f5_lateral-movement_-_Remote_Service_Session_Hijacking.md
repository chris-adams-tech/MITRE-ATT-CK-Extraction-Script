---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Logon Session: Logon Session Creation'
id: attack-pattern--5b0ad6f8-6a16-4966-a4ef-d09ea6e2a9f5
mitre_attack_url: https://attack.mitre.org/techniques/T1563
name: Remote Service Session Hijacking
platforms:
- Linux
- macOS
- Windows
tactics:
- lateral-movement
title: lateral-movement - Remote Service Session Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content, Command: Command Execution, Process: Process Creation, Logon Session: Logon Session Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1563](https://attack.mitre.org/techniques/T1563) |

# Remote Service Session Hijacking (attack-pattern--5b0ad6f8-6a16-4966-a4ef-d09ea6e2a9f5)

## Description
Adversaries may take control of preexisting sessions with remote services to move laterally in an environment. Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet, SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous interaction with that service.

Adversaries may commandeer these sessions to carry out actions on remote systems. [Remote Service Session Hijacking](https://attack.mitre.org/techniques/T1563) differs from use of [Remote Services](https://attack.mitre.org/techniques/T1021) because it hijacks an existing session rather than creating a new session using [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation: RDP Hijacking Medium)(Citation: Breach Post-mortem SSH Hijack)

## Detection
Use of these services may be legitimate, depending upon the network environment and how it is used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior with that service. Monitor for user accounts logged into systems they would not normally access or access patterns to multiple systems over a relatively short period of time.

Monitor for processes and command-line arguments associated with hijacking service sessions.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1563)
- [RDP Hijacking Medium](https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6)
- [Breach Post-mortem SSH Hijack](https://matrix.org/blog/2019/05/08/post-mortem-and-remediations-for-apr-11-security-incident)
