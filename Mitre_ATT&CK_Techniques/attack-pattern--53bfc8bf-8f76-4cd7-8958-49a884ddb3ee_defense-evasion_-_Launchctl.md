---
id: attack-pattern--53bfc8bf-8f76-4cd7-8958-49a884ddb3ee
mitre_attack_url: https://attack.mitre.org/techniques/T1152
name: Launchctl
platforms:
- macOS
tactics:
- defense-evasion
- execution
- persistence
title: defense-evasion - Launchctl
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, execution, persistence |
| **Platforms** | macOS |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1152](https://attack.mitre.org/techniques/T1152) |

# Launchctl (attack-pattern--53bfc8bf-8f76-4cd7-8958-49a884ddb3ee)

## Description
Launchctl controls the macOS launchd process which handles things like launch agents and launch daemons, but can execute other commands or programs itself. Launchctl supports taking subcommands on the command-line, interactively, or even redirected from standard input. By loading or reloading launch agents or launch daemons, adversaries can install persistence or execute changes they made  (Citation: Sofacy Komplex Trojan). Running a command from launchctl is as simple as <code>launchctl submit -l <labelName> -- /Path/to/thing/to/execute "arg" "arg" "arg"</code>. Loading, unloading, or reloading launch agents or launch daemons can require elevated privileges. 

Adversaries can abuse this functionality to execute code or even bypass whitelisting if launchctl is an allowed process.

## Detection
Knock Knock can be used to detect persistent programs such as those installed via launchctl as launch agents or launch daemons. Additionally, every launch agent or launch daemon must have a corresponding plist file on disk somewhere which can be monitored. Monitor process execution from launchctl/launchd for unusual or unknown processes.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1152)
- [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
