---
contributors:
- TruKno
- Liran Ravich, CardinalOps
- Serhii Melnyk, Trustwave SpiderLabs
- Rahmat Nurfauzi, @infosecn1nja, PT Xynexis International
- '@_montysecurity'
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--3a32740a-11b0-4bcf-b0a9-3abd0f6d3cd5
mitre_attack_url: https://attack.mitre.org/techniques/T1059/010
name: AutoHotKey & AutoIT
platforms:
- Windows
tactics:
- execution
title: execution - AutoHotKey & AutoIT
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/010](https://attack.mitre.org/techniques/T1059/010) |

# AutoHotKey & AutoIT (attack-pattern--3a32740a-11b0-4bcf-b0a9-3abd0f6d3cd5)

## Description
Adversaries may execute commands and perform malicious tasks using AutoIT and AutoHotKey automation scripts. AutoIT and AutoHotkey (AHK) are scripting languages that enable users to automate Windows tasks. These automation scripts can be used to perform a wide variety of actions, such as clicking on buttons, entering text, and opening and closing programs.(Citation: AutoIT)(Citation: AutoHotKey)

Adversaries may use AHK (`.ahk`) and AutoIT (`.au3`) scripts to execute malicious code on a victim's system. For example, adversaries have used for AHK to execute payloads and other modular malware such as keyloggers. Adversaries have also used custom AHK files containing embedded malware as [Phishing](https://attack.mitre.org/techniques/T1566) payloads.(Citation: Splunk DarkGate)

These scripts may also be compiled into self-contained executable payloads (`.exe`).(Citation: AutoIT)(Citation: AutoHotKey)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/010)
- [AutoHotKey](https://www.autohotkey.com/docs/v1/Program.htm)
- [AutoIT](https://www.autoitscript.com/autoit3/docs/intro/running.htm)
- [Splunk DarkGate](https://www.splunk.com/en_us/blog/security/enter-the-gates-an-analysis-of-the-darkgate-autoit-loader.html)
