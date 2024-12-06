---
contributors:
- Michael Raggi @aRtAGGI
- Andrew Northern, @ex_raritas
- Gregory Lesnewich, @greglesnewich
data_sources:
- 'File: File Metadata'
- 'File: File Creation'
id: attack-pattern--887274fc-2d63-4bdc-82f3-fae56d1d5fdc
mitre_attack_url: https://attack.mitre.org/techniques/T1027/012
name: LNK Icon Smuggling
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - LNK Icon Smuggling
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | File: File Metadata, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/012](https://attack.mitre.org/techniques/T1027/012) |

# LNK Icon Smuggling (attack-pattern--887274fc-2d63-4bdc-82f3-fae56d1d5fdc)

## Description
Adversaries may smuggle commands to download malicious payloads past content filters by hiding them within otherwise seemingly benign windows shortcut files. Windows shortcut files (.LNK) include many metadata fields, including an icon location field (also known as the `IconEnvironmentDataBlock`) designed to specify the path to an icon file that is to be displayed for the LNK file within a host directory. 

Adversaries may abuse this LNK metadata to download malicious payloads. For example, adversaries have been observed using LNK files as phishing payloads to deliver malware. Once invoked (e.g., [Malicious File](https://attack.mitre.org/techniques/T1204/002)), payloads referenced via external URLs within the LNK icon location field may be downloaded. These files may also then be invoked by [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)/[System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218) arguments within the target path field of the LNK.(Citation: Unprotect Shortcut)(Citation: Booby Trap Shortcut 2017)

LNK Icon Smuggling may also be utilized post compromise, such as malicious scripts executing an LNK on an infected host to download additional malicious payloads. 


## Detection



## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/012)
- [Unprotect Shortcut](https://unprotect.it/technique/shortcut-hiding/)
- [Booby Trap Shortcut 2017](https://www.uperesia.com/booby-trapped-shortcut)
