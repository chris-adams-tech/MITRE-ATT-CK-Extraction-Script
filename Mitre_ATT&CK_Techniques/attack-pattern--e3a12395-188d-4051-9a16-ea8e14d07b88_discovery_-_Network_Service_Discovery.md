---
contributors:
- Praetorian
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Command: Command Execution'
- 'Cloud Service: Cloud Service Enumeration'
id: attack-pattern--e3a12395-188d-4051-9a16-ea8e14d07b88
mitre_attack_url: https://attack.mitre.org/techniques/T1046
name: Network Service Discovery
platforms:
- Windows
- IaaS
- Linux
- macOS
- Containers
- Network
tactics:
- discovery
title: discovery - Network Service Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, IaaS, Linux, macOS, Containers, Network |
| **Data Sources** | Network Traffic: Network Traffic Flow, Command: Command Execution, Cloud Service: Cloud Service Enumeration |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1046](https://attack.mitre.org/techniques/T1046) |

# Network Service Discovery (attack-pattern--e3a12395-188d-4051-9a16-ea8e14d07b88)

## Description
Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port and/or vulnerability scans using tools that are brought onto a system.(Citation: CISA AR21-126A FIVEHANDS May 2021)   

Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.

Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as <code>dns-sd -B _ssh._tcp .</code>) to find other systems broadcasting the ssh service.(Citation: apple doco bonjour description)(Citation: macOS APT Activity Bradley)

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Normal, benign system and network events from legitimate remote service scanning may be uncommon, depending on the environment and how they are used. Legitimate open port and vulnerability scanning may be conducted within the environment and will need to be deconflicted with any detection capabilities developed. Network intrusion detection systems can also be used to identify scanning activity. Monitor for process use of the networks and inspect intra-network flows to detect port scans.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1046)
- [apple doco bonjour description](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html)
- [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [macOS APT Activity Bradley](https://themittenmac.com/what-does-apt-activity-look-like-on-macos/)
