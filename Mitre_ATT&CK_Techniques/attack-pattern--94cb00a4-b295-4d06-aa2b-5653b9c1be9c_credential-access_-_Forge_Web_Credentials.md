---
contributors:
- Dylan Silva, AWS Security
data_sources:
- 'Web Credential: Web Credential Usage'
- 'Web Credential: Web Credential Creation'
- 'Logon Session: Logon Session Creation'
id: attack-pattern--94cb00a4-b295-4d06-aa2b-5653b9c1be9c
mitre_attack_url: https://attack.mitre.org/techniques/T1606
name: Forge Web Credentials
platforms:
- SaaS
- Windows
- macOS
- Linux
- IaaS
- Office Suite
- Identity Provider
tactics:
- credential-access
title: credential-access - Forge Web Credentials
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | SaaS, Windows, macOS, Linux, IaaS, Office Suite, Identity Provider |
| **Data Sources** | Web Credential: Web Credential Usage, Web Credential: Web Credential Creation, Logon Session: Logon Session Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1606](https://attack.mitre.org/techniques/T1606) |

# Forge Web Credentials (attack-pattern--94cb00a4-b295-4d06-aa2b-5653b9c1be9c)

## Description
Adversaries may forge credential materials that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens, or other materials to authenticate and authorize user access.

Adversaries may generate these credential materials in order to gain access to web resources. This differs from [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539), [Steal Application Access Token](https://attack.mitre.org/techniques/T1528), and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted from legitimate users.

The generation of web credentials often requires secret values, such as passwords, [Private Keys](https://attack.mitre.org/techniques/T1552/004), or other cryptographic seed values.(Citation: GitHub AWS-ADFS-Credential-Generator) Adversaries may also forge tokens by taking advantage of features such as the `AssumeRole` and `GetFederationToken` APIs in AWS, which allow users to request temporary security credentials (i.e., [Temporary Elevated Cloud Access](https://attack.mitre.org/techniques/T1548/005)), or the `zmprov gdpak` command in Zimbra, which generates a pre-authentication key that can be used to generate tokens for any user in the domain.(Citation: AWS Temporary Security Credentials)(Citation: Zimbra Preauth)

Once forged, adversaries may use these web credentials to access resources (ex: [Use Alternate Authentication Material](https://attack.mitre.org/techniques/T1550)), which may bypass multi-factor and other authentication protection mechanisms.(Citation: Pass The Cookie)(Citation: Unit 42 Mac Crypto Cookies January 2019)(Citation: Microsoft SolarWinds Customer Guidance)  

## Detection
Monitor for anomalous authentication activity, such as logons or other user session activity associated with unknown accounts. Monitor for unexpected and abnormal access to resources, including access of websites and cloud-based applications by the same user in different locations or by different systems that do not match expected configurations.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1606)
- [AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html)
- [Unit 42 Mac Crypto Cookies January 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
- [GitHub AWS-ADFS-Credential-Generator](https://github.com/pvanbuijtene/aws-adfs-credential-generator)
- [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)
- [Pass The Cookie](https://wunderwuzzi23.github.io/blog/passthecookie.html)
- [Zimbra Preauth](https://wiki.zimbra.com/wiki/Preauth)
