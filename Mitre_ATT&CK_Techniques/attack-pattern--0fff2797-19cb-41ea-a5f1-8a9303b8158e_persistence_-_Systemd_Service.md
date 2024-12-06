---
contributors:
- Tony Lambert, Red Canary
id: attack-pattern--0fff2797-19cb-41ea-a5f1-8a9303b8158e
mitre_attack_url: https://attack.mitre.org/techniques/T1501
name: Systemd Service
platforms:
- Linux
tactics:
- persistence
title: persistence - Systemd Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Linux |
| **Permissions Required** | root, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1501](https://attack.mitre.org/techniques/T1501) |

# Systemd Service (attack-pattern--0fff2797-19cb-41ea-a5f1-8a9303b8158e)

## Description
Systemd services can be used to establish persistence on a Linux system. The systemd service manager is commonly used for managing background daemon processes (also known as services) and other system resources.(Citation: Linux man-pages: systemd January 2014)(Citation: Freedesktop.org Linux systemd 29SEP2018) Systemd is the default initialization (init) system on many Linux distributions starting with Debian 8, Ubuntu 15.04, CentOS 7, RHEL 7, Fedora 15, and replaces legacy init systems including SysVinit and Upstart while remaining backwards compatible with the aforementioned init systems.

Systemd utilizes configuration files known as service units to control how services boot and under what conditions. By default, these unit files are stored in the <code>/etc/systemd/system</code> and <code>/usr/lib/systemd/system</code> directories and have the file extension <code>.service</code>. Each service unit file may contain numerous directives that can execute system commands. 

* ExecStart, ExecStartPre, and ExecStartPost directives cover execution of commands when a services is started manually by 'systemctl' or on system start if the service is set to automatically start. 
* ExecReload directive covers when a service restarts. 
* ExecStop and ExecStopPost directives cover when a service is stopped or manually by 'systemctl'.

Adversaries have used systemd functionality to establish persistent access to victim systems by creating and/or modifying service unit files that cause systemd to execute malicious commands at recurring intervals, such as at system boot.(Citation: Anomali Rocke March 2019)(Citation: gist Arch package compromise 10JUL2018)(Citation: Arch Linux Package Systemd Compromise BleepingComputer 10JUL2018)(Citation: acroread package compromised Arch Linux Mail 8JUL2018)

While adversaries typically require root privileges to create/modify service unit files in the <code>/etc/systemd/system</code> and <code>/usr/lib/systemd/system</code> directories, low privilege users can create/modify service unit files in directories such as <code>~/.config/systemd/user/</code> to achieve user-level persistence.(Citation: Rapid7 Service Persistence 22JUNE2016)

## Detection
Systemd service unit files may be detected by auditing file creation and modification events within the <code>/etc/systemd/system</code>, <code>/usr/lib/systemd/system/</code>, and <code>/home/<username>/.config/systemd/user/</code> directories, as well as associated symbolic links. Suspicious processes or scripts spawned in this manner will have a parent process of ‘systemd’, a parent process ID of 1, and will usually execute as the ‘root’ user.

Suspicious systemd services can also be identified by comparing results against a trusted system baseline. Malicious systemd services may be detected by using the systemctl utility to examine system wide services: <code>systemctl list-units -–type=service –all</code>. Analyze the contents of <code>.service</code> files present on the file system and ensure that they refer to legitimate, expected executables.

Auditing the execution and command-line arguments of the 'systemctl' utility, as well related utilities such as <code>/usr/sbin/service</code> may reveal malicious systemd service execution.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1501)
- [Linux man-pages: systemd January 2014](http://man7.org/linux/man-pages/man1/systemd.1.html)
- [Freedesktop.org Linux systemd 29SEP2018](https://www.freedesktop.org/wiki/Software/systemd/)
- [Anomali Rocke March 2019](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [gist Arch package compromise 10JUL2018](https://gist.github.com/campuscodi/74d0d2e35d8fd9499c76333ce027345a)
- [Arch Linux Package Systemd Compromise BleepingComputer 10JUL2018](https://www.bleepingcomputer.com/news/security/malware-found-in-arch-linux-aur-package-repository/)
- [acroread package compromised Arch Linux Mail 8JUL2018](https://lists.archlinux.org/pipermail/aur-general/2018-July/034153.html)
- [Rapid7 Service Persistence 22JUNE2016](https://www.rapid7.com/db/modules/exploit/linux/local/service_persistence)
