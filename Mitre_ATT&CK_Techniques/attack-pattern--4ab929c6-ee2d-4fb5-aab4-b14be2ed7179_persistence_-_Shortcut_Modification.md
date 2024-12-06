---
contributors:
- David French, Elastic
- Bobby, Filar, Elastic
- Travis Smith, Tripwire
data_sources:
- 'File: File Modification'
- 'Process: Process Creation'
- 'File: File Creation'
id: attack-pattern--4ab929c6-ee2d-4fb5-aab4-b14be2ed7179
mitre_attack_url: https://attack.mitre.org/techniques/T1547/009
name: Shortcut Modification
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Shortcut Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | File: File Modification, Process: Process Creation, File: File Creation |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/009](https://attack.mitre.org/techniques/T1547/009) |

# Shortcut Modification (attack-pattern--4ab929c6-ee2d-4fb5-aab4-b14be2ed7179)

## Description
Adversaries may create or modify shortcuts that can execute a program during system boot or user login. Shortcuts or symbolic links are used to reference other files or programs that will be opened or executed when the shortcut is clicked or executed by a system startup process.

Adversaries may abuse shortcuts in the startup folder to execute their tools and achieve persistence.(Citation: Shortcut for Persistence ) Although often used as payloads in an infection chain (e.g. [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001)), adversaries may also create a new shortcut as a means of indirection, while also abusing [Masquerading](https://attack.mitre.org/techniques/T1036) to make the malicious shortcut appear as a legitimate program. Adversaries can also edit the target path or entirely replace an existing shortcut so their malware will be executed instead of the intended legitimate program.

Shortcuts can also be abused to establish persistence by implementing other methods. For example, LNK browser extensions may be modified (e.g. [Browser Extensions](https://attack.mitre.org/techniques/T1176)) to persistently launch malware.

## Detection
Since a shortcut's target path likely will not change, modifications to shortcut files that do not correlate with known software changes, patches, removal, etc., may be suspicious. Analysis should attempt to relate shortcut file change or creation events to other potentially suspicious events based on known adversary behavior such as process launches of unknown executables that make network connections.

Monitor for LNK files created with a Zone Identifier value greater than 1, which may indicate that the LNK file originated from outside of the network.(Citation: BSidesSLC 2020 - LNK Elastic)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/009)
- [Shortcut for Persistence ](https://www.elastic.co/guide/en/security/7.17/shortcut-file-written-or-modified-for-persistence.html#shortcut-file-written-or-modified-for-persistence)
- [BSidesSLC 2020 - LNK Elastic](https://www.youtube.com/watch?v=nJ0UsyiUEqQ)
