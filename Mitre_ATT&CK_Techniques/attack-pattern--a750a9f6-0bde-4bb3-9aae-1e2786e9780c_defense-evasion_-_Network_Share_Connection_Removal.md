---
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'User Account: User Account Authentication'
id: attack-pattern--a750a9f6-0bde-4bb3-9aae-1e2786e9780c
mitre_attack_url: https://attack.mitre.org/techniques/T1070/005
name: Network Share Connection Removal
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Network Share Connection Removal
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Network Traffic: Network Traffic Content, Command: Command Execution, Process: Process Creation, User Account: User Account Authentication |
| **System Requirements** | Established network share connection to a remote system. Level of access depends on permissions of the account used. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1070/005](https://attack.mitre.org/techniques/T1070/005) |

# Network Share Connection Removal (attack-pattern--a750a9f6-0bde-4bb3-9aae-1e2786e9780c)

## Description
Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation. Windows shared drive and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) connections can be removed when no longer needed. [Net](https://attack.mitre.org/software/S0039) is an example utility that can be used to remove network share connections with the <code>net use \\system\share /delete</code> command. (Citation: Technet Net Use)

## Detection
Network share connections may be common depending on how an network environment is used. Monitor command-line invocation of <code>net use</code> commands associated with establishing and removing remote shares over SMB, including following best practices for detection of [Windows Admin Shares](https://attack.mitre.org/techniques/T1077). SMB traffic between systems may also be captured and decoded to look for related network share session and file transfer activity. Windows authentication logs are also useful in determining when authenticated network shares are established and by which account, and can be used to correlate network share activity to other events to investigate potentially malicious activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1070/005)
- [Technet Net Use](https://technet.microsoft.com/bb490717.aspx)
