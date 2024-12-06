---
contributors:
- Matthew Molyett, @s1air, Cisco Talos
id: attack-pattern--91ce1ede-107f-4d8b-bf4c-735e8789c94b
mitre_attack_url: https://attack.mitre.org/techniques/T1141
name: Input Prompt
platforms:
- macOS
- Windows
tactics:
- credential-access
title: credential-access - Input Prompt
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | macOS, Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1141](https://attack.mitre.org/techniques/T1141) |

# Input Prompt (attack-pattern--91ce1ede-107f-4d8b-bf4c-735e8789c94b)

## Description
When programs are executed that need additional privileges than are present in the current user context, it is common for the operating system to prompt the user for proper credentials to authorize the elevated privileges for the task (ex: [Bypass User Account Control](https://attack.mitre.org/techniques/T1088)).

Adversaries may mimic this functionality to prompt users for credentials with a seemingly legitimate prompt for a number of reasons that mimic normal usage, such as a fake installer requiring additional access or a fake malware removal suite.(Citation: OSX Malware Exploits MacKeeper) This type of prompt can be used to collect credentials via various languages such as [AppleScript](https://attack.mitre.org/techniques/T1155)(Citation: LogRhythm Do You Trust Oct 2014)(Citation: OSX Keydnap malware) and [PowerShell](https://attack.mitre.org/techniques/T1086)(Citation: LogRhythm Do You Trust Oct 2014)(Citation: Enigma Phishing for Credentials Jan 2015).

## Detection
Monitor process execution for unusual programs as well as malicious instances of [Scripting](https://attack.mitre.org/techniques/T1064) that could be used to prompt users for credentials.

Inspect and scrutinize input prompts for indicators of illegitimacy, such as non-traditional banners, text, timing, and/or sources.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1141)
- [capec](https://capec.mitre.org/data/definitions/569.html)
- [OSX Malware Exploits MacKeeper](https://baesystemsai.blogspot.com/2015/06/new-mac-os-malware-exploits-mackeeper.html)
- [LogRhythm Do You Trust Oct 2014](https://logrhythm.com/blog/do-you-trust-your-computer/)
- [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
- [Enigma Phishing for Credentials Jan 2015](https://enigma0x3.net/2015/01/21/phishing-for-credentials-if-you-want-it-just-ask/)
