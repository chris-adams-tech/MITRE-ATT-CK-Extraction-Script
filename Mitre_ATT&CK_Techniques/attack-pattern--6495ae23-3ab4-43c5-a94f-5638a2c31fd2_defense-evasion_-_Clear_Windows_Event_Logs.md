---
contributors:
- Lucas Heiligenstein
data_sources:
- 'Command: Command Execution'
- 'File: File Deletion'
- 'Process: OS API Execution'
- 'Process: Process Creation'
id: attack-pattern--6495ae23-3ab4-43c5-a94f-5638a2c31fd2
mitre_attack_url: https://attack.mitre.org/techniques/T1070/001
name: Clear Windows Event Logs
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Clear Windows Event Logs
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, File: File Deletion, Process: OS API Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1070/001](https://attack.mitre.org/techniques/T1070/001) |

# Clear Windows Event Logs (attack-pattern--6495ae23-3ab4-43c5-a94f-5638a2c31fd2)

## Description
Adversaries may clear Windows Event Logs to hide the activity of an intrusion. Windows Event Logs are a record of a computer's alerts and notifications. There are three system-defined sources of events: System, Application, and Security, with five event types: Error, Warning, Information, Success Audit, and Failure Audit.


With administrator privileges, the event logs can be cleared with the following utility commands:

* <code>wevtutil cl system</code>
* <code>wevtutil cl application</code>
* <code>wevtutil cl security</code>

These logs may also be cleared through other mechanisms, such as the event viewer GUI or [PowerShell](https://attack.mitre.org/techniques/T1059/001). For example, adversaries may use the PowerShell command <code>Remove-EventLog -LogName Security</code> to delete the Security EventLog and after reboot, disable future logging.  Note: events may still be generated and logged in the .evtx file between the time the command is run and the reboot.(Citation: disable_win_evt_logging)

Adversaries may also attempt to clear logs by directly deleting the stored log files within `C:\Windows\System32\winevt\logs\`.

## Detection
Deleting Windows event logs (via native binaries (Citation: Microsoft wevtutil Oct 2017), API functions (Citation: Microsoft EventLog.Clear), or [PowerShell](https://attack.mitre.org/techniques/T1059/001) (Citation: Microsoft Clear-EventLog)) may also generate an alterable event (Event ID 1102: "The audit log was cleared").

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1070/001)
- [disable_win_evt_logging](https://ptylu.github.io/content/report/report.html?report=25)
- [Microsoft Clear-EventLog](https://docs.microsoft.com/powershell/module/microsoft.powershell.management/clear-eventlog)
- [Microsoft EventLog.Clear](https://msdn.microsoft.com/library/system.diagnostics.eventlog.clear.aspx)
- [Microsoft wevtutil Oct 2017](https://docs.microsoft.com/windows-server/administration/windows-commands/wevtutil)
