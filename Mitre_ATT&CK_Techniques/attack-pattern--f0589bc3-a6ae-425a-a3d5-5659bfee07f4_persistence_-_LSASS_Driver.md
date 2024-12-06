---
contributors:
- Vincent Le Toux
data_sources:
- 'Module: Module Load'
- 'File: File Creation'
- 'Driver: Driver Load'
- 'File: File Modification'
id: attack-pattern--f0589bc3-a6ae-425a-a3d5-5659bfee07f4
mitre_attack_url: https://attack.mitre.org/techniques/T1547/008
name: LSASS Driver
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - LSASS Driver
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Module: Module Load, File: File Creation, Driver: Driver Load, File: File Modification |
| **Permissions Required** | SYSTEM, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/008](https://attack.mitre.org/techniques/T1547/008) |

# LSASS Driver (attack-pattern--f0589bc3-a6ae-425a-a3d5-5659bfee07f4)

## Description
Adversaries may modify or add LSASS drivers to obtain persistence on compromised systems. The Windows security subsystem is a set of components that manage and enforce the security policy for a computer or domain. The Local Security Authority (LSA) is the main component responsible for local security policy and user authentication. The LSA includes multiple dynamic link libraries (DLLs) associated with various other security functions, all of which run in the context of the LSA Subsystem Service (LSASS) lsass.exe process.(Citation: Microsoft Security Subsystem)

Adversaries may target LSASS drivers to obtain persistence. By either replacing or adding illegitimate drivers (e.g., [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574)), an adversary can use LSA operations to continuously execute malicious payloads.

## Detection
With LSA Protection enabled, monitor the event logs (Events 3033 and 3063) for failed attempts to load LSA plug-ins and drivers. (Citation: Microsoft LSA Protection Mar 2014) Also monitor DLL load operations in lsass.exe. (Citation: Microsoft DLL Security)

Utilize the Sysinternals Autoruns/Autorunsc utility (Citation: TechNet Autoruns) to examine loaded drivers associated with the LSA. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/008)
- [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)
- [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)
- [Microsoft Security Subsystem](https://technet.microsoft.com/library/cc961760.aspx)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
