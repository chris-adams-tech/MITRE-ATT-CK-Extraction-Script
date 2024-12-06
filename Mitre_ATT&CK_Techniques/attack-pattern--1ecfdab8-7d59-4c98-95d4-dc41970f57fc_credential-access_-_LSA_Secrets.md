---
contributors:
- Ed Williams, Trustwave, SpiderLabs
data_sources:
- 'Windows Registry: Windows Registry Key Access'
- 'Command: Command Execution'
id: attack-pattern--1ecfdab8-7d59-4c98-95d4-dc41970f57fc
mitre_attack_url: https://attack.mitre.org/techniques/T1003/004
name: LSA Secrets
platforms:
- Windows
tactics:
- credential-access
title: credential-access - LSA Secrets
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Access, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1003/004](https://attack.mitre.org/techniques/T1003/004) |

# LSA Secrets (attack-pattern--1ecfdab8-7d59-4c98-95d4-dc41970f57fc)

## Description
Adversaries with SYSTEM access to a host may attempt to access Local Security Authority (LSA) secrets, which can contain a variety of different credential materials, such as credentials for service accounts.(Citation: Passcape LSA Secrets)(Citation: Microsoft AD Admin Tier Model)(Citation: Tilbury Windows Credentials) LSA secrets are stored in the registry at <code>HKEY_LOCAL_MACHINE\SECURITY\Policy\Secrets</code>. LSA secrets can also be dumped from memory.(Citation: ired Dumping LSA Secrets)

[Reg](https://attack.mitre.org/software/S0075) can be used to extract from the Registry. [Mimikatz](https://attack.mitre.org/software/S0002) can be used to extract secrets from memory.(Citation: ired Dumping LSA Secrets)

## Detection
Monitor processes and command-line arguments for program execution that may be indicative of credential dumping. Remote access tools may contain built-in features or incorporate existing tools like Mimikatz. PowerShell scripts also exist that contain credential dumping functionality, such as PowerSploit's Invoke-Mimikatz module,(Citation: Powersploit) which may require additional logging features to be configured in the operating system to collect necessary information for analysis.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1003/004)
- [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)
- [ired Dumping LSA Secrets](https://ired.team/offensive-security/credential-access-and-credential-dumping/dumping-lsa-secrets)
- [Microsoft AD Admin Tier Model](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material?redirectedfrom=MSDN)
- [Passcape LSA Secrets](https://www.passcape.com/index.php?section=docsys&cmd=details&id=23)
- [Powersploit](https://github.com/mattifestation/PowerSploit)
