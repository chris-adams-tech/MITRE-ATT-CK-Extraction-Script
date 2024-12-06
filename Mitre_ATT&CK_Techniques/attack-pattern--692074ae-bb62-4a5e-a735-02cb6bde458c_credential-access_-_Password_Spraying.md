---
contributors:
- Microsoft Threat Intelligence Center (MSTIC)
- John Strand
data_sources:
- 'User Account: User Account Authentication'
- 'Application Log: Application Log Content'
id: attack-pattern--692074ae-bb62-4a5e-a735-02cb6bde458c
mitre_attack_url: https://attack.mitre.org/techniques/T1110/003
name: Password Spraying
platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Containers
- Network
- Office Suite
- Identity Provider
tactics:
- credential-access
title: credential-access - Password Spraying
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Containers, Network, Office Suite, Identity Provider |
| **Data Sources** | User Account: User Account Authentication, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1110/003](https://attack.mitre.org/techniques/T1110/003) |

# Password Spraying (attack-pattern--692074ae-bb62-4a5e-a735-02cb6bde458c)

## Description
Adversaries may use a single or small list of commonly used passwords against many different accounts to attempt to acquire valid account credentials. Password spraying uses one password (e.g. 'Password01'), or a small list of commonly used passwords, that may match the complexity policy of the domain. Logins are attempted with that password against many different accounts on a network to avoid account lockouts that would normally occur when brute forcing a single account with many passwords. (Citation: BlackHillsInfosec Password Spraying)

Typically, management services over commonly used ports are used when password spraying. Commonly targeted services include the following:

* SSH (22/TCP)
* Telnet (23/TCP)
* FTP (21/TCP)
* NetBIOS / SMB / Samba (139/TCP & 445/TCP)
* LDAP (389/TCP)
* Kerberos (88/TCP)
* RDP / Terminal Services (3389/TCP)
* HTTP/HTTP Management Services (80/TCP & 443/TCP)
* MSSQL (1433/TCP)
* Oracle (1521/TCP)
* MySQL (3306/TCP)
* VNC (5900/TCP)

In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing federated authentication protocols," as well as externally facing email applications, such as Office 365.(Citation: US-CERT TA18-068A 2018)

In default environments, LDAP and Kerberos connection attempts are less likely to trigger events over SMB, which creates Windows "logon failure" event ID 4625.

## Detection
Monitor authentication logs for system and application login failures of [Valid Accounts](https://attack.mitre.org/techniques/T1078). Specifically, monitor for many failed authentication attempts across various accounts that may result from password spraying attempts.

Consider the following event IDs:(Citation: Trimarc Detecting Password Spraying)

* Domain Controllers: "Audit Logon" (Success & Failure) for event ID 4625.
* Domain Controllers: "Audit Kerberos Authentication Service" (Success & Failure) for event ID 4771.
* All systems: "Audit Logon" (Success & Failure) for event ID 4648.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1110/003)
- [Trimarc Detecting Password Spraying](https://www.trimarcsecurity.com/single-post/2018/05/06/Trimarc-Research-Detecting-Password-Spraying-with-Security-Event-Auditing)
- [BlackHillsInfosec Password Spraying](http://www.blackhillsinfosec.com/?p=4645)
- [US-CERT TA18-068A 2018](https://www.us-cert.gov/ncas/alerts/TA18-086A)
