---
contributors:
- Expel
- Arun Seelagan, CISA
data_sources:
- 'Firewall: Firewall Disable'
- 'Firewall: Firewall Rule Modification'
id: attack-pattern--77532a55-c283-4cd2-bc5d-2d0b65e9d88c
mitre_attack_url: https://attack.mitre.org/techniques/T1562/007
name: Disable or Modify Cloud Firewall
platforms:
- IaaS
tactics:
- defense-evasion
title: defense-evasion - Disable or Modify Cloud Firewall
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | IaaS |
| **Data Sources** | Firewall: Firewall Disable, Firewall: Firewall Rule Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/007](https://attack.mitre.org/techniques/T1562/007) |

# Disable or Modify Cloud Firewall (attack-pattern--77532a55-c283-4cd2-bc5d-2d0b65e9d88c)

## Description
Adversaries may disable or modify a firewall within a cloud environment to bypass controls that limit access to cloud resources. Cloud firewalls are separate from system firewalls that are described in [Disable or Modify System Firewall](https://attack.mitre.org/techniques/T1562/004). 

Cloud environments typically utilize restrictive security groups and firewall rules that only allow network activity from trusted IP addresses via expected ports and protocols. An adversary with appropriate permissions may introduce new firewall rules or policies to allow access into a victim cloud environment and/or move laterally from the cloud control plane to the data plane. For example, an adversary may use a script or utility that creates new ingress rules in existing security groups (or creates new security groups entirely) to allow any TCP/IP connectivity to a cloud-hosted instance.(Citation: Palo Alto Unit 42 Compromised Cloud Compute Credentials 2022) They may also remove networking limitations to support traffic associated with malicious activity (such as cryptomining).(Citation: Expel IO Evil in AWS)(Citation: Palo Alto Unit 42 Compromised Cloud Compute Credentials 2022)

Modifying or disabling a cloud firewall may enable adversary C2 communications, lateral movement, and/or data exfiltration that would otherwise not be allowed. It may also be used to open up resources for [Brute Force](https://attack.mitre.org/techniques/T1110) or [Endpoint Denial of Service](https://attack.mitre.org/techniques/T1499). 

## Detection
Monitor cloud logs for modification or creation of new security groups or firewall rules.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/007)
- [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)
- [Palo Alto Unit 42 Compromised Cloud Compute Credentials 2022](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)
