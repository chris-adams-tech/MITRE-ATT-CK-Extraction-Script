---
contributors:
- Philip Winther
- Shailesh Tiwary (Indian Army)
- Mark Wee
- Jeff Sakowicz, Microsoft Identity Developer Platform Services (IDPM Services)
- Saisha Agrawal, Microsoft Threat Intelligent Center (MSTIC)
- Kobi Haimovich, CardinalOps
- Menachem Goldstein
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--2b742742-28c3-4e1b-bab7-8350d6300fa7
mitre_attack_url: https://attack.mitre.org/techniques/T1566/002
name: Spearphishing Link
platforms:
- Linux
- macOS
- Windows
- SaaS
- Identity Provider
- Office Suite
tactics:
- initial-access
title: initial-access - Spearphishing Link
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Linux, macOS, Windows, SaaS, Identity Provider, Office Suite |
| **Data Sources** | Network Traffic: Network Traffic Flow, Application Log: Application Log Content, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1566/002](https://attack.mitre.org/techniques/T1566/002) |

# Spearphishing Link (attack-pattern--2b742742-28c3-4e1b-bab7-8350d6300fa7)

## Description
Adversaries may send spearphishing emails with a malicious link in an attempt to gain access to victim systems. Spearphishing with a link is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of links to download malware contained in email, instead of attaching malicious files to the email itself, to avoid defenses that may inspect email attachments. Spearphishing may also involve social engineering techniques, such as posing as a trusted source.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this case, the malicious emails contain links. Generally, the links will be accompanied by social engineering text and require the user to actively click or copy and paste a URL into a browser, leveraging [User Execution](https://attack.mitre.org/techniques/T1204). The visited website may compromise the web browser using an exploit, or the user will be prompted to download applications, documents, zip files, or even executables depending on the pretext for the email in the first place.

Adversaries may also include links that are intended to interact directly with an email reader, including embedded images intended to exploit the end system directly. Additionally, adversaries may use seemingly benign links that abuse special characters to mimic legitimate websites (known as an "IDN homograph attack").(Citation: CISA IDN ST05-016) URLs may also be obfuscated by taking advantage of quirks in the URL schema, such as the acceptance of integer- or hexadecimal-based hostname formats and the automatic discarding of text before an “@” symbol: for example, `hxxp://google.com@1157586937`.(Citation: Mandiant URL Obfuscation 2023)

Adversaries may also utilize links to perform consent phishing, typically with OAuth 2.0 request URLs that when accepted by the user provide permissions/access for malicious applications, allowing adversaries to  [Steal Application Access Token](https://attack.mitre.org/techniques/T1528)s.(Citation: Trend Micro Pawn Storm OAuth 2017) These stolen access tokens allow the adversary to perform various actions on behalf of the user via API calls. (Citation: Microsoft OAuth 2.0 Consent Phishing 2021)

Adversaries may also utilize spearphishing links to [Steal Application Access Token](https://attack.mitre.org/techniques/T1528)s that grant immediate access to the victim environment. For example, a user may be lured through “consent phishing” into granting adversaries permissions/access via a malicious OAuth 2.0 request URL .(Citation: Trend Micro Pawn Storm OAuth 2017)(Citation: Microsoft OAuth 2.0 Consent Phishing 2021)

Similarly, malicious links may also target device-based authorization, such as OAuth 2.0 device authorization grant flow which is typically used to authenticate devices without UIs/browsers. Known as “device code phishing,” an adversary may send a link that directs the victim to a malicious authorization page where the user is tricked into entering a code/credentials that produces a device token.(Citation: SecureWorks Device Code Phishing 2021)(Citation: Netskope Device Code Phishing 2021)(Citation: Optiv Device Code Phishing 2021)

## Detection
URL inspection within email (including expanding shortened links) can help detect links leading to known malicious sites as well as links redirecting to adversary infrastructure based by upon suspicious OAuth patterns with unusual TLDs.(Citation: Microsoft OAuth 2.0 Consent Phishing 2021). Detonation chambers can be used to detect these links and either automatically go to these sites to determine if they're potentially malicious, or wait and capture the content if a user visits the link.

Filtering based on DKIM+SPF or header analysis can help detect when the email sender is spoofed.(Citation: Microsoft Anti Spoofing)(Citation: ACSC Email Spoofing)

Because this technique usually involves user interaction on the endpoint, many of the possible detections take place once [User Execution](https://attack.mitre.org/techniques/T1204) occurs.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1566/002)
- [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)
- [CISA IDN ST05-016](https://us-cert.cisa.gov/ncas/tips/ST05-016)
- [Trend Micro Pawn Storm OAuth 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/pawn-storm-abuses-open-authentication-advanced-social-engineering-attacks)
- [Netskope Device Code Phishing 2021](https://www.netskope.com/blog/new-phishing-attacks-exploiting-oauth-authorization-flows-part-1)
- [Microsoft OAuth 2.0 Consent Phishing 2021](https://www.microsoft.com/security/blog/2021/07/14/microsoft-delivers-comprehensive-solution-to-battle-rise-in-consent-phishing-emails/)
- [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)
- [Mandiant URL Obfuscation 2023](https://www.mandiant.com/resources/blog/url-obfuscation-schema-abuse)
- [Optiv Device Code Phishing 2021](https://www.optiv.com/insights/source-zero/blog/microsoft-365-oauth-device-code-flow-and-phishing)
- [SecureWorks Device Code Phishing 2021](https://www.secureworks.com/blog/oauths-device-code-flow-abused-in-phishing-attacks)
