---
contributors:
- Menachem Goldstein
data_sources:
- 'User Account: User Account Creation'
id: attack-pattern--d349c66e-18e1-4d8b-a2d7-65af7cbd2ba0
mitre_attack_url: https://attack.mitre.org/techniques/T1036/010
name: Masquerade Account Name
platforms:
- Linux
- macOS
- Windows
- SaaS
- IaaS
- Containers
- Office Suite
- Identity Provider
tactics:
- defense-evasion
title: defense-evasion - Masquerade Account Name
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, SaaS, IaaS, Containers, Office Suite, Identity Provider |
| **Data Sources** | User Account: User Account Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/010](https://attack.mitre.org/techniques/T1036/010) |

# Masquerade Account Name (attack-pattern--d349c66e-18e1-4d8b-a2d7-65af7cbd2ba0)

## Description
Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign. This will typically occur during [Create Account](https://attack.mitre.org/techniques/T1136), although accounts may also be renamed at a later date. This may also coincide with [Account Access Removal](https://attack.mitre.org/techniques/T1531) if the actor first deletes an account before re-creating one with the same name.(Citation: Huntress MOVEit 2023)

Often, adversaries will attempt to masquerade as service accounts, such as those associated with legitimate software, data backups, or container cluster management.(Citation: Elastic CUBA Ransomware 2022)(Citation: Aquasec Kubernetes Attack 2023) They may also give accounts generic, trustworthy names, such as “admin”, “help”, or “root.”(Citation: Invictus IR Cloud Ransomware 2024) Sometimes adversaries may model account names off of those already existing in the system, as a follow-on behavior to [Account Discovery](https://attack.mitre.org/techniques/T1087).  

Note that this is distinct from [Impersonation](https://attack.mitre.org/techniques/T1656), which describes impersonating specific trusted individuals or organizations, rather than user or service account names.  

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/010)
- [Elastic CUBA Ransomware 2022](https://www.elastic.co/security-labs/cuba-ransomware-campaign-analysis)
- [Invictus IR Cloud Ransomware 2024](https://www.invictus-ir.com/news/ransomware-in-the-cloud)
- [Huntress MOVEit 2023](https://www.huntress.com/blog/moveit-transfer-critical-vulnerability-rapid-response)
- [Aquasec Kubernetes Attack 2023](https://blog.aquasec.com/leveraging-kubernetes-rbac-to-backdoor-clusters)
