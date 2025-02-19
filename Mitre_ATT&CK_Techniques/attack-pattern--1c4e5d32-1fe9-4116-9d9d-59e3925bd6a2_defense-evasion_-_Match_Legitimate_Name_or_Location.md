---
contributors:
- Yossi Weizman, Azure Defender Research Team
- Vishwas Manral, McAfee
data_sources:
- 'File: File Metadata'
- 'Image: Image Metadata'
- 'Process: Process Metadata'
- 'Process: Process Creation'
id: attack-pattern--1c4e5d32-1fe9-4116-9d9d-59e3925bd6a2
mitre_attack_url: https://attack.mitre.org/techniques/T1036/005
name: Match Legitimate Name or Location
platforms:
- Linux
- macOS
- Windows
- Containers
tactics:
- defense-evasion
title: defense-evasion - Match Legitimate Name or Location
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, Containers |
| **Data Sources** | File: File Metadata, Image: Image Metadata, Process: Process Metadata, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/005](https://attack.mitre.org/techniques/T1036/005) |

# Match Legitimate Name or Location (attack-pattern--1c4e5d32-1fe9-4116-9d9d-59e3925bd6a2)

## Description
Adversaries may match or approximate the name or location of legitimate files or resources when naming/placing them. This is done for the sake of evading defenses and observation. This may be done by placing an executable in a commonly trusted directory (ex: under System32) or giving it the name of a legitimate, trusted program (ex: svchost.exe). In containerized environments, this may also be done by creating a resource in a namespace that matches the naming convention of a container pod or cluster. Alternatively, a file or container image name given may be a close approximation to legitimate programs/images or something innocuous.

Adversaries may also use the same icon of the file they are trying to mimic.

## Detection
Collect file hashes; file names that do not match their expected hash are suspect. Perform file monitoring; files with known names but in unusual locations are suspect. Likewise, files that are modified outside of an update or patch are suspect.

If file names are mismatched between the file name on disk and that of the binary's PE metadata, this is a likely indicator that a binary was renamed after it was compiled. Collecting and comparing disk and resource filenames for binaries by looking to see if the InternalName, OriginalFilename, and/or ProductName match what is expected could provide useful leads, but may not always be indicative of malicious activity. (Citation: Elastic Masquerade Ball) Do not focus on the possible names a file could have, but instead on the command-line arguments that are known to be used and are distinct because it will have a better rate of detection.(Citation: Twitter ItsReallyNick Masquerading Update)

In containerized environments, use image IDs and layer hashes to compare images instead of relying only on their names.(Citation: Docker Images) Monitor for the unexpected creation of new resources within your cluster in Kubernetes, especially those created by atypical users.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/005)
- [Twitter ItsReallyNick Masquerading Update](https://x.com/ItsReallyNick/status/1055321652777619457)
- [Docker Images](https://docs.docker.com/engine/reference/commandline/images/)
- [Elastic Masquerade Ball](https://www.elastic.co/blog/how-hunt-masquerade-ball)
