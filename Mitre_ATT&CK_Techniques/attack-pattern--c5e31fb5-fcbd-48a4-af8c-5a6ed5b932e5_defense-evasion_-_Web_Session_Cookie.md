---
contributors:
- Johann Rehberger
id: attack-pattern--c5e31fb5-fcbd-48a4-af8c-5a6ed5b932e5
mitre_attack_url: https://attack.mitre.org/techniques/T1506
name: Web Session Cookie
platforms:
- Office 365
- SaaS
tactics:
- defense-evasion
- lateral-movement
title: defense-evasion - Web Session Cookie
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, lateral-movement |
| **Platforms** | Office 365, SaaS |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1506](https://attack.mitre.org/techniques/T1506) |

# Web Session Cookie (attack-pattern--c5e31fb5-fcbd-48a4-af8c-5a6ed5b932e5)

## Description
Adversaries can use stolen session cookies to authenticate to web applications and services. This technique bypasses some multi-factor authentication protocols since the session is already authenticated.(Citation: Pass The Cookie)

Authentication cookies are commonly used in web applications, including cloud-based services, after a user has authenticated to the service so credentials are not passed and re-authentication does not need to occur as frequently. Cookies are often valid for an extended period of time, even if the web application is not actively used. After the cookie is obtained through [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539), the adversary then imports the cookie into a browser they control and is able to use the site or application as the user for as long as the session cookie is active. Once logged into the site, an adversary can access sensitive information, read email, or perform actions that the victim account has permissions to perform.

There have been examples of malware targeting session cookies to bypass multi-factor authentication systems.(Citation: Unit 42 Mac Crypto Cookies January 2019) 

## Detection
Monitor for anomalous access of websites and cloud-based applications by the same user in different locations or by different systems that do not match expected configurations.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1506)
- [Pass The Cookie](https://wunderwuzzi23.github.io/blog/passthecookie.html)
- [Unit 42 Mac Crypto Cookies January 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
