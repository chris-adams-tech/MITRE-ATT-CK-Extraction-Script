---
contributors:
- Austin Clark, @c2defense
- Hubert Mank
data_sources:
- 'Process: Process Creation'
- 'Sensor Health: Host Status'
- 'Command: Command Execution'
id: attack-pattern--ff73aa03-0090-4464-83ac-f89e233c02bc
mitre_attack_url: https://attack.mitre.org/techniques/T1529
name: System Shutdown/Reboot
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- impact
title: impact - System Shutdown/Reboot
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Process: Process Creation, Sensor Health: Host Status, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1529](https://attack.mitre.org/techniques/T1529) |

# System Shutdown/Reboot (attack-pattern--ff73aa03-0090-4464-83ac-f89e233c02bc)

## Description
Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) (e.g. <code>reload</code>).(Citation: Microsoft Shutdown Oct 2017)(Citation: alert_TA18_106A)

Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery.

Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002) or [Inhibit System Recovery](https://attack.mitre.org/techniques/T1490), to hasten the intended effects on system availability.(Citation: Talos Nyetya June 2017)(Citation: Talos Olympic Destroyer 2018)

## Detection
Use process monitoring to monitor the execution and command line parameters of binaries involved in shutting down or rebooting systems. Windows event logs may also designate activity associated with a shutdown/reboot, ex. Event ID 1074 and 6006. Unexpected or unauthorized commands from network cli on network devices may also be associated with shutdown/reboot, e.g. the <code>reload</code> command.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1529)
- [Talos Nyetya June 2017](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)
- [alert_TA18_106A](https://www.cisa.gov/uscert/ncas/alerts/TA18-106A)
- [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Microsoft Shutdown Oct 2017](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown)
