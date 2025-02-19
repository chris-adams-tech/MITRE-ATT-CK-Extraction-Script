---
id: attack-pattern--b82f7d37-b826-4ec9-9391-8e121c78aed7
mitre_attack_url: https://attack.mitre.org/techniques/T1488
name: Disk Content Wipe
platforms:
- Linux
- macOS
- Windows
tactics:
- impact
title: impact - Disk Content Wipe
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows |
| **Permissions Required** | User, Administrator, root, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1488](https://attack.mitre.org/techniques/T1488) |

# Disk Content Wipe (attack-pattern--b82f7d37-b826-4ec9-9391-8e121c78aed7)

## Description
Adversaries may erase the contents of storage devices on specific systems as well as large numbers of systems in a network to interrupt availability to system and network resources.

Adversaries may partially or completely overwrite the contents of a storage device rendering the data irrecoverable through the storage interface.(Citation: Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware)(Citation: DOJ Lazarus Sony 2018) Instead of wiping specific disk structures or files, adversaries with destructive intent may wipe arbitrary portions of disk content. To wipe disk content, adversaries may acquire direct access to the hard drive in order to overwrite arbitrarily sized portions of disk with random data.(Citation: Novetta Blockbuster Destructive Malware) Adversaries have been observed leveraging third-party drivers like [RawDisk](https://attack.mitre.org/software/S0364) to directly access disk content.(Citation: Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware) This behavior is distinct from [Data Destruction](https://attack.mitre.org/techniques/T1485) because sections of the disk erased instead of individual files.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disk content may have worm-like features to propagate across a network by leveraging additional techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [Windows Admin Shares](https://attack.mitre.org/techniques/T1077).(Citation: Novetta Blockbuster Destructive Malware)

## Detection
Look for attempts to read/write to sensitive locations like the partition boot sector or BIOS parameter block/superblock. Monitor for unusual kernel driver installation activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1488)
- [Novetta Blockbuster](https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Blockbuster Destructive Malware](https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [DOJ Lazarus Sony 2018](https://www.justice.gov/opa/press-release/file/1092091/download)
