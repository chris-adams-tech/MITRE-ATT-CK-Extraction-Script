---
contributors:
- Philip Winther
- Sebastian Salla, McAfee
- Robert Simmons, @MalwareUtkonos
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--8982a661-d84c-48c0-b4ec-1db29c6cf3bc
mitre_attack_url: https://attack.mitre.org/techniques/T1598/002
name: Spearphishing Attachment
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Spearphishing Attachment
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **Data Sources** | Network Traffic: Network Traffic Flow, Application Log: Application Log Content, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1598/002](https://attack.mitre.org/techniques/T1598/002) |

# Spearphishing Attachment (attack-pattern--8982a661-d84c-48c0-b4ec-1db29c6cf3bc)

## Description
Adversaries may send spearphishing messages with a malicious attachment to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon the recipient populating information then returning the file.(Citation: Sophos Attachment)(Citation: GitHub Phishery) The text of the spearphishing email usually tries to give a plausible reason why the file should be filled-in, such as a request for information from a business associate. Adversaries may also use information from previous reconnaissance efforts (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)) to craft persuasive and believable lures.

## Detection
Monitor for suspicious email activity, such as numerous accounts receiving messages from a single unusual/unknown sender. Filtering based on DKIM+SPF or header analysis can help detect when the email sender is spoofed.(Citation: Microsoft Anti Spoofing)(Citation: ACSC Email Spoofing)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1598/002)
- [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)
- [Sophos Attachment](https://nakedsecurity.sophos.com/2020/10/02/serious-security-phishing-without-links-when-phishers-bring-along-their-own-web-pages/)
- [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)
- [GitHub Phishery](https://github.com/ryhanson/phishery)
