---
id: attack-pattern--f44731de-ea9f-406d-9b83-30ecbb9b4392
mitre_attack_url: https://attack.mitre.org/techniques/T1035
name: Service Execution
platforms:
- Windows
tactics:
- execution
title: execution - Service Execution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1035](https://attack.mitre.org/techniques/T1035) |

# Service Execution (attack-pattern--f44731de-ea9f-406d-9b83-30ecbb9b4392)

## Description
Adversaries may execute a binary, command, or script via a method that interacts with Windows services, such as the Service Control Manager. This can be done by either creating a new service or modifying an existing service. This technique is the execution used in conjunction with [New Service](https://attack.mitre.org/techniques/T1050) and [Modify Existing Service](https://attack.mitre.org/techniques/T1031) during service persistence or privilege escalation.

## Detection
Changes to service Registry entries and command-line invocation of tools capable of modifying services that do not correlate with known software, patch cycles, etc., may be suspicious. If a service is used only to execute a binary or script and not to persist, then it will likely be changed back to its original form shortly after the service is restarted so the service is not left broken, as is the case with the common administrator tool [PsExec](https://attack.mitre.org/software/S0029).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1035)
