---
contributors:
- Shailesh Tiwary (Indian Army)
- Saisha Agrawal, Microsoft Threat Intelligent Center (MSTIC)
- Jeff Sakowicz, Microsoft Identity Developer Platform Services (IDPM Services)
- Mark Wee
- Ian Davila, Tidal Cyber
- Dylan Silva, AWS Security
- Jack Burns, HubSpot
- Blake Strom, Microsoft Threat Intelligence
- Pawel Partyka, Microsoft Threat Intelligence
data_sources:
- 'Web Credential: Web Credential Usage'
id: attack-pattern--f005e783-57d4-4837-88ad-dbe7faee1c51
mitre_attack_url: https://attack.mitre.org/techniques/T1550/001
name: Application Access Token
platforms:
- SaaS
- Containers
- IaaS
- Office Suite
- Identity Provider
tactics:
- defense-evasion
- lateral-movement
title: defense-evasion - Application Access Token
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, lateral-movement |
| **Platforms** | SaaS, Containers, IaaS, Office Suite, Identity Provider |
| **Data Sources** | Web Credential: Web Credential Usage |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1550/001](https://attack.mitre.org/techniques/T1550/001) |

# Application Access Token (attack-pattern--f005e783-57d4-4837-88ad-dbe7faee1c51)

## Description
Adversaries may use stolen application access tokens to bypass the typical authentication process and access restricted accounts, information, or services on remote systems. These tokens are typically stolen from users or services and used in lieu of login credentials.

Application access tokens are used to make authorized API requests on behalf of a user or service and are commonly used to access resources in cloud, container-based applications, and software-as-a-service (SaaS).(Citation: Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019) 

OAuth is one commonly implemented framework that issues tokens to users for access to systems. These frameworks are used collaboratively to verify the user and determine what actions the user is allowed to perform. Once identity is established, the token allows actions to be authorized, without passing the actual credentials of the user. Therefore, compromise of the token can grant the adversary access to resources of other sites through a malicious application.(Citation: okta)

For example, with a cloud-based email service, once an OAuth access token is granted to a malicious application, it can potentially gain long-term access to features of the user account if a "refresh" token enabling background access is awarded.(Citation: Microsoft Identity Platform Access 2019) With an OAuth access token an adversary can use the user-granted REST API to perform functions such as email searching and contact enumeration.(Citation: Staaldraad Phishing with OAuth 2017)

Compromised access tokens may be used as an initial step in compromising other services. For example, if a token grants access to a victim’s primary email, the adversary may be able to extend access to all other services which the target subscribes by triggering forgotten password routines. In AWS and GCP environments, adversaries can trigger a request for a short-lived access token with the privileges of another user account.(Citation: Google Cloud Service Account Credentials)(Citation: AWS Temporary Security Credentials) The adversary can then use this token to request data or perform actions the original account could not. If permissions for this feature are misconfigured – for example, by allowing all users to request a token for a particular account - an adversary may be able to gain initial access to a Cloud Account or escalate their privileges.(Citation: Rhino Security Labs Enumerating AWS Roles)

Direct API access through a token negates the effectiveness of a second authentication factor and may be immune to intuitive countermeasures like changing passwords.  For example, in AWS environments, an adversary who compromises a user’s AWS API credentials may be able to use the `sts:GetFederationToken` API call to create a federated user session, which will have the same permissions as the original user but may persist even if the original user credentials are deactivated.(Citation: Crowdstrike AWS User Federation Persistence) Additionally, access abuse over an API channel can be difficult to detect even from the service provider end, as the access can still align well with a legitimate workflow.

## Detection
Monitor access token activity for abnormal use and permissions granted to unusual or suspicious applications and APIs. Additionally, administrators should review logs for calls to the AWS Security Token Service (STS) and usage of GCP service accounts in order to identify anomalous actions.(Citation: AWS Logging IAM Calls)(Citation: GCP Monitoring Service Account Usage)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1550/001)
- [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)
- [Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019](https://auth0.com/blog/why-should-use-accesstokens-to-secure-an-api/)
- [AWS Logging IAM Calls](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html)
- [AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html)
- [Microsoft Identity Platform Access 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens)
- [Google Cloud Service Account Credentials](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials)
- [GCP Monitoring Service Account Usage](https://cloud.google.com/iam/docs/service-account-monitoring)
- [okta](https://developer.okta.com/blog/2018/06/20/what-happens-if-your-jwt-is-stolen)
- [Rhino Security Labs Enumerating AWS Roles](https://rhinosecuritylabs.com/aws/assume-worst-aws-assume-role-enumeration)
- [Staaldraad Phishing with OAuth 2017](https://staaldraad.github.io/2017/08/02/o356-phishing-with-oauth/)
