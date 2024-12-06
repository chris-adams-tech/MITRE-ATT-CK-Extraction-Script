---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Drive: Drive Creation'
- 'Application Log: Application Log Content'
id: attack-pattern--d40239b3-05ff-46d8-9bdd-b46d13463ef9
mitre_attack_url: https://attack.mitre.org/techniques/T1200
name: Hardware Additions
platforms:
- Windows
- Linux
- macOS
tactics:
- initial-access
title: initial-access - Hardware Additions
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Network Traffic: Network Traffic Flow, Drive: Drive Creation, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1200](https://attack.mitre.org/techniques/T1200) |

# Hardware Additions (attack-pattern--d40239b3-05ff-46d8-9bdd-b46d13463ef9)

## Description
Adversaries may introduce computer accessories, networking hardware, or other computing devices into a system or network that can be used as a vector to gain access. Rather than just connecting and distributing payloads via removable storage (i.e. [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091)), more robust hardware additions can be used to introduce new functionalities and/or features into a system that can then be abused.

While public references of usage by threat actors are scarce, many red teams/penetration testers leverage hardware additions for initial access. Commercial and open source products can be leveraged with capabilities such as passive network tapping, network traffic modification (i.e. [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557)), keystroke injection, kernel memory reading via DMA, addition of new wireless access to an existing network, and others.(Citation: Ossmann Star Feb 2011)(Citation: Aleks Weapons Nov 2015)(Citation: Frisk DMA August 2016)(Citation: McMillan Pwn March 2012)

## Detection
Asset management systems may help with the detection of computer systems or network devices that should not exist on a network. 

Endpoint sensors may be able to detect the addition of hardware via USB, Thunderbolt, and other external device communication ports.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1200)
- [Ossmann Star Feb 2011](https://ossmann.blogspot.com/2011/02/throwing-star-lan-tap.html)
- [Aleks Weapons Nov 2015](https://www.youtube.com/watch?v=lDvf4ScWbcQ)
- [McMillan Pwn March 2012](https://arstechnica.com/information-technology/2012/03/the-pwn-plug-is-a-little-white-box-that-can-hack-your-network/)
- [Frisk DMA August 2016](https://www.youtube.com/watch?v=fXthwl6ShOg)
