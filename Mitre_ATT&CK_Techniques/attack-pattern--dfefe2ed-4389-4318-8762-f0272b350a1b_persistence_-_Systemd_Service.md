---
contributors:
- Tony Lambert, Red Canary
- Emad Al-Mousa, Saudi Aramco
- Tim (Wadhwa-)Brown
data_sources:
- 'Command: Command Execution'
- 'File: File Modification'
- 'Service: Service Creation'
- 'Service: Service Modification'
- 'Process: Process Creation'
- 'File: File Creation'
id: attack-pattern--dfefe2ed-4389-4318-8762-f0272b350a1b
mitre_attack_url: https://attack.mitre.org/techniques/T1543/002
name: Systemd Service
platforms:
- Linux
tactics:
- persistence
- privilege-escalation
title: persistence - Systemd Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Linux |
| **Data Sources** | Command: Command Execution, File: File Modification, Service: Service Creation, Service: Service Modification, Process: Process Creation, File: File Creation |
| **Permissions Required** | User, root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1543/002](https://attack.mitre.org/techniques/T1543/002) |

# Systemd Service (attack-pattern--dfefe2ed-4389-4318-8762-f0272b350a1b)

## Description
Adversaries may create or modify systemd services to repeatedly execute malicious payloads as part of persistence. Systemd is a system and service manager commonly used for managing background daemon processes (also known as services) and other system resources.(Citation: Linux man-pages: systemd January 2014) Systemd is the default initialization (init) system on many Linux distributions replacing legacy init systems, including SysVinit and Upstart, while remaining backwards compatible.  

Systemd utilizes unit configuration files with the `.service` file extension to encode information about a service's process. By default, system level unit files are stored in the `/systemd/system` directory of the root owned directories (`/`). User level unit files are stored in the `/systemd/user` directories of the user owned directories (`$HOME`).(Citation: lambert systemd 2022) 

Inside the `.service` unit files, the following directives are used to execute commands:(Citation: freedesktop systemd.service)  

* `ExecStart`, `ExecStartPre`, and `ExecStartPost` directives execute when a service is started manually by `systemctl` or on system start if the service is set to automatically start.
* `ExecReload` directive executes when a service restarts. 
* `ExecStop`, `ExecStopPre`, and `ExecStopPost` directives execute when a service is stopped.  

Adversaries have created new service files, altered the commands a `.service` file’s directive executes, and modified the user directive a `.service` file executes as, which could result in privilege escalation. Adversaries may also place symbolic links in these directories, enabling systemd to find these payloads regardless of where they reside on the filesystem.(Citation: Anomali Rocke March 2019)(Citation: airwalk backdoor unix systems)(Citation: Rapid7 Service Persistence 22JUNE2016) 

The .service file’s User directive can be used to run service as a specific user, which could result in privilege escalation based on specific user/group permissions. 

## Detection
Monitor file creation and modification events of Systemd service unit configuration files in the default directory locations for `root` & `user` level permissions. Suspicious processes or scripts spawned in this manner will have a parent process of ‘systemd’, a parent process ID of 1, and will usually execute as the `root` user.(Citation: lambert systemd 2022) 

Suspicious systemd services can also be identified by comparing results against a trusted system baseline. Malicious systemd services may be detected by using the systemctl utility to examine system wide services: `systemctl list-units -–type=service –all`. Analyze the contents of `.service` files present on the file system and ensure that they refer to legitimate, expected executables, and symbolic links.(Citation: Berba hunting linux systemd)

Auditing the execution and command-line arguments of the `systemctl` utility, as well related utilities such as `/usr/sbin/service` may reveal malicious systemd service execution.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1543/002)
- [airwalk backdoor unix systems](http://www.ouah.org/backdoors.html)
- [Anomali Rocke March 2019](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [freedesktop systemd.service](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
- [Linux man-pages: systemd January 2014](http://man7.org/linux/man-pages/man1/systemd.1.html)
- [Berba hunting linux systemd](https://pberba.github.io/security/2022/01/30/linux-threat-hunting-for-persistence-systemd-timers-cron/)
- [Rapid7 Service Persistence 22JUNE2016](https://www.rapid7.com/db/modules/exploit/linux/local/service_persistence)
- [lambert systemd 2022](https://redcanary.com/blog/attck-t1501-understanding-systemd-service-persistence/)
