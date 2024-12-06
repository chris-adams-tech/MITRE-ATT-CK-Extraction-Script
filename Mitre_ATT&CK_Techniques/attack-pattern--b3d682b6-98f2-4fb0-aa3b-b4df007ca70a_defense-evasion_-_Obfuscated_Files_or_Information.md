---
contributors:
- Red Canary
- Christiaan Beek, @ChristiaanBeek
data_sources:
- 'WMI: WMI Creation'
- 'Script: Script Execution'
- 'File: File Creation'
- 'Module: Module Load'
- 'Application Log: Application Log Content'
- 'Command: Command Execution'
- 'File: File Metadata'
- 'Process: OS API Execution'
- 'Windows Registry: Windows Registry Key Creation'
- 'Process: Process Creation'
id: attack-pattern--b3d682b6-98f2-4fb0-aa3b-b4df007ca70a
mitre_attack_url: https://attack.mitre.org/techniques/T1027
name: Obfuscated Files or Information
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- defense-evasion
title: defense-evasion - Obfuscated Files or Information
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | WMI: WMI Creation, Script: Script Execution, File: File Creation, Module: Module Load, Application Log: Application Log Content, Command: Command Execution, File: File Metadata, Process: OS API Execution, Windows Registry: Windows Registry Key Creation, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027](https://attack.mitre.org/techniques/T1027) |

# Obfuscated Files or Information (attack-pattern--b3d682b6-98f2-4fb0-aa3b-b4df007ca70a)

## Description
Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. 

Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Sometimes a user's action may be required to open and [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140) for [User Execution](https://attack.mitre.org/techniques/T1204). The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary. (Citation: Volexity PowerDuke November 2016) Adversaries may also use compressed or archived scripts, such as JavaScript. 

Portions of files can also be encoded to hide the plain-text strings that would otherwise help defenders with discovery. (Citation: Linux/Cdorked.A We Live Security Analysis) Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled. (Citation: Carbon Black Obfuscation Sept 2016)

Adversaries may also abuse [Command Obfuscation](https://attack.mitre.org/techniques/T1027/010) to obscure commands executed from payloads or directly via [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059). Environment variables, aliases, characters, and other platform/language specific semantics can be used to evade signature based detections and application control mechanisms. (Citation: FireEye Obfuscation June 2017) (Citation: FireEye Revoke-Obfuscation July 2017)(Citation: PaloAlto EncodedCommand March 2017) 

## Detection
Detection of file obfuscation is difficult unless artifacts are left behind by the obfuscation process that are uniquely detectable with a signature. If detection of the obfuscation itself is not possible, it may be possible to detect the malicious activity that caused the obfuscated file (for example, the method that was used to write, read, or modify the file on the file system). 

Flag and analyze commands containing indicators of obfuscation and known suspicious syntax such as uninterpreted escape characters like '''^''' and '''"'''. Windows' Sysmon and Event ID 4688 displays command-line arguments for processes. Deobfuscation tools can be used to detect these indicators in files/payloads. (Citation: GitHub Revoke-Obfuscation) (Citation: FireEye Revoke-Obfuscation July 2017) (Citation: GitHub Office-Crackros Aug 2016) 

Obfuscation used in payloads for Initial Access can be detected at the network. Use network intrusion detection systems and email gateway filtering to identify compressed and encrypted attachments and scripts. Some email attachment detonation systems can open compressed and encrypted attachments. Payloads delivered over an encrypted connection from a website require encrypted network traffic inspection. 

The first detection of a malicious tool may trigger an anti-virus or other security tool alert. Similar events may also occur at the boundary through network IDS, email scanning appliance, etc. The initial detection should be treated as an indication of a potentially more invasive intrusion. The alerting system should be thoroughly investigated beyond that initial alert for activity that was not detected. Adversaries may continue with an operation, assuming that individual events like an anti-virus detect will not be investigated or that an analyst will not be able to conclusively link that event to other activity occurring on the network. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027)
- [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [GitHub Revoke-Obfuscation](https://github.com/danielbohannon/Revoke-Obfuscation)
- [FireEye Obfuscation June 2017](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)
- [FireEye Revoke-Obfuscation July 2017](https://www.fireeye.com/content/dam/fireeye-www/blog/pdfs/revoke-obfuscation-report.pdf)
- [GitHub Office-Crackros Aug 2016](https://github.com/itsreallynick/office-crackros)
- [Linux/Cdorked.A We Live Security Analysis](https://www.welivesecurity.com/2013/04/26/linuxcdorked-new-apache-backdoor-in-the-wild-serves-blackhole/)
- [Carbon Black Obfuscation Sept 2016](https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/)
- [PaloAlto EncodedCommand March 2017](https://researchcenter.paloaltonetworks.com/2017/03/unit42-pulling-back-the-curtains-on-encodedcommand-powershell-attacks/)
