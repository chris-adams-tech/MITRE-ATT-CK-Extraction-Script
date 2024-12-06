---
id: attack-pattern--dd901512-6e37-4155-943b-453e3777b125
mitre_attack_url: https://attack.mitre.org/techniques/T1159
name: Launch Agent
platforms:
- macOS
tactics:
- persistence
title: persistence - Launch Agent
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | macOS |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1159](https://attack.mitre.org/techniques/T1159) |

# Launch Agent (attack-pattern--dd901512-6e37-4155-943b-453e3777b125)

## Description
Per Apple’s developer documentation, when a user logs in, a per-user launchd process is started which loads the parameters for each launch-on-demand user agent from the property list (plist) files found in <code>/System/Library/LaunchAgents</code>, <code>/Library/LaunchAgents</code>, and <code>$HOME/Library/LaunchAgents</code> (Citation: AppleDocs Launch Agent Daemons) (Citation: OSX Keydnap malware) (Citation: Antiquated Mac Malware). These launch agents have property list files which point to the executables that will be launched (Citation: OSX.Dok Malware).
 
Adversaries may install a new launch agent that can be configured to execute at login by using launchd or launchctl to load a plist into the appropriate directories  (Citation: Sofacy Komplex Trojan)  (Citation: Methods of Mac Malware Persistence). The agent name may be disguised by using a name from a related operating system or benign software. Launch Agents are created with user level privileges and are executed with the privileges of the user when they log in (Citation: OSX Malware Detection) (Citation: OceanLotus for OS X). They can be set up to execute when a specific user logs in (in the specific user’s directory structure) or when any user logs in (which requires administrator privileges).

## Detection
Monitor Launch Agent creation through additional plist files and utilities such as Objective-See’s  KnockKnock application. Launch Agents also require files on disk for persistence which can also be monitored via other file monitoring applications.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1159)
- [AppleDocs Launch Agent Daemons](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
- [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
- [Antiquated Mac Malware](https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/)
- [OSX.Dok Malware](https://blog.malwarebytes.com/threat-analysis/2017/04/new-osx-dok-malware-intercepts-web-traffic/)
- [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [OSX Malware Detection](https://www.synack.com/wp-content/uploads/2016/03/RSA_OSX_Malware.pdf)
- [OceanLotus for OS X](https://www.alienvault.com/blogs/labs-research/oceanlotus-for-os-x-an-application-bundle-pretending-to-be-an-adobe-flash-update)
