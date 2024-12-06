---
contributors:
- Prasanth Sadanala, Cigna Information Protection (CIP) - Threat Response Engineering
  Team
- Lucas Heiligenstein
data_sources:
- 'Sensor Health: Host Status'
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Modification'
- 'Script: Script Execution'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Creation'
- 'Application Log: Application Log Content'
id: attack-pattern--4eb28bed-d11a-4641-9863-c2ac017d910a
mitre_attack_url: https://attack.mitre.org/techniques/T1562/002
name: Disable Windows Event Logging
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Disable Windows Event Logging
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Sensor Health: Host Status, Command: Command Execution, Windows Registry: Windows Registry Key Modification, Script: Script Execution, Process: Process Creation, Windows Registry: Windows Registry Key Creation, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/002](https://attack.mitre.org/techniques/T1562/002) |

# Disable Windows Event Logging (attack-pattern--4eb28bed-d11a-4641-9863-c2ac017d910a)

## Description
Adversaries may disable Windows event logging to limit data that can be leveraged for detections and audits. Windows event logs record user and system activity such as login attempts, process creation, and much more.(Citation: Windows Log Events) This data is used by security tools and analysts to generate detections.

The EventLog service maintains event logs from various system components and applications.(Citation: EventLog_Core_Technologies) By default, the service automatically starts when a system powers on. An audit policy, maintained by the Local Security Policy (secpol.msc), defines which system events the EventLog service logs. Security audit policy settings can be changed by running secpol.msc, then navigating to <code>Security Settings\Local Policies\Audit Policy</code> for basic audit policy settings or <code>Security Settings\Advanced Audit Policy Configuration</code> for advanced audit policy settings.(Citation: Audit_Policy_Microsoft)(Citation: Advanced_sec_audit_policy_settings) <code>auditpol.exe</code> may also be used to set audit policies.(Citation: auditpol)

Adversaries may target system-wide logging or just that of a particular application. For example, the Windows EventLog service may be disabled using the <code>Set-Service -Name EventLog -Status Stopped</code> or <code>sc config eventlog start=disabled</code> commands (followed by manually stopping the service using <code>Stop-Service  -Name EventLog</code>).(Citation: Disable_Win_Event_Logging)(Citation: disable_win_evt_logging) Additionally, the service may be disabled by modifying the “Start” value in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog</code> then restarting the system for the change to take effect.(Citation: disable_win_evt_logging)

There are several ways to disable the EventLog service via registry key modification. First, without Administrator privileges, adversaries may modify the "Start" value in the key <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Security</code>, then reboot the system to disable the Security EventLog.(Citation: winser19_file_overwrite_bug_twitter) Second, with Administrator privilege, adversaries may modify the same values in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-System</code> and <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Application</code> to disable the entire EventLog.(Citation: disable_win_evt_logging)

Additionally, adversaries may use <code>auditpol</code> and its sub-commands in a command prompt to disable auditing or clear the audit policy. To enable or disable a specified setting or audit category, adversaries may use the <code>/success</code> or <code>/failure</code> parameters. For example, <code>auditpol /set /category:”Account Logon” /success:disable /failure:disable</code> turns off auditing for the Account Logon category.(Citation: auditpol.exe_STRONTIC)(Citation: T1562.002_redcanaryco) To clear the audit policy, adversaries may run the following lines: <code>auditpol /clear /y</code> or <code>auditpol /remove /allusers</code>.(Citation: T1562.002_redcanaryco)

By disabling Windows event logging, adversaries can operate while leaving less evidence of a compromise behind.

## Detection
Monitor processes and command-line arguments for commands that can be used to disable logging. For example, [Wevtutil](https://attack.mitre.org/software/S0645), `auditpol`, `sc stop EventLog`, and offensive tooling (such as [Mimikatz](https://attack.mitre.org/software/S0002) and `Invoke-Phant0m`) may be used to clear logs.(Citation: def_ev_win_event_logging)(Citation: evt_log_tampering)  

In Event Viewer, Event ID 1102 under the “Security” Windows Log and Event ID 104 under the “System” Windows Log both indicate logs have been cleared.(Citation: def_ev_win_event_logging) `Service Control Manager Event ID 7035` in Event Viewer may indicate the termination of the EventLog service.(Citation: evt_log_tampering) Additionally, gaps in the logs, e.g. non-sequential Event Record IDs, may indicate that the logs may have been tampered.

Monitor the addition of the MiniNT registry key in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`, which may disable Event Viewer.(Citation: def_ev_win_event_logging)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/002)
- [Disable_Win_Event_Logging](https://dmcxblue.gitbook.io/red-team-notes-2-0/red-team-techniques/defense-evasion/t1562-impair-defenses/disable-windows-event-logging)
- [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)
- [EventLog_Core_Technologies](https://www.coretechnologies.com/blog/windows-services/eventlog/)
- [Audit_Policy_Microsoft](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/audit-policy)
- [Windows Log Events](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/)
- [disable_win_evt_logging](https://ptylu.github.io/content/report/report.html?report=25)
- [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
- [winser19_file_overwrite_bug_twitter](https://web.archive.org/web/20211107115646/https://twitter.com/klinix5/status/1457316029114327040)
- [T1562.002_redcanaryco](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.md)
- [Advanced_sec_audit_policy_settings](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
- [auditpol.exe_STRONTIC](https://strontic.github.io/xcyclopedia/library/auditpol.exe-214E0EA1F7F7C27C82D23F183F9D23F1.html)
- [evt_log_tampering](https://svch0st.medium.com/event-log-tampering-part-1-disrupting-the-eventlog-service-8d4b7d67335c)
