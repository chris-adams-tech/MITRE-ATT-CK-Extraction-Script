---
contributors:
- Suzy Schapperle - Microsoft Azure Red Team
- Shailesh Tiwary (Indian Army)
- Mark Wee
- Jeff Sakowicz, Microsoft Identity Developer Platform Services (IDPM Services)
- Saisha Agrawal, Microsoft Threat Intelligent Center (MSTIC)
- Ram Pliskin, Microsoft Azure Security Center
- Jack Burns, HubSpot
- Arun Seelagan, CISA
data_sources:
- 'Active Directory: Active Directory Object Modification'
- 'User Account: User Account Modification'
id: attack-pattern--890c9858-598c-401d-a4d5-c67ebcdd703a
mitre_attack_url: https://attack.mitre.org/techniques/T1528
name: Steal Application Access Token
platforms:
- SaaS
- Containers
- IaaS
- Office Suite
- Identity Provider
tactics:
- credential-access
title: credential-access - Steal Application Access Token
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | SaaS, Containers, IaaS, Office Suite, Identity Provider |
| **Data Sources** | Active Directory: Active Directory Object Modification, User Account: User Account Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1528](https://attack.mitre.org/techniques/T1528) |

# Steal Application Access Token (attack-pattern--890c9858-598c-401d-a4d5-c67ebcdd703a)

## Description
Adversaries can steal application access tokens as a means of acquiring credentials to access remote systems and resources.

Application access tokens are used to make authorized API requests on behalf of a user or service and are commonly used as a way to access resources in cloud and container-based applications and software-as-a-service (SaaS).(Citation: Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019)  Adversaries who steal account API tokens in cloud and containerized environments may be able to access data and perform actions with the permissions of these accounts, which can lead to privilege escalation and further compromise of the environment.

For example, in Kubernetes environments, processes running inside a container may communicate with the Kubernetes API server using service account tokens. If a container is compromised, an adversary may be able to steal the container’s token and thereby gain access to Kubernetes API commands.(Citation: Kubernetes Service Accounts)  Similarly, instances within continuous-development / continuous-integration (CI/CD) pipelines will often use API tokens to authenticate to other services for testing and deployment.(Citation: Cider Security Top 10 CICD Security Risks) If these pipelines are compromised, adversaries may be able to steal these tokens and leverage their privileges.

Token theft can also occur through social engineering, in which case user action may be required to grant access. OAuth is one commonly implemented framework that issues tokens to users for access to systems. An application desiring access to cloud-based services or protected APIs can gain entry using OAuth 2.0 through a variety of authorization protocols. An example commonly-used sequence is Microsoft's Authorization Code Grant flow.(Citation: Microsoft Identity Platform Protocols May 2019)(Citation: Microsoft - OAuth Code Authorization flow - June 2019) An OAuth access token enables a third-party application to interact with resources containing user data in the ways requested by the application without obtaining user credentials. 
 
Adversaries can leverage OAuth authorization by constructing a malicious application designed to be granted access to resources with the target user's OAuth token.(Citation: Amnesty OAuth Phishing Attacks, August 2019)(Citation: Trend Micro Pawn Storm OAuth 2017) The adversary will need to complete registration of their application with the authorization server, for example Microsoft Identity Platform using Azure Portal, the Visual Studio IDE, the command-line interface, PowerShell, or REST API calls.(Citation: Microsoft - Azure AD App Registration - May 2019) Then, they can send a [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002) to the target user to entice them to grant access to the application. Once the OAuth access token is granted, the application can gain potentially long-term access to features of the user account through [Application Access Token](https://attack.mitre.org/techniques/T1550/001).(Citation: Microsoft - Azure AD Identity Tokens - Aug 2019)

Application access tokens may function within a limited lifetime, limiting how long an adversary can utilize the stolen token. However, in some cases, adversaries can also steal application refresh tokens(Citation: Auth0 Understanding Refresh Tokens), allowing them to obtain new access tokens without prompting the user.  



## Detection
Administrators should set up monitoring to trigger automatic alerts when policy criteria are met. For example, using a Cloud Access Security Broker (CASB), admins can create a “High severity app permissions” policy that generates alerts if apps request high severity permissions or send permissions requests for too many users.

Security analysts can hunt for malicious apps using the tools available in their CASB, identity provider, or resource provider (depending on platform.) For example, they can filter for apps that are authorized by a small number of users, apps requesting high risk permissions, permissions incongruous with the app’s purpose, or apps with old “Last authorized” fields. A specific app can be investigated using an activity log displaying activities the app has performed, although some activities may be mis-logged as being performed by the user. App stores can be useful resources to further investigate suspicious apps.

Administrators can set up a variety of logs and leverage audit tools to monitor actions that can be conducted as a result of OAuth 2.0 access. For instance, audit reports enable admins to identify privilege escalation actions such as role creations or policy modifications, which could be actions performed after initial access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1528)
- [Amnesty OAuth Phishing Attacks, August 2019](https://www.amnesty.org/en/latest/research/2019/08/evolving-phishing-attacks-targeting-journalists-and-human-rights-defenders-from-the-middle-east-and-north-africa/)
- [Auth0 Understanding Refresh Tokens](https://auth0.com/learn/refresh-tokens/)
- [Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019](https://auth0.com/blog/why-should-use-accesstokens-to-secure-an-api/)
- [Cider Security Top 10 CICD Security Risks](https://www.cidersecurity.io/top-10-cicd-security-risks/)
- [Trend Micro Pawn Storm OAuth 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/pawn-storm-abuses-open-authentication-advanced-social-engineering-attacks)
- [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)
- [Microsoft - Azure AD Identity Tokens - Aug 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens)
- [Microsoft - Azure AD App Registration - May 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Microsoft - OAuth Code Authorization flow - June 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)
- [Microsoft Identity Platform Protocols May 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols)
