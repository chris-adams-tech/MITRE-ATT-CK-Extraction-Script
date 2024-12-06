---
contributors:
- Matthew Molyett, @s1air, Cisco Talos
data_sources:
- 'Script: Script Execution'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--a2029942-0a85-4947-b23c-ca434698171d
mitre_attack_url: https://attack.mitre.org/techniques/T1056/002
name: GUI Input Capture
platforms:
- macOS
- Windows
- Linux
tactics:
- collection
- credential-access
title: collection - GUI Input Capture
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection, credential-access |
| **Platforms** | macOS, Windows, Linux |
| **Data Sources** | Script: Script Execution, Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1056/002](https://attack.mitre.org/techniques/T1056/002) |

# GUI Input Capture (attack-pattern--a2029942-0a85-4947-b23c-ca434698171d)

## Description
Adversaries may mimic common operating system GUI components to prompt users for credentials with a seemingly legitimate prompt. When programs are executed that need additional privileges than are present in the current user context, it is common for the operating system to prompt the user for proper credentials to authorize the elevated privileges for the task (ex: [Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002)).

Adversaries may mimic this functionality to prompt users for credentials with a seemingly legitimate prompt for a number of reasons that mimic normal usage, such as a fake installer requiring additional access or a fake malware removal suite.(Citation: OSX Malware Exploits MacKeeper) This type of prompt can be used to collect credentials via various languages such as [AppleScript](https://attack.mitre.org/techniques/T1059/002)(Citation: LogRhythm Do You Trust Oct 2014)(Citation: OSX Keydnap malware)(Citation: Spoofing credential dialogs) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).(Citation: LogRhythm Do You Trust Oct 2014)(Citation: Enigma Phishing for Credentials Jan 2015)(Citation: Spoofing credential dialogs) On Linux systems adversaries may launch dialog boxes prompting users for credentials from malicious shell scripts or the command line (i.e. [Unix Shell](https://attack.mitre.org/techniques/T1059/004)).(Citation: Spoofing credential dialogs)

Adversaries may also mimic common software authentication requests, such as those from browsers or email clients. This may also be paired with user activity monitoring (i.e., [Browser Information Discovery](https://attack.mitre.org/techniques/T1217) and/or [Application Window Discovery](https://attack.mitre.org/techniques/T1010)) to spoof prompts when users are naturally accessing sensitive sites/data.

## Detection
Monitor process execution for unusual programs as well as malicious instances of [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) that could be used to prompt users for credentials. For example, command/script history including abnormal parameters (such as requests for credentials and/or strings related to creating password prompts) may be malicious.(Citation: Spoofing credential dialogs) 

Inspect and scrutinize input prompts for indicators of illegitimacy, such as non-traditional banners, text, timing, and/or sources. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1056/002)
- [LogRhythm Do You Trust Oct 2014](https://logrhythm.com/blog/do-you-trust-your-computer/)
- [Spoofing credential dialogs](https://embracethered.com/blog/posts/2021/spoofing-credential-dialogs/)
- [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
- [Enigma Phishing for Credentials Jan 2015](https://enigma0x3.net/2015/01/21/phishing-for-credentials-if-you-want-it-just-ask/)
- [OSX Malware Exploits MacKeeper](https://baesystemsai.blogspot.com/2015/06/new-mac-os-malware-exploits-mackeeper.html)
