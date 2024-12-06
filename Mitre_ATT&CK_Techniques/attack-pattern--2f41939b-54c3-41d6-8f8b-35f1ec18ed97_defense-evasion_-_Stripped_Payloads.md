---
data_sources:
- 'File: File Metadata'
id: attack-pattern--2f41939b-54c3-41d6-8f8b-35f1ec18ed97
mitre_attack_url: https://attack.mitre.org/techniques/T1027/008
name: Stripped Payloads
platforms:
- macOS
- Linux
- Windows
- Network
tactics:
- defense-evasion
title: defense-evasion - Stripped Payloads
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Linux, Windows, Network |
| **Data Sources** | File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/008](https://attack.mitre.org/techniques/T1027/008) |

# Stripped Payloads (attack-pattern--2f41939b-54c3-41d6-8f8b-35f1ec18ed97)

## Description
Adversaries may attempt to make a payload difficult to analyze by removing symbols, strings, and other human readable information. Scripts and executables may contain variables names and other strings that help developers document code functionality. Symbols are often created by an operating system’s `linker` when executable payloads are compiled. Reverse engineers use these symbols and strings to analyze code and to identify functionality in payloads.(Citation: Mandiant golang stripped binaries explanation)(Citation: intezer stripped binaries elf files 2018)

Adversaries may use stripped payloads in order to make malware analysis more difficult. For example, compilers and other tools may provide features to remove or obfuscate strings and symbols. Adversaries have also used stripped payload formats, such as run-only AppleScripts, a compiled and stripped version of [AppleScript](https://attack.mitre.org/techniques/T1059/002), to evade detection and analysis. The lack of human-readable information may directly hinder detection and analysis of payloads.(Citation: SentinelLabs reversing run-only applescripts 2021)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/008)
- [intezer stripped binaries elf files 2018](https://www.intezer.com/blog/malware-analysis/executable-linkable-format-101-part-2-symbols/)
- [SentinelLabs reversing run-only applescripts 2021](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)
- [Mandiant golang stripped binaries explanation](https://www.mandiant.com/resources/blog/golang-internals-symbol-recovery)
