---
contributors:
- Austin Clark, @c2defense
data_sources:
- 'Driver: Driver Load'
- 'Drive: Drive Access'
- 'Command: Command Execution'
- 'Drive: Drive Modification'
- 'Process: Process Creation'
id: attack-pattern--1988cc35-ced8-4dad-b2d1-7628488fa967
mitre_attack_url: https://attack.mitre.org/techniques/T1561
name: Disk Wipe
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- impact
title: impact - Disk Wipe
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Driver: Driver Load, Drive: Drive Access, Command: Command Execution, Drive: Drive Modification, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1561](https://attack.mitre.org/techniques/T1561) |

# Disk Wipe (attack-pattern--1988cc35-ced8-4dad-b2d1-7628488fa967)

## Description
Adversaries may wipe or corrupt raw disk data on specific systems or in large numbers in a network to interrupt availability to system and network resources. With direct write access to a disk, adversaries may attempt to overwrite portions of disk data. Adversaries may opt to wipe arbitrary portions of disk data and/or wipe disk structures like the master boot record (MBR). A complete wipe of all disk sectors may be attempted.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disks may have worm-like features to propagate across a network by leveraging additional techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Novetta Blockbuster Destructive Malware)

On network devices, adversaries may wipe configuration files and other data from the device using [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `erase`.(Citation: erase_cmd_cisco)

## Detection
Look for attempts to read/write to sensitive locations like the partition boot sector, master boot record, disk partition table, or BIOS parameter block/superblock. Monitor for direct access read/write attempts using the <code>\\\\.\\</code> notation.(Citation: Microsoft Sysmon v6 May 2017) Monitor for unusual kernel driver installation activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1561)
- [erase_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/D_through_E.html#wp3557227463)
- [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [Microsoft Sysmon v6 May 2017](https://docs.microsoft.com/sysinternals/downloads/sysmon)
