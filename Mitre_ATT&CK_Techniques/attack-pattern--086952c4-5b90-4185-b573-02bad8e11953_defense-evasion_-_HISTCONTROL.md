---
id: attack-pattern--086952c4-5b90-4185-b573-02bad8e11953
mitre_attack_url: https://attack.mitre.org/techniques/T1148
name: HISTCONTROL
platforms:
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - HISTCONTROL
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1148](https://attack.mitre.org/techniques/T1148) |

# HISTCONTROL (attack-pattern--086952c4-5b90-4185-b573-02bad8e11953)

## Description
The <code>HISTCONTROL</code> environment variable keeps track of what should be saved by the <code>history</code> command and eventually into the <code>~/.bash_history</code> file when a user logs out. This setting can be configured to ignore commands that start with a space by simply setting it to "ignorespace". <code>HISTCONTROL</code> can also be set to ignore duplicate commands by setting it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples. This means that “ ls” will not be saved, but “ls” would be saved by history. <code>HISTCONTROL</code> does not exist by default on macOS, but can be set by the user and will be respected. Adversaries can use this to operate without leaving traces by simply prepending a space to all of their terminal commands.

## Detection
Correlating a user session with a distinct lack of new commands in their <code>.bash_history</code> can be a clue to suspicious behavior. Additionally, users checking or changing their <code>HISTCONTROL</code> environment variable is also suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1148)
- [capec](https://capec.mitre.org/data/definitions/13.html)
