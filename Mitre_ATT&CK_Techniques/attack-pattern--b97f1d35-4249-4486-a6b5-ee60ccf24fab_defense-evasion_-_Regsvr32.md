---
contributors:
- Casey Smith
data_sources:
- 'Module: Module Load'
- 'Command: Command Execution'
- 'Network Traffic: Network Connection Creation'
- 'Process: Process Creation'
id: attack-pattern--b97f1d35-4249-4486-a6b5-ee60ccf24fab
mitre_attack_url: https://attack.mitre.org/techniques/T1218/010
name: Regsvr32
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Regsvr32
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Module: Module Load, Command: Command Execution, Network Traffic: Network Connection Creation, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/010](https://attack.mitre.org/techniques/T1218/010) |

# Regsvr32 (attack-pattern--b97f1d35-4249-4486-a6b5-ee60ccf24fab)

## Description
Adversaries may abuse Regsvr32.exe to proxy execution of malicious code. Regsvr32.exe is a command-line program used to register and unregister object linking and embedding controls, including dynamic link libraries (DLLs), on Windows systems. The Regsvr32.exe binary may also be signed by Microsoft. (Citation: Microsoft Regsvr32)

Malicious usage of Regsvr32.exe may avoid triggering security tools that may not monitor execution of, and modules loaded by, the regsvr32.exe process because of allowlists or false positives from Windows using regsvr32.exe for normal operations. Regsvr32.exe can also be used to specifically bypass application control using functionality to load COM scriptlets to execute DLLs under user permissions. Since Regsvr32.exe is network and proxy aware, the scripts can be loaded by passing a uniform resource locator (URL) to file on an external Web server as an argument during invocation. This method makes no changes to the Registry as the COM object is not actually registered, only executed. (Citation: LOLBAS Regsvr32) This variation of the technique is often referred to as a "Squiblydoo" and has been used in campaigns targeting governments. (Citation: Carbon Black Squiblydoo Apr 2016) (Citation: FireEye Regsvr32 Targeting Mongolian Gov)

Regsvr32.exe can also be leveraged to register a COM Object used to establish persistence via [Component Object Model Hijacking](https://attack.mitre.org/techniques/T1546/015). (Citation: Carbon Black Squiblydoo Apr 2016)

## Detection
Use process monitoring to monitor the execution and arguments of regsvr32.exe. Compare recent invocations of regsvr32.exe with prior history of known good arguments and loaded files to determine anomalous and potentially adversarial activity. Command arguments used before and after the regsvr32.exe invocation may also be useful in determining the origin and purpose of the script or DLL being loaded. (Citation: Carbon Black Squiblydoo Apr 2016)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/010)
- [FireEye Regsvr32 Targeting Mongolian Gov](https://www.fireeye.com/blog/threat-research/2017/02/spear_phishing_techn.html)
- [LOLBAS Regsvr32](https://lolbas-project.github.io/lolbas/Binaries/Regsvr32/)
- [Microsoft Regsvr32](https://support.microsoft.com/en-us/kb/249873)
- [Carbon Black Squiblydoo Apr 2016](https://www.carbonblack.com/2016/04/28/threat-advisory-squiblydoo-continues-trend-of-attackers-using-native-os-tools-to-live-off-the-land/)
