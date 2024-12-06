---
contributors:
- SarathKumar Rajendran, Trimble Inc
data_sources:
- 'File: File Modification'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Scheduled Job: Scheduled Job Creation'
id: attack-pattern--a542bac9-7bc1-4da7-9a09-96f69e23cc21
mitre_attack_url: https://attack.mitre.org/techniques/T1053/006
name: Systemd Timers
platforms:
- Linux
tactics:
- execution
- persistence
- privilege-escalation
title: execution - Systemd Timers
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, persistence, privilege-escalation |
| **Platforms** | Linux |
| **Data Sources** | File: File Modification, Process: Process Creation, Command: Command Execution, Scheduled Job: Scheduled Job Creation |
| **Permissions Required** | User, root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1053/006](https://attack.mitre.org/techniques/T1053/006) |

# Systemd Timers (attack-pattern--a542bac9-7bc1-4da7-9a09-96f69e23cc21)

## Description
Adversaries may abuse systemd timers to perform task scheduling for initial or recurring execution of malicious code. Systemd timers are unit files with file extension <code>.timer</code> that control services. Timers can be set to run on a calendar event or after a time span relative to a starting point. They can be used as an alternative to [Cron](https://attack.mitre.org/techniques/T1053/003) in Linux environments.(Citation: archlinux Systemd Timers Aug 2020) Systemd timers may be activated remotely via the <code>systemctl</code> command line utility, which operates over [SSH](https://attack.mitre.org/techniques/T1021/004).(Citation: Systemd Remote Control)

Each <code>.timer</code> file must have a corresponding <code>.service</code> file with the same name, e.g., <code>example.timer</code> and <code>example.service</code>. <code>.service</code> files are [Systemd Service](https://attack.mitre.org/techniques/T1543/002) unit files that are managed by the systemd system and service manager.(Citation: Linux man-pages: systemd January 2014) Privileged timers are written to <code>/etc/systemd/system/</code> and <code>/usr/lib/systemd/system</code> while user level are written to <code>~/.config/systemd/user/</code>.

An adversary may use systemd timers to execute malicious code at system startup or on a scheduled basis for persistence.(Citation: Arch Linux Package Systemd Compromise BleepingComputer 10JUL2018)(Citation: gist Arch package compromise 10JUL2018)(Citation: acroread package compromised Arch Linux Mail 8JUL2018) Timers installed using privileged paths may be used to maintain root level persistence. Adversaries may also install user level timers to achieve user level persistence.(Citation: Falcon Sandbox smp: 28553b3a9d)

## Detection
Systemd timer unit files may be detected by auditing file creation and modification events within the <code>/etc/systemd/system</code>, <code>/usr/lib/systemd/system/</code>, and <code>~/.config/systemd/user/</code> directories, as well as associated symbolic links. Suspicious processes or scripts spawned in this manner will have a parent process of ‘systemd’, a parent process ID of 1, and will usually execute as the ‘root’ user.

Suspicious systemd timers can also be identified by comparing results against a trusted system baseline. Malicious systemd timers may be detected by using the systemctl utility to examine system wide timers: <code>systemctl list-timers –all</code>. Analyze the contents of corresponding <code>.service</code> files present on the file system and ensure that they refer to legitimate, expected executables.

Audit the execution and command-line arguments of the 'systemd-run' utility as it may be used to create timers.(Citation: archlinux Systemd Timers Aug 2020)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1053/006)
- [Systemd Remote Control](https://www.tecmint.com/control-systemd-services-on-remote-linux-server/)
- [archlinux Systemd Timers Aug 2020](https://wiki.archlinux.org/index.php/Systemd/Timers)
- [gist Arch package compromise 10JUL2018](https://gist.github.com/campuscodi/74d0d2e35d8fd9499c76333ce027345a)
- [Arch Linux Package Systemd Compromise BleepingComputer 10JUL2018](https://www.bleepingcomputer.com/news/security/malware-found-in-arch-linux-aur-package-repository/)
- [acroread package compromised Arch Linux Mail 8JUL2018](https://lists.archlinux.org/pipermail/aur-general/2018-July/034153.html)
- [Falcon Sandbox smp: 28553b3a9d](https://www.hybrid-analysis.com/sample/28553b3a9d2ad4361d33d29ac4bf771d008e0073cec01b5561c6348a608f8dd7?environmentId=300)
- [Linux man-pages: systemd January 2014](http://man7.org/linux/man-pages/man1/systemd.1.html)
