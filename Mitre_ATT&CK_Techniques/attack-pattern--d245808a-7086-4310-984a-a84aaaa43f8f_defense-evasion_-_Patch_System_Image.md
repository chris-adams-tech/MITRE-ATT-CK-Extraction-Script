---
data_sources:
- 'File: File Modification'
id: attack-pattern--d245808a-7086-4310-984a-a84aaaa43f8f
mitre_attack_url: https://attack.mitre.org/techniques/T1601/001
name: Patch System Image
platforms:
- Network
tactics:
- defense-evasion
title: defense-evasion - Patch System Image
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Network |
| **Data Sources** | File: File Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1601/001](https://attack.mitre.org/techniques/T1601/001) |

# Patch System Image (attack-pattern--d245808a-7086-4310-984a-a84aaaa43f8f)

## Description
Adversaries may modify the operating system of a network device to introduce new capabilities or weaken existing defenses.(Citation: Killing the myth of Cisco IOS rootkits) (Citation: Killing IOS diversity myth) (Citation: Cisco IOS Shellcode) (Citation: Cisco IOS Forensics Developments) (Citation: Juniper Netscreen of the Dead) Some network devices are built with a monolithic architecture, where the entire operating system and most of the functionality of the device is contained within a single file.  Adversaries may change this file in storage, to be loaded in a future boot, or in memory during runtime.

To change the operating system in storage, the adversary will typically use the standard procedures available to device operators. This may involve downloading a new file via typical protocols used on network devices, such as TFTP, FTP, SCP, or a console connection.  The original file may be overwritten, or a new file may be written alongside of it and the device reconfigured to boot to the compromised image.

To change the operating system in memory, the adversary typically can use one of two methods. In the first, the adversary would make use of native debug commands in the original, unaltered running operating system that allow them to directly modify the relevant memory addresses containing the running operating system.  This method typically requires administrative level access to the device.

In the second method for changing the operating system in memory, the adversary would make use of the boot loader. The boot loader is the first piece of software that loads when the device starts that, in turn, will launch the operating system.  Adversaries may use malicious code previously implanted in the boot loader, such as through the [ROMMONkit](https://attack.mitre.org/techniques/T1542/004) method, to directly manipulate running operating system code in memory.  This malicious code in the bootloader provides the capability of direct memory manipulation to the adversary, allowing them to patch the live operating system during runtime.

By modifying the instructions stored in the system image file, adversaries may either weaken existing defenses or provision new capabilities that the device did not have before. Examples of existing defenses that can be impeded include encryption, via [Weaken Encryption](https://attack.mitre.org/techniques/T1600), authentication, via [Network Device Authentication](https://attack.mitre.org/techniques/T1556/004), and perimeter defenses, via [Network Boundary Bridging](https://attack.mitre.org/techniques/T1599).  Adding new capabilities for the adversary’s purpose include [Keylogging](https://attack.mitre.org/techniques/T1056/001), [Multi-hop Proxy](https://attack.mitre.org/techniques/T1090/003), and [Port Knocking](https://attack.mitre.org/techniques/T1205/001).

Adversaries may also compromise existing commands in the operating system to produce false output to mislead defenders.   When this method is used in conjunction with [Downgrade System Image](https://attack.mitre.org/techniques/T1601/002), one example of a compromised system command may include changing the output of the command that shows the version of the currently running operating system.  By patching the operating system, the adversary can change this command to instead display the original, higher revision number that they replaced through the system downgrade. 

When the operating system is patched in storage, this can be achieved in either the resident storage (typically a form of flash memory, which is non-volatile) or via [TFTP Boot](https://attack.mitre.org/techniques/T1542/005). 

When the technique is performed on the running operating system in memory and not on the stored copy, this technique will not survive across reboots.  However, live memory modification of the operating system can be combined with [ROMMONkit](https://attack.mitre.org/techniques/T1542/004) to achieve persistence. 

## Detection
Compare the checksum of the operating system file with the checksum of a known good copy from a trusted source.  Some embedded network device platforms may have the capability to calculate the checksum of the file, while others may not.  Even for those platforms that have the capability, it is recommended to download a copy of the file to a trusted computer to calculate the checksum with software that is not compromised.(Citation: Cisco IOS Software Integrity Assurance - Image File Verification)

Many vendors of embedded network devices can provide advanced debugging support that will allow them to work with device owners to validate the integrity of the operating system running in memory.  If a compromise of the operating system is suspected, contact the vendor technical support and seek such services for a more thorough inspection of the current running system.  (Citation: Cisco IOS Software Integrity Assurance - Run-Time Memory Verification)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1601/001)
- [Killing the myth of Cisco IOS rootkits](https://drwho.virtadpt.net/images/killing_the_myth_of_cisco_ios_rootkits.pdf)
- [Killing IOS diversity myth](https://www.usenix.org/legacy/event/woot/tech/final_files/Cui.pdf)
- [Cisco IOS Shellcode](http://2015.zeronights.org/assets/files/05-Nosenko.pdf)
- [Cisco IOS Forensics Developments](https://www.recurity-labs.com/research/RecurityLabs_Developments_in_IOS_Forensics.pdf)
- [Juniper Netscreen of the Dead](https://www.blackhat.com/presentations/bh-usa-09/NEILSON/BHUSA09-Neilson-NetscreenDead-SLIDES.pdf)
- [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)
- [Cisco IOS Software Integrity Assurance - Run-Time Memory Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#13)
