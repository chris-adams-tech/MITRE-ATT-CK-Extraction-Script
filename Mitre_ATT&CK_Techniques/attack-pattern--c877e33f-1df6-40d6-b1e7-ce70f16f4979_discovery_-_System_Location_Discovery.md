---
contributors:
- Pooja Natarajan, NEC Corporation India
- Hiroki Nagahama, NEC Corporation
- Manikantan Srinivasan, NEC Corporation India
- Wes Hurd
- Katie Nickels, Red Canary
data_sources:
- 'Process: Process Creation'
- 'Process: OS API Execution'
- 'Command: Command Execution'
id: attack-pattern--c877e33f-1df6-40d6-b1e7-ce70f16f4979
mitre_attack_url: https://attack.mitre.org/techniques/T1614
name: System Location Discovery
platforms:
- Windows
- Linux
- macOS
- IaaS
tactics:
- discovery
title: discovery - System Location Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, Linux, macOS, IaaS |
| **Data Sources** | Process: Process Creation, Process: OS API Execution, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1614](https://attack.mitre.org/techniques/T1614) |

# System Location Discovery (attack-pattern--c877e33f-1df6-40d6-b1e7-ce70f16f4979)

## Description

Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [System Location Discovery](https://attack.mitre.org/techniques/T1614) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.(Citation: FBI Ragnar Locker 2020)(Citation: Sophos Geolocation 2016)(Citation: Bleepingcomputer RAT malware 2020) Windows API functions such as <code>GetLocaleInfoW</code> can also be used to determine the locale of the host.(Citation: FBI Ragnar Locker 2020) In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.(Citation: AWS Instance Identity Documents)(Citation: Microsoft Azure Instance Metadata 2021)

Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.(Citation: Securelist Trasparent Tribe 2020)(Citation: Sophos Geolocation 2016)

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system location information. Remote access tools with built-in features may interact directly with the Windows API, such as calling <code> GetLocaleInfoW</code> to gather information.(Citation: FBI Ragnar Locker 2020)

Monitor traffic flows to geo-location service provider sites, such as ip-api and ipinfo.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1614)
- [Bleepingcomputer RAT malware 2020](https://www.bleepingcomputer.com/news/security/new-rat-malware-gets-commands-via-discord-has-ransomware-feature/)
- [AWS Instance Identity Documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html)
- [Securelist Trasparent Tribe 2020](https://securelist.com/transparent-tribe-part-1/98127/)
- [FBI Ragnar Locker 2020](https://s3.documentcloud.org/documents/20413525/fbi-flash-indicators-of-compromise-ragnar-locker-ransomware-11192020-bc.pdf)
- [Microsoft Azure Instance Metadata 2021](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service?tabs=windows)
- [Sophos Geolocation 2016](https://news.sophos.com/en-us/2016/05/03/location-based-ransomware-threat-research/)
