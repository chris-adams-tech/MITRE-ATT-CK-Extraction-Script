---
data_sources:
- 'Drive: Drive Modification'
- 'Firmware: Firmware Modification'
- 'File: File Modification'
id: attack-pattern--0f20e3cb-245b-4a61-8a91-2d93f7cb0e9b
mitre_attack_url: https://attack.mitre.org/techniques/T1014
name: Rootkit
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Rootkit
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Drive: Drive Modification, Firmware: Firmware Modification, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1014](https://attack.mitre.org/techniques/T1014) |

# Rootkit (attack-pattern--0f20e3cb-245b-4a61-8a91-2d93f7cb0e9b)

## Description
Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information. (Citation: Symantec Windows Rootkits) 

Rootkits or rootkit enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor, Master Boot Record, or [System Firmware](https://attack.mitre.org/techniques/T1542/001). (Citation: Wikipedia Rootkit) Rootkits have been seen for Windows, Linux, and Mac OS X systems. (Citation: CrowdStrike Linux Rootkit) (Citation: BlackHat Mac OSX Rootkit)

## Detection
Some rootkit protections may be built into anti-virus or operating system software. There are dedicated rootkit detection tools that look for specific types of rootkit behavior. Monitor for the existence of unrecognized DLLs, devices, services, and changes to the MBR. (Citation: Wikipedia Rootkit)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1014)
- [CrowdStrike Linux Rootkit](https://www.crowdstrike.com/blog/http-iframe-injecting-linux-rootkit/)
- [BlackHat Mac OSX Rootkit](http://www.blackhat.com/docs/asia-14/materials/Tsai/WP-Asia-14-Tsai-You-Cant-See-Me-A-Mac-OS-X-Rootkit-Uses-The-Tricks-You-Havent-Known-Yet.pdf)
- [Symantec Windows Rootkits](https://www.symantec.com/avcenter/reference/windows.rootkit.overview.pdf)
- [Wikipedia Rootkit](https://en.wikipedia.org/wiki/Rootkit)
