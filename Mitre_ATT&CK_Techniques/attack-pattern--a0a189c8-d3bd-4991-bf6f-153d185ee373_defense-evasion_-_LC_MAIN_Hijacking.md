---
id: attack-pattern--a0a189c8-d3bd-4991-bf6f-153d185ee373
mitre_attack_url: https://attack.mitre.org/techniques/T1149
name: LC_MAIN Hijacking
platforms:
- macOS
tactics:
- defense-evasion
title: defense-evasion - LC_MAIN Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1149](https://attack.mitre.org/techniques/T1149) |

# LC_MAIN Hijacking (attack-pattern--a0a189c8-d3bd-4991-bf6f-153d185ee373)

## Description
**This technique has been deprecated and should no longer be used.**

As of OS X 10.8, mach-O binaries introduced a new header called LC_MAIN that points to the binary’s entry point for execution. Previously, there were two headers to achieve this same effect: LC_THREAD and LC_UNIXTHREAD  (Citation: Prolific OSX Malware History). The entry point for a binary can be hijacked so that initial execution flows to a malicious addition (either another section or a code cave) and then goes back to the initial entry point so that the victim doesn’t know anything was different  (Citation: Methods of Mac Malware Persistence). By modifying a binary in this way, application whitelisting can be bypassed because the file name or application path is still the same.

## Detection
Determining the original entry point for a binary is difficult, but checksum and signature verification is very possible. Modifying the LC_MAIN entry point or adding in an additional LC_MAIN entry point invalidates the signature for the file and can be detected. Collect running process information and compare against known applications to look for suspicious behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1149)
- [Prolific OSX Malware History](https://assets.documentcloud.org/documents/2459197/bit9-carbon-black-threat-research-report-2015.pdf)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
