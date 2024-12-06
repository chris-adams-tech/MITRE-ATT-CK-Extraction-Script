---
data_sources:
- 'Process: Process Creation'
id: attack-pattern--ffe59ad3-ad9b-4b9f-b74f-5beb3c309dc1
mitre_attack_url: https://attack.mitre.org/techniques/T1564/010
name: Process Argument Spoofing
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Process Argument Spoofing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1564/010](https://attack.mitre.org/techniques/T1564/010) |

# Process Argument Spoofing (attack-pattern--ffe59ad3-ad9b-4b9f-b74f-5beb3c309dc1)

## Description
Adversaries may attempt to hide process command-line arguments by overwriting process memory. Process command-line arguments are stored in the process environment block (PEB), a data structure used by Windows to store various information about/used by a process. The PEB includes the process command-line arguments that are referenced when executing the process. When a process is created, defensive tools/sensors that monitor process creations may retrieve the process arguments from the PEB.(Citation: Microsoft PEB 2021)(Citation: Xpn Argue Like Cobalt 2019)

Adversaries may manipulate a process PEB to evade defenses. For example, [Process Hollowing](https://attack.mitre.org/techniques/T1055/012) can be abused to spawn a process in a suspended state with benign arguments. After the process is spawned and the PEB is initialized (and process information is potentially logged by tools/sensors), adversaries may override the PEB to modify the command-line arguments (ex: using the [Native API](https://attack.mitre.org/techniques/T1106) <code>WriteProcessMemory()</code> function) then resume process execution with malicious arguments.(Citation: Cobalt Strike Arguments 2019)(Citation: Xpn Argue Like Cobalt 2019)(Citation: Nviso Spoof Command Line 2020)

Adversaries may also execute a process with malicious command-line arguments then patch the memory with benign arguments that may bypass subsequent process memory analysis.(Citation: FireEye FiveHands April 2021)

This behavior may also be combined with other tricks (such as [Parent PID Spoofing](https://attack.mitre.org/techniques/T1134/004)) to manipulate or further evade process-based detections.

## Detection
Detection of process argument spoofing may be difficult as adversaries may momentarily modify stored arguments used for malicious execution. These changes may bypass process creation detection and/or later process memory analysis. Consider monitoring for [Process Hollowing](https://attack.mitre.org/techniques/T1055/012), which includes monitoring for process creation (especially those in a suspended state) as well as access and/or modifications of these processes (especially by the parent process) via Windows API calls.(Citation: Nviso Spoof Command Line 2020)(Citation: Mandiant Endpoint Evading 2019)

Analyze process behavior to determine if a process is performing actions it usually does not and/or do no align with its logged command-line arguments.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1564/010)
- [Microsoft PEB 2021](https://docs.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb)
- [Xpn Argue Like Cobalt 2019](https://blog.xpnsec.com/how-to-argue-like-cobalt-strike/)
- [Cobalt Strike Arguments 2019](https://blog.cobaltstrike.com/2019/01/02/cobalt-strike-3-13-why-do-we-argue/)
- [Nviso Spoof Command Line 2020](https://blog.nviso.eu/2020/02/04/the-return-of-the-spoof-part-2-command-line-spoofing/)
- [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [Mandiant Endpoint Evading 2019](https://www.mandiant.com/resources/staying-hidden-on-the-endpoint-evading-detection-with-shellcode)
