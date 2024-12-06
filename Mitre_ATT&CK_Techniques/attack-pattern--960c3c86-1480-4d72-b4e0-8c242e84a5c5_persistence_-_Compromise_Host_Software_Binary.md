---
contributors:
- CrowdStrike Falcon OverWatch
- Liran Ravich, CardinalOps
- "Jamie Williams (U \u03C9 U), PANW Unit 42"
data_sources:
- 'File: File Deletion'
- 'File: File Modification'
- 'File: File Metadata'
- 'File: File Creation'
id: attack-pattern--960c3c86-1480-4d72-b4e0-8c242e84a5c5
mitre_attack_url: https://attack.mitre.org/techniques/T1554
name: Compromise Host Software Binary
platforms:
- Linux
- macOS
- Windows
tactics:
- persistence
title: persistence - Compromise Host Software Binary
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Deletion, File: File Modification, File: File Metadata, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1554](https://attack.mitre.org/techniques/T1554) |

# Compromise Host Software Binary (attack-pattern--960c3c86-1480-4d72-b4e0-8c242e84a5c5)

## Description
Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.

Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., [Modify Authentication Process](https://attack.mitre.org/techniques/T1556)).(Citation: Google Cloud Mandiant UNC3886 2024)

An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching)(Citation: Unit42 Banking Trojans Hooking 2022) prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow.(Citation: ESET FontOnLake Analysis 2021)

After modifying a binary, an adversary may attempt to [Impair Defenses](https://attack.mitre.org/techniques/T1562) by preventing it from updating (e.g., via the `yum-versionlock` command or `versionlock.list` file in Linux systems that use the yum package manager).(Citation: Google Cloud Mandiant UNC3886 2024)

## Detection
Collect and analyze signing certificate metadata and check signature validity on software that executes within the environment. Look for changes to client software that do not correlate with known software or patch cycles. 

Consider monitoring for anomalous behavior from client applications, such as atypical module loads, file reads/writes, or network connections.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1554)
- [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Unit42 Banking Trojans Hooking 2022](https://unit42.paloaltonetworks.com/banking-trojan-techniques/#post-125550-_rm3d6xxbk52n)
- [ESET FontOnLake Analysis 2021](https://web-assets.esetstatic.com/wls/2021/10/eset_fontonlake.pdf)
