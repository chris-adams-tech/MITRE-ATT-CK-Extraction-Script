---
contributors:
- Jack Burns, HubSpot
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Web Credential: Web Credential Usage'
id: attack-pattern--861b8fd2-57f3-4ee1-ab5d-c19c3b8c7a4a
mitre_attack_url: https://attack.mitre.org/techniques/T1606/001
name: Web Cookies
platforms:
- Linux
- macOS
- Windows
- SaaS
- IaaS
tactics:
- credential-access
title: credential-access - Web Cookies
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS, Windows, SaaS, IaaS |
| **Data Sources** | Logon Session: Logon Session Creation, Web Credential: Web Credential Usage |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1606/001](https://attack.mitre.org/techniques/T1606/001) |

# Web Cookies (attack-pattern--861b8fd2-57f3-4ee1-ab5d-c19c3b8c7a4a)

## Description
Adversaries may forge web cookies that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies to authenticate and authorize user access.

Adversaries may generate these cookies in order to gain access to web resources. This differs from [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539) and other similar behaviors in that the cookies are new and forged by the adversary, rather than stolen or intercepted from legitimate users. Most common web applications have standardized and documented cookie values that can be generated using provided tools or interfaces.(Citation: Pass The Cookie) The generation of web cookies often requires secret values, such as passwords, [Private Keys](https://attack.mitre.org/techniques/T1552/004), or other cryptographic seed values.

Once forged, adversaries may use these web cookies to access resources ([Web Session Cookie](https://attack.mitre.org/techniques/T1550/004)), which may bypass multi-factor and other authentication protection mechanisms.(Citation: Volexity SolarWinds)(Citation: Pass The Cookie)(Citation: Unit 42 Mac Crypto Cookies January 2019)

## Detection
Monitor for anomalous authentication activity, such as logons or other user session activity associated with unknown accounts. Monitor for unexpected and abnormal access to resources, including access of websites and cloud-based applications by the same user in different locations or by different systems that do not match expected configurations.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1606/001)
- [Volexity SolarWinds](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)
- [Unit 42 Mac Crypto Cookies January 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
- [Pass The Cookie](https://wunderwuzzi23.github.io/blog/passthecookie.html)
