---
contributors:
- Tim (Wadhwa-)Brown
- Cody Thomas, SpecterOps
data_sources:
- 'Command: Command Execution'
- 'Logon Session: Logon Session Metadata'
- 'Active Directory: Active Directory Credential Request'
- 'File: File Access'
id: attack-pattern--3fc01293-ef5e-41c6-86ce-61f10706b64a
mitre_attack_url: https://attack.mitre.org/techniques/T1558
name: Steal or Forge Kerberos Tickets
platforms:
- Windows
- Linux
- macOS
tactics:
- credential-access
title: credential-access - Steal or Forge Kerberos Tickets
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Command: Command Execution, Logon Session: Logon Session Metadata, Active Directory: Active Directory Credential Request, File: File Access |
| **System Requirements** | Kerberos authentication enabled |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1558](https://attack.mitre.org/techniques/T1558) |

# Steal or Forge Kerberos Tickets (attack-pattern--3fc01293-ef5e-41c6-86ce-61f10706b64a)

## Description
Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003). Kerberos is an authentication protocol widely used in modern Windows domain environments. In Kerberos environments, referred to as “realms”, there are three basic participants: client, service, and Key Distribution Center (KDC).(Citation: ADSecurity Kerberos Ring Decoder) Clients request access to a service and through the exchange of Kerberos tickets, originating from KDC, they are granted access after having successfully authenticated. The KDC is responsible for both authentication and ticket granting.  Adversaries may attempt to abuse Kerberos by stealing tickets or forging tickets to enable unauthorized access.

On Windows, the built-in <code>klist</code> utility can be used to list and analyze cached Kerberos tickets.(Citation: Microsoft Klist)


## Detection
Monitor for anomalous Kerberos activity, such as malformed or blank fields in Windows logon/logoff events (Event ID 4624, 4672, 4634), RC4 encryption within ticket granting tickets (TGTs), and ticket granting service (TGS) requests without preceding TGT requests.(Citation: ADSecurity Detecting Forged Tickets)(Citation: Stealthbits Detect PtT 2019)(Citation: CERT-EU Golden Ticket Protection)

Monitor the lifetime of TGT tickets for values that differ from the default domain duration.(Citation: Microsoft Kerberos Golden Ticket)

Monitor for indications of [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003) being used to move laterally. 

Enable Audit Kerberos Service Ticket Operations to log Kerberos TGS service ticket requests. Particularly investigate irregular patterns of activity (ex: accounts making numerous requests, Event ID 4769, within a small time frame, especially if they also request RC4 encryption [Type 0x17]).(Citation: Microsoft Detecting Kerberoasting Feb 2018) (Citation: AdSecurity Cracking Kerberos Dec 2015)

Monitor for unexpected processes interacting with lsass.exe.(Citation: Medium Detecting Attempts to Steal Passwords from Memory) Common credential dumpers such as [Mimikatz](https://attack.mitre.org/software/S0002) access the LSA Subsystem Service (LSASS) process by opening the process, locating the LSA secrets key, and decrypting the sections in memory where credential details, including Kerberos tickets, are stored.

Monitor for unusual processes accessing <code>secrets.ldb</code> and <code>.secrets.mkey</code> located in <code>/var/lib/sss/secrets/</code>.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1558)
- [CERT-EU Golden Ticket Protection](https://cert.europa.eu/static/WhitePapers/UPDATED%20-%20CERT-EU_Security_Whitepaper_2014-007_Kerberos_Golden_Ticket_Protection_v1_4.pdf)
- [Microsoft Detecting Kerberoasting Feb 2018](https://blogs.technet.microsoft.com/motiba/2018/02/23/detecting-kerberoasting-activity-using-azure-security-center/)
- [Medium Detecting Attempts to Steal Passwords from Memory](https://medium.com/threatpunter/detecting-attempts-to-steal-passwords-from-memory-558f16dce4ea)
- [Stealthbits Detect PtT 2019](https://blog.stealthbits.com/detect-pass-the-ticket-attacks)
- [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)
- [ADSecurity Detecting Forged Tickets](https://adsecurity.org/?p=1515)
- [Microsoft Kerberos Golden Ticket](https://gallery.technet.microsoft.com/scriptcenter/Kerberos-Golden-Ticket-b4814285)
- [Microsoft Klist](https://docs.microsoft.com/windows-server/administration/windows-commands/klist)
- [ADSecurity Kerberos Ring Decoder](https://adsecurity.org/?p=227)
