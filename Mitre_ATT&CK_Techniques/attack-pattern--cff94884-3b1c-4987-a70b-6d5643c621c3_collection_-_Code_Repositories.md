---
contributors:
- Itamar Mizrahi, Cymptom
- Toby Kohlenberg
- Josh Liburdi, @jshlbrd
data_sources:
- 'Application Log: Application Log Content'
- 'Logon Session: Logon Session Creation'
id: attack-pattern--cff94884-3b1c-4987-a70b-6d5643c621c3
mitre_attack_url: https://attack.mitre.org/techniques/T1213/003
name: Code Repositories
platforms:
- SaaS
tactics:
- collection
title: collection - Code Repositories
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | SaaS |
| **Data Sources** | Application Log: Application Log Content, Logon Session: Logon Session Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1213/003](https://attack.mitre.org/techniques/T1213/003) |

# Code Repositories (attack-pattern--cff94884-3b1c-4987-a70b-6d5643c621c3)

## Description
Adversaries may leverage code repositories to collect valuable information. Code repositories are tools/services that store source code and automate software builds. They may be hosted internally or privately on third party sites such as Github, GitLab, SourceForge, and BitBucket. Users typically interact with code repositories through a web application or command-line utilities such as git.

Once adversaries gain access to a victim network or a private code repository, they may collect sensitive information such as proprietary source code or [Unsecured Credentials](https://attack.mitre.org/techniques/T1552) contained within software's source code.  Having access to software's source code may allow adversaries to develop [Exploits](https://attack.mitre.org/techniques/T1587/004), while credentials may provide access to additional resources using [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation: Wired Uber Breach)(Citation: Krebs Adobe)

**Note:** This is distinct from [Code Repositories](https://attack.mitre.org/techniques/T1593/003), which focuses on conducting [Reconnaissance](https://attack.mitre.org/tactics/TA0043) via public code repositories.

## Detection
Monitor access to code repositories, especially performed by privileged users such as Active Directory Domain or Enterprise Administrators as these types of accounts should generally not be used to access code repositories. In environments with high-maturity, it may be possible to leverage User-Behavioral Analytics (UBA) platforms to detect and alert on user-based anomalies.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1213/003)
- [Wired Uber Breach](https://www.wired.com/story/uber-paid-off-hackers-to-hide-a-57-million-user-data-breach/)
- [Krebs Adobe](https://krebsonsecurity.com/2013/10/adobe-to-announce-source-code-customer-data-breach/)
