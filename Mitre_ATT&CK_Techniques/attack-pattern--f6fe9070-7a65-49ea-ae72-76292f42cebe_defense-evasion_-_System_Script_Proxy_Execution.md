---
contributors:
- Praetorian
- Wes Hurd
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Script: Script Execution'
id: attack-pattern--f6fe9070-7a65-49ea-ae72-76292f42cebe
mitre_attack_url: https://attack.mitre.org/techniques/T1216
name: System Script Proxy Execution
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - System Script Proxy Execution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation, Script: Script Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1216](https://attack.mitre.org/techniques/T1216) |

# System Script Proxy Execution (attack-pattern--f6fe9070-7a65-49ea-ae72-76292f42cebe)

## Description
Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files. Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be used to proxy execution of other files.(Citation: LOLBAS Project) This behavior may be abused by adversaries to execute malicious files that could bypass application control and signature validation on systems.(Citation: GitHub Ultimate AppLocker Bypass List)

## Detection
Monitor script processes, such as `cscript`, and command-line parameters for scripts like PubPrn.vbs that may be used to proxy execution of malicious files.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1216)
- [GitHub Ultimate AppLocker Bypass List](https://github.com/api0cradle/UltimateAppLockerByPassList)
- [LOLBAS Project](https://github.com/LOLBAS-Project/LOLBAS#criteria)
