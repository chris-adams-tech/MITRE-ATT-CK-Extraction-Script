---
contributors:
- Ye Yint Min Thu Htut, Offensive Security Team, DBS Bank
- Praetorian
id: attack-pattern--cf7b3a06-8b42-4c33-bbe9-012120027925
mitre_attack_url: https://attack.mitre.org/techniques/T1500
name: Compile After Delivery
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Compile After Delivery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Permissions Required** | User |
| **System Requirements** | Compiler software (either native to the system or delivered by the adversary) |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1500](https://attack.mitre.org/techniques/T1500) |

# Compile After Delivery (attack-pattern--cf7b3a06-8b42-4c33-bbe9-012120027925)

## Description
Adversaries may attempt to make payloads difficult to discover and analyze by delivering files to victims as uncompiled code. Similar to [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027), text-based source code files may subvert analysis and scrutiny from protections targeting executables/binaries. These payloads will need to be compiled before execution; typically via native utilities such as csc.exe or GCC/MinGW.(Citation: ClearSky MuddyWater Nov 2018)

Source code payloads may also be encrypted, encoded, and/or embedded within other files, such as those delivered as a [Spearphishing Attachment](https://attack.mitre.org/techniques/T1193). Payloads may also be delivered in formats unrecognizable and inherently benign to the native OS (ex: EXEs on macOS/Linux) before later being (re)compiled into a proper executable binary with a bundled compiler and execution framework.(Citation: TrendMicro WindowsAppMac)


## Detection
Monitor the execution file paths and command-line arguments for common compilers, such as csc.exe and GCC/MinGW, and correlate with other suspicious behavior to reduce false positives from normal user and administrator behavior. The compilation of payloads may also generate file creation and/or file write events. Look for non-native binary formats and cross-platform compiler and execution frameworks like Mono and determine if they have a legitimate purpose on the system.(Citation: TrendMicro WindowsAppMac) Typically these should only be used in specific and limited cases, like for software development.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1500)
- [ClearSky MuddyWater Nov 2018](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)
- [TrendMicro WindowsAppMac](https://blog.trendmicro.com/trendlabs-security-intelligence/windows-app-runs-on-mac-downloads-info-stealer-and-adware/)
