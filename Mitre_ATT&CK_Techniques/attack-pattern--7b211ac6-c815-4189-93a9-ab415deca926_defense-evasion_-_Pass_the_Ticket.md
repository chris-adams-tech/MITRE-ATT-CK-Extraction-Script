---
contributors:
- Vincent Le Toux
- Ryan Becwar
data_sources:
- 'User Account: User Account Authentication'
- 'Logon Session: Logon Session Creation'
- 'Active Directory: Active Directory Credential Request'
id: attack-pattern--7b211ac6-c815-4189-93a9-ab415deca926
mitre_attack_url: https://attack.mitre.org/techniques/T1550/003
name: Pass the Ticket
platforms:
- Windows
tactics:
- defense-evasion
- lateral-movement
title: defense-evasion - Pass the Ticket
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, lateral-movement |
| **Platforms** | Windows |
| **Data Sources** | User Account: User Account Authentication, Logon Session: Logon Session Creation, Active Directory: Active Directory Credential Request |
| **System Requirements** | Kerberos authentication enabled |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1550/003](https://attack.mitre.org/techniques/T1550/003) |

# Pass the Ticket (attack-pattern--7b211ac6-c815-4189-93a9-ab415deca926)

## Description
Adversaries may “pass the ticket” using stolen Kerberos tickets to move laterally within an environment, bypassing normal system access controls. Pass the ticket (PtT) is a method of authenticating to a system using Kerberos tickets without having access to an account's password. Kerberos authentication can be used as the first step to lateral movement to a remote system.

When preforming PtT, valid Kerberos tickets for [Valid Accounts](https://attack.mitre.org/techniques/T1078) are captured by [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). A user's service tickets or ticket granting ticket (TGT) may be obtained, depending on the level of access. A service ticket allows for access to a particular resource, whereas a TGT can be used to request service tickets from the Ticket Granting Service (TGS) to access any resource the user has privileges to access.(Citation: ADSecurity AD Kerberos Attacks)(Citation: GentilKiwi Pass the Ticket)

A [Silver Ticket](https://attack.mitre.org/techniques/T1558/002) can be obtained for services that use Kerberos as an authentication mechanism and are used to generate tickets to access that particular resource and the system that hosts the resource (e.g., SharePoint).(Citation: ADSecurity AD Kerberos Attacks)

A [Golden Ticket](https://attack.mitre.org/techniques/T1558/001) can be obtained for the domain using the Key Distribution Service account KRBTGT account NTLM hash, which enables generation of TGTs for any account in Active Directory.(Citation: Campbell 2014)

Adversaries may also create a valid Kerberos ticket using other user information, such as stolen password hashes or AES keys. For example, "overpassing the hash" involves using a NTLM password hash to authenticate as a user (i.e. [Pass the Hash](https://attack.mitre.org/techniques/T1550/002)) while also using the password hash to create a valid Kerberos ticket.(Citation: Stealthbits Overpass-the-Hash)

## Detection
Audit all Kerberos authentication and credential use events and review for discrepancies. Unusual remote authentication events that correlate with other suspicious activity (such as writing and executing binaries) may indicate malicious activity.

Event ID 4769 is generated on the Domain Controller when using a golden ticket after the KRBTGT password has been reset twice, as mentioned in the mitigation section. The status code 0x1F indicates the action has failed due to "Integrity check on decrypted field failed" and indicates misuse by a previously invalidated golden ticket.(Citation: CERT-EU Golden Ticket Protection)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1550/003)
- [CERT-EU Golden Ticket Protection](https://cert.europa.eu/static/WhitePapers/UPDATED%20-%20CERT-EU_Security_Whitepaper_2014-007_Kerberos_Golden_Ticket_Protection_v1_4.pdf)
- [Campbell 2014](http://defcon.org/images/defcon-22/dc-22-presentations/Campbell/DEFCON-22-Christopher-Campbell-The-Secret-Life-of-Krbtgt.pdf)
- [GentilKiwi Pass the Ticket](https://web.archive.org/web/20210515214027/https://blog.gentilkiwi.com/securite/mimikatz/pass-the-ticket-kerberos)
- [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)
- [Stealthbits Overpass-the-Hash](https://stealthbits.com/blog/how-to-detect-overpass-the-hash-attacks/)
