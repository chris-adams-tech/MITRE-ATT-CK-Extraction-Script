---
contributors:
- Erye Hernandez, Palo Alto Networks
data_sources:
- 'File: File Metadata'
id: attack-pattern--e51137a5-1cdc-499e-911a-abaedaa5ac86
mitre_attack_url: https://attack.mitre.org/techniques/T1036/006
name: Space after Filename
platforms:
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - Space after Filename
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS |
| **Data Sources** | File: File Metadata |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/006](https://attack.mitre.org/techniques/T1036/006) |

# Space after Filename (attack-pattern--e51137a5-1cdc-499e-911a-abaedaa5ac86)

## Description
Adversaries can hide a program's true filetype by changing the extension of a file. With certain file types (specifically this does not work with .app extensions), appending a space to the end of a filename will change how the file is processed by the operating system.

For example, if there is a Mach-O executable file called <code>evil.bin</code>, when it is double clicked by a user, it will launch Terminal.app and execute. If this file is renamed to <code>evil.txt</code>, then when double clicked by a user, it will launch with the default text editing application (not executing the binary). However, if the file is renamed to <code>evil.txt </code> (note the space at the end), then when double clicked by a user, the true file type is determined by the OS and handled appropriately and the binary will be executed (Citation: Mac Backdoors are back).

Adversaries can use this feature to trick users into double clicking benign-looking files of any format and ultimately executing something malicious.

## Detection
It's not common for spaces to be at the end of filenames, so this is something that can easily be checked with file monitoring. From the user's perspective though, this is very hard to notice from within the Finder.app or on the command-line in Terminal.app. Processes executed from binaries containing non-standard extensions in the filename are suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/006)
- [Mac Backdoors are back](https://arstechnica.com/security/2016/07/after-hiatus-in-the-wild-mac-backdoors-are-suddenly-back/)
