---
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--ee7ff928-801c-4f34-8a99-3df965e581a5
mitre_attack_url: https://attack.mitre.org/techniques/T1602/001
name: SNMP (MIB Dump)
platforms:
- Network
tactics:
- collection
title: collection - SNMP (MIB Dump)
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Network |
| **Data Sources** | Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Content |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1602/001](https://attack.mitre.org/techniques/T1602/001) |

# SNMP (MIB Dump) (attack-pattern--ee7ff928-801c-4f34-8a99-3df965e581a5)

## Description
Adversaries may target the Management Information Base (MIB) to collect and/or mine valuable information in a network managed using Simple Network Management Protocol (SNMP).

The MIB is a configuration repository that stores variable information accessible via SNMP in the form of object identifiers (OID). Each OID identifies a variable that can be read or set and permits active management tasks, such as configuration changes, through remote modification of these variables. SNMP can give administrators great insight in their systems, such as, system information, description of hardware, physical location, and software packages(Citation: SANS Information Security Reading Room Securing SNMP Securing SNMP). The MIB may also contain device operational information, including running configuration, routing table, and interface details.

Adversaries may use SNMP queries to collect MIB content directly from SNMP-managed devices in order to collect network information that allows the adversary to build network maps and facilitate future targeted exploitation.(Citation: US-CERT-TA18-106A)(Citation: Cisco Blog Legacy Device Attacks) 

## Detection
Identify network traffic sent or received by untrusted hosts or networks that expose MIB content or use unauthorized protocols.(Citation: Cisco Advisory SNMP v3 Authentication Vulnerabilities)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1602/001)
- [SANS Information Security Reading Room Securing SNMP Securing SNMP](https://www.sans.org/reading-room/whitepapers/networkdevs/securing-snmp-net-snmp-snmpv3-1051)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
- [Cisco Advisory SNMP v3 Authentication Vulnerabilities](https://tools.cisco.com/security/center/content/CiscoAppliedMitigationBulletin/cisco-amb-20080610-SNMPv3)
