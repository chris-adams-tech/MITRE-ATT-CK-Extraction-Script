---
contributors:
- Harshal Tupsamudre, Qualys
data_sources:
- 'Process: Process Creation'
- 'Process: OS API Execution'
- 'Windows Registry: Windows Registry Key Access'
- 'Command: Command Execution'
id: attack-pattern--c1b68a96-3c48-49ea-a6c0-9b27359f9c19
mitre_attack_url: https://attack.mitre.org/techniques/T1614/001
name: System Language Discovery
platforms:
- Windows
- Linux
- macOS
tactics:
- discovery
title: discovery - System Language Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Process: Process Creation, Process: OS API Execution, Windows Registry: Windows Registry Key Access, Command: Command Execution |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1614/001](https://attack.mitre.org/techniques/T1614/001) |

# System Language Discovery (attack-pattern--c1b68a96-3c48-49ea-a6c0-9b27359f9c19)

## Description
Adversaries may attempt to gather information about the system language of a victim in order to infer the geographical location of that host. This information may be used to shape follow-on behaviors, including whether the adversary infects the target and/or attempts specific actions. This decision may be employed by malware developers and operators to reduce their risk of attracting the attention of specific law enforcement agencies or prosecution/scrutiny from other entities.(Citation: Malware System Language Check)

There are various sources of data an adversary could use to infer system language, such as system defaults and keyboard layouts. Specific checks will vary based on the target and/or adversary, but may involve behaviors such as [Query Registry](https://attack.mitre.org/techniques/T1012) and calls to [Native API](https://attack.mitre.org/techniques/T1106) functions.(Citation: CrowdStrike Ryuk January 2019) 

For example, on a Windows system adversaries may attempt to infer the language of a system by querying the registry key <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language</code> or parsing the outputs of Windows API functions <code>GetUserDefaultUILanguage</code>, <code>GetSystemDefaultUILanguage</code>, <code>GetKeyboardLayoutList</code> and <code>GetUserDefaultLangID</code>.(Citation: Darkside Ransomware Cybereason)(Citation: Securelist JSWorm)(Citation: SecureList SynAck Doppelgänging May 2018)

On a macOS or Linux system, adversaries may query <code>locale</code> to retrieve the value of the <code>$LANG</code> environment variable.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system language information. This may include calls to various API functions and interaction with system configuration settings such as the Windows Registry.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1614/001)
- [Malware System Language Check](https://www.welivesecurity.com/2009/01/15/malware-trying-to-avoid-some-countries/)
- [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [Darkside Ransomware Cybereason](https://www.cybereason.com/blog/cybereason-vs-darkside-ransomware)
- [Securelist JSWorm](https://securelist.com/evolution-of-jsworm-ransomware/102428/)
- [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
