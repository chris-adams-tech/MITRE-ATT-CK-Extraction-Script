---
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Process: Process Creation'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--2db31dcd-54da-405d-acef-b9129b816ed6
mitre_attack_url: https://attack.mitre.org/techniques/T1021/004
name: SSH
platforms:
- Linux
- macOS
tactics:
- lateral-movement
title: lateral-movement - SSH
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Linux, macOS |
| **Data Sources** | Logon Session: Logon Session Creation, Process: Process Creation, Network Traffic: Network Connection Creation |
| **System Requirements** | An SSH server is configured and running. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1021/004](https://attack.mitre.org/techniques/T1021/004) |

# SSH (attack-pattern--2db31dcd-54da-405d-acef-b9129b816ed6)

## Description
Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into remote machines using Secure Shell (SSH). The adversary may then perform actions as the logged-on user.

SSH is a protocol that allows authorized users to open remote shells on other computers. Many Linux and macOS versions come with SSH installed by default, although typically disabled until the user enables it. The SSH server can be configured to use standard password authentication or public-private keypairs in lieu of or in addition to a password. In this authentication scenario, the user’s public key must be in a special file on the computer running the server that lists which keypairs are allowed to login as that user.

## Detection
Use of SSH may be legitimate depending on the environment and how it’s used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior with SSH. Monitor for user accounts logged into systems they would not normally access or access patterns to multiple systems over a relatively short period of time.

On macOS systems <code>log show --predicate 'process = "sshd"'</code> can be used to review incoming SSH connection attempts for suspicious activity. The command <code>log show --info --predicate 'process = "ssh" or eventMessage contains "ssh"'</code> can be used to review outgoing SSH connection activity.(Citation: Apple Unified Log Analysis Remote Login and Screen Sharing)

On Linux systems SSH activity can be found in the logs located in <code>/var/log/auth.log</code> or <code>/var/log/secure</code> depending on the distro you are using.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1021/004)
- [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)
