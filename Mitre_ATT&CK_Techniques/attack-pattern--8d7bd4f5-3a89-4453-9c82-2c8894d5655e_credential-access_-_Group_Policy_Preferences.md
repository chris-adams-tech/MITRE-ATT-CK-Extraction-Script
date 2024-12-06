---
data_sources:
- 'File: File Access'
- 'Command: Command Execution'
id: attack-pattern--8d7bd4f5-3a89-4453-9c82-2c8894d5655e
mitre_attack_url: https://attack.mitre.org/techniques/T1552/006
name: Group Policy Preferences
platforms:
- Windows
tactics:
- credential-access
title: credential-access - Group Policy Preferences
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | File: File Access, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1552/006](https://attack.mitre.org/techniques/T1552/006) |

# Group Policy Preferences (attack-pattern--8d7bd4f5-3a89-4453-9c82-2c8894d5655e)

## Description
Adversaries may attempt to find unsecured credentials in Group Policy Preferences (GPP). GPP are tools that allow administrators to create domain policies with embedded credentials. These policies allow administrators to set local accounts.(Citation: Microsoft GPP 2016)

These group policies are stored in SYSVOL on a domain controller. This means that any domain user can view the SYSVOL share and decrypt the password (using the AES key that has been made public).(Citation: Microsoft GPP Key)

The following tools and scripts can be used to gather and decrypt the password file from Group Policy Preference XML files:

* Metasploit’s post exploitation module: <code>post/windows/gather/credentials/gpp</code>
* Get-GPPPassword(Citation: Obscuresecurity Get-GPPPassword)
* gpprefdecrypt.py

On the SYSVOL share, adversaries may use the following command to enumerate potential GPP XML files: <code>dir /s * .xml</code>


## Detection
Monitor for attempts to access SYSVOL that involve searching for XML files. 

Deploy a new XML file with permissions set to Everyone:Deny and monitor for Access Denied errors.(Citation: ADSecurity Finding Passwords in SYSVOL)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1552/006)
- [Obscuresecurity Get-GPPPassword](https://obscuresecurity.blogspot.co.uk/2012/05/gpp-password-retrieval-with-powershell.html)
- [Microsoft GPP 2016](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn581922(v%3Dws.11))
- [Microsoft GPP Key](https://msdn.microsoft.com/library/cc422924.aspx)
- [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)
