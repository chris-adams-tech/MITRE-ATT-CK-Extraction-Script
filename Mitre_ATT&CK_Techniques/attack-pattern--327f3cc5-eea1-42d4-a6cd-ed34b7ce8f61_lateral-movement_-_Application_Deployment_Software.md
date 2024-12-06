---
id: attack-pattern--327f3cc5-eea1-42d4-a6cd-ed34b7ce8f61
mitre_attack_url: https://attack.mitre.org/techniques/T1017
name: Application Deployment Software
platforms:
- Linux
- macOS
- Windows
tactics:
- lateral-movement
title: lateral-movement - Application Deployment Software
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Linux, macOS, Windows |
| **System Requirements** | Access to application deployment software (EPO, HPCA, Altiris, etc.) |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1017](https://attack.mitre.org/techniques/T1017) |

# Application Deployment Software (attack-pattern--327f3cc5-eea1-42d4-a6cd-ed34b7ce8f61)

## Description
Adversaries may deploy malicious software to systems within a network using application deployment systems employed by enterprise administrators. The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access to the deployment server, or specific domain credentials may be required. However, the system may require an administrative account to log in or to perform software deployment.

Access to a network-wide or enterprise-wide software deployment system enables an adversary to have remote code execution on all systems that are connected to such a system. The access may be used to laterally move to systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.

## Detection
Monitor application deployments from a secondary system. Perform application deployment at regular times so that irregular deployment activity stands out. Monitor process activity that does not correlate to known good software. Monitor account login activity on the deployment system.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1017)
- [capec](https://capec.mitre.org/data/definitions/187.html)
