---
contributors:
- Oleg Kolesnikov, Securonix
- Nick Carr, Mandiant
- David Lu, Tripwire
- "Felipe Esp\xF3sito, @Pr0teus"
- Elastic
- Bartosz Jerzman
- Menachem Goldstein
data_sources:
- 'File: File Modification'
- 'Process: Process Metadata'
- 'Service: Service Creation'
- 'Service: Service Metadata'
- 'Process: Process Creation'
- 'Image: Image Metadata'
- 'Scheduled Job: Scheduled Job Metadata'
- 'User Account: User Account Creation'
- 'File: File Metadata'
- 'Scheduled Job: Scheduled Job Modification'
- 'Command: Command Execution'
- 'Process: OS API Execution'
id: attack-pattern--42e8de7b-37b2-4258-905a-6897815e58e0
mitre_attack_url: https://attack.mitre.org/techniques/T1036
name: Masquerading
platforms:
- Linux
- macOS
- Windows
- Containers
tactics:
- defense-evasion
title: defense-evasion - Masquerading
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, Containers |
| **Data Sources** | File: File Modification, Process: Process Metadata, Service: Service Creation, Service: Service Metadata, Process: Process Creation, Image: Image Metadata, Scheduled Job: Scheduled Job Metadata, User Account: User Account Creation, File: File Metadata, Scheduled Job: Scheduled Job Modification, Command: Command Execution, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036](https://attack.mitre.org/techniques/T1036) |

# Masquerading (attack-pattern--42e8de7b-37b2-4258-905a-6897815e58e0)

## Description
Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

Renaming abusable system utilities to evade security monitoring is also a form of [Masquerading](https://attack.mitre.org/techniques/T1036).(Citation: LOLBAS Main Site)

## Detection
Collect file hashes; file names that do not match their expected hash are suspect. Perform file monitoring; files with known names but in unusual locations are suspect. Likewise, files that are modified outside of an update or patch are suspect.

If file names are mismatched between the file name on disk and that of the binary's PE metadata, this is a likely indicator that a binary was renamed after it was compiled. Collecting and comparing disk and resource filenames for binaries by looking to see if the InternalName, OriginalFilename, and/or ProductName match what is expected could provide useful leads, but may not always be indicative of malicious activity. (Citation: Elastic Masquerade Ball) Do not focus on the possible names a file could have, but instead on the command-line arguments that are known to be used and are distinct because it will have a better rate of detection.(Citation: Twitter ItsReallyNick Masquerading Update)

Look for indications of common characters that may indicate an attempt to trick users into misidentifying the file type, such as a space as the last character of a file name or the right-to-left override characters"\u202E", "[U+202E]", and "%E2%80%AE”.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036)
- [Twitter ItsReallyNick Masquerading Update](https://x.com/ItsReallyNick/status/1055321652777619457)
- [Elastic Masquerade Ball](https://www.elastic.co/blog/how-hunt-masquerade-ball)
- [LOLBAS Main Site](https://lolbas-project.github.io/)
