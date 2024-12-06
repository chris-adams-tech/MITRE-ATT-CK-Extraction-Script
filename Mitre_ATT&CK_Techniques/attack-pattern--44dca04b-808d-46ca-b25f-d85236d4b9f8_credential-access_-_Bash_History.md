---
id: attack-pattern--44dca04b-808d-46ca-b25f-d85236d4b9f8
mitre_attack_url: https://attack.mitre.org/techniques/T1139
name: Bash History
platforms:
- Linux
- macOS
tactics:
- credential-access
title: credential-access - Bash History
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1139](https://attack.mitre.org/techniques/T1139) |

# Bash History (attack-pattern--44dca04b-808d-46ca-b25f-d85236d4b9f8)

## Description
Bash keeps track of the commands users type on the command-line with the "history" utility. Once a user logs out, the history is flushed to the user’s <code>.bash_history</code> file. For each user, this file resides at the same location: <code>~/.bash_history</code>. Typically, this file keeps track of the user’s last 500 commands. Users often type usernames and passwords on the command-line as parameters to programs, which then get saved to this file when they log out. Attackers can abuse this by looking through the file for potential credentials. (Citation: External to DA, the OS X Way)

## Detection
Monitoring when the user's <code>.bash_history</code> is read can help alert to suspicious activity. While users do typically rely on their history of commands, they often access this history through other utilities like "history" instead of commands like <code>cat ~/.bash_history</code>.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1139)
- [External to DA, the OS X Way](http://www.slideshare.net/StephanBorosh/external-to-da-the-os-x-way)
