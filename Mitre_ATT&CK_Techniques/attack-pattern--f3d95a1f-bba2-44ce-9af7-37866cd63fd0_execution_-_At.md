---
data_sources:
- 'Command: Command Execution'
- 'Scheduled Job: Scheduled Job Creation'
- 'Network Traffic: Network Traffic Flow'
- 'Process: Process Creation'
- 'File: File Modification'
id: attack-pattern--f3d95a1f-bba2-44ce-9af7-37866cd63fd0
mitre_attack_url: https://attack.mitre.org/techniques/T1053/002
name: At
platforms:
- Windows
- Linux
- macOS
tactics:
- execution
- persistence
- privilege-escalation
title: execution - At
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, persistence, privilege-escalation |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Command: Command Execution, Scheduled Job: Scheduled Job Creation, Network Traffic: Network Traffic Flow, Process: Process Creation, File: File Modification |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1053/002](https://attack.mitre.org/techniques/T1053/002) |

# At (attack-pattern--f3d95a1f-bba2-44ce-9af7-37866cd63fd0)

## Description
Adversaries may abuse the [at](https://attack.mitre.org/software/S0110) utility to perform task scheduling for initial or recurring execution of malicious code. The [at](https://attack.mitre.org/software/S0110) utility exists as an executable within Windows, Linux, and macOS for scheduling tasks at a specified time and date. Although deprecated in favor of [Scheduled Task](https://attack.mitre.org/techniques/T1053/005)'s [schtasks](https://attack.mitre.org/software/S0111) in Windows environments, using [at](https://attack.mitre.org/software/S0110) requires that the Task Scheduler service be running, and the user to be logged on as a member of the local Administrators group. In addition to explicitly running the `at` command, adversaries may also schedule a task with [at](https://attack.mitre.org/software/S0110) by directly leveraging the [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) `Win32_ScheduledJob` WMI class.(Citation: Malicious Life by Cybereason)

On Linux and macOS, [at](https://attack.mitre.org/software/S0110) may be invoked by the superuser as well as any users added to the <code>at.allow</code> file. If the <code>at.allow</code> file does not exist, the <code>at.deny</code> file is checked. Every username not listed in <code>at.deny</code> is allowed to invoke [at](https://attack.mitre.org/software/S0110). If the <code>at.deny</code> exists and is empty, global use of [at](https://attack.mitre.org/software/S0110) is permitted. If neither file exists (which is often the baseline) only the superuser is allowed to use [at](https://attack.mitre.org/software/S0110).(Citation: Linux at)

Adversaries may use [at](https://attack.mitre.org/software/S0110) to execute programs at system startup or on a scheduled basis for [Persistence](https://attack.mitre.org/tactics/TA0003). [at](https://attack.mitre.org/software/S0110) can also be abused to conduct remote [Execution](https://attack.mitre.org/tactics/TA0002) as part of [Lateral Movement](https://attack.mitre.org/tactics/TA0008) and/or to run a process under the context of a specified account (such as SYSTEM).

In Linux environments, adversaries may also abuse [at](https://attack.mitre.org/software/S0110) to break out of restricted environments by using a task to spawn an interactive system shell or to run system commands. Similarly, [at](https://attack.mitre.org/software/S0110) may also be used for [Privilege Escalation](https://attack.mitre.org/tactics/TA0004) if the binary is allowed to run as superuser via <code>sudo</code>.(Citation: GTFObins at)

## Detection
Monitor process execution from the svchost.exe in Windows 10 and the Windows Task Scheduler taskeng.exe for older versions of Windows. (Citation: Twitter Leoloobeek Scheduled Task) If scheduled tasks are not used for persistence, then the adversary is likely to remove the task when the action is complete. Monitor Windows Task Scheduler stores in %systemroot%\System32\Tasks for change entries related to scheduled tasks that do not correlate with known software, patch cycles, etc.

Configure event logging for scheduled task creation and changes by enabling the "Microsoft-Windows-TaskScheduler/Operational" setting within the event logging service. (Citation: TechNet Forum Scheduled Task Operational Setting) Several events will then be logged on scheduled task activity, including: (Citation: TechNet Scheduled Task Events)(Citation: Microsoft Scheduled Task Events Win10)

* Event ID 106 on Windows 7, Server 2008 R2 - Scheduled task registered
* Event ID 140 on Windows 7, Server 2008 R2 / 4702 on Windows 10, Server 2016 - Scheduled task updated
* Event ID 141 on Windows 7, Server 2008 R2 / 4699 on Windows 10, Server 2016 - Scheduled task deleted
* Event ID 4698 on Windows 10, Server 2016 - Scheduled task created
* Event ID 4700 on Windows 10, Server 2016 - Scheduled task enabled
* Event ID 4701 on Windows 10, Server 2016 - Scheduled task disabled

Tools such as Sysinternals Autoruns may also be used to detect system changes that could be attempts at persistence, including listing current scheduled tasks. (Citation: TechNet Autoruns)

Remote access tools with built-in features may interact directly with the Windows API to perform these functions outside of typical system utilities. Tasks may also be created through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001), so additional logging may need to be configured to gather the appropriate data.

In Linux and macOS environments, monitor scheduled task creation using command-line invocation. Legitimate scheduled tasks may be created during installation of new software or through system administration functions. Look for changes to tasks that do not correlate with known software, patch cycles, etc. 

Review all jobs using the <code>atq</code> command and ensure IP addresses stored in the <code>SSH_CONNECTION</code> and <code>SSH_CLIENT</code> variables, machines that created the jobs, are trusted hosts. All [at](https://attack.mitre.org/software/S0110) jobs are stored in <code>/var/spool/cron/atjobs/</code>.(Citation: rowland linux at 2019)

Suspicious program execution through scheduled tasks may show up as outlier processes that have not been seen before when compared against historical data. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for [Command and Control](https://attack.mitre.org/tactics/TA0011), learning details about the environment through [Discovery](https://attack.mitre.org/tactics/TA0007), and [Lateral Movement](https://attack.mitre.org/tactics/TA0008).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1053/002)
- [rowland linux at 2019](https://www.linkedin.com/pulse/getting-attacker-ip-address-from-malicious-linux-job-craig-rowland/)
- [GTFObins at](https://gtfobins.github.io/gtfobins/at/)
- [Linux at](https://man7.org/linux/man-pages/man1/at.1p.html)
- [Twitter Leoloobeek Scheduled Task](https://x.com/leoloobeek/status/939248813465853953)
- [Microsoft Scheduled Task Events Win10](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-object-access-events)
- [TechNet Scheduled Task Events](https://technet.microsoft.com/library/dd315590.aspx)
- [Malicious Life by Cybereason](https://www.cybereason.com/blog/wmi-lateral-movement-win32#blog-subscribe)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
- [TechNet Forum Scheduled Task Operational Setting](https://social.technet.microsoft.com/Forums/en-US/e5bca729-52e7-4fcb-ba12-3225c564674c/scheduled-tasks-history-retention-settings?forum=winserver8gen)
