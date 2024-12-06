---
data_sources:
- 'Module: Module Load'
- 'File: File Metadata'
- 'Process: OS API Execution'
id: attack-pattern--ea4c2f9c-9df1-477c-8c42-6da1118f2ac4
mitre_attack_url: https://attack.mitre.org/techniques/T1027/007
name: Dynamic API Resolution
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Dynamic API Resolution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Module: Module Load, File: File Metadata, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/007](https://attack.mitre.org/techniques/T1027/007) |

# Dynamic API Resolution (attack-pattern--ea4c2f9c-9df1-477c-8c42-6da1118f2ac4)

## Description
Adversaries may obfuscate then dynamically resolve API functions called by their malware in order to conceal malicious functionalities and impair defensive analysis. Malware commonly uses various [Native API](https://attack.mitre.org/techniques/T1106) functions provided by the OS to perform various tasks such as those involving processes, files, and other system artifacts.

API functions called by malware may leave static artifacts such as strings in payload files. Defensive analysts may also uncover which functions a binary file may execute via an import address table (IAT) or other structures that help dynamically link calling code to the shared modules that provide functions.(Citation: Huntress API Hash)(Citation: IRED API Hashing)

To avoid static or other defensive analysis, adversaries may use dynamic API resolution to conceal malware characteristics and functionalities. Similar to [Software Packing](https://attack.mitre.org/techniques/T1027/002), dynamic API resolution may change file signatures and obfuscate malicious API function calls until they are resolved and invoked during runtime.

Various methods may be used to obfuscate malware calls to API functions. For example, hashes of function names are commonly stored in malware in lieu of literal strings. Malware can use these hashes (or other identifiers) to manually reproduce the linking and loading process using functions such as `GetProcAddress()` and `LoadLibrary()`. These hashes/identifiers can also be further obfuscated using encryption or other string manipulation tricks (requiring various forms of [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140) during execution).(Citation: BlackHat API Packers)(Citation: Drakonia HInvoke)(Citation: Huntress API Hash)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/007)
- [Huntress API Hash](https://www.huntress.com/blog/hackers-no-hashing-randomizing-api-hashes-to-evade-cobalt-strike-shellcode-detection)
- [BlackHat API Packers](https://www.blackhat.com/docs/us-15/materials/us-15-Choi-API-Deobfuscator-Resolving-Obfuscated-API-Functions-In-Modern-Packers.pdf)
- [Drakonia HInvoke](https://dr4k0nia.github.io/dotnet/coding/2022/08/10/HInvoke-and-avoiding-PInvoke.html?s=03)
- [IRED API Hashing](https://www.ired.team/offensive-security/defense-evasion/windows-api-hashing-in-malware)
