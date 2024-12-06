---
contributors:
- Rory McCune, Aqua Security
- Jay Chen, Palo Alto Networks
- Yossi Weizman, Azure Defender Research Team
- Vishwas Manral, McAfee
- Microsoft Threat Intelligence Center (MSTIC)
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'File: File Access'
id: attack-pattern--837f9164-50af-4ac0-8219-379d8a74cefc
mitre_attack_url: https://attack.mitre.org/techniques/T1552/001
name: Credentials In Files
platforms:
- Windows
- IaaS
- Linux
- macOS
- Containers
tactics:
- credential-access
title: credential-access - Credentials In Files
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows, IaaS, Linux, macOS, Containers |
| **Data Sources** | Command: Command Execution, Process: Process Creation, File: File Access |
| **System Requirements** | Access to files |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1552/001](https://attack.mitre.org/techniques/T1552/001) |

# Credentials In Files (attack-pattern--837f9164-50af-4ac0-8219-379d8a74cefc)

## Description
Adversaries may search local file systems and remote file shares for files containing insecurely stored credentials. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords.

It is possible to extract passwords from backups or saved virtual machines through [OS Credential Dumping](https://attack.mitre.org/techniques/T1003).(Citation: CG 2014) Passwords may also be obtained from Group Policy Preferences stored on the Windows Domain Controller.(Citation: SRD GPP)

In cloud and/or containerized environments, authenticated user and service account credentials are often stored in local configuration and credential files.(Citation: Unit 42 Hildegard Malware) They may also be found as parameters to deployment commands in container logs.(Citation: Unit 42 Unsecured Docker Daemons) In some cases, these files can be copied and reused on another machine or the contents can be read and then used to authenticate without needing to copy any files.(Citation: Specter Ops - Cloud Credential Storage)

## Detection
While detecting adversaries accessing these files may be difficult without knowing they exist in the first place, it may be possible to detect adversary use of credentials they have obtained. Monitor the command-line arguments of executing processes for suspicious words or regular expressions that may indicate searching for a password (for example: password, pwd, login, secure, or credentials). See [Valid Accounts](https://attack.mitre.org/techniques/T1078) for more information.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1552/001)
- [CG 2014](http://carnal0wnage.attackresearch.com/2014/05/mimikatz-against-virtual-machine-memory.html)
- [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [Unit 42 Unsecured Docker Daemons](https://unit42.paloaltonetworks.com/attackers-tactics-and-techniques-in-unsecured-docker-daemons-revealed/)
- [Specter Ops - Cloud Credential Storage](https://posts.specterops.io/head-in-the-clouds-bd038bb69e48)
- [SRD GPP](http://blogs.technet.com/b/srd/archive/2014/05/13/ms14-025-an-update-for-group-policy-preferences.aspx)
