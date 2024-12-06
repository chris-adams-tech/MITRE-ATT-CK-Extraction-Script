---
data_sources:
- 'Module: Module Load'
- 'File: File Creation'
- 'File: File Modification'
id: attack-pattern--fc742192-19e3-466c-9eb5-964a97b29490
mitre_attack_url: https://attack.mitre.org/techniques/T1574/004
name: Dylib Hijacking
platforms:
- macOS
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - Dylib Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | macOS |
| **Data Sources** | Module: Module Load, File: File Creation, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/004](https://attack.mitre.org/techniques/T1574/004) |

# Dylib Hijacking (attack-pattern--fc742192-19e3-466c-9eb5-964a97b29490)

## Description
Adversaries may execute their own payloads by placing a malicious dynamic library (dylib) with an expected name in a path a victim application searches at runtime. The dynamic loader will try to find the dylibs based on the sequential order of the search paths. Paths to dylibs may be prefixed with <code>@rpath</code>, which allows developers to use relative paths to specify an array of search paths used at runtime based on the location of the executable.  Additionally, if weak linking is used, such as the <code>LC_LOAD_WEAK_DYLIB</code> function, an application will still execute even if an expected dylib is not present. Weak linking enables developers to run an application on multiple macOS versions as new APIs are added.

Adversaries may gain execution by inserting malicious dylibs with the name of the missing dylib in the identified path.(Citation: Wardle Dylib Hijack Vulnerable Apps)(Citation: Wardle Dylib Hijacking OSX 2015)(Citation: Github EmpireProject HijackScanner)(Citation: Github EmpireProject CreateHijacker Dylib) Dylibs are loaded into an application's address space allowing the malicious dylib to inherit the application's privilege level and resources. Based on the application, this could result in privilege escalation and uninhibited network access. This method may also evade detection from security products since the execution is masked under a legitimate process.(Citation: Writing Bad Malware for OSX)(Citation: wardle artofmalware volume1)(Citation: MalwareUnicorn macOS Dylib Injection MachO)

## Detection
Monitor file systems for moving, renaming, replacing, or modifying dylibs. Changes in the set of dylibs that are loaded by a process (compared to past behavior) that do not correlate with known software, patches, etc., are suspicious. Check the system for multiple dylibs with the same name and monitor which versions have historically been loaded into a process. 

Run path dependent libraries can include <code>LC_LOAD_DYLIB</code>, <code>LC_LOAD_WEAK_DYLIB</code>, and <code>LC_RPATH</code>. Other special keywords are recognized by the macOS loader are <code>@rpath</code>, <code>@loader_path</code>, and <code>@executable_path</code>.(Citation: Apple Developer Doco Archive Run-Path) These loader instructions can be examined for individual binaries or frameworks using the <code>otool -l</code> command. Objective-See's Dylib Hijacking Scanner can be used to identify applications vulnerable to dylib hijacking.(Citation: Wardle Dylib Hijack Vulnerable Apps)(Citation: Github EmpireProject HijackScanner)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/004)
- [MalwareUnicorn macOS Dylib Injection MachO](https://malwareunicorn.org/workshops/macos_dylib_injection.html#5)
- [Apple Developer Doco Archive Run-Path](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/RunpathDependentLibraries.html)
- [Wardle Dylib Hijacking OSX 2015](https://www.virusbulletin.com/uploads/pdf/magazine/2015/vb201503-dylib-hijacking.pdf)
- [Writing Bad Malware for OSX](https://www.blackhat.com/docs/us-15/materials/us-15-Wardle-Writing-Bad-A-Malware-For-OS-X.pdf)
- [Wardle Dylib Hijack Vulnerable Apps](https://objective-see.com/blog/blog_0x46.html)
- [wardle artofmalware volume1](https://taomm.org/vol1/pdfs.html)
- [Github EmpireProject HijackScanner](https://github.com/EmpireProject/Empire/blob/master/lib/modules/python/situational_awareness/host/osx/HijackScanner.py)
- [Github EmpireProject CreateHijacker Dylib](https://github.com/EmpireProject/Empire/blob/08cbd274bef78243d7a8ed6443b8364acd1fc48b/lib/modules/python/persistence/osx/CreateHijacker.py)
