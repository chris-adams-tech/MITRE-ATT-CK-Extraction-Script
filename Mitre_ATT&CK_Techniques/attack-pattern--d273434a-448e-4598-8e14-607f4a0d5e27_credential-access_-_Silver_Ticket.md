---
data_sources:
- 'Logon Session: Logon Session Metadata'
id: attack-pattern--d273434a-448e-4598-8e14-607f4a0d5e27
mitre_attack_url: https://attack.mitre.org/techniques/T1558/002
name: Silver Ticket
platforms:
- Windows
tactics:
- credential-access
title: credential-access - Silver Ticket
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Logon Session: Logon Session Metadata |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1558/002](https://attack.mitre.org/techniques/T1558/002) |

# Silver Ticket (attack-pattern--d273434a-448e-4598-8e14-607f4a0d5e27)

## Description
Adversaries who have the password hash of a target service account (e.g. SharePoint, MSSQL) may forge Kerberos ticket granting service (TGS) tickets, also known as silver tickets. Kerberos TGS tickets are also known as service tickets.(Citation: ADSecurity Silver Tickets)

Silver tickets are more limited in scope in than golden tickets in that they only enable adversaries to access a particular resource (e.g. MSSQL) and the system that hosts the resource; however, unlike golden tickets, adversaries with the ability to forge silver tickets are able to create TGS tickets without interacting with the Key Distribution Center (KDC), potentially making detection more difficult.(Citation: ADSecurity Detecting Forged Tickets)

Password hashes for target services may be obtained using [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) or [Kerberoasting](https://attack.mitre.org/techniques/T1558/003).

## Detection
Monitor for anomalous Kerberos activity, such as malformed or blank fields in Windows logon/logoff events (Event ID 4624, 4634, 4672).(Citation: ADSecurity Detecting Forged Tickets) 

Monitor for unexpected processes interacting with lsass.exe.(Citation: Medium Detecting Attempts to Steal Passwords from Memory) Common credential dumpers such as Mimikatz access the LSA Subsystem Service (LSASS) process by opening the process, locating the LSA secrets key, and decrypting the sections in memory where credential details, including Kerberos tickets, are stored.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1558/002)
- [ADSecurity Silver Tickets](https://adsecurity.org/?p=2011)
- [ADSecurity Detecting Forged Tickets](https://adsecurity.org/?p=1515)
- [Medium Detecting Attempts to Steal Passwords from Memory](https://medium.com/threatpunter/detecting-attempts-to-steal-passwords-from-memory-558f16dce4ea)
