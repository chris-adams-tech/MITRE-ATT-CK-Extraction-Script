---
contributors:
  - Arun Seelagan, CISA
data_sources:
  - "Logon Session: Logon Session Creation"
  - "Application Log: Application Log Content"
  - "Cloud Service: Cloud Service Metadata"
id: attack-pattern--0c4b4fda-9062-47da-98b9-ceae2dcf052a
mitre_attack_url: https://attack.mitre.org/techniques/T1213/002
name: Sharepoint
platforms:
  - Windows
  - Office Suite
tactics:
  - collection
title: T1213.002 - collection - Sharepoint
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | Logon Session: Logon Session Creation, Application Log: Application Log Content, Cloud Service: Cloud Service Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1213/002](https://attack.mitre.org/techniques/T1213/002) |

# Sharepoint (attack-pattern--0c4b4fda-9062-47da-98b9-ceae2dcf052a)

## Description
Adversaries may leverage the SharePoint repository as a source to mine valuable information. SharePoint will often contain useful information for an adversary to learn about the structure and functionality of the internal network and systems. For example, the following is a list of example information that may hold potential value to an adversary and may also be found on SharePoint:

* Policies, procedures, and standards
* Physical / logical network diagrams
* System architecture diagrams
* Technical system documentation
* Testing / development credentials (i.e., [Unsecured Credentials](https://attack.mitre.org/techniques/T1552))
* Work / project schedules
* Source code snippets
* Links to network shares and other internal resources


## Detection
The user access logging within Microsoft's SharePoint can be configured to report access to certain pages and documents. (Citation: Microsoft SharePoint Logging). As information repositories generally have a considerably large user base, detection of malicious use can be non-trivial. At minimum, access to information repositories performed by privileged users (for example, Active Directory Domain, Enterprise, or Schema Administrators) should be closely monitored and alerted upon, as these types of accounts should generally not be used to access information repositories. If the capability exists, it may be of value to monitor and alert on users that are retrieving and viewing a large number of documents and pages; this behavior may be indicative of programmatic means being used to retrieve all data within the repository. In environments with high-maturity, it may be possible to leverage User-Behavioral Analytics (UBA) platforms to detect and alert on user based anomalies. 



## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1213/002)
- [Microsoft SharePoint Logging](https://support.office.com/en-us/article/configure-audit-settings-for-a-site-collection-a9920c97-38c0-44f2-8bcb-4cf1e2ae22d2)
