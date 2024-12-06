---
id: attack-pattern--5ad95aaa-49c1-4784-821d-2e83f47b079b
mitre_attack_url: https://attack.mitre.org/techniques/T1155
name: AppleScript
platforms:
- macOS
tactics:
- execution
title: execution - AppleScript
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1155](https://attack.mitre.org/techniques/T1155) |

# AppleScript (attack-pattern--5ad95aaa-49c1-4784-821d-2e83f47b079b)

## Description
macOS and OS X applications send AppleEvent messages to each other for interprocess communications (IPC). These messages can be easily scripted with AppleScript for local or remote IPC. Osascript executes AppleScript and any other Open Scripting Architecture (OSA) language scripts. A list of OSA languages installed on a system can be found by using the <code>osalang</code> program.
AppleEvent messages can be sent independently or as part of a script. These events can locate open windows, send keystrokes, and interact with almost any open application locally or remotely. 

Adversaries can use this to interact with open SSH connection, move to remote machines, and even present users with fake dialog boxes. These events cannot start applications remotely (they can start them locally though), but can interact with applications if they're already running remotely. Since this is a scripting language, it can be used to launch more common techniques as well such as a reverse shell via python  (Citation: Macro Malware Targets Macs). Scripts can be run from the command-line via <code>osascript /path/to/script</code> or <code>osascript -e "script here"</code>.

## Detection
Monitor for execution of AppleScript through osascript that may be related to other suspicious behavior occurring on the system.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1155)
- [Macro Malware Targets Macs](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/macro-malware-targets-macs/)
