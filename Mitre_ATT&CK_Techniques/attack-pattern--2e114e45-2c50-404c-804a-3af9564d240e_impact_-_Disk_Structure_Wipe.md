---
id: attack-pattern--2e114e45-2c50-404c-804a-3af9564d240e
mitre_attack_url: https://attack.mitre.org/techniques/T1487
name: Disk Structure Wipe
platforms:
- Windows
- macOS
- Linux
tactics:
- impact
title: impact - Disk Structure Wipe
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, macOS, Linux |
| **Permissions Required** | Administrator, root, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1487](https://attack.mitre.org/techniques/T1487) |

# Disk Structure Wipe (attack-pattern--2e114e45-2c50-404c-804a-3af9564d240e)

## Description
Adversaries may corrupt or wipe the disk data structures on hard drive necessary to boot systems; targeting specific critical systems as well as a large number of systems in a network to interrupt availability to system and network resources. 

Adversaries may attempt to render the system unable to boot by overwriting critical data located in structures such as the master boot record (MBR) or partition table.(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) The data contained in disk structures may include the initial executable code for loading an operating system or the location of the file system partitions on disk. If this information is not present, the computer will not be able to load an operating system during the boot process, leaving the computer unavailable. [Disk Structure Wipe](https://attack.mitre.org/techniques/T1487) may be performed in isolation, or along with [Disk Content Wipe](https://attack.mitre.org/techniques/T1488) if all sectors of a disk are wiped.

To maximize impact on the target organization, malware designed for destroying disk structures may have worm-like features to propagate across a network by leveraging other techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [Windows Admin Shares](https://attack.mitre.org/techniques/T1077).(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)

## Detection
Look for attempts to read/write to sensitive locations like the master boot record and the disk partition table. Monitor for unusual kernel driver installation activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1487)
- [Symantec Shamoon 2012](https://www.symantec.com/connect/blogs/shamoon-attacks)
- [FireEye Shamoon Nov 2016](https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)
- [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
