---
contributors:
- Ryan Benson, Exabeam
- Barry Shteiman, Exabeam
- Sylvain Gil, Exabeam
- RedHuntLabs, @redhuntlabs
id: attack-pattern--4579d9c9-d5b9-45e0-9848-0104637b579f
mitre_attack_url: https://attack.mitre.org/techniques/T1503
name: Credentials from Web Browsers
platforms:
- Linux
- macOS
- Windows
tactics:
- credential-access
title: credential-access - Credentials from Web Browsers
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS, Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1503](https://attack.mitre.org/techniques/T1503) |

# Credentials from Web Browsers (attack-pattern--4579d9c9-d5b9-45e0-9848-0104637b579f)

## Description
Adversaries may acquire credentials from web browsers by reading files specific to the target browser.  (Citation: Talos Olympic Destroyer 2018) 

Web browsers commonly save credentials such as website usernames and passwords so that they do not need to be entered manually in the future. Web browsers typically store the credentials in an encrypted format within a credential store; however, methods exist to extract plaintext credentials from web browsers.

For example, on Windows systems, encrypted credentials may be obtained from Google Chrome by reading a database file, <code>AppData\Local\Google\Chrome\User Data\Default\Login Data</code> and executing a SQL query: <code>SELECT action_url, username_value, password_value FROM logins;</code>. The plaintext password can then be obtained by passing the encrypted credentials to the Windows API function <code>CryptUnprotectData</code>, which uses the victim’s cached logon credentials as the decryption key. (Citation: Microsoft CryptUnprotectData April 2018)
 
Adversaries have executed similar procedures for common web browsers such as FireFox, Safari, Edge, etc. (Citation: Proofpoint Vega Credential Stealer May 2018)(Citation: FireEye HawkEye Malware July 2017)

Adversaries may also acquire credentials by searching web browser process memory for patterns that commonly match credentials.(Citation: GitHub Mimikittenz July 2016)

After acquiring credentials from web browsers, adversaries may attempt to recycle the credentials across different systems and/or accounts in order to expand access. This can result in significantly furthering an adversary's objective in cases where credentials gained from web browsers overlap with privileged accounts (e.g. domain administrator).

## Detection
Identify web browser files that contain credentials such as Google Chrome’s Login Data database file: <code>AppData\Local\Google\Chrome\User Data\Default\Login Data</code>. Monitor file read events of web browser files that contain credentials, especially when the reading process is unrelated to the subject web browser. Monitor process execution logs to include PowerShell Transcription focusing on those that perform a combination of behaviors including reading web browser process memory, utilizing regular expressions, and those that contain numerous keywords for common web applications (Gmail, Twitter, Office365, etc.).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1503)
- [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Microsoft CryptUnprotectData April 2018](https://docs.microsoft.com/en-us/windows/desktop/api/dpapi/nf-dpapi-cryptunprotectdata)
- [Proofpoint Vega Credential Stealer May 2018](https://www.proofpoint.com/us/threat-insight/post/new-vega-stealer-shines-brightly-targeted-campaign)
- [FireEye HawkEye Malware July 2017](https://www.fireeye.com/blog/threat-research/2017/07/hawkeye-malware-distributed-in-phishing-campaign.html)
- [GitHub Mimikittenz July 2016](https://github.com/putterpanda/mimikittenz)
