---
contributors:
- Travis Smith, Tripwire
id: attack-pattern--970cdb5c-02fb-4c38-b17e-d6327cf3c810
mitre_attack_url: https://attack.mitre.org/techniques/T1023
name: Shortcut Modification
platforms:
- Windows
tactics:
- persistence
title: persistence - Shortcut Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1023](https://attack.mitre.org/techniques/T1023) |

# Shortcut Modification (attack-pattern--970cdb5c-02fb-4c38-b17e-d6327cf3c810)

## Description
Shortcuts or symbolic links are ways of referencing other files or programs that will be opened or executed when the shortcut is clicked or executed by a system startup process. Adversaries could use shortcuts to execute their tools for persistence. They may create a new shortcut as a means of indirection that may use [Masquerading](https://attack.mitre.org/techniques/T1036) to look like a legitimate program. Adversaries could also edit the target path or entirely replace an existing shortcut so their tools will be executed instead of the intended legitimate program.

## Detection
Since a shortcut's target path likely will not change, modifications to shortcut files that do not correlate with known software changes, patches, removal, etc., may be suspicious. Analysis should attempt to relate shortcut file change or creation events to other potentially suspicious events based on known adversary behavior such as process launches of unknown executables that make network connections.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1023)
- [capec](https://capec.mitre.org/data/definitions/132.html)
