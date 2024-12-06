---
contributors:
- Matthew Demaske, Adaptforward
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Logon Session: Logon Session Creation'
- 'Network Traffic: Network Connection Creation'
- 'Process: Process Creation'
- 'Logon Session: Logon Session Metadata'
id: attack-pattern--eb062747-2193-45de-8fa2-e62549c37ddf
mitre_attack_url: https://attack.mitre.org/techniques/T1021/001
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
| **Data Sources** | Network Traffic: Network Traffic Flow, Logon Session: Logon Session Creation, Network Traffic: Network Connection Creation, Process: Process Creation, Logon Session: Logon Session Metadata |
| **System Requirements** | RDP service enabled, account in the Remote Desktop Users group |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1021/001](https://attack.mitre.org/techniques/T1021/001) |

# Remote Desktop Protocol (attack-pattern--eb062747-2193-45de-8fa2-e62549c37ddf)

## Description
Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into a computer using the Remote Desktop Protocol (RDP). The adversary may then perform actions as the logged-on user.

Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).(Citation: TechNet Remote Desktop Services) 

Adversaries may connect to a remote system over RDP/RDS to expand access if the service is enabled and allows access to accounts with known credentials. Adversaries will likely use Credential Access techniques to acquire credentials to use with RDP. Adversaries may also use RDP in conjunction with the [Accessibility Features](https://attack.mitre.org/techniques/T1546/008) or [Terminal Services DLL](https://attack.mitre.org/techniques/T1505/005) for Persistence.(Citation: Alperovitch Malware)

## Detection
Use of RDP may be legitimate, depending on the network environment and how it is used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior with RDP. Monitor for user accounts logged into systems they would not normally access or access patterns to multiple systems over a relatively short period of time.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1021/001)
- [Alperovitch Malware](http://blog.crowdstrike.com/adversary-tricks-crowdstrike-treats/)
- [TechNet Remote Desktop Services](https://technet.microsoft.com/en-us/windowsserver/ee236407.aspx)
