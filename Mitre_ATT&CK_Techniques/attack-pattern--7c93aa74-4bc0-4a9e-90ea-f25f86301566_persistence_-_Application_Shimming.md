---
id: attack-pattern--7c93aa74-4bc0-4a9e-90ea-f25f86301566
mitre_attack_url: https://attack.mitre.org/techniques/T1138
name: Application Shimming
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Application Shimming
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1138](https://attack.mitre.org/techniques/T1138) |

# Application Shimming (attack-pattern--7c93aa74-4bc0-4a9e-90ea-f25f86301566)

## Description
The Microsoft Windows Application Compatibility Infrastructure/Framework (Application Shim) was created to allow for backward compatibility of software as the operating system codebase changes over time. For example, the application shimming feature allows developers to apply fixes to applications (without rewriting code) that were created for Windows XP so that it will work with Windows 10. (Citation: Elastic Process Injection July 2017) Within the framework, shims are created to act as a buffer between the program (or more specifically, the Import Address Table) and the Windows OS. When a program is executed, the shim cache is referenced to determine if the program requires the use of the shim database (.sdb). If so, the shim database uses [Hooking](https://attack.mitre.org/techniques/T1179) to redirect the code as necessary in order to communicate with the OS. 

A list of all shims currently installed by the default Windows installer (sdbinst.exe) is kept in:

* <code>%WINDIR%\AppPatch\sysmain.sdb</code>
* <code>hklm\software\microsoft\windows nt\currentversion\appcompatflags\installedsdb</code>

Custom databases are stored in:

* <code>%WINDIR%\AppPatch\custom & %WINDIR%\AppPatch\AppPatch64\Custom</code>
* <code>hklm\software\microsoft\windows nt\currentversion\appcompatflags\custom</code>

To keep shims secure, Windows designed them to run in user mode so they cannot modify the kernel and you must have administrator privileges to install a shim. However, certain shims can be used to [Bypass User Account Control](https://attack.mitre.org/techniques/T1088) (UAC) (RedirectEXE), inject DLLs into processes (InjectDLL), disable Data Execution Prevention (DisableNX) and Structure Exception Handling (DisableSEH), and intercept memory addresses (GetProcAddress). Similar to [Hooking](https://attack.mitre.org/techniques/T1179), utilizing these shims may allow an adversary to perform several malicious acts such as elevate privileges, install backdoors, disable defenses like Windows Defender, etc.

## Detection
There are several public tools available that will detect shims that are currently available (Citation: Black Hat 2015 App Shim):

* Shim-Process-Scanner - checks memory of every running process for any Shim flags
* Shim-Detector-Lite - detects installation of custom shim databases
* Shim-Guard - monitors registry for any shim installations
* ShimScanner - forensic tool to find active shims in memory
* ShimCacheMem - Volatility plug-in that pulls shim cache from memory (note: shims are only cached after reboot)

Monitor process execution for sdbinst.exe and command-line arguments for potential indications of application shim abuse.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1138)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [Black Hat 2015 App Shim](https://www.blackhat.com/docs/eu-15/materials/eu-15-Pierce-Defending-Against-Malicious-Application-Compatibility-Shims-wp.pdf)
