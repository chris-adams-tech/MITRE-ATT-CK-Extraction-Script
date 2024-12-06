---
contributors:
  - David Galazin @themalwareman1
  - Andrew Northern, @ex_raritas
  - Jai Minton, @Cyberraiju
data_sources:
  - "File: File Creation"
  - "File: File Metadata"
id: attack-pattern--0d91b3c0-5e50-47c3-949a-2a796f04d144
mitre_attack_url: https://attack.mitre.org/techniques/T1027/013
name: Encrypted/Encoded File
platforms:
  - Linux
  - macOS
  - Windows
tactics:
  - defense-evasion
title: T1027.013 - defense-evasion - Encrypted/Encoded File
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Creation, File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/013](https://attack.mitre.org/techniques/T1027/013) |

# Encrypted/Encoded File (attack-pattern--0d91b3c0-5e50-47c3-949a-2a796f04d144)

## Description
Adversaries may encrypt or encode files to obfuscate strings, bytes, and other specific patterns to impede detection. Encrypting and/or encoding file content aims to conceal malicious artifacts within a file used in an intrusion. Many other techniques, such as [Software Packing](https://attack.mitre.org/techniques/T1027/002), [Steganography](https://attack.mitre.org/techniques/T1027/003), and [Embedded Payloads](https://attack.mitre.org/techniques/T1027/009), share this same broad objective. Encrypting and/or encoding files could lead to a lapse in detection of static signatures, only for this malicious content to be revealed (i.e., [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140)) at the time of execution/use.

This type of file obfuscation can be applied to many file artifacts present on victim hosts, such as malware log/configuration and payload files.(Citation: File obfuscation) Files can be encrypted with a hardcoded or user-supplied key, as well as otherwise obfuscated using standard encoding/compression schemes such as Base64.

The entire content of a file may be obfuscated, or just specific functions or values (such as C2 addresses). Encryption and encoding may also be applied in redundant layers for additional protection.

For example, adversaries may abuse password-protected Word documents or self-extracting (SFX) archives as a method of encrypting/encoding a file such as a [Phishing](https://attack.mitre.org/techniques/T1566) payload. These files typically function by attaching the intended archived content to a decompressor stub that is executed when the file is invoked (e.g., [User Execution](https://attack.mitre.org/techniques/T1204)).(Citation: SFX - Encrypted/Encoded File) 

Adversaries may also abuse file-specific as well as custom encoding schemes. For example, Byte Order Mark (BOM) headers in text files may be abused to manipulate and obfuscate file content until [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) execution.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/013)
- [File obfuscation](https://www.crowdstrike.com/blog/shlayer-malvertising-campaigns-still-using-flash-update-disguise/)
- [SFX - Encrypted/Encoded File](https://www.crowdstrike.com/blog/self-extracting-archives-decoy-files-and-their-hidden-payloads/)
