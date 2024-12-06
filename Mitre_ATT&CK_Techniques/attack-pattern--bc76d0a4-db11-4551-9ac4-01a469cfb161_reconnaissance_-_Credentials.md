---
contributors:
- Vinayak Wadhwa, Lucideus
- Lee Christensen, SpecterOps
- Toby Kohlenberg
- "Massimo Giaimo, W\xFCrth Group Cyber Defence Center"
id: attack-pattern--bc76d0a4-db11-4551-9ac4-01a469cfb161
mitre_attack_url: https://attack.mitre.org/techniques/T1589/001
name: Credentials
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Credentials
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1589/001](https://attack.mitre.org/techniques/T1589/001) |

# Credentials (attack-pattern--bc76d0a4-db11-4551-9ac4-01a469cfb161)

## Description
Adversaries may gather credentials that can be used during targeting. Account credentials gathered by adversaries may be those directly associated with the target victim organization or attempt to take advantage of the tendency for users to use the same passwords across personal and business accounts.

Adversaries may gather credentials from potential victims in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598). Adversaries may also compromise sites then add malicious content designed to collect website authentication cookies from visitors.(Citation: ATT ScanBox) (Citation: Register Deloitte)(Citation: Register Uber)(Citation: Detectify Slack Tokens)(Citation: Forbes GitHub Creds)(Citation: GitHub truffleHog)(Citation: GitHub Gitrob)(Citation: CNET Leaks) Where multi-factor authentication (MFA) based on out-of-band communications is in use, adversaries may compromise a service provider to gain access to MFA codes and one-time passwords (OTP).(Citation: Okta Scatter Swine 2022)

Credential information may also be exposed to adversaries via leaks to online or other accessible data sets (ex: [Search Engines](https://attack.mitre.org/techniques/T1593/002), breach dumps, code repositories, etc.). Adversaries may purchase credentials from dark web markets, such as Russian Market and 2easy, or through access to Telegram channels that distribute logs from infostealer malware.(Citation: Bleeping Computer 2easy 2021)(Citation: SecureWorks Infostealers 2023)(Citation: Bleeping Computer Stealer Logs 2023)

Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Valid Accounts](https://attack.mitre.org/techniques/T1078)). 

## Detection
Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders.

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1589/001)
- [Bleeping Computer 2easy 2021](https://www.bleepingcomputer.com/news/security/2easy-now-a-significant-dark-web-marketplace-for-stolen-data/)
- [ATT ScanBox](https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks)
- [Detectify Slack Tokens](https://labs.detectify.com/2016/04/28/slack-bot-token-leakage-exposing-business-critical-information/)
- [GitHub truffleHog](https://github.com/dxa4481/truffleHog)
- [Bleeping Computer Stealer Logs 2023](https://www.bleepingcomputer.com/news/security/dissecting-the-dark-web-supply-chain-stealer-logs-in-context/)
- [Register Uber](https://www.theregister.com/2015/02/28/uber_subpoenas_github_for_hacker_details/)
- [GitHub Gitrob](https://github.com/michenriksen/gitrob)
- [CNET Leaks](https://www.cnet.com/news/massive-breach-leaks-773-million-emails-21-million-passwords/)
- [Okta Scatter Swine 2022](https://sec.okta.com/scatterswine)
- [Forbes GitHub Creds](https://www.forbes.com/sites/runasandvik/2014/01/14/attackers-scrape-github-for-cloud-service-credentials-hijack-account-to-mine-virtual-currency/#242c479d3196)
- [SecureWorks Infostealers 2023](https://www.secureworks.com/research/the-growing-threat-from-infostealers)
- [Register Deloitte](https://www.theregister.com/2017/09/26/deloitte_leak_github_and_google/)
