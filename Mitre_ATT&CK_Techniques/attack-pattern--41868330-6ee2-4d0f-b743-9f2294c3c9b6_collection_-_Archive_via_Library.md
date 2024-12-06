---
data_sources:
- 'Script: Script Execution'
- 'File: File Creation'
id: attack-pattern--41868330-6ee2-4d0f-b743-9f2294c3c9b6
mitre_attack_url: https://attack.mitre.org/techniques/T1560/002
name: Archive via Library
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
title: collection - Archive via Library
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Script: Script Execution, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1560/002](https://attack.mitre.org/techniques/T1560/002) |

# Archive via Library (attack-pattern--41868330-6ee2-4d0f-b743-9f2294c3c9b6)

## Description
An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party libraries. Many libraries exist that can archive data, including [Python](https://attack.mitre.org/techniques/T1059/006) rarfile (Citation: PyPI RAR), libzip (Citation: libzip), and zlib (Citation: Zlib Github). Most libraries include functionality to encrypt and/or compress data.

Some archival libraries are preinstalled on systems, such as bzip2 on macOS and Linux, and zip on Windows. Note that the libraries are different from the utilities. The libraries can be linked against when compiling, while the utilities require spawning a subshell, or a similar execution mechanism.

## Detection
Monitor processes for accesses to known archival libraries. This may yield a significant number of benign events, depending on how systems in the environment are typically used.

Consider detecting writing of files with extensions and/or headers associated with compressed or encrypted file types. Detection efforts may focus on follow-on exfiltration activity, where compressed or encrypted files can be detected in transit with a network intrusion detection or data loss prevention system analyzing file headers.(Citation: Wikipedia File Header Signatures)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1560/002)
- [PyPI RAR](https://pypi.org/project/rarfile/)
- [libzip](https://libzip.org/)
- [Zlib Github](https://github.com/madler/zlib)
- [Wikipedia File Header Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
