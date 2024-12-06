---
contributors:
- Antonio Piazza, @antman1p
data_sources:
- 'File: File Modification'
- 'Service: Service Modification'
- 'File: File Creation'
- 'Service: Service Creation'
- 'Command: Command Execution'
id: attack-pattern--d10cbd34-42e3-45c0-84d2-535a09849584
mitre_attack_url: https://attack.mitre.org/techniques/T1543/001
name: Launch Agent
platforms:
- macOS
tactics:
- persistence
- privilege-escalation
title: persistence - Launch Agent
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS |
| **Data Sources** | File: File Modification, Service: Service Modification, File: File Creation, Service: Service Creation, Command: Command Execution |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1543/001](https://attack.mitre.org/techniques/T1543/001) |

# Launch Agent (attack-pattern--d10cbd34-42e3-45c0-84d2-535a09849584)

## Description
Adversaries may create or modify launch agents to repeatedly execute malicious payloads as part of persistence. When a user logs in, a per-user launchd process is started which loads the parameters for each launch-on-demand user agent from the property list (.plist) file found in <code>/System/Library/LaunchAgents</code>, <code>/Library/LaunchAgents</code>, and <code>~/Library/LaunchAgents</code>.(Citation: AppleDocs Launch Agent Daemons)(Citation: OSX Keydnap malware) (Citation: Antiquated Mac Malware) Property list files use the <code>Label</code>, <code>ProgramArguments </code>, and <code>RunAtLoad</code> keys to identify the Launch Agent's name, executable location, and execution time.(Citation: OSX.Dok Malware) Launch Agents are often installed to perform updates to programs, launch user specified programs at login, or to conduct other developer tasks.

 Launch Agents can also be executed using the [Launchctl](https://attack.mitre.org/techniques/T1569/001) command.
 
Adversaries may install a new Launch Agent that executes at login by placing a .plist file into the appropriate folders with the <code>RunAtLoad</code> or <code>KeepAlive</code> keys set to <code>true</code>.(Citation: Sofacy Komplex Trojan)(Citation: Methods of Mac Malware Persistence) The Launch Agent name may be disguised by using a name from the related operating system or benign software. Launch Agents are created with user level privileges and execute with user level permissions.(Citation: OSX Malware Detection)(Citation: OceanLotus for OS X) 

## Detection
Monitor Launch Agent creation through additional plist files and utilities such as Objective-See’s  KnockKnock application. Launch Agents also require files on disk for persistence which can also be monitored via other file monitoring applications.

Ensure Launch Agent's <code> ProgramArguments </code> key pointing to executables located in the <code>/tmp</code> or <code>/shared</code> folders are in alignment with enterprise policy. Ensure all Launch Agents with the <code>RunAtLoad</code> key set to <code>true</code> are in alignment with policy. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1543/001)
- [AppleDocs Launch Agent Daemons](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
- [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
- [OceanLotus for OS X](https://www.alienvault.com/blogs/labs-research/oceanlotus-for-os-x-an-application-bundle-pretending-to-be-an-adobe-flash-update)
- [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [OSX Malware Detection](https://www.synack.com/wp-content/uploads/2016/03/RSA_OSX_Malware.pdf)
- [Antiquated Mac Malware](https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/)
- [OSX.Dok Malware](https://blog.malwarebytes.com/threat-analysis/2017/04/new-osx-dok-malware-intercepts-web-traffic/)
