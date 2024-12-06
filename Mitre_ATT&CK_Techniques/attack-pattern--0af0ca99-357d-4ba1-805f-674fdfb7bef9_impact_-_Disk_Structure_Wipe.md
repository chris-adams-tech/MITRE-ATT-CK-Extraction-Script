---
contributors:
  - Austin Clark, @c2defense
data_sources:
  - "Driver: Driver Load"
  - "Drive: Drive Modification"
  - "Drive: Drive Access"
  - "Command: Command Execution"
  - "Process: Process Creation"
id: attack-pattern--0af0ca99-357d-4ba1-805f-674fdfb7bef9
mitre_attack_url: https://attack.mitre.org/techniques/T1561/002
name: Disk Structure Wipe
platforms:
  - Linux
  - macOS
  - Windows
  - Network
tactics:
  - impact
title: T1561.002 - impact - Disk Structure Wipe
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Driver: Driver Load, Drive: Drive Modification, Drive: Drive Access, Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1561/002](https://attack.mitre.org/techniques/T1561/002) |

# Disk Structure Wipe (attack-pattern--0af0ca99-357d-4ba1-805f-674fdfb7bef9)

## Description
Adversaries may corrupt or wipe the disk data structures on a hard drive necessary to boot a system; targeting specific critical systems or in large numbers in a network to interrupt availability to system and network resources. 

Adversaries may attempt to render the system unable to boot by overwriting critical data located in structures such as the master boot record (MBR) or partition table.(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) The data contained in disk structures may include the initial executable code for loading an operating system or the location of the file system partitions on disk. If this information is not present, the computer will not be able to load an operating system during the boot process, leaving the computer unavailable. [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002) may be performed in isolation, or along with [Disk Content Wipe](https://attack.mitre.org/techniques/T1561/001) if all sectors of a disk are wiped.

On a network devices, adversaries may reformat the file system using [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `format`.(Citation: format_cmd_cisco)

To maximize impact on the target organization, malware designed for destroying disk structures may have worm-like features to propagate across a network by leveraging other techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)

## Detection
Look for attempts to read/write to sensitive locations like the master boot record and the disk partition table. Monitor for direct access read/write attempts using the <code>\\\\.\\</code> notation.(Citation: Microsoft Sysmon v6 May 2017) Monitor for unusual kernel driver installation activity.

For network infrastructure devices, collect AAA logging to monitor for `format` commands being run to erase the file structure and prevent recovery of the device.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1561/002)
- [format_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/F_through_K.html#wp2829794668)
- [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
- [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [FireEye Shamoon Nov 2016](https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)
- [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Microsoft Sysmon v6 May 2017](https://docs.microsoft.com/sysinternals/downloads/sysmon)
- [Symantec Shamoon 2012](https://www.symantec.com/connect/blogs/shamoon-attacks)
