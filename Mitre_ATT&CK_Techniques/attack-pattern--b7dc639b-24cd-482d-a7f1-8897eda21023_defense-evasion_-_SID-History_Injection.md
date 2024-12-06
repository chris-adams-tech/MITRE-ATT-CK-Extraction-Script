---
contributors:
- Alain Homewood, Insomnia Security
- Vincent Le Toux
data_sources:
- 'Active Directory: Active Directory Object Modification'
- 'Process: OS API Execution'
- 'User Account: User Account Metadata'
id: attack-pattern--b7dc639b-24cd-482d-a7f1-8897eda21023
mitre_attack_url: https://attack.mitre.org/techniques/T1134/005
name: SID-History Injection
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - SID-History Injection
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Active Directory: Active Directory Object Modification, Process: OS API Execution, User Account: User Account Metadata |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1134/005](https://attack.mitre.org/techniques/T1134/005) |

# SID-History Injection (attack-pattern--b7dc639b-24cd-482d-a7f1-8897eda21023)

## Description
Adversaries may use SID-History Injection to escalate privileges and bypass access controls. The Windows security identifier (SID) is a unique value that identifies a user or group account. SIDs are used by Windows security in both security descriptors and access tokens. (Citation: Microsoft SID) An account can hold additional SIDs in the SID-History Active Directory attribute (Citation: Microsoft SID-History Attribute), allowing inter-operable account migration between domains (e.g., all values in SID-History are included in access tokens).

With Domain Administrator (or equivalent) rights, harvested or well-known SID values (Citation: Microsoft Well Known SIDs Jun 2017) may be inserted into SID-History to enable impersonation of arbitrary users/groups such as Enterprise Administrators. This manipulation may result in elevated access to local resources and/or access to otherwise inaccessible domains via lateral movement techniques such as [Remote Services](https://attack.mitre.org/techniques/T1021), [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002), or [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006).

## Detection
Examine data in user’s SID-History attributes using the PowerShell <code>Get-ADUser</code> cmdlet (Citation: Microsoft Get-ADUser), especially users who have SID-History values from the same domain. (Citation: AdSecurity SID History Sept 2015) Also monitor account management events on Domain Controllers for successful and failed changes to SID-History. (Citation: AdSecurity SID History Sept 2015) (Citation: Microsoft DsAddSidHistory)

Monitor for Windows API calls to the <code>DsAddSidHistory</code> function. (Citation: Microsoft DsAddSidHistory)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1134/005)
- [Microsoft SID](https://msdn.microsoft.com/library/windows/desktop/aa379571.aspx)
- [Microsoft SID-History Attribute](https://msdn.microsoft.com/library/ms679833.aspx)
- [Microsoft Well Known SIDs Jun 2017](https://support.microsoft.com/help/243330/well-known-security-identifiers-in-windows-operating-systems)
- [Microsoft Get-ADUser](https://technet.microsoft.com/library/ee617241.aspx)
- [AdSecurity SID History Sept 2015](https://adsecurity.org/?p=1772)
- [Microsoft DsAddSidHistory](https://msdn.microsoft.com/library/ms677982.aspx)
