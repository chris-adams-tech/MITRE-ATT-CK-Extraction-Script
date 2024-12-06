---
contributors:
- Romain Dumont, ESET
- Mike Hartley @mikehartley10
data_sources:
- 'Process: OS API Execution'
- 'File: File Modification'
- 'File: File Metadata'
- 'Command: Command Execution'
id: attack-pattern--47f2d673-ca62-47e9-929b-1b0be9657611
mitre_attack_url: https://attack.mitre.org/techniques/T1070/006
name: Timestomp
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Timestomp
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: OS API Execution, File: File Modification, File: File Metadata, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1070/006](https://attack.mitre.org/techniques/T1070/006) |

# Timestomp (attack-pattern--47f2d673-ca62-47e9-929b-1b0be9657611)

## Description
Adversaries may modify file time attributes to hide new files or changes to existing files. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder and blend malicious files with legitimate files.

Both the `$STANDARD_INFORMATION` (`$SI`) and `$FILE_NAME` (`$FN`) attributes record times in a Master File Table (MFT) file.(Citation: Inversecos Timestomping 2022) `$SI` (dates/time stamps) is displayed to the end user, including in the File System view, while `$FN` is dealt with by the kernel.(Citation: Magnet Forensics)

Modifying the `$SI` attribute is the most common method of timestomping because it can be modified at the user level using API calls. `$FN` timestomping, however, typically requires interacting with the system kernel or moving or renaming a file.(Citation: Inversecos Timestomping 2022)

Adversaries modify timestamps on files so that they do not appear conspicuous to forensic investigators or file analysis tools. In order to evade detections that rely on identifying discrepancies between the `$SI` and `$FN` attributes, adversaries may also engage in “double timestomping” by modifying times on both attributes simultaneously.(Citation: Double Timestomping)

Timestomping may be used along with file name [Masquerading](https://attack.mitre.org/techniques/T1036) to hide malware and tools.(Citation: WindowsIR Anti-Forensic Techniques)

## Detection
Forensic techniques exist to detect aspects of files that have had their timestamps modified. (Citation: WindowsIR Anti-Forensic Techniques) It may be possible to detect timestomping using file modification monitoring that collects information on file handle opens and can compare timestamp values.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1070/006)
- [WindowsIR Anti-Forensic Techniques](http://windowsir.blogspot.com/2013/07/howto-determinedetect-use-of-anti.html)
- [Inversecos Timestomping 2022](https://www.inversecos.com/2022/04/defence-evasion-technique-timestomping.html)
- [Magnet Forensics](https://www.magnetforensics.com/blog/expose-evidence-of-timestomping-with-the-ntfs-timestamp-mismatch-artifact-in-magnet-axiom-4-4/)
- [Double Timestomping](https://x.com/matthewdunwoody/status/1519846657646604289)
