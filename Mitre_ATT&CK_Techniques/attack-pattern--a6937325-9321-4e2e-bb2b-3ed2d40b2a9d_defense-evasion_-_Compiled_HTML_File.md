---
contributors:
- Rahmat Nurfauzi, @infosecn1nja, PT Xynexis International
data_sources:
- 'File: File Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--a6937325-9321-4e2e-bb2b-3ed2d40b2a9d
mitre_attack_url: https://attack.mitre.org/techniques/T1218/001
name: Compiled HTML File
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Compiled HTML File
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | File: File Creation, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/001](https://attack.mitre.org/techniques/T1218/001) |

# Compiled HTML File (attack-pattern--a6937325-9321-4e2e-bb2b-3ed2d40b2a9d)

## Description
Adversaries may abuse Compiled HTML files (.chm) to conceal malicious code. CHM files are commonly distributed as part of the Microsoft HTML Help system. CHM files are compressed compilations of various content such as HTML documents, images, and scripting/web related programming languages such VBA, JScript, Java, and ActiveX. (Citation: Microsoft HTML Help May 2018) CHM content is displayed using underlying components of the Internet Explorer browser (Citation: Microsoft HTML Help ActiveX) loaded by the HTML Help executable program (hh.exe). (Citation: Microsoft HTML Help Executable Program)

A custom CHM file containing embedded payloads could be delivered to a victim then triggered by [User Execution](https://attack.mitre.org/techniques/T1204). CHM execution may also bypass application application control on older and/or unpatched systems that do not account for execution of binaries through hh.exe. (Citation: MsitPros CHM Aug 2017) (Citation: Microsoft CVE-2017-8625 Aug 2017)

## Detection
Monitor and analyze the execution and arguments of hh.exe. (Citation: MsitPros CHM Aug 2017) Compare recent invocations of hh.exe with prior history of known good arguments to determine anomalous and potentially adversarial activity (ex: obfuscated and/or malicious commands). Non-standard process execution trees may also indicate suspicious or malicious behavior, such as if hh.exe is the parent process for suspicious processes and activity relating to other adversarial techniques.

Monitor presence and use of CHM files, especially if they are not typically used within an environment.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/001)
- [Microsoft CVE-2017-8625 Aug 2017](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8625)
- [Microsoft HTML Help May 2018](https://docs.microsoft.com/previous-versions/windows/desktop/htmlhelp/microsoft-html-help-1-4-sdk)
- [Microsoft HTML Help Executable Program](https://msdn.microsoft.com/windows/desktop/ms524405)
- [Microsoft HTML Help ActiveX](https://msdn.microsoft.com/windows/desktop/ms644670)
- [MsitPros CHM Aug 2017](https://oddvar.moe/2017/08/13/bypassing-device-guard-umci-using-chm-cve-2017-8625/)
