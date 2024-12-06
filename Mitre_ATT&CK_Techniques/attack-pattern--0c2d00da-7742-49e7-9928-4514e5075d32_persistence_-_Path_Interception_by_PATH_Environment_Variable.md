---
contributors:
  - Stefan Kanthak
data_sources:
  - "File: File Creation"
  - "Windows Registry: Windows Registry Key Modification"
  - "Process: Process Creation"
id: attack-pattern--0c2d00da-7742-49e7-9928-4514e5075d32
mitre_attack_url: https://attack.mitre.org/techniques/T1574/007
name: Path Interception by PATH Environment Variable
platforms:
  - Windows
  - macOS
  - Linux
tactics:
  - persistence
  - privilege-escalation
  - defense-evasion
title: T1574.007 - persistence - Path Interception by PATH Environment Variable
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | File: File Creation, Windows Registry: Windows Registry Key Modification, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/007](https://attack.mitre.org/techniques/T1574/007) |

# Path Interception by PATH Environment Variable (attack-pattern--0c2d00da-7742-49e7-9928-4514e5075d32)

## Description
Adversaries may execute their own malicious payloads by hijacking environment variables used to load libraries. The PATH environment variable contains a list of directories (User and System) that the OS searches sequentially through in search of the binary that was called from a script or the command line. 

Adversaries can place a malicious program in an earlier entry in the list of directories stored in the PATH environment variable, resulting in the operating system executing the malicious binary rather than the legitimate binary when it searches sequentially through that PATH listing.

For example, on Windows if an adversary places a malicious program named "net.exe" in `C:\example path`, which by default precedes `C:\Windows\system32\net.exe` in the PATH environment variable, when "net" is executed from the command-line the `C:\example path` will be called instead of the system's legitimate executable at `C:\Windows\system32\net.exe`. Some methods of executing a program rely on the PATH environment variable to determine the locations that are searched when the path for the program is not given, such as executing programs from a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059).(Citation: ExpressVPN PATH env Windows 2021)

Adversaries may also directly modify the $PATH variable specifying the directories to be searched.  An adversary can modify the `$PATH` variable to point to a directory they have write access. When a program using the $PATH variable is called, the OS searches the specified directory and executes the malicious binary. On macOS, this can also be performed through modifying the $HOME variable. These variables can be modified using the command-line, launchctl, [Unix Shell Configuration Modification](https://attack.mitre.org/techniques/T1546/004), or modifying the `/etc/paths.d` folder contents.(Citation: uptycs Fake POC linux malware 2023)(Citation: nixCraft macOS PATH variables)(Citation: Elastic Rules macOS launchctl 2022)

## Detection
Monitor file creation for files named after partial directories and in locations that may be searched for common processes through the environment variable, or otherwise should not be user writable. Monitor the executing process for process executable paths that are named for partial directories. Monitor file creation for programs that are named after Windows system programs or programs commonly executed without a path (such as "findstr," "net," and "python"). If this activity occurs outside of known administration activity, upgrades, installations, or patches, then it may be suspicious.

Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/007)
- [Elastic Rules macOS launchctl 2022](https://www.elastic.co/guide/en/security/7.17/prebuilt-rule-7-16-4-modification-of-environment-variable-via-launchctl.html)
- [ExpressVPN PATH env Windows 2021](https://www.expressvpn.com/blog/cybersecurity-lessons-a-path-vulnerability-in-windows/)
- [uptycs Fake POC linux malware 2023](https://www.uptycs.com/blog/new-poc-exploit-backdoor-malware)
- [nixCraft macOS PATH variables](https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/)
