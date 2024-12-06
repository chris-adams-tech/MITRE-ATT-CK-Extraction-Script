---
contributors:
- Vincent Le Toux
id: attack-pattern--6e6845c2-347a-4a6f-a2d1-b74a18ebd352
mitre_attack_url: https://attack.mitre.org/techniques/T1177
name: LSASS Driver
platforms:
- Windows
tactics:
- execution
- persistence
title: execution - LSASS Driver
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, persistence |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1177](https://attack.mitre.org/techniques/T1177) |

# LSASS Driver (attack-pattern--6e6845c2-347a-4a6f-a2d1-b74a18ebd352)

## Description
The Windows security subsystem is a set of components that manage and enforce the security policy for a computer or domain. The Local Security Authority (LSA) is the main component responsible for local security policy and user authentication. The LSA includes multiple dynamic link libraries (DLLs) associated with various other security functions, all of which run in the context of the LSA Subsystem Service (LSASS) lsass.exe process. (Citation: Microsoft Security Subsystem)

Adversaries may target lsass.exe drivers to obtain execution and/or persistence. By either replacing or adding illegitimate drivers (e.g., [DLL Side-Loading](https://attack.mitre.org/techniques/T1073) or [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1038)), an adversary can achieve arbitrary code execution triggered by continuous LSA operations.

## Detection
With LSA Protection enabled, monitor the event logs (Events 3033 and 3063) for failed attempts to load LSA plug-ins and drivers. (Citation: Microsoft LSA Protection Mar 2014)

Utilize the Sysinternals Autoruns/Autorunsc utility (Citation: TechNet Autoruns) to examine loaded drivers associated with the LSA.

Utilize the Sysinternals Process Monitor utility to monitor DLL load operations in lsass.exe. (Citation: Microsoft DLL Security)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1177)
- [Microsoft Security Subsystem](https://technet.microsoft.com/library/cc961760.aspx)
- [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
- [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)
