---
contributors:
- Oleg Kolesnikov, Securonix
- Mayuresh Dani, Qualys
- Harshal Tupsamudre, Qualys
- Travis Smith, Qualys
- ExtraHop
data_sources:
- 'File: File Modification'
- 'Cloud Storage: Cloud Storage Modification'
- 'Network Share: Network Share Access'
- 'File: File Creation'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--b80d107d-fa0d-4b60-9684-b0433e8bdba0
mitre_attack_url: https://attack.mitre.org/techniques/T1486
name: Data Encrypted for Impact
platforms:
- Linux
- macOS
- Windows
- IaaS
tactics:
- impact
title: impact - Data Encrypted for Impact
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows, IaaS |
| **Data Sources** | File: File Modification, Cloud Storage: Cloud Storage Modification, Network Share: Network Share Access, File: File Creation, Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1486](https://attack.mitre.org/techniques/T1486) |

# Data Encrypted for Impact (attack-pattern--b80d107d-fa0d-4b60-9684-b0433e8bdba0)

## Description
Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availability to system and network resources. They can attempt to render stored data inaccessible by encrypting files or data on local and remote drives and withholding access to a decryption key. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted.(Citation: US-CERT Ransomware 2016)(Citation: FireEye WannaCry 2017)(Citation: US-CERT NotPetya 2017)(Citation: US-CERT SamSam 2018)

In the case of ransomware, it is typical that common user files like Office documents, PDFs, images, videos, audio, text, and source code files will be encrypted (and often renamed and/or tagged with specific file markers). Adversaries may need to first employ other behaviors, such as [File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222) or [System Shutdown/Reboot](https://attack.mitre.org/techniques/T1529), in order to unlock and/or gain access to manipulate these files.(Citation: CarbonBlack Conti July 2020) In some cases, adversaries may encrypt critical system files, disk partitions, and the MBR.(Citation: US-CERT NotPetya 2017) 

To maximize impact on the target organization, malware designed for encrypting data may have worm-like features to propagate across a network by leveraging other attack techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: FireEye WannaCry 2017)(Citation: US-CERT NotPetya 2017) Encryption malware may also leverage [Internal Defacement](https://attack.mitre.org/techniques/T1491/001), such as changing victim wallpapers, or otherwise intimidate victims by sending ransom notes or other messages to connected printers (known as "print bombing").(Citation: NHS Digital Egregor Nov 2020)

In cloud environments, storage objects within compromised accounts may also be encrypted.(Citation: Rhino S3 Ransomware Part 1)

## Detection
Use process monitoring to monitor the execution and command line parameters of binaries involved in data destruction activity, such as vssadmin, wbadmin, and bcdedit. Monitor for the creation of suspicious files as well as unusual file modification activity. In particular, look for large quantities of file modifications in user directories.

In some cases, monitoring for unusual kernel driver installation activity can aid in detection.

In cloud environments, monitor for events that indicate storage objects have been anomalously replaced by copies.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1486)
- [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
- [Rhino S3 Ransomware Part 1](https://rhinosecuritylabs.com/aws/s3-ransomware-part-1-attack-vector/)
- [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
- [US-CERT Ransomware 2016](https://www.us-cert.gov/ncas/alerts/TA16-091A)
- [US-CERT NotPetya 2017](https://www.us-cert.gov/ncas/alerts/TA17-181A)
- [US-CERT SamSam 2018](https://www.us-cert.gov/ncas/alerts/AA18-337A)
