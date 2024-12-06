---
contributors:
- Ivan Sinyakov
data_sources:
- 'File: File Creation'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'File: File Modification'
id: attack-pattern--9c45eaa3-8604-4780-8988-b5074dbb9ecd
mitre_attack_url: https://attack.mitre.org/techniques/T1546/014
name: Emond
platforms:
- macOS
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Emond
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | macOS |
| **Data Sources** | File: File Creation, Command: Command Execution, Process: Process Creation, File: File Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/014](https://attack.mitre.org/techniques/T1546/014) |

# Emond (attack-pattern--9c45eaa3-8604-4780-8988-b5074dbb9ecd)

## Description
Adversaries may gain persistence and elevate privileges by executing malicious content triggered by the Event Monitor Daemon (emond). Emond is a [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) that accepts events from various services, runs them through a simple rules engine, and takes action. The emond binary at <code>/sbin/emond</code> will load any rules from the <code>/etc/emond.d/rules/</code> directory and take action once an explicitly defined event takes place.

The rule files are in the plist format and define the name, event type, and action to take. Some examples of event types include system startup and user authentication. Examples of actions are to run a system command or send an email. The emond service will not launch if there is no file present in the QueueDirectories path <code>/private/var/db/emondClients</code>, specified in the [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) configuration file at<code>/System/Library/LaunchDaemons/com.apple.emond.plist</code>.(Citation: xorrior emond Jan 2018)(Citation: magnusviri emond Apr 2016)(Citation: sentinelone macos persist Jun 2019)

Adversaries may abuse this service by writing a rule to execute commands when a defined event occurs, such as system start up or user authentication.(Citation: xorrior emond Jan 2018)(Citation: magnusviri emond Apr 2016)(Citation: sentinelone macos persist Jun 2019) Adversaries may also be able to escalate privileges from administrator to root as the emond service is executed with root privileges by the [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) service.

## Detection
Monitor emond rules creation by checking for files created or modified in <code>/etc/emond.d/rules/</code> and <code>/private/var/db/emondClients</code>.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/014)
- [magnusviri emond Apr 2016](http://www.magnusviri.com/Mac/what-is-emond.html)
- [xorrior emond Jan 2018](https://www.xorrior.com/emond-persistence/)
- [sentinelone macos persist Jun 2019](https://www.sentinelone.com/blog/how-malware-persists-on-macos/)
