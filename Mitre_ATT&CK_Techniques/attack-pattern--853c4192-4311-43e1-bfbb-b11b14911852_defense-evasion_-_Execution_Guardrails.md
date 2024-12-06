---
contributors:
- Nick Carr, Mandiant
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--853c4192-4311-43e1-bfbb-b11b14911852
mitre_attack_url: https://attack.mitre.org/techniques/T1480
name: Execution Guardrails
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Execution Guardrails
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1480](https://attack.mitre.org/techniques/T1480) |

# Execution Guardrails (attack-pattern--853c4192-4311-43e1-bfbb-b11b14911852)

## Description
Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign.(Citation: FireEye Kevin Mandia Guardrails) Values an adversary can provide about a target system or environment to use as guardrails may include specific network share names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.(Citation: FireEye Outlook Dec 2019)

Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497). While use of [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.

Adversaries may identify and block certain user-agents to evade defenses and narrow the scope of their attack to victims and platforms on which it will be most effective. A user-agent self-identifies data such as a user's software application, operating system, vendor, and version. Adversaries may check user-agents for operating system identification and then only serve malware for the exploitable software while ignoring all other operating systems.(Citation: Trellix-Qakbot)

## Detection
Detecting the use of guardrails may be difficult depending on the implementation. Monitoring for suspicious processes being spawned that gather a variety of system information or perform other forms of [Discovery](https://attack.mitre.org/tactics/TA0007), especially in a short period of time, may aid in detection.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1480)
- [FireEye Outlook Dec 2019](https://www.fireeye.com/blog/threat-research/2019/12/breaking-the-rules-tough-outlook-for-home-page-attacks.html)
- [Trellix-Qakbot](https://www.trellix.com/blogs/research/qakbot-evolves-to-onenote-malware-distribution/)
- [FireEye Kevin Mandia Guardrails](https://www.cyberscoop.com/kevin-mandia-fireeye-u-s-malware-nice/)
