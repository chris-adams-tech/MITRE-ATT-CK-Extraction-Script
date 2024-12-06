---
id: attack-pattern--ffe742ed-9100-4686-9e00-c331da544787
mitre_attack_url: https://attack.mitre.org/techniques/T1077
name: Windows Admin Shares
platforms:
- Windows
tactics:
- lateral-movement
title: lateral-movement - Windows Admin Shares
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows |
| **Permissions Required** | Administrator |
| **System Requirements** | File and printer sharing over SMB enabled.
Host/network firewalls not blocking SMB ports between source and destination.
Use of domain account in administrator group on remote system or default system admin account. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1077](https://attack.mitre.org/techniques/T1077) |

# Windows Admin Shares (attack-pattern--ffe742ed-9100-4686-9e00-c331da544787)

## Description
Windows systems have hidden network shares that are accessible only to administrators and provide the ability for remote file copy and other administrative functions. Example network shares include <code>C$</code>, <code>ADMIN$</code>, and <code>IPC$</code>. 

Adversaries may use this technique in conjunction with administrator-level [Valid Accounts](https://attack.mitre.org/techniques/T1078) to remotely access a networked system over server message block (SMB) (Citation: Wikipedia SMB) to interact with systems using remote procedure calls (RPCs), (Citation: TechNet RPC) transfer files, and run transferred binaries through remote Execution. Example execution techniques that rely on authenticated sessions over SMB/RPC are [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), [Service Execution](https://attack.mitre.org/techniques/T1035), and [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047). Adversaries can also use NTLM hashes to access administrator shares on systems with [Pass the Hash](https://attack.mitre.org/techniques/T1075) and certain configuration and patch levels. (Citation: Microsoft Admin Shares)

The [Net](https://attack.mitre.org/software/S0039) utility can be used to connect to Windows admin shares on remote systems using <code>net use</code> commands with valid credentials. (Citation: Technet Net Use)

## Detection
Ensure that proper logging of accounts used to log into systems is turned on and centrally collected. Windows logging is able to collect success/failure for accounts that may be used to move laterally and can be collected using tools such as Windows Event Forwarding. (Citation: Lateral Movement Payne) (Citation: Windows Event Forwarding Payne) Monitor remote login events and associated SMB activity for file transfers and remote process execution. Monitor the actions of remote users who connect to administrative shares. Monitor for use of tools and commands to connect to remote shares, such as [Net](https://attack.mitre.org/software/S0039), on the command-line interface and Discovery techniques that could be used to find remotely accessible systems.(Citation: Medium Detecting Lateral Movement)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1077)
- [capec](https://capec.mitre.org/data/definitions/561.html)
- [Wikipedia SMB](https://en.wikipedia.org/wiki/Server_Message_Block)
- [TechNet RPC](https://technet.microsoft.com/en-us/library/cc787851.aspx)
- [Microsoft Admin Shares](http://support.microsoft.com/kb/314984)
- [Technet Net Use](https://technet.microsoft.com/bb490717.aspx)
- [Lateral Movement Payne](https://docs.microsoft.com/en-us/archive/blogs/jepayne/tracking-lateral-movement-part-one-special-groups-and-specific-service-accounts)
- [Windows Event Forwarding Payne](https://docs.microsoft.com/en-us/archive/blogs/jepayne/monitoring-what-matters-windows-event-forwarding-for-everyone-even-if-you-already-have-a-siem)
- [Medium Detecting Lateral Movement](https://medium.com/threatpunter/detecting-lateral-movement-using-sysmon-and-splunk-318d3be141bc)
