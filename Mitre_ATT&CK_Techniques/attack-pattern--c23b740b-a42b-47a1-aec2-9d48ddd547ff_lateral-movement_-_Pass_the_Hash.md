---
contributors:
- Travis Smith, Tripwire
id: attack-pattern--c23b740b-a42b-47a1-aec2-9d48ddd547ff
mitre_attack_url: https://attack.mitre.org/techniques/T1075
name: Pass the Hash
platforms:
- Windows
tactics:
- lateral-movement
title: lateral-movement - Pass the Hash
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows |
| **System Requirements** | Requires Microsoft Windows as target system |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1075](https://attack.mitre.org/techniques/T1075) |

# Pass the Hash (attack-pattern--c23b740b-a42b-47a1-aec2-9d48ddd547ff)

## Description
Pass the hash (PtH) is a method of authenticating as a user without having access to the user's cleartext password. This method bypasses standard authentication steps that require a cleartext password, moving directly into the portion of the authentication that uses the password hash. In this technique, valid password hashes for the account being used are captured using a Credential Access technique. Captured hashes are used with PtH to authenticate as that user. Once authenticated, PtH may be used to perform actions on local or remote systems. 

Windows 7 and higher with KB2871997 require valid domain user credentials or RID 500 administrator hashes. (Citation: NSA Spotting)

## Detection
Audit all logon and credential use events and review for discrepancies. Unusual remote logins that correlate with other suspicious activity (such as writing and executing binaries) may indicate malicious activity. NTLM LogonType 3 authentications that are not associated to a domain login and are not anonymous logins are suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1075)
- [capec](https://capec.mitre.org/data/definitions/644.html)
- [NSA Spotting](https://apps.nsa.gov/iaarchive/library/reports/spotting-the-adversary-with-windows-event-log-monitoring.cfm)
