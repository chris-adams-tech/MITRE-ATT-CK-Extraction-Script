---
contributors:
- Joas Antonio dos Santos, @C0d3Cr4zy
data_sources:
- 'File: File Access'
- 'Process: Process Creation'
- 'Drive: Drive Creation'
- 'File: File Creation'
id: attack-pattern--3b744087-9945-4a6f-91e8-9dbceda417a4
mitre_attack_url: https://attack.mitre.org/techniques/T1091
name: Replication Through Removable Media
platforms:
- Windows
tactics:
- lateral-movement
- initial-access
title: lateral-movement - Replication Through Removable Media
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement, initial-access |
| **Platforms** | Windows |
| **Data Sources** | File: File Access, Process: Process Creation, Drive: Drive Creation, File: File Creation |
| **System Requirements** | Removable media allowed, Autorun enabled or vulnerability present that allows for code execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1091](https://attack.mitre.org/techniques/T1091) |

# Replication Through Removable Media (attack-pattern--3b744087-9945-4a6f-91e8-9dbceda417a4)

## Description
Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media's firmware itself.

Mobile devices may also be used to infect PCs with malware if connected via USB.(Citation: Exploiting Smartphone USB ) This infection may be achieved using devices (Android, iOS, etc.) and, in some instances, USB charging cables.(Citation: Windows Malware Infecting Android)(Citation: iPhone Charging Cable Hack) For example, when a smartphone is connected to a system, it may appear to be mounted similar to a USB-connected disk drive. If malware that is compatible with the connected system is on the mobile device, the malware could infect the machine (especially if Autorun features are enabled).

## Detection
Monitor file access on removable media. Detect processes that execute from removable media after it is mounted or when initiated by a user. If a remote access tool is used in this manner to move laterally, then additional actions are likely to occur after execution, such as opening network connections for Command and Control and system and network information Discovery.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1091)
- [Windows Malware Infecting Android](https://www.computerworld.com/article/2486903/windows-malware-tries-to-infect-android-devices-connected-to-pcs.html)
- [iPhone Charging Cable Hack](https://techcrunch.com/2019/08/12/iphone-charging-cable-hack-computer-def-con/)
- [Exploiting Smartphone USB ](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.226.3427&rep=rep1&type=pdf)
