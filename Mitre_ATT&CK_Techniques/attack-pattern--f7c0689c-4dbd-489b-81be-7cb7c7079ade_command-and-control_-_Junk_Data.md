---
data_sources:
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--f7c0689c-4dbd-489b-81be-7cb7c7079ade
mitre_attack_url: https://attack.mitre.org/techniques/T1001/001
name: Junk Data
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Junk Data
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1001/001](https://attack.mitre.org/techniques/T1001/001) |

# Junk Data (attack-pattern--f7c0689c-4dbd-489b-81be-7cb7c7079ade)

## Description
Adversaries may add junk data to protocols used for command and control to make detection more difficult.(Citation: FireEye SUNBURST Backdoor December 2020) By adding random or meaningless data to the protocols used for command and control, adversaries can prevent trivial methods for decoding, deciphering, or otherwise analyzing the traffic. Examples may include appending/prepending data with junk characters or writing junk characters between significant characters. 

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used.(Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1001/001)
- [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
