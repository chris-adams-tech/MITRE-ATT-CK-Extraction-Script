---
contributors:
- Philip Winther
- Sebastian Salla, McAfee
- Menachem Goldstein
- Robert Simmons, @MalwareUtkonos
- Elpidoforos Maragkos, @emaragkos
- Joas Antonio dos Santos, @C0d3Cr4zy
- Austin Herrin
- Obsidian Security
- Sam Seabrook, Duke Energy
data_sources:
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--2d3f5b3c-54ca-4f4d-bb1f-849346d31230
mitre_attack_url: https://attack.mitre.org/techniques/T1598/003
name: Spearphishing Link
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Spearphishing Link
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **Data Sources** | Application Log: Application Log Content, Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1598/003](https://attack.mitre.org/techniques/T1598/003) |

# Spearphishing Link (attack-pattern--2d3f5b3c-54ca-4f4d-bb1f-849346d31230)

## Description
Adversaries may send spearphishing messages with a malicious link to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, the malicious emails contain links generally accompanied by social engineering text to coax the user to actively click or copy and paste a URL into a browser.(Citation: TrendMictro Phishing)(Citation: PCMag FakeLogin) The given website may be a clone of a legitimate site (such as an online or corporate login portal) or may closely resemble a legitimate site in appearance and have a URL containing elements from the real site. URLs may also be obfuscated by taking advantage of quirks in the URL schema, such as the acceptance of integer- or hexadecimal-based hostname formats and the automatic discarding of text before an “@” symbol: for example, `hxxp://google.com@1157586937`.(Citation: Mandiant URL Obfuscation 2023)

Adversaries may also embed “tracking pixels”, "web bugs", or "web beacons" within phishing messages to verify the receipt of an email, while also potentially profiling and tracking victim information such as IP address.(Citation: NIST Web Bug) (Citation: Ryte Wiki) These mechanisms often appear as small images (typically one pixel in size) or otherwise obfuscated objects and are typically delivered as HTML code containing a link to a remote server. (Citation: Ryte Wiki)(Citation: IAPP)

Adversaries may also be able to spoof a complete website using what is known as a "browser-in-the-browser" (BitB) attack. By generating a fake browser popup window with an HTML-based address bar that appears to contain a legitimate URL (such as an authentication portal), they may be able to prompt users to enter their credentials while bypassing typical URL verification methods.(Citation: ZScaler BitB 2020)(Citation: Mr. D0x BitB 2022)

Adversaries can use phishing kits such as `EvilProxy` and `Evilginx2` to perform adversary-in-the-middle phishing by proxying the connection between the victim and the legitimate website. On a successful login, the victim is redirected to the legitimate website, while the adversary captures their session cookie (i.e., [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539)) in addition to their username and password. This may enable the adversary to then bypass MFA via [Web Session Cookie](https://attack.mitre.org/techniques/T1550/004).(Citation: Proofpoint Human Factor)

Adversaries may also send a malicious link in the form of Quick Response (QR) Codes (also known as “quishing”). These links may direct a victim to a credential phishing page.(Citation: QR-campaign-energy-firm) By using a QR code, the URL may not be exposed in the email and may thus go undetected by most automated email security scans.(Citation: qr-phish-agriculture) These QR codes may be scanned by or delivered directly  to a user’s mobile device (i.e., [Phishing](https://attack.mitre.org/techniques/T1660)), which may be less secure in several relevant ways.(Citation: qr-phish-agriculture) For example, mobile users may not be able to notice minor differences between genuine and credential harvesting websites due to mobile’s smaller form factor.

From the fake website, information is gathered in web forms and sent to the adversary. Adversaries may also use information from previous reconnaissance efforts (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)) to craft persuasive and believable lures.

## Detection
Monitor for suspicious email activity, such as numerous accounts receiving messages from a single unusual/unknown sender. Filtering based on DKIM+SPF or header analysis can help detect when the email sender is spoofed.(Citation: Microsoft Anti Spoofing)(Citation: ACSC Email Spoofing)

Monitor for references to uncategorized or known-bad sites. URL inspection within email (including expanding shortened links) can also help detect links leading to known malicious sites.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1598/003)
- [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)
- [TrendMictro Phishing](https://www.trendmicro.com/en_us/research/20/i/tricky-forms-of-phishing.html)
- [IAPP](https://iapp.org/resources/article/web-beacon/)
- [QR-campaign-energy-firm](https://therecord.media/phishing-campaign-used-qr-codes-to-target-energy-firm)
- [PCMag FakeLogin](https://www.pcmag.com/news/hackers-try-to-phish-united-nations-staffers-with-fake-login-pages)
- [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)
- [Mr. D0x BitB 2022](https://mrd0x.com/browser-in-the-browser-phishing-attack/)
- [Mandiant URL Obfuscation 2023](https://www.mandiant.com/resources/blog/url-obfuscation-schema-abuse)
- [NIST Web Bug](https://csrc.nist.gov/glossary/term/web_bug)
- [Proofpoint Human Factor](https://www.proofpoint.com/sites/default/files/threat-reports/pfpt-us-tr-human-factor-report.pdf)
- [Ryte Wiki](https://en.ryte.com/wiki/Tracking_Pixel)
- [qr-phish-agriculture](https://www.proofpoint.com/us/blog/email-and-cloud-threats/cybersecurity-stop-month-qr-code-phishing)
- [ZScaler BitB 2020](https://www.zscaler.com/blogs/security-research/fake-sites-stealing-steam-credentials)
