---
contributors:
- William Cain
- Alfredo Abarca
data_sources:
- 'Cloud Storage: Cloud Storage Access'
- 'Network Traffic: Network Traffic Flow'
- 'Command: Command Execution'
- 'Network Traffic: Network Traffic Content'
- 'Application Log: Application Log Content'
- 'File: File Access'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--a19e86f8-1c0a-4fea-8407-23b73d615776
mitre_attack_url: https://attack.mitre.org/techniques/T1048
name: Exfiltration Over Alternative Protocol
platforms:
- Linux
- macOS
- Windows
- SaaS
- IaaS
- Network
- Office Suite
tactics:
- exfiltration
title: exfiltration - Exfiltration Over Alternative Protocol
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows, SaaS, IaaS, Network, Office Suite |
| **Data Sources** | Cloud Storage: Cloud Storage Access, Network Traffic: Network Traffic Flow, Command: Command Execution, Network Traffic: Network Traffic Content, Application Log: Application Log Content, File: File Access, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1048](https://attack.mitre.org/techniques/T1048) |

# Exfiltration Over Alternative Protocol (attack-pattern--a19e86f8-1c0a-4fea-8407-23b73d615776)

## Description
Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.  

Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Adversaries may also opt to encrypt and/or obfuscate these alternate channels. 

[Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048) can be done using various common operating system utilities such as [Net](https://attack.mitre.org/software/S0039)/SMB or FTP.(Citation: Palo Alto OilRig Oct 2016) On macOS and Linux <code>curl</code> may be used to invoke protocols such as HTTP/S or FTP/S to exfiltrate data from a system.(Citation: 20 macOS Common Tools and Techniques)

Many IaaS and SaaS platforms (such as Microsoft Exchange, Microsoft SharePoint, GitHub, and AWS S3) support the direct download of files, emails, source code, and other sensitive information via the web console or [Cloud API](https://attack.mitre.org/techniques/T1059/009).

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1048)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
- [Palo Alto OilRig Oct 2016](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)
- [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
