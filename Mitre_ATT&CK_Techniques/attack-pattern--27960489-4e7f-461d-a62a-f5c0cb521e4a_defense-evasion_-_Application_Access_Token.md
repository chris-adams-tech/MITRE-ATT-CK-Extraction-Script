---
contributors:
- Mark Wee
- Jeff Sakowicz, Microsoft Identity Developer Platform Services (IDPM Services)
- Saisha Agrawal, Microsoft Threat Intelligent Center (MSTIC)
- Shailesh Tiwary (Indian Army)
- Jack Burns, HubSpot
id: attack-pattern--27960489-4e7f-461d-a62a-f5c0cb521e4a
mitre_attack_url: https://attack.mitre.org/techniques/T1527
name: Application Access Token
platforms:
- SaaS
- Office 365
tactics:
- defense-evasion
- lateral-movement
title: defense-evasion - Application Access Token
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, lateral-movement |
| **Platforms** | SaaS, Office 365 |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1527](https://attack.mitre.org/techniques/T1527) |

# Application Access Token (attack-pattern--27960489-4e7f-461d-a62a-f5c0cb521e4a)

## Description
Adversaries may use application access tokens to bypass the typical authentication process and access restricted accounts, information, or services on remote systems. These tokens are typically stolen from users and used in lieu of login credentials.

Application access tokens are used to make authorized API requests on behalf of a user and are commonly used as a way to access resources in cloud-based applications and software-as-a-service (SaaS).(Citation: Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019) OAuth is one commonly implemented framework that issues tokens to users for access to systems. These frameworks are used collaboratively to verify the user and determine what actions the user is allowed to perform. Once identity is established, the token allows actions to be authorized, without passing the actual credentials of the user. Therefore, compromise of the token can grant the adversary access to resources of other sites through a malicious application.(Citation: okta)

For example, with a cloud-based email service once an OAuth access token is granted to a malicious application, it can potentially gain long-term access to features of the user account if a "refresh" token enabling background access is awarded.(Citation: Microsoft Identity Platform Access 2019) With an OAuth access token an adversary can use the user-granted REST API to perform functions such as email searching and contact enumeration.(Citation: Staaldraad Phishing with OAuth 2017)

Compromised access tokens may be used as an initial step in compromising other services. For example, if a token grants access to a victim’s primary email, the adversary may be able to extend access to all other services which the target subscribes by triggering forgotten password routines. Direct API access through a token negates the effectiveness of a second authentication factor and may be immune to intuitive countermeasures like changing passwords. Access abuse over an API channel can be difficult to detect even from the service provider end, as the access can still align well with a legitimate workflow.


## Detection
Monitor access token activity for abnormal use and permissions granted to unusual or suspicious applications. Administrators can set up a variety of logs and leverage audit tools to monitor actions that can be conducted as a result of OAuth 2.0 access. For instance, audit reports enable admins to identify privilege escalation actions such as role creations or policy modifications, which could be actions performed after initial access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1527)
- [Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019](https://auth0.com/blog/why-should-use-accesstokens-to-secure-an-api/)
- [Microsoft Identity Platform Access 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens)
- [okta](https://developer.okta.com/blog/2018/06/20/what-happens-if-your-jwt-is-stolen)
- [Staaldraad Phishing with OAuth 2017](https://staaldraad.github.io/2017/08/02/o356-phishing-with-oauth/)
