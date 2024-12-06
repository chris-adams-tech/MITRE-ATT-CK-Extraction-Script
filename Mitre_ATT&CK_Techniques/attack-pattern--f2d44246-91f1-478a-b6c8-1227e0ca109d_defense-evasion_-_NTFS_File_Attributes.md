---
contributors:
- Red Canary
- Oddvar Moe, @oddvarmoe
id: attack-pattern--f2d44246-91f1-478a-b6c8-1227e0ca109d
mitre_attack_url: https://attack.mitre.org/techniques/T1096
name: NTFS File Attributes
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - NTFS File Attributes
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **System Requirements** | NTFS partitioned hard drive |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1096](https://attack.mitre.org/techniques/T1096) |

# NTFS File Attributes (attack-pattern--f2d44246-91f1-478a-b6c8-1227e0ca109d)

## Description
Every New Technology File System (NTFS) formatted partition contains a Master File Table (MFT) that maintains a record for every file/directory on the partition. (Citation: SpectorOps Host-Based Jul 2017) Within MFT entries are file attributes, (Citation: Microsoft NTFS File Attributes Aug 2010) such as Extended Attributes (EA) and Data [known as Alternate Data Streams (ADSs) when more than one Data attribute is present], that can be used to store arbitrary data (and even complete files). (Citation: SpectorOps Host-Based Jul 2017) (Citation: Microsoft File Streams) (Citation: MalwareBytes ADS July 2015) (Citation: Microsoft ADS Mar 2014)

Adversaries may store malicious data or binaries in file attribute metadata instead of directly in files. This may be done to evade some defenses, such as static indicator scanning tools and anti-virus. (Citation: Journey into IR ZeroAccess NTFS EA) (Citation: MalwareBytes ADS July 2015)

## Detection
Forensic techniques exist to identify information stored in NTFS EA. (Citation: Journey into IR ZeroAccess NTFS EA) Monitor calls to the ZwSetEaFile and ZwQueryEaFile Windows API functions as well as binaries used to interact with EA, (Citation: Oddvar Moe ADS1 Jan 2018) (Citation: Oddvar Moe ADS2 Apr 2018) and consider regularly scanning for the presence of modified information. (Citation: SpectorOps Host-Based Jul 2017)

There are many ways to create and interact with ADSs using Windows utilities. Monitor for operations (execution, copies, etc.) with file names that contain colons. This syntax (ex: <code>file.ext:ads[.ext]</code>) is commonly associated with ADSs. (Citation: Microsoft ADS Mar 2014) (Citation: Oddvar Moe ADS1 Jan 2018) (Citation: Oddvar Moe ADS2 Apr 2018) For a more exhaustive list of utilities that can be used to execute and create ADSs, see https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f.

The Streams tool of Sysinternals can be used to uncover files with ADSs. The <code>dir /r</code> command can also be used to display ADSs. (Citation: Symantec ADS May 2009) Many PowerShell commands (such as Get-Item, Set-Item, Remove-Item, and Get-ChildItem) can also accept a <code>-stream</code> parameter to interact with ADSs. (Citation: MalwareBytes ADS July 2015) (Citation: Microsoft ADS Mar 2014)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1096)
- [SpectorOps Host-Based Jul 2017](https://posts.specterops.io/host-based-threat-modeling-indicator-design-a9dbbb53d5ea)
- [Microsoft NTFS File Attributes Aug 2010](https://blogs.technet.microsoft.com/askcore/2010/08/25/ntfs-file-attributes/)
- [Microsoft File Streams](http://msdn.microsoft.com/en-us/library/aa364404)
- [MalwareBytes ADS July 2015](https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/)
- [Microsoft ADS Mar 2014](https://blogs.technet.microsoft.com/askcore/2013/03/24/alternate-data-streams-in-ntfs/)
- [Journey into IR ZeroAccess NTFS EA](http://journeyintoir.blogspot.com/2012/12/extracting-zeroaccess-from-ntfs.html)
- [Oddvar Moe ADS1 Jan 2018](https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/)
- [Oddvar Moe ADS2 Apr 2018](https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/)
- [Symantec ADS May 2009](https://www.symantec.com/connect/articles/what-you-need-know-about-alternate-data-streams-windows-your-data-secure-can-you-restore)
