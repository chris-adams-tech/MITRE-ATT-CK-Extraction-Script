---
data_sources:
- 'Process: Process Creation'
- 'File: File Creation'
- 'File: File Metadata'
- 'Command: Command Execution'
id: attack-pattern--ec8fc7e2-b356-455c-8db5-2e37be158e7d
mitre_attack_url: https://attack.mitre.org/techniques/T1564/001
name: Hidden Files and Directories
platforms:
- Windows
- macOS
- Linux
tactics:
- defense-evasion
title: defense-evasion - Hidden Files and Directories
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Process: Process Creation, File: File Creation, File: File Metadata, Command: Command Execution |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1564/001](https://attack.mitre.org/techniques/T1564/001) |

# Hidden Files and Directories (attack-pattern--ec8fc7e2-b356-455c-8db5-2e37be158e7d)

## Description
Adversaries may set files and directories to be hidden to evade detection mechanisms. To prevent normal users from accidentally changing special files on a system, most operating systems have the concept of a ‘hidden’ file. These files don’t show up when a user browses the file system with a GUI or when using normal commands on the command line. Users must explicitly ask to show the hidden files either via a series of Graphical User Interface (GUI) prompts or with command line switches (<code>dir /a</code> for Windows and <code>ls –a</code> for Linux and macOS).

On Linux and Mac, users can mark specific files as hidden simply by putting a “.” as the first character in the file or folder name  (Citation: Sofacy Komplex Trojan) (Citation: Antiquated Mac Malware). Files and folders that start with a period, ‘.’, are by default hidden from being viewed in the Finder application and standard command-line utilities like “ls”. Users must specifically change settings to have these files viewable.

Files on macOS can also be marked with the UF_HIDDEN flag which prevents them from being seen in Finder.app, but still allows them to be seen in Terminal.app (Citation: WireLurker). On Windows, users can mark specific files as hidden by using the attrib.exe binary. Many applications create these hidden files and folders to store information so that it doesn’t clutter up the user’s workspace. For example, SSH utilities create a .ssh folder that’s hidden and contains the user’s known hosts and keys.

Adversaries can use this to their advantage to hide files and folders anywhere on the system and evading a typical user or system analysis that does not incorporate investigation of hidden files.

## Detection
Monitor the file system and shell commands for files being created with a leading "." and the Windows command-line use of attrib.exe to add the hidden attribute.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1564/001)
- [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
- [Antiquated Mac Malware](https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/)
- [WireLurker](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/Unit_42/unit42-wirelurker.pdf)
