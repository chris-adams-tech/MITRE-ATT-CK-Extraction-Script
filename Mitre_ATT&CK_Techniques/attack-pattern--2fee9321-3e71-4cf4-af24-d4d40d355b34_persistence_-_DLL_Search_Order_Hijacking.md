---
contributors:
- Travis Smith, Tripwire
- Stefan Kanthak
- Marina Liang
- Ami Holeston, CrowdStrike
- Will Alexander, CrowdStrike
data_sources:
- 'File: File Modification'
- 'Module: Module Load'
- 'File: File Creation'
id: attack-pattern--2fee9321-3e71-4cf4-af24-d4d40d355b34
mitre_attack_url: https://attack.mitre.org/techniques/T1574/001
name: DLL Search Order Hijacking
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - DLL Search Order Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | File: File Modification, Module: Module Load, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/001](https://attack.mitre.org/techniques/T1574/001) |

# DLL Search Order Hijacking (attack-pattern--2fee9321-3e71-4cf4-af24-d4d40d355b34)

## Description
Adversaries may execute their own malicious payloads by hijacking the search order used to load DLLs. Windows systems use a common method to look for required DLLs to load into a program. (Citation: Microsoft Dynamic Link Library Search Order)(Citation: FireEye Hijacking July 2010) Hijacking DLL loads may be for the purpose of establishing persistence as well as elevating privileges and/or evading restrictions on file execution.

There are many ways an adversary can hijack DLL loads. Adversaries may plant trojan dynamic-link library files (DLLs) in a directory that will be searched before the location of a legitimate library that will be requested by a program, causing Windows to load their malicious library when it is called for by the victim program. Adversaries may also perform DLL preloading, also called binary planting attacks, (Citation: OWASP Binary Planting) by placing a malicious DLL with the same name as an ambiguously specified DLL in a location that Windows searches before the legitimate DLL. Often this location is the current working directory of the program.(Citation: FireEye fxsst June 2011) Remote DLL preloading attacks occur when a program sets its current directory to a remote location such as a Web share before loading a DLL. (Citation: Microsoft Security Advisory 2269637)

Phantom DLL hijacking is a specific type of DLL search order hijacking where adversaries target references to non-existent DLL files.(Citation: Hexacorn DLL Hijacking)(Citation: Adversaries Hijack DLLs) They may be able to load their own malicious DLL by planting it with the correct name in the location of the missing module.

Adversaries may also directly modify the search order via DLL redirection, which after being enabled (in the Registry and creation of a redirection file) may cause a program to load a different DLL.(Citation: Microsoft Dynamic-Link Library Redirection)(Citation: Microsoft Manifests)(Citation: FireEye DLL Search Order Hijacking)

If a search order-vulnerable program is configured to run at a higher privilege level, then the adversary-controlled DLL that is loaded will also be executed at the higher level. In this case, the technique could be used for privilege escalation from user to administrator or SYSTEM or from administrator to SYSTEM, depending on the program. Programs that fall victim to path hijacking may appear to behave normally because malicious DLLs may be configured to also load the legitimate DLLs they were meant to replace.

## Detection
Monitor file systems for moving, renaming, replacing, or modifying DLLs. Changes in the set of DLLs that are loaded by a process (compared with past behavior) that do not correlate with known software, patches, etc., are suspicious. Monitor DLLs loaded into a process and detect DLLs that have the same file name but abnormal paths. Modifications to or creation of `.manifest` and `.local` redirection files that do not correlate with software updates are suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/001)
- [Adversaries Hijack DLLs](https://www.crowdstrike.com/blog/4-ways-adversaries-hijack-dlls/)
- [FireEye Hijacking July 2010](https://www.fireeye.com/blog/threat-research/2010/07/malware-persistence-windows-registry.html)
- [FireEye fxsst June 2011](https://www.fireeye.com/blog/threat-research/2011/06/fxsst.html)
- [Hexacorn DLL Hijacking](https://www.hexacorn.com/blog/2013/12/08/beyond-good-ol-run-key-part-5/)
- [Microsoft Security Advisory 2269637](https://docs.microsoft.com/en-us/security-updates/securityadvisories/2010/2269637)
- [Microsoft Dynamic-Link Library Redirection](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-redirection?redirectedfrom=MSDN)
- [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)
- [Microsoft Manifests](https://msdn.microsoft.com/en-US/library/aa375365)
- [FireEye DLL Search Order Hijacking](https://www.fireeye.com/blog/threat-research/2010/08/dll-search-order-hijacking-revisited.html)
- [OWASP Binary Planting](https://www.owasp.org/index.php/Binary_planting)
