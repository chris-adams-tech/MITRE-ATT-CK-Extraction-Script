---
contributors:
- Matt Burrough, @mattburrough, Microsoft
- Vinayak Wadhwa, SAFE Security
id: attack-pattern--70910fbd-58dc-4c1c-8c48-814d11fcd022
mitre_attack_url: https://attack.mitre.org/techniques/T1593/003
name: Code Repositories
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Code Repositories
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1593/003](https://attack.mitre.org/techniques/T1593/003) |

# Code Repositories (attack-pattern--70910fbd-58dc-4c1c-8c48-814d11fcd022)

## Description
Adversaries may search public code repositories for information about victims that can be used during targeting. Victims may store code in repositories on various third-party websites such as GitHub, GitLab, SourceForge, and BitBucket. Users typically interact with code repositories through a web application or command-line utilities such as git.  

Adversaries may search various public code repositories for various information about a victim. Public code repositories can often be a source of various general information about victims, such as commonly used programming languages and libraries as well as the names of employees. Adversaries may also identify more sensitive data, including accidentally leaked credentials or API keys.(Citation: GitHub Cloud Service Credentials) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Compromise Accounts](https://attack.mitre.org/techniques/T1586) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Valid Accounts](https://attack.mitre.org/techniques/T1078) or [Phishing](https://attack.mitre.org/techniques/T1566)). 

**Note:** This is distinct from [Code Repositories](https://attack.mitre.org/techniques/T1213/003), which focuses on [Collection](https://attack.mitre.org/tactics/TA0009) from private and internally hosted code repositories. 

## Detection
Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders. 

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1593/003)
- [GitHub Cloud Service Credentials](https://www.forbes.com/sites/runasandvik/2014/01/14/attackers-scrape-github-for-cloud-service-credentials-hijack-account-to-mine-virtual-currency/)
