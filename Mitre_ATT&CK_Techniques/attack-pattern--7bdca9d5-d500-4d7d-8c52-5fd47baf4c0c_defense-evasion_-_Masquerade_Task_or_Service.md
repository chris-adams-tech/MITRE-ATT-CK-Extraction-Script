---
data_sources:
- 'Scheduled Job: Scheduled Job Modification'
- 'Service: Service Creation'
- 'Command: Command Execution'
- 'Service: Service Metadata'
- 'Scheduled Job: Scheduled Job Metadata'
id: attack-pattern--7bdca9d5-d500-4d7d-8c52-5fd47baf4c0c
mitre_attack_url: https://attack.mitre.org/techniques/T1036/004
name: Masquerade Task or Service
platforms:
- Windows
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - Masquerade Task or Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Scheduled Job: Scheduled Job Modification, Service: Service Creation, Command: Command Execution, Service: Service Metadata, Scheduled Job: Scheduled Job Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/004](https://attack.mitre.org/techniques/T1036/004) |

# Masquerade Task or Service (attack-pattern--7bdca9d5-d500-4d7d-8c52-5fd47baf4c0c)

## Description
Adversaries may attempt to manipulate the name of a task or service to make it appear legitimate or benign. Tasks/services executed by the Task Scheduler or systemd will typically be given a name and/or description.(Citation: TechNet Schtasks)(Citation: Systemd Service Units) Windows services will have a service name as well as a display name. Many benign tasks and services exist that have commonly associated names. Adversaries may give tasks or services names that are similar or identical to those of legitimate ones.

Tasks or services contain other fields, such as a description, that adversaries may attempt to make appear legitimate.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Fysbis Dr Web Analysis)

## Detection
Look for changes to tasks and services that do not correlate with known software, patch cycles, etc. Suspicious program execution through scheduled tasks or services may show up as outlier processes that have not been seen before when compared against historical data. Monitor processes and command-line arguments for actions that could be taken to create tasks or services. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/004)
- [Fysbis Dr Web Analysis](https://vms.drweb.com/virus/?i=4276269)
- [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Systemd Service Units](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
- [TechNet Schtasks](https://technet.microsoft.com/en-us/library/bb490996.aspx)
