---
contributors:
- Marina Liang
- "Wojciech Regu\u0142a @_r3ggi"
- Csaba Fitzl @theevilbit of Kandji
data_sources:
- 'Command: Command Execution'
- 'File: File Modification'
- 'Process: Process Creation'
id: attack-pattern--e8a0a025-3601-4755-abfb-8d08283329fb
mitre_attack_url: https://attack.mitre.org/techniques/T1548/006
name: TCC Manipulation
platforms:
- macOS
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - TCC Manipulation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | macOS |
| **Data Sources** | Command: Command Execution, File: File Modification, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1548/006](https://attack.mitre.org/techniques/T1548/006) |

# TCC Manipulation (attack-pattern--e8a0a025-3601-4755-abfb-8d08283329fb)

## Description
Adversaries can manipulate or abuse the Transparency, Consent, & Control (TCC) service or database to grant malicious executables elevated permissions. TCC is a Privacy & Security macOS control mechanism used to determine if the running process has permission to access the data or services protected by TCC, such as screen sharing, camera, microphone, or Full Disk Access (FDA).

When an application requests to access data or a service protected by TCC, the TCC daemon (`tccd`) checks the TCC database, located at `/Library/Application Support/com.apple.TCC/TCC.db` (and `~/` equivalent), and an overwrites file (if connected to an MDM) for existing permissions. If permissions do not exist, then the user is prompted to grant permission. Once permissions are granted, the database stores the application's permissions and will not prompt the user again unless reset. For example, when a web browser requests permissions to the user's webcam, once granted the web browser may not explicitly prompt the user again.(Citation: welivesecurity TCC)

Adversaries may access restricted data or services protected by TCC through abusing applications previously granted permissions through [Process Injection](https://attack.mitre.org/techniques/T1055) or executing a malicious binary using another application. For example, adversaries can use Finder, a macOS native app with FDA permissions, to execute a malicious [AppleScript](https://attack.mitre.org/techniques/T1059/002). When executing under the Finder App, the malicious [AppleScript](https://attack.mitre.org/techniques/T1059/002) inherits access to all files on the system without requiring a user prompt. When System Integrity Protection (SIP) is disabled, TCC protections are also disabled. For a system without SIP enabled, adversaries can manipulate the TCC database to add permissions to their malicious executable through loading an adversary controlled TCC database using environment variables and [Launchctl](https://attack.mitre.org/techniques/T1569/001).(Citation: TCC macOS bypass)(Citation: TCC Database)



## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1548/006)
- [welivesecurity TCC](https://www.welivesecurity.com/2022/07/19/i-see-what-you-did-there-look-cloudmensis-macos-spyware/)
- [TCC Database](https://interpressecurity.com/resources/return-of-the-macos-tcc/)
- [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)
