---
contributors:
- Yossi Nisani, Cymptom
- James Dunn, @jamdunnDFW, EY
- Swapnil Kumbhar
- Jacques Pluviose, @Jacqueswildy_IT
- Dan Nutting, @KerberToast
data_sources:
- 'Active Directory: Active Directory Credential Request'
id: attack-pattern--3986e7fd-a8e9-4ecb-bfc6-55920855912b
mitre_attack_url: https://attack.mitre.org/techniques/T1558/004
name: AS-REP Roasting
platforms:
- Windows
tactics:
- credential-access
title: credential-access - AS-REP Roasting
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Active Directory: Active Directory Credential Request |
| **System Requirements** | Valid domain account |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1558/004](https://attack.mitre.org/techniques/T1558/004) |

# AS-REP Roasting (attack-pattern--3986e7fd-a8e9-4ecb-bfc6-55920855912b)

## Description
Adversaries may reveal credentials of accounts that have disabled Kerberos preauthentication by [Password Cracking](https://attack.mitre.org/techniques/T1110/002) Kerberos messages.(Citation: Harmj0y Roasting AS-REPs Jan 2017) 

Preauthentication offers protection against offline [Password Cracking](https://attack.mitre.org/techniques/T1110/002). When enabled, a user requesting access to a resource initiates communication with the Domain Controller (DC) by sending an Authentication Server Request (AS-REQ) message with a timestamp that is encrypted with the hash of their password. If and only if the DC is able to successfully decrypt the timestamp with the hash of the user’s password, it will then send an Authentication Server Response (AS-REP) message that contains the Ticket Granting Ticket (TGT) to the user. Part of the AS-REP message is signed with the user’s password.(Citation: Microsoft Kerberos Preauth 2014)

For each account found without preauthentication, an adversary may send an AS-REQ message without the encrypted timestamp and receive an AS-REP message with TGT data which may be encrypted with an insecure algorithm such as RC4. The recovered encrypted data may be vulnerable to offline [Password Cracking](https://attack.mitre.org/techniques/T1110/002) attacks similarly to [Kerberoasting](https://attack.mitre.org/techniques/T1558/003) and expose plaintext credentials. (Citation: Harmj0y Roasting AS-REPs Jan 2017)(Citation: Stealthbits Cracking AS-REP Roasting Jun 2019) 

An account registered to a domain, with or without special privileges, can be abused to list all domain accounts that have preauthentication disabled by utilizing Windows tools like [PowerShell](https://attack.mitre.org/techniques/T1059/001) with an LDAP filter. Alternatively, the adversary may send an AS-REQ message for each user. If the DC responds without errors, the account does not require preauthentication and the AS-REP message will already contain the encrypted data. (Citation: Harmj0y Roasting AS-REPs Jan 2017)(Citation: Stealthbits Cracking AS-REP Roasting Jun 2019)

Cracked hashes may enable [Persistence](https://attack.mitre.org/tactics/TA0003), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004), and [Lateral Movement](https://attack.mitre.org/tactics/TA0008) via access to [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation: SANS Attacking Kerberos Nov 2014)

## Detection
Enable Audit Kerberos Service Ticket Operations to log Kerberos TGS service ticket requests. Particularly investigate irregular patterns of activity (ex: accounts making numerous requests, Event ID 4768 and 4769, within a small time frame, especially if they also request RC4 encryption [Type 0x17], pre-authentication not required [Type: 0x0]).(Citation: AdSecurity Cracking Kerberos Dec 2015)(Citation: Microsoft Detecting Kerberoasting Feb 2018)(Citation: Microsoft 4768 TGT 2017)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1558/004)
- [Microsoft Detecting Kerberoasting Feb 2018](https://blogs.technet.microsoft.com/motiba/2018/02/23/detecting-kerberoasting-activity-using-azure-security-center/)
- [Harmj0y Roasting AS-REPs Jan 2017](https://blog.harmj0y.net/activedirectory/roasting-as-reps/)
- [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)
- [SANS Attacking Kerberos Nov 2014](https://redsiege.com/kerberoast-slides)
- [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)
- [Microsoft 4768 TGT 2017](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4768)
- [Microsoft Kerberos Preauth 2014](https://social.technet.microsoft.com/wiki/contents/articles/23559.kerberos-pre-authentication-why-it-should-not-be-disabled.aspx)
