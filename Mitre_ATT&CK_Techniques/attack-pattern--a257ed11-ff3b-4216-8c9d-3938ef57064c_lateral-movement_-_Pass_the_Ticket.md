---
contributors:
- Ryan Becwar
- Vincent Le Toux
id: attack-pattern--a257ed11-ff3b-4216-8c9d-3938ef57064c
mitre_attack_url: https://attack.mitre.org/techniques/T1097
name: Pass the Ticket
platforms:
- Windows
tactics:
- lateral-movement
title: lateral-movement - Pass the Ticket
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows |
| **System Requirements** | Requires Microsoft Windows as a target system and Kerberos authentication enabled. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1097](https://attack.mitre.org/techniques/T1097) |

# Pass the Ticket (attack-pattern--a257ed11-ff3b-4216-8c9d-3938ef57064c)

## Description
Pass the ticket (PtT) is a method of authenticating to a system using Kerberos tickets without having access to an account's password. Kerberos authentication can be used as the first step to lateral movement to a remote system.

In this technique, valid Kerberos tickets for [Valid Accounts](https://attack.mitre.org/techniques/T1078) are captured by [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). A user's service tickets or ticket granting ticket (TGT) may be obtained, depending on the level of access. A service ticket allows for access to a particular resource, whereas a TGT can be used to request service tickets from the Ticket Granting Service (TGS) to access any resource the user has privileges to access. (Citation: ADSecurity AD Kerberos Attacks) (Citation: GentilKiwi Pass the Ticket)

Silver Tickets can be obtained for services that use Kerberos as an authentication mechanism and are used to generate tickets to access that particular resource and the system that hosts the resource (e.g., SharePoint). (Citation: ADSecurity AD Kerberos Attacks)

Golden Tickets can be obtained for the domain using the Key Distribution Service account KRBTGT account NTLM hash, which enables generation of TGTs for any account in Active Directory. (Citation: Campbell 2014)

## Detection
Audit all Kerberos authentication and credential use events and review for discrepancies. Unusual remote authentication events that correlate with other suspicious activity (such as writing and executing binaries) may indicate malicious activity.

Event ID 4769 is generated on the Domain Controller when using a golden ticket after the KRBTGT password has been reset twice, as mentioned in the mitigation section. The status code 0x1F indicates the action has failed due to "Integrity check on decrypted field failed" and indicates misuse by a previously invalidated golden ticket. (Citation: CERT-EU Golden Ticket Protection)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1097)
- [capec](https://capec.mitre.org/data/definitions/645.html)
- [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)
- [GentilKiwi Pass the Ticket](http://blog.gentilkiwi.com/securite/mimikatz/pass-the-ticket-kerberos)
- [Campbell 2014](http://defcon.org/images/defcon-22/dc-22-presentations/Campbell/DEFCON-22-Christopher-Campbell-The-Secret-Life-of-Krbtgt.pdf)
- [CERT-EU Golden Ticket Protection](https://cert.europa.eu/static/WhitePapers/UPDATED%20-%20CERT-EU_Security_Whitepaper_2014-007_Kerberos_Golden_Ticket_Protection_v1_4.pdf)
