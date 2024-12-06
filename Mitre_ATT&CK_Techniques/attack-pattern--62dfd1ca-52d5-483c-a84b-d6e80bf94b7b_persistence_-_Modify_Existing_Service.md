---
contributors:
- Travis Smith, Tripwire
- Matthew Demaske, Adaptforward
id: attack-pattern--62dfd1ca-52d5-483c-a84b-d6e80bf94b7b
mitre_attack_url: https://attack.mitre.org/techniques/T1031
name: Modify Existing Service
platforms:
- Windows
tactics:
- persistence
title: persistence - Modify Existing Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1031](https://attack.mitre.org/techniques/T1031) |

# Modify Existing Service (attack-pattern--62dfd1ca-52d5-483c-a84b-d6e80bf94b7b)

## Description
Windows service configuration information, including the file path to the service's executable or recovery programs/commands, is stored in the Registry. Service configurations can be modified using utilities such as sc.exe and [Reg](https://attack.mitre.org/software/S0075).

Adversaries can modify an existing service to persist malware on a system by using system utilities or by using custom tools to interact with the Windows API. Use of existing services is a type of [Masquerading](https://attack.mitre.org/techniques/T1036) that may make detection analysis more challenging. Modifying existing services may interrupt their functionality or may enable services that are disabled or otherwise not commonly used.

Adversaries may also intentionally corrupt or kill services to execute malicious recovery programs/commands. (Citation: Twitter Service Recovery Nov 2017) (Citation: Microsoft Service Recovery Feb 2013)

## Detection
Look for changes to service Registry entries that do not correlate with known software, patch cycles, etc. Changes to the binary path and the service startup type changed from manual or disabled to automatic, if it does not typically do so, may be suspicious. Tools such as Sysinternals Autoruns may also be used to detect system service changes that could be attempts at persistence. (Citation: TechNet Autoruns) 

Service information is stored in the Registry at <code>HKLM\SYSTEM\CurrentControlSet\Services</code>.

Command-line invocation of tools capable of modifying services may be unusual, depending on how systems are typically used in a particular environment. Collect service utility execution and service binary path arguments used for analysis. Service binary paths may even be changed to execute [cmd](https://attack.mitre.org/software/S0106) commands or scripts.

Look for abnormal process call trees from known services and for execution of other commands that could relate to Discovery or other adversary techniques. Services may also be modified through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1086), so additional logging may need to be configured to gather the appropriate data.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1031)
- [capec](https://capec.mitre.org/data/definitions/551.html)
- [Twitter Service Recovery Nov 2017](https://twitter.com/r0wdy_/status/936365549553991680)
- [Microsoft Service Recovery Feb 2013](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753662(v=ws.11))
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
