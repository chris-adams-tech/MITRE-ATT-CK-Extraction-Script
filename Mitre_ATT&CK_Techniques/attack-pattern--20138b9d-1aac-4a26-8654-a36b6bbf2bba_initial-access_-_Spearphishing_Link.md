---
contributors:
- Shailesh Tiwary (Indian Army)
- Mark Wee
- Jeff Sakowicz, Microsoft Identity Developer Platform Services (IDPM Services)
- Saisha Agrawal, Microsoft Threat Intelligent Center (MSTIC)
id: attack-pattern--20138b9d-1aac-4a26-8654-a36b6bbf2bba
mitre_attack_url: https://attack.mitre.org/techniques/T1192
name: Spearphishing Link
platforms:
- Windows
- macOS
- Linux
- Office 365
- SaaS
tactics:
- initial-access
title: initial-access - Spearphishing Link
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Windows, macOS, Linux, Office 365, SaaS |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1192](https://attack.mitre.org/techniques/T1192) |

# Spearphishing Link (attack-pattern--20138b9d-1aac-4a26-8654-a36b6bbf2bba)

## Description
Spearphishing with a link is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of links to download malware contained in email, instead of attaching malicious files to the email itself, to avoid defenses that may inspect email attachments. 

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this case, the malicious emails contain links. Generally, the links will be accompanied by social engineering text and require the user to actively click or copy and paste a URL into a browser, leveraging [User Execution](https://attack.mitre.org/techniques/T1204). The visited website may compromise the web browser using an exploit, or the user will be prompted to download applications, documents, zip files, or even executables depending on the pretext for the email in the first place. Adversaries may also include links that are intended to interact directly with an email reader, including embedded images intended to exploit the end system directly or verify the receipt of an email (i.e. web bugs/web beacons). Links may also direct users to malicious applications  designed to [Steal Application Access Token](https://attack.mitre.org/techniques/T1528)s, like OAuth tokens, in order to gain access to protected applications and information.(Citation: Trend Micro Pawn Storm OAuth 2017)

## Detection
URL inspection within email (including expanding shortened links) can help detect links leading to known malicious sites. Detonation chambers can be used to detect these links and either automatically go to these sites to determine if they're potentially malicious, or wait and capture the content if a user visits the link.

Because this technique usually involves user interaction on the endpoint, many of the possible detections for Spearphishing Link take place once [User Execution](https://attack.mitre.org/techniques/T1204) occurs.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1192)
- [capec](https://capec.mitre.org/data/definitions/163.html)
- [Trend Micro Pawn Storm OAuth 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/pawn-storm-abuses-open-authentication-advanced-social-engineering-attacks)
