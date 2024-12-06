---
contributors:
- Microsoft Threat Intelligence Center (MSTIC)
- Johann Rehberger
- Menachem Goldstein
data_sources:
- 'Process: Process Access'
- 'File: File Access'
id: attack-pattern--10ffac09-e42d-4f56-ab20-db94c67d76ff
mitre_attack_url: https://attack.mitre.org/techniques/T1539
name: Steal Web Session Cookie
platforms:
- Linux
- macOS
- Windows
- SaaS
- Office Suite
tactics:
- credential-access
title: credential-access - Steal Web Session Cookie
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS, Windows, SaaS, Office Suite |
| **Data Sources** | Process: Process Access, File: File Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1539](https://attack.mitre.org/techniques/T1539) |

# Steal Web Session Cookie (attack-pattern--10ffac09-e42d-4f56-ab20-db94c67d76ff)

## Description
An adversary may steal web application or service session cookies and use them to gain access to web applications or Internet services as an authenticated user without needing credentials. Web applications and services often use session cookies as an authentication token after a user has authenticated to a website.

Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services). Session cookies can be used to bypasses some multi-factor authentication protocols.(Citation: Pass The Cookie)

There are several examples of malware targeting cookies from web browsers on the local system.(Citation: Kaspersky TajMahal April 2019)(Citation: Unit 42 Mac Crypto Cookies January 2019) Adversaries may also steal cookies by injecting malicious JavaScript content into websites or relying on [User Execution](https://attack.mitre.org/techniques/T1204) by tricking victims into running malicious JavaScript in their browser.(Citation: Talos Roblox Scam 2023)(Citation: Krebs Discord Bookmarks 2023)

There are also open source frameworks such as `Evilginx2` and `Muraena` that can gather session cookies through a malicious proxy (e.g., [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557)) that can be set up by an adversary and used in phishing campaigns.(Citation: Github evilginx2)(Citation: GitHub Mauraena)

After an adversary acquires a valid cookie, they can then perform a [Web Session Cookie](https://attack.mitre.org/techniques/T1550/004) technique to login to the corresponding web application.

## Detection
Monitor for attempts to access files and repositories on a local system that are used to store browser session cookies. Monitor for attempts by programs to inject into or dump browser process memory.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1539)
- [Krebs Discord Bookmarks 2023](https://krebsonsecurity.com/2023/05/discord-admins-hacked-by-malicious-bookmarks/)
- [Unit 42 Mac Crypto Cookies January 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
- [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
- [Github evilginx2](https://github.com/kgretzky/evilginx2)
- [GitHub Mauraena](https://github.com/muraenateam/muraena)
- [Pass The Cookie](https://wunderwuzzi23.github.io/blog/passthecookie.html)
- [Talos Roblox Scam 2023](https://blog.talosintelligence.com/roblox-scam-overview/)
