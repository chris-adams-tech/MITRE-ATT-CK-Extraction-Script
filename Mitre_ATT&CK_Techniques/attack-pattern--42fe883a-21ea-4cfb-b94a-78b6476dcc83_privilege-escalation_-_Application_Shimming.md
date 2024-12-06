---
data_sources:
- 'File: File Modification'
- 'Module: Module Load'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--42fe883a-21ea-4cfb-b94a-78b6476dcc83
mitre_attack_url: https://attack.mitre.org/techniques/T1546/011
name: Application Shimming
platforms:
- Windows
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Application Shimming
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Windows |
| **Data Sources** | File: File Modification, Module: Module Load, Windows Registry: Windows Registry Key Modification, Command: Command Execution, Process: Process Creation |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/011](https://attack.mitre.org/techniques/T1546/011) |

# Application Shimming (attack-pattern--42fe883a-21ea-4cfb-b94a-78b6476dcc83)

## Description
Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by application shims. The Microsoft Windows Application Compatibility Infrastructure/Framework (Application Shim) was created to allow for backward compatibility of software as the operating system codebase changes over time. For example, the application shimming feature allows developers to apply fixes to applications (without rewriting code) that were created for Windows XP so that it will work with Windows 10. (Citation: Elastic Process Injection July 2017)

Within the framework, shims are created to act as a buffer between the program (or more specifically, the Import Address Table) and the Windows OS. When a program is executed, the shim cache is referenced to determine if the program requires the use of the shim database (.sdb). If so, the shim database uses hooking to redirect the code as necessary in order to communicate with the OS. 

A list of all shims currently installed by the default Windows installer (sdbinst.exe) is kept in:

* <code>%WINDIR%\AppPatch\sysmain.sdb</code> and
* <code>hklm\software\microsoft\windows nt\currentversion\appcompatflags\installedsdb</code>

Custom databases are stored in:

* <code>%WINDIR%\AppPatch\custom & %WINDIR%\AppPatch\AppPatch64\Custom</code> and
* <code>hklm\software\microsoft\windows nt\currentversion\appcompatflags\custom</code>

To keep shims secure, Windows designed them to run in user mode so they cannot modify the kernel and you must have administrator privileges to install a shim. However, certain shims can be used to [Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002) (UAC and RedirectEXE), inject DLLs into processes (InjectDLL), disable Data Execution Prevention (DisableNX) and Structure Exception Handling (DisableSEH), and intercept memory addresses (GetProcAddress).

Utilizing these shims may allow an adversary to perform several malicious acts such as elevate privileges, install backdoors, disable defenses like Windows Defender, etc. (Citation: FireEye Application Shimming) Shims can also be abused to establish persistence by continuously being invoked by affected programs.

## Detection
There are several public tools available that will detect shims that are currently available (Citation: Black Hat 2015 App Shim):

* Shim-Process-Scanner - checks memory of every running process for any shim flags
* Shim-Detector-Lite - detects installation of custom shim databases
* Shim-Guard - monitors registry for any shim installations
* ShimScanner - forensic tool to find active shims in memory
* ShimCacheMem - Volatility plug-in that pulls shim cache from memory (note: shims are only cached after reboot)

Monitor process execution for sdbinst.exe and command-line arguments for potential indications of application shim abuse.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/011)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [FireEye Application Shimming](http://files.brucon.org/2015/Tomczak_and_Ballenthin_Shims_for_the_Win.pdf)
- [Black Hat 2015 App Shim](https://www.blackhat.com/docs/eu-15/materials/eu-15-Pierce-Defending-Against-Malicious-Application-Compatibility-Shims-wp.pdf)
