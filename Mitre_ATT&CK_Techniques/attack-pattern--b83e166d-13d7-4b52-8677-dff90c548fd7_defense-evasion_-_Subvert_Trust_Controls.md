---
data_sources:
- 'Module: Module Load'
- 'Windows Registry: Windows Registry Key Creation'
- 'File: File Metadata'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'File: File Modification'
- 'Windows Registry: Windows Registry Key Modification'
id: attack-pattern--b83e166d-13d7-4b52-8677-dff90c548fd7
mitre_attack_url: https://attack.mitre.org/techniques/T1553
name: Subvert Trust Controls
platforms:
- Windows
- macOS
- Linux
tactics:
- defense-evasion
title: defense-evasion - Subvert Trust Controls
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Module: Module Load, Windows Registry: Windows Registry Key Creation, File: File Metadata, Command: Command Execution, Process: Process Creation, File: File Modification, Windows Registry: Windows Registry Key Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1553](https://attack.mitre.org/techniques/T1553) |

# Subvert Trust Controls (attack-pattern--b83e166d-13d7-4b52-8677-dff90c548fd7)

## Description
Adversaries may undermine security controls that will either warn users of untrusted activity or prevent execution of untrusted programs. Operating systems and security products may contain mechanisms to identify programs or websites as possessing some level of trust. Examples of such features would include a program being allowed to run because it is signed by a valid code signing certificate, a program prompting the user with a warning because it has an attribute set from being downloaded from the Internet, or getting an indication that you are about to connect to an untrusted site.

Adversaries may attempt to subvert these trust mechanisms. The method adversaries use will depend on the specific mechanism they seek to subvert. Adversaries may conduct [File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222) or [Modify Registry](https://attack.mitre.org/techniques/T1112) in support of subverting these controls.(Citation: SpectorOps Subverting Trust Sept 2017) Adversaries may also create or steal code signing certificates to acquire trust on target systems.(Citation: Securelist Digital Certificates)(Citation: Symantec Digital Certificates) 

## Detection
Collect and analyze signing certificate metadata on software that executes within the environment to look for unusual certificate characteristics and outliers. Periodically baseline registered SIPs and trust providers (Registry entries and files on disk), specifically looking for new, modified, or non-Microsoft entries. (Citation: SpectorOps Subverting Trust Sept 2017) A system's root certificates are unlikely to change frequently. Monitor new certificates installed on a system that could be due to malicious activity.(Citation: SpectorOps Code Signing Dec 2017)

Analyze Autoruns data for oddities and anomalies, specifically malicious files attempting persistent execution by hiding within auto-starting locations. Autoruns will hide entries signed by Microsoft or Windows by default, so ensure "Hide Microsoft Entries" and "Hide Windows Entries" are both deselected.(Citation: SpectorOps Subverting Trust Sept 2017) 

Monitor and investigate attempts to modify extended file attributes with utilities such as <code>xattr</code>. Built-in system utilities may generate high false positive alerts, so compare against baseline knowledge for how systems are typically used and correlate modification events with other indications of malicious activity where possible. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1553)
- [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)
- [SpectorOps Subverting Trust Sept 2017](https://specterops.io/assets/resources/SpecterOps_Subverting_Trust_in_Windows.pdf)
- [Securelist Digital Certificates](https://securelist.com/why-you-shouldnt-completely-trust-files-signed-with-digital-certificates/68593/)
- [Symantec Digital Certificates](http://www.symantec.com/connect/blogs/how-attackers-steal-private-keys-digital-certificates)
