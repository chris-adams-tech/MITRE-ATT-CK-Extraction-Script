---
data_sources:
- 'File: File Creation'
- 'Process: Process Creation'
- 'File: File Modification'
- 'Command: Command Execution'
id: attack-pattern--dca670cf-eeec-438f-8185-fd959d9ef211
mitre_attack_url: https://attack.mitre.org/techniques/T1037/004
name: RC Scripts
platforms:
- macOS
- Linux
- Network
tactics:
- persistence
- privilege-escalation
title: persistence - RC Scripts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS, Linux, Network |
| **Data Sources** | File: File Creation, Process: Process Creation, File: File Modification, Command: Command Execution |
| **Permissions Required** | root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1037/004](https://attack.mitre.org/techniques/T1037/004) |

# RC Scripts (attack-pattern--dca670cf-eeec-438f-8185-fd959d9ef211)

## Description
Adversaries may establish persistence by modifying RC scripts which are executed during a Unix-like system’s startup. These files allow system administrators to map and start custom services at startup for different run levels. RC scripts require root privileges to modify.

Adversaries can establish persistence by adding a malicious binary path or shell commands to <code>rc.local</code>, <code>rc.common</code>, and other RC scripts specific to the Unix-like distribution.(Citation: IranThreats Kittens Dec 2017)(Citation: Intezer HiddenWasp Map 2019) Upon reboot, the system executes the script's contents as root, resulting in persistence.

Adversary abuse of RC scripts is especially effective for lightweight Unix-like distributions using the root user as default, such as IoT or embedded systems.(Citation: intezer-kaiji-malware)

Several Unix-like systems have moved to Systemd and deprecated the use of RC scripts. This is now a deprecated mechanism in macOS in favor of [Launchd](https://attack.mitre.org/techniques/T1053/004). (Citation: Apple Developer Doco Archive Launchd)(Citation: Startup Items) This technique can be used on Mac OS X Panther v10.3 and earlier versions which still execute the RC scripts.(Citation: Methods of Mac Malware Persistence) To maintain backwards compatibility some systems, such as Ubuntu, will execute the RC scripts if they exist with the correct file permissions.(Citation: Ubuntu Manpage systemd rc)

## Detection
Monitor for unexpected changes to RC scripts in the <code>/etc/</code> directory. Monitor process execution resulting from RC scripts for unusual or unknown applications or behavior.

Monitor for <code>/etc/rc.local</code> file creation. Although types of RC scripts vary for each Unix-like distribution, several execute <code>/etc/rc.local</code> if present. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1037/004)
- [Apple Developer Doco Archive Launchd](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
- [Startup Items](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html)
- [Ubuntu Manpage systemd rc](http://manpages.ubuntu.com/manpages/bionic/man8/systemd-rc-local-generator.8.html)
- [IranThreats Kittens Dec 2017](https://iranthreats.github.io/resources/attribution-flying-rocket-kitten/)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [intezer-kaiji-malware](https://www.intezer.com/blog/research/kaiji-new-chinese-linux-malware-turning-to-golang/)
- [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)
