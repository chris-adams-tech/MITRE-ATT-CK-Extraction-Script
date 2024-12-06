---
data_sources:
- 'File: File Access'
- 'Command: Command Execution'
id: attack-pattern--d0b4fcdb-d67d-4ed2-99ce-788b12f8c0f4
mitre_attack_url: https://attack.mitre.org/techniques/T1003/008
name: /etc/passwd and /etc/shadow
platforms:
- Linux
tactics:
- credential-access
title: credential-access - /etc/passwd and /etc/shadow
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux |
| **Data Sources** | File: File Access, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1003/008](https://attack.mitre.org/techniques/T1003/008) |

# /etc/passwd and /etc/shadow (attack-pattern--d0b4fcdb-d67d-4ed2-99ce-788b12f8c0f4)

## Description
Adversaries may attempt to dump the contents of <code>/etc/passwd</code> and <code>/etc/shadow</code> to enable offline password cracking. Most modern Linux operating systems use a combination of <code>/etc/passwd</code> and <code>/etc/shadow</code> to store user account information including password hashes in <code>/etc/shadow</code>. By default, <code>/etc/shadow</code> is only readable by the root user.(Citation: Linux Password and Shadow File Formats)

The Linux utility, unshadow, can be used to combine the two files in a format suited for password cracking utilities such as John the Ripper:(Citation: nixCraft - John the Ripper) <code># /usr/bin/unshadow /etc/passwd /etc/shadow > /tmp/crack.password.db</code>


## Detection
The AuditD monitoring tool, which ships stock in many Linux distributions, can be used to watch for hostile processes attempting to access <code>/etc/passwd</code> and <code>/etc/shadow</code>, alerting on the pid, process name, and arguments of such programs.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1003/008)
- [Linux Password and Shadow File Formats](https://www.tldp.org/LDP/lame/LAME/linux-admin-made-easy/shadow-file-formats.html)
- [nixCraft - John the Ripper](https://www.cyberciti.biz/faq/unix-linux-password-cracking-john-the-ripper/)
