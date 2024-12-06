---
data_sources:
  - "Network Traffic: Network Traffic Content"
  - "Network Traffic: Network Connection Creation"
id: attack-pattern--0ad7bc5c-235a-4048-944b-3b286676cb74
mitre_attack_url: https://attack.mitre.org/techniques/T1602
name: Data from Configuration Repository
platforms:
  - Network
tactics:
  - collection
title: T1602 - collection - Data from Configuration Repository
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Network |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1602](https://attack.mitre.org/techniques/T1602) |

# Data from Configuration Repository (attack-pattern--0ad7bc5c-235a-4048-944b-3b286676cb74)

## Description
Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories may also facilitate remote access and administration of devices.

Adversaries may target these repositories in order to collect large quantities of sensitive system administration data. Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data, much of which may align with adversary Discovery objectives.(Citation: US-CERT-TA18-106A)(Citation: US-CERT TA17-156A SNMP Abuse 2017)

## Detection
Identify network traffic sent or received by untrusted hosts or networks that solicits and obtains the configuration information of the queried device.(Citation: Cisco Advisory SNMP v3 Authentication Vulnerabilities)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1602)
- [Cisco Advisory SNMP v3 Authentication Vulnerabilities](https://tools.cisco.com/security/center/content/CiscoAppliedMitigationBulletin/cisco-amb-20080610-SNMPv3)
- [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
