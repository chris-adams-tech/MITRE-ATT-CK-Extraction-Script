---
contributors:
- Christiaan Beek, @ChristiaanBeek
data_sources:
- 'File: File Metadata'
- 'File: File Creation'
id: attack-pattern--7e7c2fba-7cca-486c-9582-4c1bb2851961
mitre_attack_url: https://attack.mitre.org/techniques/T1553/005
name: Mark-of-the-Web Bypass
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Mark-of-the-Web Bypass
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | File: File Metadata, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1553/005](https://attack.mitre.org/techniques/T1553/005) |

# Mark-of-the-Web Bypass (attack-pattern--7e7c2fba-7cca-486c-9582-4c1bb2851961)

## Description
Adversaries may abuse specific file formats to subvert Mark-of-the-Web (MOTW) controls. In Windows, when files are downloaded from the Internet, they are tagged with a hidden NTFS Alternate Data Stream (ADS) named <code>Zone.Identifier</code> with a specific value known as the MOTW.(Citation: Microsoft Zone.Identifier 2020) Files that are tagged with MOTW are protected and cannot perform certain actions. For example, starting in MS Office 10, if a MS Office file has the MOTW, it will open in Protected View. Executables tagged with the MOTW will be processed by Windows Defender SmartScreen that compares files with an allowlist of well-known executables. If the file is not known/trusted, SmartScreen will prevent the execution and warn the user not to run it.(Citation: Beek Use of VHD Dec 2020)(Citation: Outflank MotW 2020)(Citation: Intezer Russian APT Dec 2020)

Adversaries may abuse container files such as compressed/archive (.arj, .gzip) and/or disk image (.iso, .vhd) file formats to deliver malicious payloads that may not be tagged with MOTW. Container files downloaded from the Internet will be marked with MOTW but the files within may not inherit the MOTW after the container files are extracted and/or mounted. MOTW is a NTFS feature and many container files do not support NTFS alternative data streams. After a container file is extracted and/or mounted, the files contained within them may be treated as local files on disk and run without protections.(Citation: Beek Use of VHD Dec 2020)(Citation: Outflank MotW 2020)

## Detection
Monitor compressed/archive and image files downloaded from the Internet as the contents may not be tagged with the MOTW. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities.(Citation: Disable automount for ISO)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1553/005)
- [Beek Use of VHD Dec 2020](https://medium.com/swlh/investigating-the-use-of-vhd-files-by-cybercriminals-3f1f08304316)
- [Outflank MotW 2020](https://outflank.nl/blog/2020/03/30/mark-of-the-web-from-a-red-teams-perspective/)
- [Intezer Russian APT Dec 2020](https://www.intezer.com/blog/research/russian-apt-uses-covid-19-lures-to-deliver-zebrocy/)
- [Microsoft Zone.Identifier 2020](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/6e3f7352-d11c-4d76-8c39-2516a9df36e8)
- [Disable automount for ISO](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)
