---
id: attack-pattern--d54416bd-0803-41ca-870a-ce1af7c05638
mitre_attack_url: https://attack.mitre.org/techniques/T1022
name: Data Encrypted
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Data Encrypted
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1022](https://attack.mitre.org/techniques/T1022) |

# Data Encrypted (attack-pattern--d54416bd-0803-41ca-870a-ce1af7c05638)

## Description
Data is encrypted before being exfiltrated in order to hide the information that is being exfiltrated from detection or to make the exfiltration less conspicuous upon inspection by a defender. The encryption is performed by a utility, programming library, or custom algorithm on the data itself and is considered separate from any encryption performed by the command and control or file transfer protocol. Common file archive formats that can encrypt files are RAR and zip.

Other exfiltration techniques likely apply as well to transfer the information out of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041) and [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048)

## Detection
Encryption software and encrypted files can be detected in many ways. Common utilities that may be present on the system or brought in by an adversary may be detectable through process monitoring and monitoring for command-line arguments for known encryption utilities. This may yield a significant amount of benign events, depending on how systems in the environment are typically used. Often the encryption key is stated within command-line invocation of the software. 

A process that loads the Windows DLL crypt32.dll may be used to perform encryption, decryption, or verification of file signatures. 

Network traffic may also be analyzed for entropy to determine if encrypted data is being transmitted. (Citation: Zhang 2013) If the communications channel is unencrypted, encrypted files of known file types can be detected in transit during exfiltration with a network intrusion detection or data loss prevention system analyzing file headers. (Citation: Wikipedia File Header Signatures)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1022)
- [Zhang 2013](http://www.netsec.colostate.edu/~zhang/DetectingEncryptedBotnetTraffic.pdf)
- [Wikipedia File Header Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
