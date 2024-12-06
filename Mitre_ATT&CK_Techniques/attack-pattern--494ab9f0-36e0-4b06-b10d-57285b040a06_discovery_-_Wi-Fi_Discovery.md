---
contributors:
- Christopher Peacock
- Uriel Kosayev
- Liran Ravich, CardinalOps
- Alex Spivakovsky, Pentera
data_sources:
- 'Process: OS API Execution'
- 'Command: Command Execution'
id: attack-pattern--494ab9f0-36e0-4b06-b10d-57285b040a06
mitre_attack_url: https://attack.mitre.org/techniques/T1016/002
name: Wi-Fi Discovery
platforms:
- Linux
- macOS
- Windows
tactics:
- discovery
title: discovery - Wi-Fi Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: OS API Execution, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1016/002](https://attack.mitre.org/techniques/T1016/002) |

# Wi-Fi Discovery (attack-pattern--494ab9f0-36e0-4b06-b10d-57285b040a06)

## Description
Adversaries may search for information about Wi-Fi networks, such as network names and passwords, on compromised systems. Adversaries may use Wi-Fi information as part of [Account Discovery](https://attack.mitre.org/techniques/T1087), [Remote System Discovery](https://attack.mitre.org/techniques/T1018), and other discovery or [Credential Access](https://attack.mitre.org/tactics/TA0006) activity to support both ongoing and future campaigns.

Adversaries may collect various types of information about Wi-Fi networks from hosts. For example, on Windows names and passwords of all Wi-Fi networks a device has previously connected to may be available through `netsh wlan show profiles` to enumerate Wi-Fi names and then `netsh wlan show profile “Wi-Fi name” key=clear` to show a Wi-Fi network’s corresponding password.(Citation: BleepingComputer Agent Tesla steal wifi passwords)(Citation: Malware Bytes New AgentTesla variant steals WiFi credentials)(Citation: Check Point APT35 CharmPower January 2022) Additionally, names and other details of locally reachable Wi-Fi networks can be discovered using calls to `wlanAPI.dll` [Native API](https://attack.mitre.org/techniques/T1106) functions.(Citation: Binary Defense Emotes Wi-Fi Spreader)

On Linux, names and passwords of all Wi-Fi-networks a device has previously connected to may be available in files under ` /etc/NetworkManager/system-connections/`.(Citation: Wi-Fi Password of All Connected Networks in Windows/Linux) On macOS, the password of a known Wi-Fi may be identified with ` security find-generic-password -wa wifiname` (requires admin username/password).(Citation: Find Wi-Fi Password on Mac)


## Detection
This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of system features.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1016/002)
- [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
- [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Wi-Fi Password of All Connected Networks in Windows/Linux](https://www.geeksforgeeks.org/wi-fi-password-connected-networks-windowslinux/)
- [Malware Bytes New AgentTesla variant steals WiFi credentials](https://www.malwarebytes.com/blog/news/2020/04/new-agenttesla-variant-steals-wifi-credentials)
- [Find Wi-Fi Password on Mac](https://mackeeper.com/blog/find-wi-fi-password-on-mac/)
- [BleepingComputer Agent Tesla steal wifi passwords](https://www.bleepingcomputer.com/news/security/hackers-steal-wifi-passwords-using-upgraded-agent-tesla-malware/)
