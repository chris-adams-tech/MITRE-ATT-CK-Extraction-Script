---
contributors:
- Oleg Skulkin, Group-IB
- Menachem Goldstein
- Harikrishnan Muthu, Cyble
- ReliaQuest
- Ale Houspanossian
- Fernando Bacchin
data_sources:
- 'Instance: Instance Start'
- 'File: File Creation'
- 'Network Traffic: Network Connection Creation'
- 'Container: Container Creation'
- 'Instance: Instance Creation'
- 'Network Traffic: Network Traffic Content'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Image: Image Creation'
- 'Application Log: Application Log Content'
- 'Container: Container Start'
id: attack-pattern--8c32eb4d-805f-4fc5-bf60-c4d476c131b5
mitre_attack_url: https://attack.mitre.org/techniques/T1204
name: User Execution
platforms:
- Linux
- Windows
- macOS
- IaaS
- Containers
tactics:
- execution
title: execution - User Execution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Linux, Windows, macOS, IaaS, Containers |
| **Data Sources** | Instance: Instance Start, File: File Creation, Network Traffic: Network Connection Creation, Container: Container Creation, Instance: Instance Creation, Network Traffic: Network Traffic Content, Process: Process Creation, Command: Command Execution, Image: Image Creation, Application Log: Application Log Content, Container: Container Start |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1204](https://attack.mitre.org/techniques/T1204) |

# User Execution (attack-pattern--8c32eb4d-805f-4fc5-bf60-c4d476c131b5)

## Description
An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of [Phishing](https://attack.mitre.org/techniques/T1566).

While [User Execution](https://attack.mitre.org/techniques/T1204) frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [Internal Spearphishing](https://attack.mitre.org/techniques/T1534).

Adversaries may also deceive users into performing actions such as:

* Enabling [Remote Access Software](https://attack.mitre.org/techniques/T1219), allowing direct control of the system to the adversary
* Running malicious JavaScript in their browser, allowing adversaries to [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539)s(Citation: Talos Roblox Scam 2023)(Citation: Krebs Discord Bookmarks 2023)
* Downloading and executing malware for [User Execution](https://attack.mitre.org/techniques/T1204)
* Coerceing users to copy, paste, and execute malicious code manually(Citation: Reliaquest-execution)(Citation: proofpoint-selfpwn)

For example, tech support scams can be facilitated through [Phishing](https://attack.mitre.org/techniques/T1566), vishing, or various forms of user interaction. Adversaries can use a combination of these methods, such as spoofing and promoting toll-free numbers or call centers that are used to direct victims to malicious websites, to deliver and execute payloads containing malware or [Remote Access Software](https://attack.mitre.org/techniques/T1219).(Citation: Telephone Attack Delivery)

## Detection
Monitor the execution of and command-line arguments for applications that may be used by an adversary to gain Initial Access that require user interaction. This includes compression applications, such as those for zip files, that can be used to [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140) in payloads.

Anti-virus can potentially detect malicious documents and files that are downloaded and executed on the user's computer. Endpoint sensing or network sensing can potentially detect malicious events once the file is opened (such as a Microsoft Word document or PDF reaching out to the internet or spawning powershell.exe).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1204)
- [Krebs Discord Bookmarks 2023](https://krebsonsecurity.com/2023/05/discord-admins-hacked-by-malicious-bookmarks/)
- [Reliaquest-execution](https://www.reliaquest.com/blog/new-execution-technique-in-clearfake-campaign/)
- [Telephone Attack Delivery](https://www.proofpoint.com/us/blog/threat-insight/caught-beneath-landline-411-telephone-oriented-attack-delivery)
- [Talos Roblox Scam 2023](https://blog.talosintelligence.com/roblox-scam-overview/)
- [proofpoint-selfpwn](https://www.proofpoint.com/us/blog/threat-insight/clipboard-compromise-powershell-self-pwn)
