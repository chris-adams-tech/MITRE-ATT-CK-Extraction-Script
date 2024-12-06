---
id: attack-pattern--ce73ea43-8e77-47ba-9c11-5e9c9c58b9ff
mitre_attack_url: https://attack.mitre.org/techniques/T1147
name: Hidden Users
platforms:
- macOS
tactics:
- defense-evasion
title: defense-evasion - Hidden Users
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS |
| **Permissions Required** | Administrator, root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1147](https://attack.mitre.org/techniques/T1147) |

# Hidden Users (attack-pattern--ce73ea43-8e77-47ba-9c11-5e9c9c58b9ff)

## Description
Every user account in macOS has a userID associated with it. When creating a user, you can specify the userID for that account. There is a property value in <code>/Library/Preferences/com.apple.loginwindow</code> called <code>Hide500Users</code> that prevents users with userIDs 500 and lower from appearing at the login screen. By using the [Create Account](https://attack.mitre.org/techniques/T1136) technique with a userID under 500 and enabling this property (setting it to Yes), an adversary can hide their user accounts much more easily: <code>sudo dscl . -create /Users/username UniqueID 401</code> (Citation: Cybereason OSX Pirrit).

## Detection
This technique prevents the new user from showing up at the log in screen, but all of the other signs of a new user still exist. The user still gets a home directory and will appear in the authentication logs.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1147)
- [Cybereason OSX Pirrit](https://cdn2.hubspot.net/hubfs/3354902/Content%20PDFs/Cybereason-Lab-Analysis-OSX-Pirrit-4-6-16.pdf)
