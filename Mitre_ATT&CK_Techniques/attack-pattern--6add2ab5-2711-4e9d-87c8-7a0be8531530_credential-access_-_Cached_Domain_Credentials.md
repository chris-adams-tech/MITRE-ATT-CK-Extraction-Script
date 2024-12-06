---
contributors:
- Ed Williams, Trustwave, SpiderLabs
- Tim (Wadhwa-)Brown
- Yves Yonan
data_sources:
- 'Command: Command Execution'
id: attack-pattern--6add2ab5-2711-4e9d-87c8-7a0be8531530
mitre_attack_url: https://attack.mitre.org/techniques/T1003/005
name: Cached Domain Credentials
platforms:
- Windows
- Linux
tactics:
- credential-access
title: credential-access - Cached Domain Credentials
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows, Linux |
| **Data Sources** | Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1003/005](https://attack.mitre.org/techniques/T1003/005) |

# Cached Domain Credentials (attack-pattern--6add2ab5-2711-4e9d-87c8-7a0be8531530)

## Description
Adversaries may attempt to access cached domain credentials used to allow authentication to occur in the event a domain controller is unavailable.(Citation: Microsoft - Cached Creds)

On Windows Vista and newer, the hash format is DCC2 (Domain Cached Credentials version 2) hash, also known as MS-Cache v2 hash.(Citation: PassLib mscache) The number of default cached credentials varies and can be altered per system. This hash does not allow pass-the-hash style attacks, and instead requires [Password Cracking](https://attack.mitre.org/techniques/T1110/002) to recover the plaintext password.(Citation: ired mscache)

On Linux systems, Active Directory credentials can be accessed through caches maintained by software like System Security Services Daemon (SSSD) or Quest Authentication Services (formerly VAS). Cached credential hashes are typically located at `/var/lib/sss/db/cache.[domain].ldb` for SSSD or `/var/opt/quest/vas/authcache/vas_auth.vdb` for Quest. Adversaries can use utilities, such as `tdbdump`, on these database files to dump the cached hashes and use [Password Cracking](https://attack.mitre.org/techniques/T1110/002) to obtain the plaintext password.(Citation: Brining MimiKatz to Unix) 

With SYSTEM or sudo access, the tools/utilities such as [Mimikatz](https://attack.mitre.org/software/S0002), [Reg](https://attack.mitre.org/software/S0075), and secretsdump.py for Windows or Linikatz for Linux can be used to extract the cached credentials.(Citation: Brining MimiKatz to Unix)

Note: Cached credentials for Windows Vista are derived using PBKDF2.(Citation: PassLib mscache)

## Detection
Monitor processes and command-line arguments for program execution that may be indicative of credential dumping. Remote access tools may contain built-in features or incorporate existing tools like Mimikatz. PowerShell scripts also exist that contain credential dumping functionality, such as PowerSploit's Invoke-Mimikatz module,(Citation: Powersploit) which may require additional logging features to be configured in the operating system to collect necessary information for analysis.

Detection of compromised [Valid Accounts](https://attack.mitre.org/techniques/T1078) in-use by adversaries may help as well.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1003/005)
- [PassLib mscache](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html)
- [ired mscache](https://ired.team/offensive-security/credential-access-and-credential-dumping/dumping-and-cracking-mscash-cached-domain-credentials)
- [Microsoft - Cached Creds](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh994565(v%3Dws.11))
- [Powersploit](https://github.com/mattifestation/PowerSploit)
- [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)
