---
data_sources:
- 'Process: Process Creation'
- 'Logon Session: Logon Session Creation'
- 'Network Traffic: Network Connection Creation'
- 'Command: Command Execution'
- 'Network Traffic: Network Traffic Flow'
- 'Service: Service Metadata'
id: attack-pattern--60d0c01d-e2bf-49dd-a453-f8a9c9fa6f65
mitre_attack_url: https://attack.mitre.org/techniques/T1021/006
name: Windows Remote Management
platforms:
- Windows
tactics:
- lateral-movement
title: lateral-movement - Windows Remote Management
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Logon Session: Logon Session Creation, Network Traffic: Network Connection Creation, Command: Command Execution, Network Traffic: Network Traffic Flow, Service: Service Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1021/006](https://attack.mitre.org/techniques/T1021/006) |

# Windows Remote Management (attack-pattern--60d0c01d-e2bf-49dd-a453-f8a9c9fa6f65)

## Description
Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with remote systems using Windows Remote Management (WinRM). The adversary may then perform actions as the logged-on user.

WinRM is the name of both a Windows service and a protocol that allows a user to interact with a remote system (e.g., run an executable, modify the Registry, modify services).(Citation: Microsoft WinRM) It may be called with the `winrm` command or by any number of programs such as PowerShell.(Citation: Jacobsen 2014) WinRM  can be used as a method of remotely interacting with [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047).(Citation: MSDN WMI)

## Detection
Monitor use of WinRM within an environment by tracking service execution. If it is not normally used or is disabled, then this may be an indicator of suspicious behavior.  Monitor processes created and actions taken by the WinRM process or a WinRM invoked script to correlate it with other related events.(Citation: Medium Detecting Lateral Movement) Also monitor for remote WMI connection attempts (typically over port 5985 when using HTTP and 5986 for HTTPS).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1021/006)
- [Medium Detecting Lateral Movement](https://medium.com/threatpunter/detecting-lateral-movement-using-sysmon-and-splunk-318d3be141bc)
- [Jacobsen 2014](https://www.slideshare.net/kieranjacobsen/lateral-movement-with-power-shell-2)
- [MSDN WMI](https://msdn.microsoft.com/en-us/library/aa394582.aspx)
- [Microsoft WinRM](https://learn.microsoft.com/en-us/windows/win32/winrm/portal)
