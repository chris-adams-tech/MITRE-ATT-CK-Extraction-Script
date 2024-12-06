---
contributors:
- "Bilal Bahad\u0131r Yenici"
- Menachem Goldstein
data_sources:
- 'File: File Access'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--866d0d6d-02c6-42bd-aa2f-02907fdc0969
mitre_attack_url: https://attack.mitre.org/techniques/T1654
name: Log Enumeration
platforms:
- Linux
- macOS
- Windows
- IaaS
tactics:
- discovery
title: discovery - Log Enumeration
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows, IaaS |
| **Data Sources** | File: File Access, Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1654](https://attack.mitre.org/techniques/T1654) |

# Log Enumeration (attack-pattern--866d0d6d-02c6-42bd-aa2f-02907fdc0969)

## Description
Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records ([Account Discovery](https://attack.mitre.org/techniques/T1087)), security or vulnerable software ([Software Discovery](https://attack.mitre.org/techniques/T1518)), or hosts within a compromised network ([Remote System Discovery](https://attack.mitre.org/techniques/T1018)).

Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or [PowerShell](https://attack.mitre.org/techniques/T1059/001) on Windows to access and/or export security event information.(Citation: WithSecure Lazarus-NoPineapple Threat Intel Report 2023)(Citation: Cadet Blizzard emerges as novel threat actor) In cloud environments, adversaries may leverage utilities such as the Azure VM Agent’s `CollectGuestLogs.exe` to collect security logs from cloud hosted infrastructure.(Citation: SIM Swapping and Abuse of the Microsoft Azure Serial Console)

Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to adversary-controlled infrastructure for offline analysis.

In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses.(Citation: Permiso GUI-Vil 2023)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1654)
- [Permiso GUI-Vil 2023](https://permiso.io/blog/s/unmasking-guivil-new-cloud-threat-actor/)
- [SIM Swapping and Abuse of the Microsoft Azure Serial Console](https://www.mandiant.com/resources/blog/sim-swapping-abuse-azure-serial)
- [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [WithSecure Lazarus-NoPineapple Threat Intel Report 2023](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Lazarus-No-Pineapple-Threat-Intelligence-Report-2023.pdf)
