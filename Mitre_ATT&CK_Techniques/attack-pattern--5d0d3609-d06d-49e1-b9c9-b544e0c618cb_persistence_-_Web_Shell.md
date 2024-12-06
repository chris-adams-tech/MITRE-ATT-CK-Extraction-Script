---
contributors:
- Arnim Rupp, Deutsche Lufthansa AG
data_sources:
- 'Application Log: Application Log Content'
- 'Process: Process Creation'
- 'File: File Creation'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
- 'File: File Modification'
id: attack-pattern--5d0d3609-d06d-49e1-b9c9-b544e0c618cb
mitre_attack_url: https://attack.mitre.org/techniques/T1505/003
name: Web Shell
platforms:
- Linux
- Windows
- macOS
- Network
tactics:
- persistence
title: persistence - Web Shell
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Linux, Windows, macOS, Network |
| **Data Sources** | Application Log: Application Log Content, Process: Process Creation, File: File Creation, Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1505/003](https://attack.mitre.org/techniques/T1505/003) |

# Web Shell (attack-pattern--5d0d3609-d06d-49e1-b9c9-b544e0c618cb)

## Description
Adversaries may backdoor web servers with web shells to establish persistent access to systems. A Web shell is a Web script that is placed on an openly accessible Web server to allow an adversary to access the Web server as a gateway into a network. A Web shell may provide a set of functions to execute or a command-line interface on the system that hosts the Web server.(Citation: volexity_0day_sophos_FW)

In addition to a server-side script, a Web shell may have a client interface program that is used to talk to the Web server (e.g. [China Chopper](https://attack.mitre.org/software/S0020) Web shell client).(Citation: Lee 2013)

## Detection
Web shells can be difficult to detect. Unlike other forms of persistent remote access, they do not initiate connections. The portion of the Web shell that is on the server may be small and innocuous looking. The PHP version of the China Chopper Web shell, for example, is the following short payload: (Citation: Lee 2013) 

<code>&lt;?php @eval($_POST['password']);&gt;</code>

Nevertheless, detection mechanisms exist. Process monitoring may be used to detect Web servers that perform suspicious actions such as spawning cmd.exe or accessing files that are not in the Web directory.(Citation: NSA Cyber Mitigating Web Shells)

File monitoring may be used to detect changes to files in the Web directory of a Web server that do not match with updates to the Web server's content and may indicate implantation of a Web shell script.(Citation: NSA Cyber Mitigating Web Shells)

Log authentication attempts to the server and any unusual traffic patterns to or from the server and internal network. (Citation: US-CERT Alert TA15-314A Web Shells)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1505/003)
- [NSA Cyber Mitigating Web Shells](https://github.com/nsacyber/Mitigating-Web-Shells)
- [volexity_0day_sophos_FW](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)
- [Lee 2013](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)
- [US-CERT Alert TA15-314A Web Shells](https://www.us-cert.gov/ncas/alerts/TA15-314A)
