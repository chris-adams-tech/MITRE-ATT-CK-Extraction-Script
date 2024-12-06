---
data_sources:
- 'File: File Modification'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Process: Process Metadata'
id: attack-pattern--1365fe3b-0f50-455d-b4da-266ce31c23b0
mitre_attack_url: https://attack.mitre.org/techniques/T1548/003
name: Sudo and Sudo Caching
platforms:
- Linux
- macOS
tactics:
- privilege-escalation
- defense-evasion
title: privilege-escalation - Sudo and Sudo Caching
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, defense-evasion |
| **Platforms** | Linux, macOS |
| **Data Sources** | File: File Modification, Command: Command Execution, Process: Process Creation, Process: Process Metadata |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1548/003](https://attack.mitre.org/techniques/T1548/003) |

# Sudo and Sudo Caching (attack-pattern--1365fe3b-0f50-455d-b4da-266ce31c23b0)

## Description
Adversaries may perform sudo caching and/or use the sudoers file to elevate privileges. Adversaries may do this to execute commands as other users or spawn processes with higher privileges.

Within Linux and MacOS systems, sudo (sometimes referred to as "superuser do") allows users to perform commands from terminals with elevated privileges and to control who can perform these commands on the system. The <code>sudo</code> command "allows a system administrator to delegate authority to give certain users (or groups of users) the ability to run some (or all) commands as root or another user while providing an audit trail of the commands and their arguments."(Citation: sudo man page 2018) Since sudo was made for the system administrator, it has some useful configuration features such as a <code>timestamp_timeout</code>, which is the amount of time in minutes between instances of <code>sudo</code> before it will re-prompt for a password. This is because <code>sudo</code> has the ability to cache credentials for a period of time. Sudo creates (or touches) a file at <code>/var/db/sudo</code> with a timestamp of when sudo was last run to determine this timeout. Additionally, there is a <code>tty_tickets</code> variable that treats each new tty (terminal session) in isolation. This means that, for example, the sudo timeout of one tty will not affect another tty (you will have to type the password again).

The sudoers file, <code>/etc/sudoers</code>, describes which users can run which commands and from which terminals. This also describes which commands users can run as other users or groups. This provides the principle of least privilege such that users are running in their lowest possible permissions for most of the time and only elevate to other users or permissions as needed, typically by prompting for a password. However, the sudoers file can also specify when to not prompt users for passwords with a line like <code>user1 ALL=(ALL) NOPASSWD: ALL</code>.(Citation: OSX.Dok Malware) Elevated privileges are required to edit this file though.

Adversaries can also abuse poor configurations of these mechanisms to escalate privileges without needing the user's password. For example, <code>/var/db/sudo</code>'s timestamp can be monitored to see if it falls within the <code>timestamp_timeout</code> range. If it does, then malware can execute sudo commands without needing to supply the user's password. Additional, if <code>tty_tickets</code> is disabled, adversaries can do this from any tty for that user.

In the wild, malware has disabled <code>tty_tickets</code> to potentially make scripting easier by issuing <code>echo \'Defaults !tty_tickets\' >> /etc/sudoers</code>.(Citation: cybereason osx proton) In order for this change to be reflected, the malware also issued <code>killall Terminal</code>. As of macOS Sierra, the sudoers file has <code>tty_tickets</code> enabled by default.

## Detection
On Linux, auditd can alert every time a user's actual ID and effective ID are different (this is what happens when you sudo). This technique is abusing normal functionality in macOS and Linux systems, but sudo has the ability to log all input and output based on the <code>LOG_INPUT</code> and <code>LOG_OUTPUT</code> directives in the <code>/etc/sudoers</code> file.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1548/003)
- [sudo man page 2018](https://www.sudo.ws/)
- [OSX.Dok Malware](https://blog.malwarebytes.com/threat-analysis/2017/04/new-osx-dok-malware-intercepts-web-traffic/)
- [cybereason osx proton](https://www.cybereason.com/blog/labs-proton-b-what-this-mac-malware-actually-does)
