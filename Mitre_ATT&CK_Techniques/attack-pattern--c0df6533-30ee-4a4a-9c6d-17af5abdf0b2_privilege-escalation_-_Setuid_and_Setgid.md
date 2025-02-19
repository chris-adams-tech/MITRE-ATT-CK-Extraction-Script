---
id: attack-pattern--c0df6533-30ee-4a4a-9c6d-17af5abdf0b2
mitre_attack_url: https://attack.mitre.org/techniques/T1166
name: Setuid and Setgid
platforms:
- Linux
- macOS
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Setuid and Setgid
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Linux, macOS |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1166](https://attack.mitre.org/techniques/T1166) |

# Setuid and Setgid (attack-pattern--c0df6533-30ee-4a4a-9c6d-17af5abdf0b2)

## Description
When the setuid or setgid bits are set on Linux or macOS for an application, this means that the application will run with the privileges of the owning user or group respectively  (Citation: setuid man page). Normally an application is run in the current user’s context, regardless of which user or group owns the application. There are instances where programs need to be executed in an elevated context to function properly, but the user running them doesn’t need the elevated privileges. Instead of creating an entry in the sudoers file, which must be done by root, any user can specify the setuid or setgid flag to be set for their own applications. These bits are indicated with an "s" instead of an "x" when viewing a file's attributes via <code>ls -l</code>. The <code>chmod</code> program can set these bits with via bitmasking, <code>chmod 4777 [file]</code> or via shorthand naming, <code>chmod u+s [file]</code>.

An adversary can take advantage of this to either do a shell escape or exploit a vulnerability in an application with the setsuid or setgid bits to get code running in a different user’s context. Additionally, adversaries can use this mechanism on their own malware to make sure they're able to execute in elevated contexts in the future  (Citation: OSX Keydnap malware).

## Detection
Monitor the file system for files that have the setuid or setgid bits set. Monitor for execution of utilities, like chmod, and their command-line arguments to look for setuid or setguid bits being set.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1166)
- [setuid man page](http://man7.org/linux/man-pages/man2/setuid.2.html)
- [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
