---
data_sources:
- 'Command: Command Execution'
- 'File: File Metadata'
- 'File: File Modification'
id: attack-pattern--6831414d-bb70-42b7-8030-d4e06b2660c9
mitre_attack_url: https://attack.mitre.org/techniques/T1548/001
name: Setuid and Setgid
platforms:
- Linux
- macOS
tactics:
- privilege-escalation
- defense-evasion
title: privilege-escalation - Setuid and Setgid
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, defense-evasion |
| **Platforms** | Linux, macOS |
| **Data Sources** | Command: Command Execution, File: File Metadata, File: File Modification |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1548/001](https://attack.mitre.org/techniques/T1548/001) |

# Setuid and Setgid (attack-pattern--6831414d-bb70-42b7-8030-d4e06b2660c9)

## Description
An adversary may abuse configurations where an application has the setuid or setgid bits set in order to get code running in a different (and possibly more privileged) user’s context. On Linux or macOS, when the setuid or setgid bits are set for an application binary, the application will run with the privileges of the owning user or group respectively.(Citation: setuid man page) Normally an application is run in the current user’s context, regardless of which user or group owns the application. However, there are instances where programs need to be executed in an elevated context to function properly, but the user running them may not have the specific required privileges.

Instead of creating an entry in the sudoers file, which must be done by root, any user can specify the setuid or setgid flag to be set for their own applications (i.e. [Linux and Mac File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222/002)). The <code>chmod</code> command can set these bits with bitmasking, <code>chmod 4777 [file]</code> or via shorthand naming, <code>chmod u+s [file]</code>. This will enable the setuid bit. To enable the setgid bit, <code>chmod 2775</code> and <code>chmod g+s</code> can be used.

Adversaries can use this mechanism on their own malware to make sure they're able to execute in elevated contexts in the future.(Citation: OSX Keydnap malware) This abuse is often part of a "shell escape" or other actions to bypass an execution environment with restricted permissions.

Alternatively, adversaries may choose to find and target vulnerable binaries with the setuid or setgid bits already enabled (i.e. [File and Directory Discovery](https://attack.mitre.org/techniques/T1083)). The setuid and setguid bits are indicated with an "s" instead of an "x" when viewing a file's attributes via <code>ls -l</code>. The <code>find</code> command can also be used to search for such files. For example, <code>find / -perm +4000 2>/dev/null</code> can be used to find files with setuid set and <code>find / -perm +2000 2>/dev/null</code> may be used for setgid. Binaries that have these bits set may then be abused by adversaries.(Citation: GTFOBins Suid)

## Detection
Monitor the file system for files that have the setuid or setgid bits set. Monitor for execution of utilities, like chmod, and their command-line arguments to look for setuid or setguid bits being set.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1548/001)
- [GTFOBins Suid](https://gtfobins.github.io/#+suid)
- [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
- [setuid man page](http://man7.org/linux/man-pages/man2/setuid.2.html)
