---
id: attack-pattern--f879d51c-5476-431c-aedf-f14d207e4d1e
mitre_attack_url: https://attack.mitre.org/techniques/T1043
name: Commonly Used Port
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Commonly Used Port
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1043](https://attack.mitre.org/techniques/T1043) |

# Commonly Used Port (attack-pattern--f879d51c-5476-431c-aedf-f14d207e4d1e)

## Description
**This technique has been deprecated. Please use [Non-Standard Port](https://attack.mitre.org/techniques/T1571) where appropriate.**

Adversaries may communicate over a commonly used port to bypass firewalls or network detection systems and to blend with normal network activity to avoid more detailed inspection. They may use commonly open ports such as

* TCP:80 (HTTP)
* TCP:443 (HTTPS)
* TCP:25 (SMTP)
* TCP/UDP:53 (DNS)

They may use the protocol associated with the port or a completely different protocol. 

For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), examples of common ports are 

* TCP/UDP:135 (RPC)
* TCP/UDP:22 (SSH)
* TCP/UDP:3389 (RDP)

## Detection
Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. (Citation: University of Birmingham C2)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1043)
- [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
