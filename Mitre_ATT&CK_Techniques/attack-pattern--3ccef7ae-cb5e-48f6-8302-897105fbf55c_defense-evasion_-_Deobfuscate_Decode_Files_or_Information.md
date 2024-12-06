---
contributors:
- Matthew Demaske, Adaptforward
- Red Canary
data_sources:
- 'Process: Process Creation'
- 'Script: Script Execution'
- 'File: File Modification'
id: attack-pattern--3ccef7ae-cb5e-48f6-8302-897105fbf55c
mitre_attack_url: https://attack.mitre.org/techniques/T1140
name: Deobfuscate/Decode Files or Information
platforms:
- Windows
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - Deobfuscate/Decode Files or Information
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Process: Process Creation, Script: Script Execution, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1140](https://attack.mitre.org/techniques/T1140) |

# Deobfuscate/Decode Files or Information (attack-pattern--3ccef7ae-cb5e-48f6-8302-897105fbf55c)

## Description
Adversaries may use [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027) to hide artifacts of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending on how they intend to use it. Methods for doing that include built-in functionality of malware or by using utilities present on the system.

One such example is the use of [certutil](https://attack.mitre.org/software/S0160) to decode a remote access tool portable executable file that has been hidden inside a certificate file.(Citation: Malwarebytes Targeted Attack against Saudi Arabia) Another example is using the Windows <code>copy /b</code> command to reassemble binary fragments into a malicious payload.(Citation: Carbon Black Obfuscation Sept 2016)

Sometimes a user's action may be required to open it for deobfuscation or decryption as part of [User Execution](https://attack.mitre.org/techniques/T1204). The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary. (Citation: Volexity PowerDuke November 2016)

## Detection
Detecting the action of deobfuscating or decoding files or information may be difficult depending on the implementation. If the functionality is contained within malware and uses the Windows API, then attempting to detect malicious behavior before or after the action may yield better results than attempting to perform analysis on loaded libraries or API calls. If scripts are used, then collecting the scripts for analysis may be necessary. Perform process and command-line monitoring to detect potentially malicious behavior related to scripts and system utilities such as [certutil](https://attack.mitre.org/software/S0160).

Monitor the execution file paths and command-line arguments for common archive file applications and extensions, such as those for Zip and RAR archive tools, and correlate with other suspicious behavior to reduce false positives from normal user and administrator behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1140)
- [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [Malwarebytes Targeted Attack against Saudi Arabia](https://blog.malwarebytes.com/cybercrime/social-engineering-cybercrime/2017/03/new-targeted-attack-saudi-arabia-government/)
- [Carbon Black Obfuscation Sept 2016](https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/)
