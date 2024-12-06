---
contributors:
- Praetorian
id: attack-pattern--b39d03cb-7b98-41c4-a878-c40c1a913dc0
mitre_attack_url: https://attack.mitre.org/techniques/T1208
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
| **Permissions Required** | User |
| **System Requirements** | Valid domain account or the ability to sniff traffic within a domain. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1208](https://attack.mitre.org/techniques/T1208) |

# Kerberoasting (attack-pattern--b39d03cb-7b98-41c4-a878-c40c1a913dc0)

## Description
Service principal names (SPNs) are used to uniquely identify each instance of a Windows service. To enable authentication, Kerberos requires that SPNs be associated with at least one service logon account (an account specifically tasked with running a service (Citation: Microsoft Detecting Kerberoasting Feb 2018)). (Citation: Microsoft SPN) (Citation: Microsoft SetSPN) (Citation: SANS Attacking Kerberos Nov 2014) (Citation: Harmj0y Kerberoast Nov 2016)

Adversaries possessing a valid Kerberos ticket-granting ticket (TGT) may request one or more Kerberos ticket-granting service (TGS) service tickets for any SPN from a domain controller (DC). (Citation: Empire InvokeKerberoast Oct 2016) (Citation: AdSecurity Cracking Kerberos Dec 2015) Portions of these tickets may be encrypted with the RC4 algorithm, meaning the Kerberos 5 TGS-REP etype 23 hash of the service account associated with the SPN is used as the private key and is thus vulnerable to offline [Brute Force](https://attack.mitre.org/techniques/T1110) attacks that may expose plaintext credentials. (Citation: AdSecurity Cracking Kerberos Dec 2015) (Citation: Empire InvokeKerberoast Oct 2016) (Citation: Harmj0y Kerberoast Nov 2016)

This same attack could be executed using service tickets captured from network traffic. (Citation: AdSecurity Cracking Kerberos Dec 2015)

Cracked hashes may enable Persistence, Privilege Escalation, and  Lateral Movement via access to [Valid Accounts](https://attack.mitre.org/techniques/T1078). (Citation: SANS Attacking Kerberos Nov 2014)

## Detection
Enable Audit Kerberos Service Ticket Operations to log Kerberos TGS service ticket requests. Particularly investigate irregular patterns of activity (ex: accounts making numerous requests, Event ID 4769, within a small time frame, especially if they also request RC4 encryption [Type 0x17]). (Citation: Microsoft Detecting Kerberoasting Feb 2018) (Citation: AdSecurity Cracking Kerberos Dec 2015)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1208)
- [Microsoft Detecting Kerberoasting Feb 2018](https://blogs.technet.microsoft.com/motiba/2018/02/23/detecting-kerberoasting-activity-using-azure-security-center/)
- [Microsoft SPN](https://msdn.microsoft.com/library/ms677949.aspx)
- [Microsoft SetSPN](https://social.technet.microsoft.com/wiki/contents/articles/717.service-principal-names-spns-setspn-syntax-setspn-exe.aspx)
- [SANS Attacking Kerberos Nov 2014](https://redsiege.com/kerberoast-slides)
- [Harmj0y Kerberoast Nov 2016](https://www.harmj0y.net/blog/powershell/kerberoasting-without-mimikatz/)
- [Empire InvokeKerberoast Oct 2016](https://github.com/EmpireProject/Empire/blob/master/data/module_source/credentials/Invoke-Kerberoast.ps1)
- [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)
