---
contributors:
- David Fiser, @anu4is, Trend Micro
- Alfredo Oliveira, Trend Micro
- Magno Logan, @magnologan, Trend Micro
- Yossi Weizman, Azure Defender Research Team
- Ed Williams, Trustwave, SpiderLabs
- Mohamed Kmal
data_sources:
- 'User Account: User Account Authentication'
- 'Command: Command Execution'
- 'Application Log: Application Log Content'
id: attack-pattern--a93494bb-4b80-4ea1-8695-3236a49916fd
mitre_attack_url: https://attack.mitre.org/techniques/T1110
name: Brute Force
platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Containers
- Network
- Office Suite
- Identity Provider
tactics:
- credential-access
title: credential-access - Brute Force
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Containers, Network, Office Suite, Identity Provider |
| **Data Sources** | User Account: User Account Authentication, Command: Command Execution, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1110](https://attack.mitre.org/techniques/T1110) |

# Brute Force (attack-pattern--a93494bb-4b80-4ea1-8695-3236a49916fd)

## Description
Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained.(Citation: TrendMicro Pawn Storm Dec 2020) Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism.(Citation: Dragos Crashoverride 2018) Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes.

Brute forcing credentials may take place at various points during a breach. For example, adversaries may attempt to brute force access to [Valid Accounts](https://attack.mitre.org/techniques/T1078) within a victim environment leveraging knowledge gathered from other post-compromise behaviors such as [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), [Account Discovery](https://attack.mitre.org/techniques/T1087), or [Password Policy Discovery](https://attack.mitre.org/techniques/T1201). Adversaries may also combine brute forcing activity with behaviors such as [External Remote Services](https://attack.mitre.org/techniques/T1133) as part of Initial Access.

## Detection
Monitor authentication logs for system and application login failures of [Valid Accounts](https://attack.mitre.org/techniques/T1078). If authentication failures are high, then there may be a brute force attempt to gain access to a system using legitimate credentials. Also monitor for many failed authentication attempts across various accounts that may result from password spraying attempts. It is difficult to detect when hashes are cracked, since this is generally done outside the scope of the target network.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1110)
- [TrendMicro Pawn Storm Dec 2020](https://www.trendmicro.com/en_us/research/20/l/pawn-storm-lack-of-sophistication-as-a-strategy.html)
- [Dragos Crashoverride 2018](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)
