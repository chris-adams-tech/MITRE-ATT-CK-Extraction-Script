---
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Application Log: Application Log Content'
id: attack-pattern--7ad38ef1-381a-406d-872a-38b136eb5ecc
mitre_attack_url: https://attack.mitre.org/techniques/T1213/001
name: Confluence
platforms:
- SaaS
tactics:
- collection
title: collection - Confluence
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | SaaS |
| **Data Sources** | Logon Session: Logon Session Creation, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1213/001](https://attack.mitre.org/techniques/T1213/001) |

# Confluence (attack-pattern--7ad38ef1-381a-406d-872a-38b136eb5ecc)

## Description

Adversaries may leverage Confluence repositories to mine valuable information. Often found in development environments alongside Atlassian JIRA, Confluence is generally used to store development-related documentation, however, in general may contain more diverse categories of useful information, such as:

* Policies, procedures, and standards
* Physical / logical network diagrams
* System architecture diagrams
* Technical system documentation
* Testing / development credentials (i.e., [Unsecured Credentials](https://attack.mitre.org/techniques/T1552))
* Work / project schedules
* Source code snippets
* Links to network shares and other internal resources


## Detection
Monitor access to Confluence repositories performed by privileged users (for example, Active Directory Domain, Enterprise, or Schema Administrators) as these types of accounts should generally not be used to access information repositories. If the capability exists, it may be of value to monitor and alert on users that are retrieving and viewing a large number of documents and pages; this behavior may be indicative of programmatic means being used to retrieve all data within the repository. In environments with high-maturity, it may be possible to leverage User-Behavioral Analytics (UBA) platforms to detect and alert on user based anomalies.

User access logging within Atlassian's Confluence can be configured to report access to certain pages and documents through AccessLogFilter. (Citation: Atlassian Confluence Logging) Additional log storage and analysis infrastructure will likely be required for more robust detection capabilities.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1213/001)
- [Atlassian Confluence Logging](https://confluence.atlassian.com/confkb/how-to-enable-user-access-logging-182943.html)
