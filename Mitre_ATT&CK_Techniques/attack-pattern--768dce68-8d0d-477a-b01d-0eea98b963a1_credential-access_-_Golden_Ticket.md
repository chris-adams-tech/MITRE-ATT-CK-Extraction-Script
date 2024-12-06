---
contributors:
- Itamar Mizrahi, Cymptom
data_sources:
- 'Active Directory: Active Directory Credential Request'
- 'Logon Session: Logon Session Metadata'
id: attack-pattern--768dce68-8d0d-477a-b01d-0eea98b963a1
mitre_attack_url: https://attack.mitre.org/techniques/T1558/001
name: Golden Ticket
platforms:
- Windows
tactics:
- credential-access
title: credential-access - Golden Ticket
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Active Directory: Active Directory Credential Request, Logon Session: Logon Session Metadata |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1558/001](https://attack.mitre.org/techniques/T1558/001) |

# Golden Ticket (attack-pattern--768dce68-8d0d-477a-b01d-0eea98b963a1)

## Description
Adversaries who have the KRBTGT account password hash may forge Kerberos ticket-granting tickets (TGT), also known as a golden ticket.(Citation: AdSecurity Kerberos GT Aug 2015) Golden tickets enable adversaries to generate authentication material for any account in Active Directory.(Citation: CERT-EU Golden Ticket Protection) 

Using a golden ticket, adversaries are then able to request ticket granting service (TGS) tickets, which enable access to specific resources. Golden tickets require adversaries to interact with the Key Distribution Center (KDC) in order to obtain TGS.(Citation: ADSecurity Detecting Forged Tickets)

The KDC service runs all on domain controllers that are part of an Active Directory domain. KRBTGT is the Kerberos Key Distribution Center (KDC) service account and is responsible for encrypting and signing all Kerberos tickets.(Citation: ADSecurity Kerberos and KRBTGT) The KRBTGT password hash may be obtained using [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) and privileged access to a domain controller.

## Detection
Monitor for anomalous Kerberos activity, such as malformed or blank fields in Windows logon/logoff events (Event ID 4624, 4672, 4634), RC4 encryption within TGTs, and TGS requests without preceding TGT requests.(Citation: ADSecurity Kerberos and KRBTGT)(Citation: CERT-EU Golden Ticket Protection)(Citation: Stealthbits Detect PtT 2019)

Monitor the lifetime of TGT tickets for values that differ from the default domain duration.(Citation: Microsoft Kerberos Golden Ticket)

Monitor for indications of [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003) being used to move laterally. 


## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1558/001)
- [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)
- [CERT-EU Golden Ticket Protection](https://cert.europa.eu/static/WhitePapers/UPDATED%20-%20CERT-EU_Security_Whitepaper_2014-007_Kerberos_Golden_Ticket_Protection_v1_4.pdf)
- [ADSecurity Detecting Forged Tickets](https://adsecurity.org/?p=1515)
- [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)
- [Stealthbits Detect PtT 2019](https://blog.stealthbits.com/detect-pass-the-ticket-attacks)
- [Microsoft Kerberos Golden Ticket](https://gallery.technet.microsoft.com/scriptcenter/Kerberos-Golden-Ticket-b4814285)
