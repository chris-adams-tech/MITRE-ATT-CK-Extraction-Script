---
contributors:
- Regina Elwell
- Praetorian
- Milos Stojadinovic
- Isif Ibrahima, Mandiant
- Obsidian Security
- Naveen Vijayaraghavan
- Nilesh Dherange (Gurucul)
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Application Log: Application Log Content'
id: attack-pattern--d28ef391-8ed4-45dc-bc4a-2f43abf54416
mitre_attack_url: https://attack.mitre.org/techniques/T1213
name: Data from Information Repositories
platforms:
- Linux
- Windows
- macOS
- SaaS
- IaaS
- Office Suite
tactics:
- collection
title: collection - Data from Information Repositories
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, Windows, macOS, SaaS, IaaS, Office Suite |
| **Data Sources** | Logon Session: Logon Session Creation, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1213](https://attack.mitre.org/techniques/T1213) |

# Data from Information Repositories (attack-pattern--d28ef391-8ed4-45dc-bc4a-2f43abf54416)

## Description
Adversaries may leverage information repositories to mine valuable information. Information repositories are tools that allow for storage of information, typically to facilitate collaboration or information sharing between users, and can store a wide variety of data that may aid adversaries in further objectives, such as Credential Access, Lateral Movement, or Defense Evasion, or direct access to the target information. Adversaries may also abuse external sharing features to share sensitive documents with recipients outside of the organization (i.e., [Transfer Data to Cloud Account](https://attack.mitre.org/techniques/T1537)). 

The following is a brief list of example information that may hold potential value to an adversary and may also be found on an information repository:

* Policies, procedures, and standards
* Physical / logical network diagrams
* System architecture diagrams
* Technical system documentation
* Testing / development credentials (i.e., [Unsecured Credentials](https://attack.mitre.org/techniques/T1552)) 
* Work / project schedules
* Source code snippets
* Links to network shares and other internal resources
* Contact or other sensitive information about business partners and customers, including personally identifiable information (PII) 

Information stored in a repository may vary based on the specific instance or environment. Specific common information repositories include the following:

* Storage services such as IaaS databases, enterprise databases, and more specialized platforms such as customer relationship management (CRM) databases 
* Collaboration platforms such as SharePoint, Confluence, and code repositories
* Messaging platforms such as Slack and Microsoft Teams 

In some cases, information repositories have been improperly secured, typically by unintentionally allowing for overly-broad access by all users or even public access to unauthenticated users. This is particularly common with cloud-native or cloud-hosted services, such as AWS Relational Database Service (RDS), Redis, or ElasticSearch.(Citation: Mitiga)(Citation: TrendMicro Exposed Redis 2020)(Citation: Cybernews Reuters Leak 2022)

## Detection
As information repositories generally have a considerably large user base, detection of malicious use can be non-trivial. At minimum, access to information repositories performed by privileged users (for example, Active Directory Domain, Enterprise, or Schema Administrators) should be closely monitored and alerted upon, as these types of accounts should generally not be used to access information repositories. If the capability exists, it may be of value to monitor and alert on users that are retrieving and viewing a large number of documents and pages; this behavior may be indicative of programmatic means being used to retrieve all data within the repository. In environments with high-maturity, it may be possible to leverage User-Behavioral Analytics (UBA) platforms to detect and alert on user based anomalies.

The user access logging within Microsoft's SharePoint can be configured to report access to certain pages and documents. (Citation: Microsoft SharePoint Logging) Sharepoint audit logging can also be configured to report when a user shares a resource. (Citation: Sharepoint Sharing Events) The user access logging within Atlassian's Confluence can also be configured to report access to certain pages and documents through AccessLogFilter. (Citation: Atlassian Confluence Logging) Additional log storage and analysis infrastructure will likely be required for more robust detection capabilities. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1213)
- [Mitiga](https://www.mitiga.io/blog/how-mitiga-found-pii-in-exposed-amazon-rds-snapshots)
- [Atlassian Confluence Logging](https://confluence.atlassian.com/confkb/how-to-enable-user-access-logging-182943.html)
- [TrendMicro Exposed Redis 2020](https://www.trendmicro.com/en_us/research/20/d/exposed-redis-instances-abused-for-remote-code-execution-cryptocurrency-mining.html)
- [Microsoft SharePoint Logging](https://support.office.com/en-us/article/configure-audit-settings-for-a-site-collection-a9920c97-38c0-44f2-8bcb-4cf1e2ae22d2)
- [Sharepoint Sharing Events](https://docs.microsoft.com/en-us/microsoft-365/compliance/use-sharing-auditing?view=o365-worldwide#sharepoint-sharing-events)
- [Cybernews Reuters Leak 2022](https://cybernews.com/security/thomson-reuters-leaked-terabytes-sensitive-data/)
