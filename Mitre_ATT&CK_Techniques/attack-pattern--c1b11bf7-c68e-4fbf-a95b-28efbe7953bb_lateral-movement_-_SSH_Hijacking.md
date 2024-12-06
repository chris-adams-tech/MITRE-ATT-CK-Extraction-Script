---
contributors:
- Anastasios Pingios
id: attack-pattern--c1b11bf7-c68e-4fbf-a95b-28efbe7953bb
mitre_attack_url: https://attack.mitre.org/techniques/T1184
name: SSH Hijacking
platforms:
- Linux
- macOS
tactics:
- lateral-movement
title: lateral-movement - SSH Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Linux, macOS |
| **Permissions Required** | User, root |
| **System Requirements** | SSH service enabled, trust relationships configured, established connections |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1184](https://attack.mitre.org/techniques/T1184) |

# SSH Hijacking (attack-pattern--c1b11bf7-c68e-4fbf-a95b-28efbe7953bb)

## Description
Secure Shell (SSH) is a standard means of remote access on Linux and macOS systems. It allows a user to connect to another system via an encrypted tunnel, commonly authenticating through a password, certificate or the use of an asymmetric encryption key pair.

In order to move laterally from a compromised host, adversaries may take advantage of trust relationships established with other systems via public key authentication in active SSH sessions by hijacking an existing connection to another system. This may occur through compromising the SSH agent itself or by having access to the agent's socket. If an adversary is able to obtain root access, then hijacking SSH sessions is likely trivial. (Citation: Slideshare Abusing SSH) (Citation: SSHjack Blackhat) (Citation: Clockwork SSH Agent Hijacking) Compromising the SSH agent also provides access to intercept SSH credentials. (Citation: Welivesecurity Ebury SSH)

[SSH Hijacking](https://attack.mitre.org/techniques/T1184) differs from use of [Remote Services](https://attack.mitre.org/techniques/T1021) because it injects into an existing SSH session rather than creating a new session using [Valid Accounts](https://attack.mitre.org/techniques/T1078).

## Detection
Use of SSH may be legitimate, depending upon the network environment and how it is used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior with SSH. Monitor for user accounts logged into systems they would not normally access or access patterns to multiple systems over a relatively short period of time. Also monitor user SSH-agent socket files being used by different users.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1184)
- [Slideshare Abusing SSH](https://www.slideshare.net/morisson/mistrusting-and-abusing-ssh-13526219)
- [SSHjack Blackhat](https://www.blackhat.com/presentations/bh-usa-05/bh-us-05-boileau.pdf)
- [Clockwork SSH Agent Hijacking](https://www.clockwork.com/news/2012/09/28/602/ssh_agent_hijacking)
- [Welivesecurity Ebury SSH](https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/)
