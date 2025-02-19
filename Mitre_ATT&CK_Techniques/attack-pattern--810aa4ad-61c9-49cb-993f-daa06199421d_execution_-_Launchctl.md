---
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Service: Service Creation'
- 'File: File Modification'
id: attack-pattern--810aa4ad-61c9-49cb-993f-daa06199421d
mitre_attack_url: https://attack.mitre.org/techniques/T1569/001
name: Launchctl
platforms:
- macOS
tactics:
- execution
title: execution - Launchctl
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | macOS |
| **Data Sources** | Process: Process Creation, Command: Command Execution, Service: Service Creation, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1569/001](https://attack.mitre.org/techniques/T1569/001) |

# Launchctl (attack-pattern--810aa4ad-61c9-49cb-993f-daa06199421d)

## Description
Adversaries may abuse launchctl to execute commands or programs. Launchctl interfaces with launchd, the service management framework for macOS. Launchctl supports taking subcommands on the command-line, interactively, or even redirected from standard input.(Citation: Launchctl Man)

Adversaries use launchctl to execute commands and programs as [Launch Agent](https://attack.mitre.org/techniques/T1543/001)s or [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)s. Common subcommands include: <code>launchctl load</code>,<code>launchctl unload</code>, and <code>launchctl start</code>. Adversaries can use scripts or manually run the commands <code>launchctl load -w "%s/Library/LaunchAgents/%s"</code> or <code>/bin/launchctl load</code> to execute [Launch Agent](https://attack.mitre.org/techniques/T1543/001)s or [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)s.(Citation: Sofacy Komplex Trojan)(Citation: 20 macOS Common Tools and Techniques)


## Detection
Every Launch Agent and Launch Daemon must have a corresponding plist file on disk which can be monitored. Monitor for recently modified or created plist files with a significant change to the executable path executed with the command-line <code>launchctl</code> command. Plist files are located in the root, system, and users <code>/Library/LaunchAgents</code> or <code>/Library/LaunchDaemons</code> folders. 

Monitor command-line execution of the <code>launchctl</code> command immediately followed by abnormal network connections. [Launch Agent](https://attack.mitre.org/techniques/T1543/001)s or [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)s with executable paths pointing to <code>/tmp</code> and <code>/Shared</code> folders locations are potentially suspicious. 

When removing [Launch Agent](https://attack.mitre.org/techniques/T1543/001)s or [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)s ensure the services are unloaded prior to deleting plist files.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1569/001)
- [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
- [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [Launchctl Man](https://ss64.com/osx/launchctl.html)
