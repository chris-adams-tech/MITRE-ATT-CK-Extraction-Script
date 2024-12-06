---
contributors:
- Sudhanshu Chauhan, @Sudhanshu_C
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Access'
id: attack-pattern--341e222a-a6e3-4f6f-b69c-831d792b1580
mitre_attack_url: https://attack.mitre.org/techniques/T1552/002
name: Credentials in Registry
platforms:
- Windows
tactics:
- credential-access
title: credential-access - Credentials in Registry
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution, Windows Registry: Windows Registry Key Access |
| **System Requirements** | Ability to query some Registry locations depends on the adversary's level of access. User permissions are usually limited to access of user-related Registry keys. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1552/002](https://attack.mitre.org/techniques/T1552/002) |

# Credentials in Registry (attack-pattern--341e222a-a6e3-4f6f-b69c-831d792b1580)

## Description
Adversaries may search the Registry on compromised systems for insecurely stored credentials. The Windows Registry stores configuration information that can be used by the system or other programs. Adversaries may query the Registry looking for credentials and passwords that have been stored for use by other programs or services. Sometimes these credentials are used for automatic logons.

Example commands to find Registry keys related to password information: (Citation: Pentestlab Stored Credentials)

* Local Machine Hive: <code>reg query HKLM /f password /t REG_SZ /s</code>
* Current User Hive: <code>reg query HKCU /f password /t REG_SZ /s</code>

## Detection
Monitor processes for applications that can be used to query the Registry, such as [Reg](https://attack.mitre.org/software/S0075), and collect command parameters that may indicate credentials are being searched. Correlate activity with related suspicious behavior that may indicate an active intrusion to reduce false positives.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1552/002)
- [Pentestlab Stored Credentials](https://pentestlab.blog/2017/04/19/stored-credentials/)
