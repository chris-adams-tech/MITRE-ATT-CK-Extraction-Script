---
contributors:
- Travis Smith, Tripwire
- Stefan Kanthak
data_sources:
- 'Service: Service Metadata'
- 'File: File Modification'
- 'File: File Creation'
- 'Process: Process Creation'
- 'Module: Module Load'
id: attack-pattern--70d81154-b187-45f9-8ec5-295d01255979
mitre_attack_url: https://attack.mitre.org/techniques/T1574/005
name: Executable Installer File Permissions Weakness
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - Executable Installer File Permissions Weakness
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Service: Service Metadata, File: File Modification, File: File Creation, Process: Process Creation, Module: Module Load |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/005](https://attack.mitre.org/techniques/T1574/005) |

# Executable Installer File Permissions Weakness (attack-pattern--70d81154-b187-45f9-8ec5-295d01255979)

## Description
Adversaries may execute their own malicious payloads by hijacking the binaries used by an installer. These processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the permissions on the file system directory containing a target binary, or permissions on the binary itself, are improperly set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original process. If the original process and thread are running under a higher permissions level, then the replaced binary will also execute under higher-level permissions, which could include SYSTEM.

Another variation of this technique can be performed by taking advantage of a weakness that is common in executable, self-extracting installers. During the installation process, it is common for installers to use a subdirectory within the <code>%TEMP%</code> directory to unpack binaries such as DLLs, EXEs, or other payloads. When installers create subdirectories and files they often do not set appropriate permissions to restrict write access, which allows for execution of untrusted code placed in the subdirectories or overwriting of binaries used in the installation process. This behavior is related to and may take advantage of [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001).

Adversaries may use this technique to replace legitimate binaries with malicious ones as a means of executing code at a higher permissions level. Some installers may also require elevated privileges that will result in privilege escalation when executing adversary controlled code. This behavior is related to [Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002). Several examples of this weakness in existing common installers have been reported to software vendors.(Citation: mozilla_sec_adv_2012)  (Citation: Executable Installers are Vulnerable) If the executing process is set to run at a specific time or during a certain event (e.g., system bootup) then this technique can also be used for persistence.

## Detection
Look for changes to binaries and service executables that may normally occur during software updates. If an executable is written, renamed, and/or moved to match an existing service executable, it could be detected and correlated with other suspicious behavior. Hashing of binaries and service executables could be used to detect replacement against historical data.

Look for abnormal process call trees from typical processes and services and for execution of other commands that could relate to Discovery or other adversary techniques.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/005)
- [mozilla_sec_adv_2012](https://www.mozilla.org/en-US/security/advisories/mfsa2012-98/)
- [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)
