---
contributors:
- Daniel Stepanic, Elastic
- RedHuntLabs, @redhuntlabs
- Austin Clark, @c2defense
data_sources:
- 'Command: Command Execution'
- 'File: File Access'
- 'Network Traffic: Network Connection Creation'
- 'Process: Process Creation'
id: attack-pattern--e358d692-23c0-4a31-9eb6-ecc13a8d7735
mitre_attack_url: https://attack.mitre.org/techniques/T1018
name: Remote System Discovery
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- discovery
title: discovery - Remote System Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Command: Command Execution, File: File Access, Network Traffic: Network Connection Creation, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1018](https://attack.mitre.org/techniques/T1018) |

# Remote System Discovery (attack-pattern--e358d692-23c0-4a31-9eb6-ecc13a8d7735)

## Description
Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as  [Ping](https://attack.mitre.org/software/S0097) or <code>net view</code> using [Net](https://attack.mitre.org/software/S0039).

Adversaries may also analyze data from local host files (ex: <code>C:\Windows\System32\Drivers\etc\hosts</code> or <code>/etc/hosts</code>) or other passive means (such as local [Arp](https://attack.mitre.org/software/S0099) cache entries) in order to discover the presence of remote systems in an environment.

Adversaries may also target discovery of network infrastructure as well as leverage [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands on network devices to gather detailed information about systems within a network (e.g. <code>show cdp neighbors</code>, <code>show arp</code>).(Citation: US-CERT-TA18-106A)(Citation: CISA AR21-126A FIVEHANDS May 2021)  


## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Normal, benign system and network events related to legitimate remote system discovery may be uncommon, depending on the environment and how they are used. Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

Monitor for processes that can be used to discover remote systems, such as <code>ping.exe</code> and <code>tracert.exe</code>, especially when executed in quick succession.(Citation: Elastic - Koadiac Detection with EQL)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1018)
- [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Elastic - Koadiac Detection with EQL](https://www.elastic.co/blog/embracing-offensive-tooling-building-detections-against-koadic-using-eql)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
