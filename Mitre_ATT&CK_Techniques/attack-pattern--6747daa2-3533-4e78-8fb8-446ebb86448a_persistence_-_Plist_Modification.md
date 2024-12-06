---
id: attack-pattern--6747daa2-3533-4e78-8fb8-446ebb86448a
mitre_attack_url: https://attack.mitre.org/techniques/T1547/011
name: Plist Modification
platforms:
- macOS
tactics:
- persistence
- privilege-escalation
title: persistence - Plist Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/011](https://attack.mitre.org/techniques/T1547/011) |

# Plist Modification (attack-pattern--6747daa2-3533-4e78-8fb8-446ebb86448a)

## Description
Adversaries can modify property list files (plist files) to execute their code as part of establishing persistence. Plist files are used by macOS applications to store properties and configuration settings for applications and services. Applications use information plist files, <code>Info.plist</code>, to tell the operating system how to handle the application at runtime using structured metadata in the form of keys and values. Plist files are formatted in XML and based on Apple's Core Foundation DTD and can be saved in text or binary format.(Citation: fileinfo plist file description) 

Adversaries can modify paths to executed binaries, add command line arguments, and insert key/pair values to plist files in auto-run locations which execute upon user logon or system startup. Through modifying plist files in these locations, adversaries can also execute a malicious dynamic library (dylib) by adding a dictionary containing the <code>DYLD_INSERT_LIBRARIES</code> key combined with a path to a malicious dylib under the <code>EnvironmentVariables</code> key in a plist file. Upon user logon, the plist is called for execution and the malicious dylib is executed within the process space. Persistence can also be achieved by modifying the <code>LSEnvironment</code> key in the application's <code>Info.plist</code> file.(Citation: wardle artofmalware volume1)

## Detection
Monitor for common command-line editors used to modify plist files located in auto-run locations, such as <code>~/LaunchAgents</code>, <code>~/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm</code>, and an application's <code>Info.plist</code>. 

Monitor for plist file modification immediately followed by code execution from <code>~/Library/Scripts</code> and <code>~/Library/Preferences</code>. Also, monitor for significant changes to any path pointers in a modified plist.

Identify new services executed from plist modified in the previous user's session. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/011)
- [fileinfo plist file description](https://fileinfo.com/extension/plist)
- [wardle artofmalware volume1](https://taomm.org/vol1/pdfs.html)
