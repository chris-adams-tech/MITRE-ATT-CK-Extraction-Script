---
data_sources:
- 'Process: Process Creation'
- 'File: File Creation'
- 'File: File Modification'
- 'Service: Service Modification'
- 'Command: Command Execution'
- 'Service: Service Creation'
id: attack-pattern--573ad264-1371-4ae0-8482-d2673b719dba
mitre_attack_url: https://attack.mitre.org/techniques/T1543/004
name: Launch Daemon
platforms:
- macOS
tactics:
- persistence
- privilege-escalation
title: persistence - Launch Daemon
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS |
| **Data Sources** | Process: Process Creation, File: File Creation, File: File Modification, Service: Service Modification, Command: Command Execution, Service: Service Creation |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1543/004](https://attack.mitre.org/techniques/T1543/004) |

# Launch Daemon (attack-pattern--573ad264-1371-4ae0-8482-d2673b719dba)

## Description
Adversaries may create or modify Launch Daemons to execute malicious payloads as part of persistence. Launch Daemons are plist files used to interact with Launchd, the service management framework used by macOS. Launch Daemons require elevated privileges to install, are executed for every user on a system prior to login, and run in the background without the need for user interaction. During the macOS initialization startup, the launchd process loads the parameters for launch-on-demand system-level daemons from plist files found in <code>/System/Library/LaunchDaemons/</code> and <code>/Library/LaunchDaemons/</code>. Required Launch Daemons parameters include a <code>Label</code> to identify the task, <code>Program</code> to provide a path to the executable, and <code>RunAtLoad</code> to specify when the task is run. Launch Daemons are often used to provide access to shared resources, updates to software, or conduct automation tasks.(Citation: AppleDocs Launch Agent Daemons)(Citation: Methods of Mac Malware Persistence)(Citation: launchd Keywords for plists)

Adversaries may install a Launch Daemon configured to execute at startup by using the <code>RunAtLoad</code> parameter set to <code>true</code> and the <code>Program</code> parameter set to the malicious executable path. The daemon name may be disguised by using a name from a related operating system or benign software (i.e. [Masquerading](https://attack.mitre.org/techniques/T1036)). When the Launch Daemon is executed, the program inherits administrative permissions.(Citation: WireLurker)(Citation: OSX Malware Detection)

Additionally, system configuration changes (such as the installation of third party package managing software) may cause folders such as <code>usr/local/bin</code> to become globally writeable. So, it is possible for poor configurations to allow an adversary to modify executables referenced by current Launch Daemon's plist files.(Citation: LaunchDaemon Hijacking)(Citation: sentinelone macos persist Jun 2019)

## Detection
Monitor for new files added to the <code>/Library/LaunchDaemons/</code> folder. The System LaunchDaemons are protected by SIP.

Some legitimate LaunchDaemons point to unsigned code that could be exploited. For Launch Daemons with the <code>RunAtLoad</code> parameter set to true, ensure the <code>Program</code> parameter points to signed code or executables are in alignment with enterprise policy. Some parameters are interchangeable with others, such as <code>Program</code> and <code>ProgramArguments</code> parameters but one must be present.(Citation: launchd Keywords for plists)



## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1543/004)
- [AppleDocs Launch Agent Daemons](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [launchd Keywords for plists](https://www.real-world-systems.com/docs/launchdPlist.1.html)
- [WireLurker](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/Unit_42/unit42-wirelurker.pdf)
- [OSX Malware Detection](https://www.synack.com/wp-content/uploads/2016/03/RSA_OSX_Malware.pdf)
- [LaunchDaemon Hijacking](https://bradleyjkemp.dev/post/launchdaemon-hijacking/)
- [sentinelone macos persist Jun 2019](https://www.sentinelone.com/blog/how-malware-persists-on-macos/)
