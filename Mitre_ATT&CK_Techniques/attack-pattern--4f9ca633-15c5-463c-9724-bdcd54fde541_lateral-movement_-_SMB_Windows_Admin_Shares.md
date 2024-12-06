---
data_sources:
- 'Network Share: Network Share Access'
- 'Network Traffic: Network Traffic Flow'
- 'Logon Session: Logon Session Creation'
- 'Network Traffic: Network Connection Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--4f9ca633-15c5-463c-9724-bdcd54fde541
mitre_attack_url: https://attack.mitre.org/techniques/T1021/002
name: SMB/Windows Admin Shares
platforms:
- Windows
tactics:
- lateral-movement
title: lateral-movement - SMB/Windows Admin Shares
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows |
| **Data Sources** | Network Share: Network Share Access, Network Traffic: Network Traffic Flow, Logon Session: Logon Session Creation, Network Traffic: Network Connection Creation, Process: Process Creation, Command: Command Execution |
| **System Requirements** | SMB enabled; Host/network firewalls not blocking SMB ports between source and destination; Use of domain account in administrator group on remote system or default system admin account. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1021/002](https://attack.mitre.org/techniques/T1021/002) |

# SMB/Windows Admin Shares (attack-pattern--4f9ca633-15c5-463c-9724-bdcd54fde541)

## Description
Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with a remote network share using Server Message Block (SMB). The adversary may then perform actions as the logged-on user.

SMB is a file, printer, and serial port sharing protocol for Windows machines on the same network or domain. Adversaries may use SMB to interact with file shares, allowing them to move laterally throughout a network. Linux and macOS implementations of SMB typically use Samba.

Windows systems have hidden network shares that are accessible only to administrators and provide the ability for remote file copy and other administrative functions. Example network shares include `C$`, `ADMIN$`, and `IPC$`. Adversaries may use this technique in conjunction with administrator-level [Valid Accounts](https://attack.mitre.org/techniques/T1078) to remotely access a networked system over SMB,(Citation: Wikipedia Server Message Block) to interact with systems using remote procedure calls (RPCs),(Citation: TechNet RPC) transfer files, and run transferred binaries through remote Execution. Example execution techniques that rely on authenticated sessions over SMB/RPC are [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), [Service Execution](https://attack.mitre.org/techniques/T1569/002), and [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047). Adversaries can also use NTLM hashes to access administrator shares on systems with [Pass the Hash](https://attack.mitre.org/techniques/T1550/002) and certain configuration and patch levels.(Citation: Microsoft Admin Shares)

## Detection
Ensure that proper logging of accounts used to log into systems is turned on and centrally collected. Windows logging is able to collect success/failure for accounts that may be used to move laterally and can be collected using tools such as Windows Event Forwarding. (Citation: Lateral Movement Payne)(Citation: Windows Event Forwarding Payne) Monitor remote login events and associated SMB activity for file transfers and remote process execution. Monitor the actions of remote users who connect to administrative shares. Monitor for use of tools and commands to connect to remote shares, such as [Net](https://attack.mitre.org/software/S0039), on the command-line interface and Discovery techniques that could be used to find remotely accessible systems.(Citation: Medium Detecting WMI Persistence)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1021/002)
- [Medium Detecting WMI Persistence](https://medium.com/threatpunter/detecting-removing-wmi-persistence-60ccbb7dff96)
- [TechNet RPC](https://technet.microsoft.com/en-us/library/cc787851.aspx)
- [Microsoft Admin Shares](http://support.microsoft.com/kb/314984)
- [Windows Event Forwarding Payne](https://docs.microsoft.com/en-us/archive/blogs/jepayne/monitoring-what-matters-windows-event-forwarding-for-everyone-even-if-you-already-have-a-siem)
- [Lateral Movement Payne](https://docs.microsoft.com/en-us/archive/blogs/jepayne/tracking-lateral-movement-part-one-special-groups-and-specific-service-accounts)
- [Wikipedia Server Message Block](https://en.wikipedia.org/wiki/Server_Message_Block)
