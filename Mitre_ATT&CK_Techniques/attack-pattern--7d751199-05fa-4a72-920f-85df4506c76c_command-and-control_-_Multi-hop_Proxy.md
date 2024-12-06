---
id: attack-pattern--7d751199-05fa-4a72-920f-85df4506c76c
mitre_attack_url: https://attack.mitre.org/techniques/T1188
name: Multi-hop Proxy
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Multi-hop Proxy
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1188](https://attack.mitre.org/techniques/T1188) |

# Multi-hop Proxy (attack-pattern--7d751199-05fa-4a72-920f-85df4506c76c)

## Description
To disguise the source of malicious traffic, adversaries may chain together multiple proxies. Typically, a defender will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not be able to identify any previous proxies before the last-hop proxy. This technique makes identifying the original source of the malicious traffic even more difficult by requiring the defender to trace malicious traffic through several proxies to identify its source.

## Detection
When observing use of Multi-hop proxies, network data from the actual command and control servers could allow correlating incoming and outgoing flows to trace malicious traffic back to its source. Multi-hop proxies can also be detected by alerting on traffic to known anonymity networks (such as [Tor](https://attack.mitre.org/software/S0183)) or known adversary infrastructure that uses this technique.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1188)
