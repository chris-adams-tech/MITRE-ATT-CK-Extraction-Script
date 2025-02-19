---
data_sources:
- 'Drive: Drive Modification'
- 'Drive: Drive Access'
- 'Driver: Driver Load'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--fb640c43-aa6b-431e-a961-a279010424ac
mitre_attack_url: https://attack.mitre.org/techniques/T1561/001
name: Disk Content Wipe
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- impact
title: impact - Disk Content Wipe
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Drive: Drive Modification, Drive: Drive Access, Driver: Driver Load, Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1561/001](https://attack.mitre.org/techniques/T1561/001) |

# Disk Content Wipe (attack-pattern--fb640c43-aa6b-431e-a961-a279010424ac)

## Description
Adversaries may erase the contents of storage devices on specific systems or in large numbers in a network to interrupt availability to system and network resources.

Adversaries may partially or completely overwrite the contents of a storage device rendering the data irrecoverable through the storage interface.(Citation: Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware)(Citation: DOJ Lazarus Sony 2018) Instead of wiping specific disk structures or files, adversaries with destructive intent may wipe arbitrary portions of disk content. To wipe disk content, adversaries may acquire direct access to the hard drive in order to overwrite arbitrarily sized portions of disk with random data.(Citation: Novetta Blockbuster Destructive Malware) Adversaries have also been observed leveraging third-party drivers like [RawDisk](https://attack.mitre.org/software/S0364) to directly access disk content.(Citation: Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware) This behavior is distinct from [Data Destruction](https://attack.mitre.org/techniques/T1485) because sections of the disk are erased instead of individual files.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disk content may have worm-like features to propagate across a network by leveraging additional techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Novetta Blockbuster Destructive Malware)

## Detection
Look for attempts to read/write to sensitive locations like the partition boot sector or BIOS parameter block/superblock. Monitor for direct access read/write attempts using the <code>\\\\.\\</code> notation.(Citation: Microsoft Sysmon v6 May 2017) Monitor for unusual kernel driver installation activity.

For network infrastructure devices, collect AAA logging to monitor for `erase` commands that delete critical configuration files.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1561/001)
- [DOJ Lazarus Sony 2018](https://www.justice.gov/opa/press-release/file/1092091/download)
- [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Microsoft Sysmon v6 May 2017](https://docs.microsoft.com/sysinternals/downloads/sysmon)
