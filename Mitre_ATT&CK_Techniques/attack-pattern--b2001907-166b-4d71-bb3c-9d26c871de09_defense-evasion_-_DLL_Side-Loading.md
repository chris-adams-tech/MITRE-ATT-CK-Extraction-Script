---
id: attack-pattern--b2001907-166b-4d71-bb3c-9d26c871de09
mitre_attack_url: https://attack.mitre.org/techniques/T1073
name: DLL Side-Loading
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - DLL Side-Loading
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1073](https://attack.mitre.org/techniques/T1073) |

# DLL Side-Loading (attack-pattern--b2001907-166b-4d71-bb3c-9d26c871de09)

## Description
Programs may specify DLLs that are loaded at runtime. Programs that improperly or vaguely specify a required DLL may be open to a vulnerability in which an unintended DLL is loaded. Side-loading vulnerabilities specifically occur when Windows Side-by-Side (WinSxS) manifests (Citation: MSDN Manifests) are not explicit enough about characteristics of the DLL to be loaded. Adversaries may take advantage of a legitimate program that is vulnerable to side-loading to load a malicious DLL. (Citation: Stewart 2014)

Adversaries likely use this technique as a means of masking actions they perform under a legitimate, trusted system or software process.

## Detection
Monitor processes for unusual activity (e.g., a process that does not use the network begins to do so). Track DLL metadata, such as a hash, and compare DLLs that are loaded at process execution time against previous executions to detect differences that do not correlate with patching or updates.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1073)
- [capec](https://capec.mitre.org/data/definitions/641.html)
- [MSDN Manifests](https://msdn.microsoft.com/en-us/library/aa375365)
- [Stewart 2014](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)
