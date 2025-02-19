---
contributors:
- Austin Clark, @c2defense
data_sources:
- 'Windows Registry: Windows Registry Key Access'
- 'Application Log: Application Log Content'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'File: File Access'
- 'User Account: User Account Authentication'
id: attack-pattern--435dfb86-2697-4867-85b5-2fef496c0517
mitre_attack_url: https://attack.mitre.org/techniques/T1552
name: Unsecured Credentials
platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Containers
- Network
- Office Suite
- Identity Provider
tactics:
- credential-access
title: credential-access - Unsecured Credentials
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Containers, Network, Office Suite, Identity Provider |
| **Data Sources** | Windows Registry: Windows Registry Key Access, Application Log: Application Log Content, Command: Command Execution, Process: Process Creation, File: File Access, User Account: User Account Authentication |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1552](https://attack.mitre.org/techniques/T1552) |

# Unsecured Credentials (attack-pattern--435dfb86-2697-4867-85b5-2fef496c0517)

## Description
Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. [Bash History](https://attack.mitre.org/techniques/T1552/003)), operating system or application-specific repositories (e.g. [Credentials in Registry](https://attack.mitre.org/techniques/T1552/002)),  or other specialized files/artifacts (e.g. [Private Keys](https://attack.mitre.org/techniques/T1552/004)).(Citation: Brining MimiKatz to Unix)

## Detection
While detecting adversaries accessing credentials may be difficult without knowing they exist in the environment, it may be possible to detect adversary use of credentials they have obtained. Monitor the command-line arguments of executing processes for suspicious words or regular expressions that may indicate searching for a password (for example: password, pwd, login, secure, or credentials). See [Valid Accounts](https://attack.mitre.org/techniques/T1078) for more information.

Monitor for suspicious file access activity, specifically indications that a process is reading multiple files in a short amount of time and/or using command-line arguments  indicative of searching for credential material (ex: regex patterns). These may be indicators of automated/scripted credential access behavior.

Monitoring when the user's <code>.bash_history</code> is read can help alert to suspicious activity. While users do typically rely on their history of commands, they often access this history through other utilities like "history" instead of commands like <code>cat ~/.bash_history</code>.

Additionally, monitor processes for applications that can be used to query the Registry, such as [Reg](https://attack.mitre.org/software/S0075), and collect command parameters that may indicate credentials are being searched. Correlate activity with related suspicious behavior that may indicate an active intrusion to reduce false positives.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1552)
- [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)
