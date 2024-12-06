---
contributors:
- William Cain
- Austin Clark, @c2defense
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'File: File Access'
- 'Network Traffic: Network Traffic Content'
- 'Command: Command Execution'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--fb8d023d-45be-47e9-bc51-f56bcae6435b
mitre_attack_url: https://attack.mitre.org/techniques/T1048/003
name: Exfiltration Over Unencrypted Non-C2 Protocol
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- exfiltration
title: exfiltration - Exfiltration Over Unencrypted Non-C2 Protocol
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Network Traffic: Network Traffic Flow, File: File Access, Network Traffic: Network Traffic Content, Command: Command Execution, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1048/003](https://attack.mitre.org/techniques/T1048/003) |

# Exfiltration Over Unencrypted Non-C2 Protocol (attack-pattern--fb8d023d-45be-47e9-bc51-f56bcae6435b)

## Description
Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.(Citation: copy_cmd_cisco)

Adversaries may opt to obfuscate this data, without the use of encryption, within network protocols that are natively unencrypted (such as HTTP, FTP, or DNS). This may include custom or publicly available encoding/compression algorithms (such as base64) as well as embedding data within protocol headers and fields. 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2) 

For network infrastructure devices, collect AAA logging to monitor for `copy` commands being run to exfiltrate configuration files to non-standard destinations over unencrypted protocols such as TFTP.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1048/003)
- [copy_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/C_commands.html#wp1068167689)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
