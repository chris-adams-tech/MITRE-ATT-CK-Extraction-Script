---
contributors:
- Microsoft Threat Intelligence Center (MSTIC)
id: attack-pattern--ba8e391f-14b5-496f-81f2-2d5ecd646c1c
mitre_attack_url: https://attack.mitre.org/techniques/T1081
name: Credentials in Files
platforms:
- Windows
- IaaS
- Linux
- macOS
tactics:
- credential-access
title: credential-access - Credentials in Files
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Permissions Required** | User, Administrator, SYSTEM |
| **System Requirements** | Access to files |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1081](https://attack.mitre.org/techniques/T1081) |

# Credentials in Files (attack-pattern--ba8e391f-14b5-496f-81f2-2d5ecd646c1c)

## Description
Adversaries may search local file systems and remote file shares for files containing passwords. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords.

It is possible to extract passwords from backups or saved virtual machines through [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). (Citation: CG 2014) Passwords may also be obtained from Group Policy Preferences stored on the Windows Domain Controller. (Citation: SRD GPP)

In cloud environments, authenticated user credentials are often stored in local configuration and credential files. In some cases, these files can be copied and reused on another machine or the contents can be read and then used to authenticate without needing to copy any files. (Citation: Specter Ops - Cloud Credential Storage)



## Detection
While detecting adversaries accessing these files may be difficult without knowing they exist in the first place, it may be possible to detect adversary use of credentials they have obtained. Monitor the command-line arguments of executing processes for suspicious words or regular expressions that may indicate searching for a password (for example: password, pwd, login, secure, or credentials). See [Valid Accounts](https://attack.mitre.org/techniques/T1078) for more information.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1081)
- [capec](https://capec.mitre.org/data/definitions/639.html)
- [CG 2014](http://carnal0wnage.attackresearch.com/2014/05/mimikatz-against-virtual-machine-memory.html)
- [SRD GPP](http://blogs.technet.com/b/srd/archive/2014/05/13/ms14-025-an-update-for-group-policy-preferences.aspx)
- [Specter Ops - Cloud Credential Storage](https://posts.specterops.io/head-in-the-clouds-bd038bb69e48)
