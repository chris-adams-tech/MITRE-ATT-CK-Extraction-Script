---
contributors:
- Brent Murphy, Elastic
- David French, Elastic
- Syed Ummar Farooqh, McAfee
- Prasad Somasamudram, McAfee
- Sekhar Sarukkai, McAfee
- Varonis Threat Labs
- Joey Lei
data_sources:
- 'Snapshot: Snapshot Deletion'
- 'Cloud Storage: Cloud Storage Modification'
- 'Process: Process Creation'
- 'File: File Deletion'
- 'Image: Image Deletion'
- 'Instance: Instance Deletion'
- 'File: File Modification'
- 'Volume: Volume Deletion'
- 'Cloud Storage: Cloud Storage Deletion'
- 'Command: Command Execution'
id: attack-pattern--d45a3d09-b3cf-48f4-9f0f-f521ee5cb05c
mitre_attack_url: https://attack.mitre.org/techniques/T1485
name: Data Destruction
platforms:
- Windows
- IaaS
- Linux
- macOS
- Containers
tactics:
- impact
title: impact - Data Destruction
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, IaaS, Linux, macOS, Containers |
| **Data Sources** | Snapshot: Snapshot Deletion, Cloud Storage: Cloud Storage Modification, Process: Process Creation, File: File Deletion, Image: Image Deletion, Instance: Instance Deletion, File: File Modification, Volume: Volume Deletion, Cloud Storage: Cloud Storage Deletion, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1485](https://attack.mitre.org/techniques/T1485) |

# Data Destruction (attack-pattern--d45a3d09-b3cf-48f4-9f0f-f521ee5cb05c)

## Description
Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018)(Citation: Talos Olympic Destroyer 2018) Common operating system file deletion commands such as <code>del</code> and <code>rm</code> often only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from [Disk Content Wipe](https://attack.mitre.org/techniques/T1561/001) and [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002) because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.

Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable.(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) In some cases politically oriented image files have been used to overwrite data.(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Talos Olympic Destroyer 2018).

In cloud environments, adversaries may leverage access to delete cloud storage objects, machine images, database instances, and other infrastructure crucial to operations to damage an organization or their customers.(Citation: Data Destruction - Threat Post)(Citation: DOJ  - Cisco Insider)

## Detection
Use process monitoring to monitor the execution and command-line parameters of binaries that could be involved in data destruction activity, such as [SDelete](https://attack.mitre.org/software/S0195). Monitor for the creation of suspicious files as well as high unusual file modification activity. In particular, look for large quantities of file modifications in user directories and under <code>C:\Windows\System32\</code>.

In cloud environments, the occurrence of anomalous high-volume deletion events, such as the <code>DeleteDBCluster</code> and <code>DeleteGlobalCluster</code> events in AWS, or a high quantity of data deletion events, such as <code>DeleteBucket</code>, within a short period of time may indicate suspicious activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1485)
- [DOJ  - Cisco Insider](https://www.justice.gov/usao-ndca/pr/san-jose-man-pleads-guilty-damaging-cisco-s-network)
- [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
- [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [FireEye Shamoon Nov 2016](https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)
- [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Data Destruction - Threat Post](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/)
- [Symantec Shamoon 2012](https://www.symantec.com/connect/blogs/shamoon-attacks)
