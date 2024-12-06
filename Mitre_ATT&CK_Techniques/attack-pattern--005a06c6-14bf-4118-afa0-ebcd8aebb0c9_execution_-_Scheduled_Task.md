---
contributors:
- Andrew Northern, @ex_raritas
- Bryan Campbell, @bry_campbell
- Zachary Abzug, @ZackDoesML
- Selena Larson, @selenalarson
- Sittikorn Sangrattanapitak
data_sources:
- 'Windows Registry: Windows Registry Key Creation'
- 'File: File Modification'
- 'File: File Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Network Traffic: Network Traffic Flow'
- 'Scheduled Job: Scheduled Job Creation'
id: attack-pattern--005a06c6-14bf-4118-afa0-ebcd8aebb0c9
mitre_attack_url: https://attack.mitre.org/techniques/T1053/005
name: Scheduled Task
platforms:
- Windows
tactics:
- execution
- persistence
- privilege-escalation
title: execution - Scheduled Task
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Creation, File: File Modification, File: File Creation, Process: Process Creation, Command: Command Execution, Network Traffic: Network Traffic Flow, Scheduled Job: Scheduled Job Creation |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1053/005](https://attack.mitre.org/techniques/T1053/005) |

# Scheduled Task (attack-pattern--005a06c6-14bf-4118-afa0-ebcd8aebb0c9)

## Description
Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution of malicious code. There are multiple ways to access the Task Scheduler in Windows. The [schtasks](https://attack.mitre.org/software/S0111) utility can be run directly on the command line, or the Task Scheduler can be opened through the GUI within the Administrator Tools section of the Control Panel.(Citation: Stack Overflow) In some cases, adversaries have used a .NET wrapper for the Windows Task Scheduler, and alternatively, adversaries have used the Windows netapi32 library and [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) (WMI) to create a scheduled task. Adversaries may also utilize the Powershell Cmdlet `Invoke-CimMethod`, which leverages WMI class `PS_ScheduledTask` to create a scheduled task via an XML path.(Citation: Red Canary - Atomic Red Team)

An adversary may use Windows Task Scheduler to execute programs at system startup or on a scheduled basis for persistence. The Windows Task Scheduler can also be abused to conduct remote Execution as part of Lateral Movement and/or to run a process under the context of a specified account (such as SYSTEM). Similar to [System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218), adversaries have also abused the Windows Task Scheduler to potentially mask one-time execution under signed/trusted system processes.(Citation: ProofPoint Serpent)

Adversaries may also create "hidden" scheduled tasks (i.e. [Hide Artifacts](https://attack.mitre.org/techniques/T1564)) that may not be visible to defender tools and manual queries used to enumerate tasks. Specifically, an adversary may hide a task from `schtasks /query` and the Task Scheduler by deleting the associated Security Descriptor (SD) registry value (where deletion of this value must be completed using SYSTEM permissions).(Citation: SigmaHQ)(Citation: Tarrask scheduled task) Adversaries may also employ alternate methods to hide tasks, such as altering the metadata (e.g., `Index` value) within associated registry keys.(Citation: Defending Against Scheduled Task Attacks in Windows Environments) 

## Detection
Monitor process execution from the <code>svchost.exe</code> in Windows 10 and the Windows Task Scheduler <code>taskeng.exe</code> for older versions of Windows. (Citation: Twitter Leoloobeek Scheduled Task) If scheduled tasks are not used for persistence, then the adversary is likely to remove the task when the action is complete. Monitor Windows Task Scheduler stores in %systemroot%\System32\Tasks for change entries related to scheduled tasks that do not correlate with known software, patch cycles, etc.

Configure event logging for scheduled task creation and changes by enabling the "Microsoft-Windows-TaskScheduler/Operational" setting within the event logging service. (Citation: TechNet Forum Scheduled Task Operational Setting) Several events will then be logged on scheduled task activity, including: (Citation: TechNet Scheduled Task Events)(Citation: Microsoft Scheduled Task Events Win10)

* Event ID 106 on Windows 7, Server 2008 R2 - Scheduled task registered
* Event ID 140 on Windows 7, Server 2008 R2 / 4702 on Windows 10, Server 2016 - Scheduled task updated
* Event ID 141 on Windows 7, Server 2008 R2 / 4699 on Windows 10, Server 2016 - Scheduled task deleted
* Event ID 4698 on Windows 10, Server 2016 - Scheduled task created
* Event ID 4700 on Windows 10, Server 2016 - Scheduled task enabled
* Event ID 4701 on Windows 10, Server 2016 - Scheduled task disabled

Tools such as Sysinternals Autoruns may also be used to detect system changes that could be attempts at persistence, including listing current scheduled tasks. (Citation: TechNet Autoruns)

Remote access tools with built-in features may interact directly with the Windows API to perform these functions outside of typical system utilities. Tasks may also be created through Windows system management tools such as Windows Management Instrumentation and PowerShell, so additional logging may need to be configured to gather the appropriate data.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1053/005)
- [ProofPoint Serpent](https://www.proofpoint.com/us/blog/threat-insight/serpent-no-swiping-new-backdoor-targets-french-entities-unique-attack-chain)
- [Defending Against Scheduled Task Attacks in Windows Environments](https://blog.qualys.com/vulnerabilities-threat-research/2022/06/20/defending-against-scheduled-task-attacks-in-windows-environments)
- [Twitter Leoloobeek Scheduled Task](https://x.com/leoloobeek/status/939248813465853953)
- [Tarrask scheduled task](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)
- [Microsoft Scheduled Task Events Win10](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-object-access-events)
- [TechNet Scheduled Task Events](https://technet.microsoft.com/library/dd315590.aspx)
- [Red Canary - Atomic Red Team](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.md)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
- [TechNet Forum Scheduled Task Operational Setting](https://social.technet.microsoft.com/Forums/en-US/e5bca729-52e7-4fcb-ba12-3225c564674c/scheduled-tasks-history-retention-settings?forum=winserver8gen)
- [SigmaHQ](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_schtasks_hide_task_via_sd_value_removal.yml)
- [Stack Overflow](https://stackoverflow.com/questions/2913816/how-to-find-the-location-of-the-scheduled-tasks-folder)
