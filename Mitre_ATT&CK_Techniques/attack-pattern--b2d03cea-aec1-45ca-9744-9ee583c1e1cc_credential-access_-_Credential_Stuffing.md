---
contributors:
- Diogo Fernandes
- Anastasios Pingios
data_sources:
- 'Application Log: Application Log Content'
- 'User Account: User Account Authentication'
id: attack-pattern--b2d03cea-aec1-45ca-9744-9ee583c1e1cc
mitre_attack_url: https://attack.mitre.org/techniques/T1110/004
name: Credential Stuffing
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
title: credential-access - Credential Stuffing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Containers, Network, Office Suite, Identity Provider |
| **Data Sources** | Application Log: Application Log Content, User Account: User Account Authentication |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1110/004](https://attack.mitre.org/techniques/T1110/004) |

# Credential Stuffing (attack-pattern--b2d03cea-aec1-45ca-9744-9ee583c1e1cc)

## Description
Adversaries may use credentials obtained from breach dumps of unrelated accounts to gain access to target accounts through credential overlap. Occasionally, large numbers of username and password pairs are dumped online when a website or service is compromised and the user account credentials accessed. The information may be useful to an adversary attempting to compromise accounts by taking advantage of the tendency for users to use the same passwords across personal and business accounts.

Credential stuffing is a risky option because it could cause numerous authentication failures and account lockouts, depending on the organization's login failure policies.

Typically, management services over commonly used ports are used when stuffing credentials. Commonly targeted services include the following:

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

## Detection
Monitor authentication logs for system and application login failures of [Valid Accounts](https://attack.mitre.org/techniques/T1078). If authentication failures are high, then there may be a brute force attempt to gain access to a system using legitimate credentials.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1110/004)
- [US-CERT TA18-068A 2018](https://www.us-cert.gov/ncas/alerts/TA18-086A)
