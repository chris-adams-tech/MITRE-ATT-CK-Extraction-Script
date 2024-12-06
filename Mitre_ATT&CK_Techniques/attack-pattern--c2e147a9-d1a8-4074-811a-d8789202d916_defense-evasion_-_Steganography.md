---
data_sources:
- 'File: File Metadata'
id: attack-pattern--c2e147a9-d1a8-4074-811a-d8789202d916
mitre_attack_url: https://attack.mitre.org/techniques/T1027/003
name: Steganography
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Steganography
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/003](https://attack.mitre.org/techniques/T1027/003) |

# Steganography (attack-pattern--c2e147a9-d1a8-4074-811a-d8789202d916)

## Description
Adversaries may use steganography techniques in order to prevent the detection of hidden information. Steganographic techniques can be used to hide data in digital media such as images, audio tracks, video clips, or text files.

[Duqu](https://attack.mitre.org/software/S0038) was an early example of malware that used steganography. It encrypted the gathered information from a victim's system and hid it within an image before exfiltrating the image to a C2 server.(Citation: Wikipedia Duqu) 

By the end of 2017, a threat group used <code>Invoke-PSImage</code> to hide [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands in an image file (.png) and execute the code on a victim's system. In this particular case the [PowerShell](https://attack.mitre.org/techniques/T1059/001) code downloaded another obfuscated script to gather intelligence from the victim's machine and communicate it back to the adversary.(Citation: McAfee Malicious Doc Targets Pyeongchang Olympics)  

## Detection
Detection of steganography is difficult unless artifacts are left behind by the obfuscation process that are detectable with a known signature. Look for strings or other signatures left in system artifacts related to decoding steganography.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/003)
- [Wikipedia Duqu](https://en.wikipedia.org/wiki/Duqu)
- [McAfee Malicious Doc Targets Pyeongchang Olympics](https://securingtomorrow.mcafee.com/mcafee-labs/malicious-document-targets-pyeongchang-olympics/)
