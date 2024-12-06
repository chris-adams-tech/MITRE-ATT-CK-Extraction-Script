---
contributors:
- Yonatan Gotlib, Deep Instinct
- Austin Clark, @c2defense
- Pallavi Sivakumaran, WithSecure
- Joey Lei
- Harjot Shah Singh
data_sources:
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Cloud Storage: Cloud Storage Deletion'
- 'Command: Command Execution'
- 'Service: Service Metadata'
- 'Snapshot: Snapshot Deletion'
- 'File: File Deletion'
id: attack-pattern--f5d8eed6-48a9-4cdf-a3d7-d1ffa99c3d2a
mitre_attack_url: https://attack.mitre.org/techniques/T1490
name: Inhibit System Recovery
platforms:
- Windows
- macOS
- Linux
- Network
- IaaS
- Containers
tactics:
- impact
title: impact - Inhibit System Recovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, macOS, Linux, Network, IaaS, Containers |
| **Data Sources** | Process: Process Creation, Windows Registry: Windows Registry Key Modification, Cloud Storage: Cloud Storage Deletion, Command: Command Execution, Service: Service Metadata, Snapshot: Snapshot Deletion, File: File Deletion |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1490](https://attack.mitre.org/techniques/T1490) |

# Inhibit System Recovery (attack-pattern--f5d8eed6-48a9-4cdf-a3d7-d1ffa99c3d2a)

## Description
Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery.(Citation: Talos Olympic Destroyer 2018)(Citation: FireEye WannaCry 2017) This may deny access to available backups and recovery options.

Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies, and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of [Data Destruction](https://attack.mitre.org/techniques/T1485) and [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486).(Citation: Talos Olympic Destroyer 2018)(Citation: FireEye WannaCry 2017) Furthermore, adversaries may disable recovery notifications, then corrupt backups.(Citation: disable_notif_synology_ransom)

A number of native Windows utilities have been used by adversaries to disable or delete system recovery features:

* <code>vssadmin.exe</code> can be used to delete all volume shadow copies on a system - <code>vssadmin.exe delete shadows /all /quiet</code>
* [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) can be used to delete volume shadow copies - <code>wmic shadowcopy delete</code>
* <code>wbadmin.exe</code> can be used to delete the Windows Backup Catalog - <code>wbadmin.exe delete catalog -quiet</code>
* <code>bcdedit.exe</code> can be used to disable automatic Windows recovery features by modifying boot configuration data - <code>bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no</code>
* <code>REAgentC.exe</code> can be used to disable Windows Recovery Environment (WinRE) repair/recovery options of an infected system
* <code>diskshadow.exe</code> can be used to delete all volume shadow copies on a system - <code>diskshadow delete shadows all</code> (Citation: Diskshadow) (Citation: Crytox Ransomware)

On network devices, adversaries may leverage [Disk Wipe](https://attack.mitre.org/techniques/T1561) to delete backup firmware images and reformat the file system, then [System Shutdown/Reboot](https://attack.mitre.org/techniques/T1529) to reload the device. Together this activity may leave network devices completely inoperable and inhibit recovery operations.

Adversaries may also delete “online” backups that are connected to their network – whether via network storage media or through folders that sync to cloud services.(Citation: ZDNet Ransomware Backups 2020) In cloud environments, adversaries may disable versioning and backup policies and delete snapshots, database backups, machine images, and prior versions of objects designed to be used in disaster recovery scenarios.(Citation: Dark Reading Code Spaces Cyber Attack)(Citation: Rhino Security Labs AWS S3 Ransomware)

## Detection
Use process monitoring to monitor the execution and command line parameters of binaries involved in inhibiting system recovery, such as vssadmin, wbadmin, bcdedit, REAgentC, and diskshadow. The Windows event logs, ex. Event ID 524 indicating a system catalog was deleted, may contain entries associated with suspicious activity.

Monitor the status of services involved in system recovery. Monitor the registry for changes associated with system recovery features (ex: the creation of <code>HKEY_CURRENT_USER\Software\Policies\Microsoft\PreviousVersions\DisableLocalPage</code>).

For network infrastructure devices, collect AAA logging to monitor for `erase`, `format`, and `reload` commands being run in succession.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1490)
- [Dark Reading Code Spaces Cyber Attack](https://www.darkreading.com/attacks-breaches/code-hosting-service-shuts-down-after-cyber-attack)
- [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
- [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Diskshadow](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskshadow)
- [Crytox Ransomware](https://www.zscaler.com/blogs/security-research/technical-analysis-crytox-ransomware)
- [Rhino Security Labs AWS S3 Ransomware](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)
- [ZDNet Ransomware Backups 2020](https://www.zdnet.com/article/ransomware-victims-thought-their-backups-were-safe-they-were-wrong/)
- [disable_notif_synology_ransom](https://x.com/TheDFIRReport/status/1498657590259109894)
