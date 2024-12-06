---
data_sources:
- 'Application Log: Application Log Content'
id: attack-pattern--bb5e59c4-abe7-40c7-8196-e373cb1e5974
mitre_attack_url: https://attack.mitre.org/techniques/T1566/004
name: Spearphishing Voice
platforms:
- Linux
- macOS
- Windows
- Identity Provider
tactics:
- initial-access
title: initial-access - Spearphishing Voice
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Linux, macOS, Windows, Identity Provider |
| **Data Sources** | Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1566/004](https://attack.mitre.org/techniques/T1566/004) |

# Spearphishing Voice (attack-pattern--bb5e59c4-abe7-40c7-8196-e373cb1e5974)

## Description
Adversaries may use voice communications to ultimately gain access to victim systems. Spearphishing voice is a specific variant of spearphishing. It is different from other forms of spearphishing in that is employs the use of manipulating a user into providing access to systems through a phone call or other forms of voice communications. Spearphishing frequently involves social engineering techniques, such as posing as a trusted source (ex: [Impersonation](https://attack.mitre.org/techniques/T1656)) and/or creating a sense of urgency or alarm for the recipient.

All forms of phishing are electronically delivered social engineering. In this scenario, adversaries are not directly sending malware to a victim vice relying on [User Execution](https://attack.mitre.org/techniques/T1204) for delivery and execution. For example, victims may receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware,(Citation: sygnia Luna Month)(Citation: CISA Remote Monitoring and Management Software) or install adversary-accessible remote management tools ([Remote Access Software](https://attack.mitre.org/techniques/T1219)) onto their computer.(Citation: Unit42 Luna Moth)

Adversaries may also combine voice phishing with [Multi-Factor Authentication Request Generation](https://attack.mitre.org/techniques/T1621) in order to trick users into divulging MFA credentials or accepting authentication prompts.(Citation: Proofpoint Vishing)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1566/004)
- [CISA Remote Monitoring and Management Software](https://www.cisa.gov/uscert/ncas/alerts/aa23-025a)
- [Unit42 Luna Moth](https://unit42.paloaltonetworks.com/luna-moth-callback-phishing/)
- [sygnia Luna Month](https://blog.sygnia.co/luna-moth-false-subscription-scams)
- [Proofpoint Vishing](https://www.proofpoint.com/us/threat-reference/vishing)
