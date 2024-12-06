---
data_sources:
- 'File: File Creation'
- 'File: File Metadata'
id: attack-pattern--11f29a39-0942-4d62-92b6-fe236cf3066e
mitre_attack_url: https://attack.mitre.org/techniques/T1036/007
name: Double File Extension
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Double File Extension
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | File: File Creation, File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/007](https://attack.mitre.org/techniques/T1036/007) |

# Double File Extension (attack-pattern--11f29a39-0942-4d62-92b6-fe236cf3066e)

## Description
Adversaries may abuse a double extension in the filename as a means of masquerading the true file type. A file name may include a secondary file type extension that may cause only the first extension to be displayed (ex: <code>File.txt.exe</code> may render in some views as just <code>File.txt</code>). However, the second extension is the true file type that determines how the file is opened and executed. The real file extension may be hidden by the operating system in the file browser (ex: explorer.exe), as well as in any software configured using or similar to the system’s policies.(Citation: PCMag DoubleExtension)(Citation: SOCPrime DoubleExtension) 

Adversaries may abuse double extensions to attempt to conceal dangerous file types of payloads. A very common usage involves tricking a user into opening what they think is a benign file type but is actually executable code. Such files often pose as email attachments and allow an adversary to gain [Initial Access](https://attack.mitre.org/tactics/TA0001) into a user’s system via [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001) then [User Execution](https://attack.mitre.org/techniques/T1204). For example, an executable file attachment named <code>Evil.txt.exe</code> may display as <code>Evil.txt</code> to a user. The user may then view it as a benign text file and open it, inadvertently executing the hidden malware.(Citation: SOCPrime DoubleExtension)

Common file types, such as text files (.txt, .doc, etc.) and image files (.jpg, .gif, etc.) are typically used as the first extension to appear benign. Executable extensions commonly regarded as dangerous, such as .exe, .lnk, .hta, and .scr, often appear as the second extension and true file type.

## Detection
Monitor for files written to disk that contain two file extensions, particularly when the second is an executable.(Citation: Seqrite DoubleExtension)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/007)
- [PCMag DoubleExtension](https://www.pcmag.com/encyclopedia/term/double-extension)
- [SOCPrime DoubleExtension](https://socprime.com/blog/rule-of-the-week-possible-malicious-file-double-extension/)
- [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)
