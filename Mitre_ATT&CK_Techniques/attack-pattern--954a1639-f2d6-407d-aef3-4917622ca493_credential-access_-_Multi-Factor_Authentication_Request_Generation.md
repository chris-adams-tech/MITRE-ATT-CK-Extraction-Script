---
contributors:
- Jon Sternstein, Stern Security
- Pawel Partyka, Microsoft 365 Defender
- Shanief Webb
- Obsidian Security
- Arun Seelagan, CISA
data_sources:
- 'User Account: User Account Authentication'
- 'Logon Session: Logon Session Metadata'
- 'Application Log: Application Log Content'
- 'Logon Session: Logon Session Creation'
id: attack-pattern--954a1639-f2d6-407d-aef3-4917622ca493
mitre_attack_url: https://attack.mitre.org/techniques/T1621
name: Multi-Factor Authentication Request Generation
platforms:
- Windows
- Linux
- macOS
- IaaS
- SaaS
- Office Suite
- Identity Provider
tactics:
- credential-access
title: credential-access - Multi-Factor Authentication Request Generation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows, Linux, macOS, IaaS, SaaS, Office Suite, Identity Provider |
| **Data Sources** | User Account: User Account Authentication, Logon Session: Logon Session Metadata, Application Log: Application Log Content, Logon Session: Logon Session Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1621](https://attack.mitre.org/techniques/T1621) |

# Multi-Factor Authentication Request Generation (attack-pattern--954a1639-f2d6-407d-aef3-4917622ca493)

## Description
Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by generating MFA requests sent to users.

Adversaries in possession of credentials to [Valid Accounts](https://attack.mitre.org/techniques/T1078) may be unable to complete the login process if they lack access to the 2FA or MFA mechanisms required as an additional credential and security control. To circumvent this, adversaries may abuse the automatic generation of push notifications to MFA services such as Duo Push, Microsoft Authenticator, Okta, or similar services to have the user grant access to their account. If adversaries lack credentials to victim accounts, they may also abuse automatic push notification generation when this option is configured for self-service password reset (SSPR).(Citation: Obsidian SSPR Abuse 2023)

In some cases, adversaries may continuously repeat login attempts in order to bombard users with MFA push notifications, SMS messages, and phone calls, potentially resulting in the user finally accepting the authentication request in response to “MFA fatigue.”(Citation: Russian 2FA Push Annoyance - Cimpanu)(Citation: MFA Fatigue Attacks - PortSwigger)(Citation: Suspected Russian Activity Targeting Government and Business Entities Around the Globe)

## Detection
Monitor user account logs as well as 2FA/MFA application logs for suspicious events: unusual login attempt source location, mismatch in location of login attempt and smart device receiving 2FA/MFA request prompts, and high volume of repeated login attempts, all of which may indicate user's primary credentials have been compromised minus 2FA/MFA mechanism. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1621)
- [Russian 2FA Push Annoyance - Cimpanu](https://therecord.media/russian-hackers-bypass-2fa-by-annoying-victims-with-repeated-push-notifications/)
- [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)
- [Suspected Russian Activity Targeting Government and Business Entities Around the Globe](https://www.mandiant.com/resources/russian-targeting-gov-business)
- [Obsidian SSPR Abuse 2023](https://www.obsidiansecurity.com/blog/behind-the-breach-self-service-password-reset-azure-ad/)
