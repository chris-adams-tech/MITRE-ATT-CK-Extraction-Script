---
contributors:
- Jorell Magtibay, National Australia Bank Limited
- Kiyohito Yamamoto, RedLark, NTT Communications
- Yusuke Kubo, RedLark, NTT Communications
data_sources:
- 'Windows Registry: Windows Registry Key Creation'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
id: attack-pattern--28170e17-8384-415c-8486-2e6b294cb803
mitre_attack_url: https://attack.mitre.org/techniques/T1562/009
name: Safe Mode Boot
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Safe Mode Boot
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Creation, Process: Process Creation, Windows Registry: Windows Registry Key Modification, Command: Command Execution |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/009](https://attack.mitre.org/techniques/T1562/009) |

# Safe Mode Boot (attack-pattern--28170e17-8384-415c-8486-2e6b294cb803)

## Description
Adversaries may abuse Windows safe mode to disable endpoint defenses. Safe mode starts up the Windows operating system with a limited set of drivers and services. Third-party security software such as endpoint detection and response (EDR) tools may not start after booting Windows in safe mode. There are two versions of safe mode: Safe Mode and Safe Mode with Networking. It is possible to start additional services after a safe mode boot.(Citation: Microsoft Safe Mode)(Citation: Sophos Snatch Ransomware 2019)

Adversaries may abuse safe mode to disable endpoint defenses that may not start with a limited boot. Hosts can be forced into safe mode after the next reboot via modifications to Boot Configuration Data (BCD) stores, which are files that manage boot application settings.(Citation: Microsoft bcdedit 2021)

Adversaries may also add their malicious applications to the list of minimal services that start in safe mode by modifying relevant Registry values (i.e. [Modify Registry](https://attack.mitre.org/techniques/T1112)). Malicious [Component Object Model](https://attack.mitre.org/techniques/T1559/001) (COM) objects may also be registered and loaded in safe mode.(Citation: Sophos Snatch Ransomware 2019)(Citation: CyberArk Labs Safe Mode 2016)(Citation: Cybereason Nocturnus MedusaLocker 2020)(Citation: BleepingComputer REvil 2021)

## Detection
Monitor Registry modification and additions for services that may start on safe mode. For example, a program can be forced to start on safe mode boot by adding a <code>\*</code> in front of the "Startup" value name: <code>HKLM\Software\Microsoft\Windows\CurrentVersion\Run\["\*Startup"="{Path}"]</code> or by adding a key to <code>HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal</code>.(Citation: BleepingComputer REvil 2021)(Citation: Sophos Snatch Ransomware 2019)

Monitor execution of processes and commands associated with making configuration changes to boot settings, such as <code>bcdedit.exe</code> and <code>bootcfg.exe</code>.(Citation: Microsoft bcdedit 2021)(Citation: Microsoft Bootcfg)(Citation: Sophos Snatch Ransomware 2019)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/009)
- [Microsoft Safe Mode](https://support.microsoft.com/en-us/windows/start-your-pc-in-safe-mode-in-windows-10-92c27cff-db89-8644-1ce4-b3e5e56fe234)
- [Sophos Snatch Ransomware 2019](https://news.sophos.com/en-us/2019/12/09/snatch-ransomware-reboots-pcs-into-safe-mode-to-bypass-protection/)
- [Microsoft bcdedit 2021](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit)
- [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)
- [Cybereason Nocturnus MedusaLocker 2020](https://www.cybereason.com/blog/medusalocker-ransomware)
- [BleepingComputer REvil 2021](https://www.bleepingcomputer.com/news/security/revil-ransomware-has-a-new-windows-safe-mode-encryption-mode/)
- [Microsoft Bootcfg](https://docs.microsoft.com/windows-server/administration/windows-commands/bootcfg)
