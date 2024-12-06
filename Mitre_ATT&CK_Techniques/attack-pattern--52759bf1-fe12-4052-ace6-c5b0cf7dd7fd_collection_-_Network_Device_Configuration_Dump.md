---
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--52759bf1-fe12-4052-ace6-c5b0cf7dd7fd
mitre_attack_url: https://attack.mitre.org/techniques/T1602/002
name: Network Device Configuration Dump
platforms:
- Network
tactics:
- collection
title: collection - Network Device Configuration Dump
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Network |
| **Data Sources** | Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Content |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1602/002](https://attack.mitre.org/techniques/T1602/002) |

# Network Device Configuration Dump (attack-pattern--52759bf1-fe12-4052-ace6-c5b0cf7dd7fd)

## Description
Adversaries may access network configuration files to collect sensitive data about the device and the network. The network configuration is a file containing parameters that determine the operation of the device. The device typically stores an in-memory copy of the configuration while operating, and a separate configuration on non-volatile storage to load after device reset. Adversaries can inspect the configuration files to reveal information about the target network and its layout, the network device and its software, or identifying legitimate accounts and credentials for later use.

Adversaries can use common management tools and protocols, such as Simple Network Management Protocol (SNMP) and Smart Install (SMI), to access network configuration files.(Citation: US-CERT TA18-106A Network Infrastructure Devices 2018)(Citation: Cisco Blog Legacy Device Attacks) These tools may be used to query specific data from a configuration repository or configure the device to export the configuration for later analysis. 

## Detection
Identify network traffic sent or received by untrusted hosts or networks. Configure signatures to identify strings that may be found in a network device configuration.(Citation: US-CERT TA18-068A 2018)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1602/002)
- [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)
- [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
- [US-CERT TA18-068A 2018](https://www.us-cert.gov/ncas/alerts/TA18-086A)
