---
contributors:
- Justin Warner, ICEBRG
data_sources:
- 'Process: Process Modification'
- 'Process: Process Access'
- 'Logon Session: Logon Session Creation'
id: attack-pattern--544b0346-29ad-41e1-a808-501bb4193f47
mitre_attack_url: https://attack.mitre.org/techniques/T1185
name: Browser Session Hijacking
platforms:
- Windows
tactics:
- collection
title: collection - Browser Session Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Modification, Process: Process Access, Logon Session: Logon Session Creation |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1185](https://attack.mitre.org/techniques/T1185) |

# Browser Session Hijacking (attack-pattern--544b0346-29ad-41e1-a808-501bb4193f47)

## Description
Adversaries may take advantage of security vulnerabilities and inherent functionality in browser software to change content, modify user-behaviors, and intercept information as part of various browser session hijacking techniques.(Citation: Wikipedia Man in the Browser)

A specific example is when an adversary injects software into a browser that allows them to inherit cookies, HTTP sessions, and SSL client certificates of a user then use the browser as a way to pivot into an authenticated intranet.(Citation: Cobalt Strike Browser Pivot)(Citation: ICEBRG Chrome Extensions) Executing browser-based behaviors such as pivoting may require specific process permissions, such as <code>SeDebugPrivilege</code> and/or high-integrity/administrator rights.

Another example involves pivoting browser traffic from the adversary's browser through the user's browser by setting up a proxy which will redirect web traffic. This does not alter the user's traffic in any way, and the proxy connection can be severed as soon as the browser is closed. The adversary assumes the security context of whichever browser process the proxy is injected into. Browsers typically create a new process for each tab that is opened and permissions and certificates are separated accordingly. With these permissions, an adversary could potentially browse to any resource on an intranet, such as [Sharepoint](https://attack.mitre.org/techniques/T1213/002) or webmail, that is accessible through the browser and which the browser has sufficient permissions. Browser pivoting may also bypass security provided by 2-factor authentication.(Citation: cobaltstrike manual)

## Detection
This may be a difficult technique to detect because adversary traffic may be masked by normal user traffic. New processes may not be created and no additional software dropped to disk. Authentication logs can be used to audit logins to specific web applications, but determining malicious logins versus benign logins may be difficult if activity matches typical user behavior. Monitor for [Process Injection](https://attack.mitre.org/techniques/T1055) against browser applications.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1185)
- [Wikipedia Man in the Browser](https://en.wikipedia.org/wiki/Man-in-the-browser)
- [Cobalt Strike Browser Pivot](https://www.cobaltstrike.com/help-browser-pivoting)
- [ICEBRG Chrome Extensions](https://www.icebrg.io/blog/malicious-chrome-extensions-enable-criminals-to-impact-over-half-a-million-users-and-global-businesses)
- [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
