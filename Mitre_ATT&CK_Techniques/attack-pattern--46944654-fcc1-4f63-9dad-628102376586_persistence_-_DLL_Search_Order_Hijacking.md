---
contributors:
- Stefan Kanthak
- Travis Smith, Tripwire
id: attack-pattern--46944654-fcc1-4f63-9dad-628102376586
mitre_attack_url: https://attack.mitre.org/techniques/T1038
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
| **Permissions Required** | User, Administrator, SYSTEM |
| **System Requirements** | Ability to add a DLL, manifest file, or .local file, directory, or junction. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1038](https://attack.mitre.org/techniques/T1038) |

# DLL Search Order Hijacking (attack-pattern--46944654-fcc1-4f63-9dad-628102376586)

## Description
Windows systems use a common method to look for required DLLs to load into a program. (Citation: Microsoft DLL Search) Adversaries may take advantage of the Windows DLL search order and programs that ambiguously specify DLLs to gain privilege escalation and persistence. 

Adversaries may perform DLL preloading, also called binary planting attacks, (Citation: OWASP Binary Planting) by placing a malicious DLL with the same name as an ambiguously specified DLL in a location that Windows searches before the legitimate DLL. Often this location is the current working directory of the program. Remote DLL preloading attacks occur when a program sets its current directory to a remote location such as a Web share before loading a DLL. (Citation: Microsoft 2269637) Adversaries may use this behavior to cause the program to load a malicious DLL. 

Adversaries may also directly modify the way a program loads DLLs by replacing an existing DLL or modifying a .manifest or .local redirection file, directory, or junction to cause the program to load a different DLL to maintain persistence or privilege escalation. (Citation: Microsoft DLL Redirection) (Citation: Microsoft Manifests) (Citation: Mandiant Search Order)

If a search order-vulnerable program is configured to run at a higher privilege level, then the adversary-controlled DLL that is loaded will also be executed at the higher level. In this case, the technique could be used for privilege escalation from user to administrator or SYSTEM or from administrator to SYSTEM, depending on the program.

Programs that fall victim to path hijacking may appear to behave normally because malicious DLLs may be configured to also load the legitimate DLLs they were meant to replace.

## Detection
Monitor file systems for moving, renaming, replacing, or modifying DLLs. Changes in the set of DLLs that are loaded by a process (compared with past behavior) that do not correlate with known software, patches, etc., are suspicious. Monitor DLLs loaded into a process and detect DLLs that have the same file name but abnormal paths. Modifications to or creation of .manifest and .local redirection files that do not correlate with software updates are suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1038)
- [capec](https://capec.mitre.org/data/definitions/471.html)
- [Microsoft DLL Search](http://msdn.microsoft.com/en-US/library/ms682586)
- [OWASP Binary Planting](https://www.owasp.org/index.php/Binary_planting)
- [Microsoft 2269637](https://msrc-blog.microsoft.com/2010/08/21/microsoft-security-advisory-2269637-released/)
- [Microsoft DLL Redirection](http://msdn.microsoft.com/en-US/library/ms682600)
- [Microsoft Manifests](https://msdn.microsoft.com/en-US/library/aa375365)
- [Mandiant Search Order](https://www.mandiant.com/blog/dll-search-order-hijacking-revisited/)
