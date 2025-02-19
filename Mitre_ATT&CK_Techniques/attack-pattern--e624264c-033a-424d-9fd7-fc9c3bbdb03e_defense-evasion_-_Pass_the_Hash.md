---
contributors:
- Blake Strom, Microsoft 365 Defender
- Travis Smith, Tripwire
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Active Directory: Active Directory Credential Request'
- 'User Account: User Account Authentication'
id: attack-pattern--e624264c-033a-424d-9fd7-fc9c3bbdb03e
mitre_attack_url: https://attack.mitre.org/techniques/T1550/002
name: Pass the Hash
platforms:
- Windows
tactics:
- defense-evasion
- lateral-movement
title: defense-evasion - Pass the Hash
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, lateral-movement |
| **Platforms** | Windows |
| **Data Sources** | Logon Session: Logon Session Creation, Active Directory: Active Directory Credential Request, User Account: User Account Authentication |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1550/002](https://attack.mitre.org/techniques/T1550/002) |

# Pass the Hash (attack-pattern--e624264c-033a-424d-9fd7-fc9c3bbdb03e)

## Description
Adversaries may “pass the hash” using stolen password hashes to move laterally within an environment, bypassing normal system access controls. Pass the hash (PtH) is a method of authenticating as a user without having access to the user's cleartext password. This method bypasses standard authentication steps that require a cleartext password, moving directly into the portion of the authentication that uses the password hash.

When performing PtH, valid password hashes for the account being used are captured using a [Credential Access](https://attack.mitre.org/tactics/TA0006) technique. Captured hashes are used with PtH to authenticate as that user. Once authenticated, PtH may be used to perform actions on local or remote systems.

Adversaries may also use stolen password hashes to "overpass the hash." Similar to PtH, this involves using a password hash to authenticate as a user but also uses the password hash to create a valid Kerberos ticket. This ticket can then be used to perform [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003) attacks.(Citation: Stealthbits Overpass-the-Hash)

## Detection
Audit all logon and credential use events and review for discrepancies. Unusual remote logins that correlate with other suspicious activity (such as writing and executing binaries) may indicate malicious activity. NTLM LogonType 3 authentications that are not associated to a domain login and are not anonymous logins are suspicious.

Event ID 4768 and 4769 will also be generated on the Domain Controller when a user requests a new ticket granting ticket or service ticket. These events combined with the above activity may be indicative of an overpass the hash attempt.(Citation: Stealthbits Overpass-the-Hash)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1550/002)
- [Stealthbits Overpass-the-Hash](https://stealthbits.com/blog/how-to-detect-overpass-the-hash-attacks/)
