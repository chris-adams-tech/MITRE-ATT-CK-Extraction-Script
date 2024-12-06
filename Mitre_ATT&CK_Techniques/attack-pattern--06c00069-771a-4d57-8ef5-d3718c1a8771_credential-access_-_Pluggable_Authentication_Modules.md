---
contributors:
- Scott Knight, @sdotknight, VMware Carbon Black
- George Allen, VMware Carbon Black
data_sources:
- 'File: File Modification'
- 'Logon Session: Logon Session Creation'
id: attack-pattern--06c00069-771a-4d57-8ef5-d3718c1a8771
mitre_attack_url: https://attack.mitre.org/techniques/T1556/003
name: Pluggable Authentication Modules
platforms:
- Linux
- macOS
tactics:
- credential-access
- defense-evasion
- persistence
title: credential-access - Pluggable Authentication Modules
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, defense-evasion, persistence |
| **Platforms** | Linux, macOS |
| **Data Sources** | File: File Modification, Logon Session: Logon Session Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1556/003](https://attack.mitre.org/techniques/T1556/003) |

# Pluggable Authentication Modules (attack-pattern--06c00069-771a-4d57-8ef5-d3718c1a8771)

## Description
Adversaries may modify pluggable authentication modules (PAM) to access user credentials or enable otherwise unwarranted access to accounts. PAM is a modular system of configuration files, libraries, and executable files which guide authentication for many services. The most common authentication module is <code>pam_unix.so</code>, which retrieves, sets, and verifies account authentication information in <code>/etc/passwd</code> and <code>/etc/shadow</code>.(Citation: Apple PAM)(Citation: Man Pam_Unix)(Citation: Red Hat PAM)

Adversaries may modify components of the PAM system to create backdoors. PAM components, such as <code>pam_unix.so</code>, can be patched to accept arbitrary adversary supplied values as legitimate credentials.(Citation: PAM Backdoor)

Malicious modifications to the PAM system may also be abused to steal credentials. Adversaries may infect PAM resources with code to harvest user credentials, since the values exchanged with PAM components may be plain-text since PAM does not store passwords.(Citation: PAM Creds)(Citation: Apple PAM)

## Detection
Monitor PAM configuration and module paths (ex: <code>/etc/pam.d/</code>) for changes. Use system-integrity tools such as AIDE and monitoring tools such as auditd to monitor PAM files.

Look for suspicious account behavior across systems that share accounts, either user, admin, or service accounts. Examples: one account logged into multiple systems simultaneously; multiple accounts logged into the same machine simultaneously; accounts logged in at odd times (ex: when the user is not present) or outside of business hours. Activity may be from interactive login sessions or process ownership from accounts being used to execute binaries on a remote system as a particular account. Correlate other security systems with login information (e.g., a user has an active login session but has not entered the building or does not have VPN access).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1556/003)
- [Apple PAM](https://opensource.apple.com/source/dovecot/dovecot-239/dovecot/doc/wiki/PasswordDatabase.PAM.txt)
- [Man Pam_Unix](https://linux.die.net/man/8/pam_unix)
- [PAM Creds](https://x-c3ll.github.io/posts/PAM-backdoor-DNS/)
- [Red Hat PAM](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/managing_smart_cards/pluggable_authentication_modules)
- [PAM Backdoor](https://github.com/zephrax/linux-pam-backdoor)
