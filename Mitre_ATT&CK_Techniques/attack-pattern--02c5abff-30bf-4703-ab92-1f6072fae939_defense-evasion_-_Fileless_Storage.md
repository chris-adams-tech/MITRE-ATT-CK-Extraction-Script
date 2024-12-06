---
contributors:
- Christopher Peacock
- Denise Tan
- Mark Wee
- Simona David
- Xavier Rousseau
- Vito Alfano, Group-IB
data_sources:
- 'Windows Registry: Windows Registry Key Creation'
- 'WMI: WMI Creation'
- 'Process: Process Creation'
id: attack-pattern--02c5abff-30bf-4703-ab92-1f6072fae939
mitre_attack_url: https://attack.mitre.org/techniques/T1027/011
name: Fileless Storage
platforms:
- Windows
- Linux
tactics:
- defense-evasion
title: defense-evasion - Fileless Storage
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, Linux |
| **Data Sources** | Windows Registry: Windows Registry Key Creation, WMI: WMI Creation, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/011](https://attack.mitre.org/techniques/T1027/011) |

# Fileless Storage (attack-pattern--02c5abff-30bf-4703-ab92-1f6072fae939)

## Description
Adversaries may store data in "fileless" formats to conceal malicious activity from defenses. Fileless storage can be broadly defined as any format other than a file. Common examples of non-volatile fileless storage in Windows systems include the Windows Registry, event logs, or WMI repository.(Citation: Microsoft Fileless)(Citation: SecureList Fileless) In Linux systems, shared memory directories such as `/dev/shm`, `/run/shm`, `/var/run`, and `/var/lock` may also be considered fileless storage, as files written to these directories are mapped directly to RAM and not stored on the disk.(Citation: Elastic Binary Executed from Shared Memory Directory)(Citation: Akami Frog4Shell 2024)(Citation: Aquasec Muhstik Malware 2024)

Similar to fileless in-memory behaviors such as [Reflective Code Loading](https://attack.mitre.org/techniques/T1620) and [Process Injection](https://attack.mitre.org/techniques/T1055), fileless data storage may remain undetected by anti-virus and other endpoint security tools that can only access specific file formats from disk storage. Leveraging fileless storage may also allow adversaries to bypass the protections offered by read-only file systems in Linux.(Citation: Sysdig Fileless Malware 23022)

Adversaries may use fileless storage to conceal various types of stored data, including payloads/shellcode (potentially being used as part of [Persistence](https://attack.mitre.org/tactics/TA0003)) and collected data not yet exfiltrated from the victim (e.g., [Local Data Staging](https://attack.mitre.org/techniques/T1074/001)). Adversaries also often encrypt, encode, splice, or otherwise obfuscate this fileless data when stored.

Some forms of fileless storage activity may indirectly create artifacts in the file system, but in central and otherwise difficult to inspect formats such as the WMI (e.g., `%SystemRoot%\System32\Wbem\Repository`) or Registry (e.g., `%SystemRoot%\System32\Config`) physical files.(Citation: Microsoft Fileless) 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/011)
- [Aquasec Muhstik Malware 2024](https://www.aquasec.com/blog/muhstik-malware-targets-message-queuing-services-applications/)
- [Elastic Binary Executed from Shared Memory Directory](https://www.elastic.co/guide/en/security/7.17/prebuilt-rule-7-16-3-binary-executed-from-shared-memory-directory.html)
- [SecureList Fileless](https://securelist.com/a-new-secret-stash-for-fileless-malware/106393/)
- [Microsoft Fileless](https://learn.microsoft.com/microsoft-365/security/intelligence/fileless-threats)
- [Sysdig Fileless Malware 23022](https://sysdig.com/blog/containers-read-only-fileless-malware/)
- [Akami Frog4Shell 2024](https://www.akamai.com/blog/security-research/fritzfrog-botnet-new-capabilities-log4shell)
