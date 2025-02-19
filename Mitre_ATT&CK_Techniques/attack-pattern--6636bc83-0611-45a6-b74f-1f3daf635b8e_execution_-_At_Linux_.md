---
id: attack-pattern--6636bc83-0611-45a6-b74f-1f3daf635b8e
mitre_attack_url: https://attack.mitre.org/techniques/T1053/001
name: At (Linux)
platforms:
- Linux
tactics:
- execution
- persistence
- privilege-escalation
title: execution - At (Linux)
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, persistence, privilege-escalation |
| **Platforms** | Linux |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1053/001](https://attack.mitre.org/techniques/T1053/001) |

# At (Linux) (attack-pattern--6636bc83-0611-45a6-b74f-1f3daf635b8e)

## Description
Adversaries may abuse the [at](https://attack.mitre.org/software/S0110) utility to perform task scheduling for initial, recurring, or future execution of malicious code. The [at](https://attack.mitre.org/software/S0110) command within Linux operating systems enables administrators to schedule tasks.(Citation: Kifarunix - Task Scheduling in Linux)

An adversary may use [at](https://attack.mitre.org/software/S0110) in Linux environments to execute programs at system startup or on a scheduled basis for persistence. [at](https://attack.mitre.org/software/S0110) can also be abused to conduct remote Execution as part of Lateral Movement and or to run a process under the context of a specified account.

Adversaries may also abuse [at](https://attack.mitre.org/software/S0110) to break out of restricted environments by using a task to spawn an interactive system shell or to run system commands. Similarly, [at](https://attack.mitre.org/software/S0110) may also be used for [Privilege Escalation](https://attack.mitre.org/tactics/TA0004) if the binary is allowed to run as superuser via <code>sudo</code>.(Citation: GTFObins at)

## Detection
Monitor scheduled task creation using command-line invocation. Legitimate scheduled tasks may be created during installation of new software or through system administration functions. Look for changes to tasks that do not correlate with known software, patch cycles, etc. 

Review all jobs using the <code>atq</code> command and ensure IP addresses stored in the <code>SSH_CONNECTION</code> and <code>SSH_CLIENT</code> variables, machines that created the jobs, are trusted hosts. All [at](https://attack.mitre.org/software/S0110) jobs are stored in <code>/var/spool/cron/atjobs/</code>.(Citation: rowland linux at 2019)

Suspicious program execution through scheduled tasks may show up as outlier processes that have not been seen before when compared against historical data. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1053/001)
- [rowland linux at 2019](https://www.linkedin.com/pulse/getting-attacker-ip-address-from-malicious-linux-job-craig-rowland/)
- [GTFObins at](https://gtfobins.github.io/gtfobins/at/)
- [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)
