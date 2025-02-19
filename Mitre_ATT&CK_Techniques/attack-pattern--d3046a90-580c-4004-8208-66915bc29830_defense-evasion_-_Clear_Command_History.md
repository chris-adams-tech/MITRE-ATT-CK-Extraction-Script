---
id: attack-pattern--d3046a90-580c-4004-8208-66915bc29830
mitre_attack_url: https://attack.mitre.org/techniques/T1146
name: Clear Command History
platforms:
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - Clear Command History
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1146](https://attack.mitre.org/techniques/T1146) |

# Clear Command History (attack-pattern--d3046a90-580c-4004-8208-66915bc29830)

## Description
In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. macOS and Linux both keep track of the commands users type in their terminal so that users can retrace what they've done. These logs can be accessed in a few different ways. While logged in, this command history is tracked in a file pointed to by the environment variable <code>HISTFILE</code>. When a user logs off a system, this information is flushed to a file in the user's home directory called <code>~/.bash_history</code>. The benefit of this is that it allows users to go back to commands they've used before in different sessions. Since everything typed on the command-line is saved, passwords passed in on the command line are also saved. Adversaries can abuse this by searching these files for cleartext passwords. Additionally, adversaries can use a variety of methods to prevent their own commands from appear in these logs such as <code>unset HISTFILE</code>, <code>export HISTFILESIZE=0</code>, <code>history -c</code>, <code>rm ~/.bash_history</code>.

## Detection
User authentication, especially via remote terminal services like SSH, without new entries in that user's <code>~/.bash_history</code> is suspicious. Additionally, the modification of the HISTFILE and HISTFILESIZE environment variables or the removal/clearing of the <code>~/.bash_history</code> file are indicators of suspicious activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1146)
