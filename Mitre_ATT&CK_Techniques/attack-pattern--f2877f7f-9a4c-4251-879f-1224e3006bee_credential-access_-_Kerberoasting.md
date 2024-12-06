---
contributors:
- Praetorian
data_sources:
- 'Active Directory: Active Directory Credential Request'
id: attack-pattern--f2877f7f-9a4c-4251-879f-1224e3006bee
mitre_attack_url: https://attack.mitre.org/techniques/T1558/003
name: Kerberoasting
platforms:
- Windows
tactics:
- credential-access
title: credential-access - Kerberoasting
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Active Directory: Active Directory Credential Request |
| **System Requirements** | Valid domain account or the ability to sniff traffic within a domain |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1558/003](https://attack.mitre.org/techniques/T1558/003) |

# Kerberoasting (attack-pattern--f2877f7f-9a4c-4251-879f-1224e3006bee)

## Description
Adversaries may abuse a valid Kerberos ticket-granting ticket (TGT) or sniff network traffic to obtain a ticket-granting service (TGS) ticket that may be vulnerable to [Brute Force](https://attack.mitre.org/techniques/T1110).(Citation: Empire InvokeKerberoast Oct 2016)(Citation: AdSecurity Cracking Kerberos Dec 2015) 

Service principal names (SPNs) are used to uniquely identify each instance of a Windows service. To enable authentication, Kerberos requires that SPNs be associated with at least one service logon account (an account specifically tasked with running a service(Citation: Microsoft Detecting Kerberoasting Feb 2018)).(Citation: Microsoft SPN)(Citation: Microsoft SetSPN)(Citation: SANS Attacking Kerberos Nov 2014)(Citation: Harmj0y Kerberoast Nov 2016)

Adversaries possessing a valid Kerberos ticket-granting ticket (TGT) may request one or more Kerberos ticket-granting service (TGS) service tickets for any SPN from a domain controller (DC).(Citation: Empire InvokeKerberoast Oct 2016)(Citation: AdSecurity Cracking Kerberos Dec 2015) Portions of these tickets may be encrypted with the RC4 algorithm, meaning the Kerberos 5 TGS-REP etype 23 hash of the service account associated with the SPN is used as the private key and is thus vulnerable to offline [Brute Force](https://attack.mitre.org/techniques/T1110) attacks that may expose plaintext credentials.(Citation: AdSecurity Cracking Kerberos Dec 2015)(Citation: Empire InvokeKerberoast Oct 2016) (Citation: Harmj0y Kerberoast Nov 2016)

This same behavior could be executed using service tickets captured from network traffic.(Citation: AdSecurity Cracking Kerberos Dec 2015)

Cracked hashes may enable [Persistence](https://attack.mitre.org/tactics/TA0003), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004), and [Lateral Movement](https://attack.mitre.org/tactics/TA0008) via access to [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation: SANS Attacking Kerberos Nov 2014)

## Detection
Enable Audit Kerberos Service Ticket Operations to log Kerberos TGS service ticket requests. Particularly investigate irregular patterns of activity (ex: accounts making numerous requests, Event ID 4769, within a small time frame, especially if they also request RC4 encryption [Type 0x17]).(Citation: Microsoft Detecting Kerberoasting Feb 2018)(Citation: AdSecurity Cracking Kerberos Dec 2015)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1558/003)
- [Microsoft Detecting Kerberoasting Feb 2018](https://blogs.technet.microsoft.com/motiba/2018/02/23/detecting-kerberoasting-activity-using-azure-security-center/)
- [Empire InvokeKerberoast Oct 2016](https://github.com/EmpireProject/Empire/blob/master/data/module_source/credentials/Invoke-Kerberoast.ps1)
- [SANS Attacking Kerberos Nov 2014](https://redsiege.com/kerberoast-slides)
- [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)
- [Microsoft SetSPN](https://social.technet.microsoft.com/wiki/contents/articles/717.service-principal-names-spns-setspn-syntax-setspn-exe.aspx)
- [Microsoft SPN](https://msdn.microsoft.com/library/ms677949.aspx)
- [Harmj0y Kerberoast Nov 2016](https://blog.harmj0y.net/powershell/kerberoasting-without-mimikatz/)
