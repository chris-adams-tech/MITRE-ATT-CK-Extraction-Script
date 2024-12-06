---
contributors:
- Gavin Knapp
data_sources:
- 'File: File Deletion'
- 'User Account: User Account Deletion'
- 'File: File Modification'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Deletion'
- 'Scheduled Job: Scheduled Job Modification'
- 'Command: Command Execution'
id: attack-pattern--d2c4e5ea-dbdf-4113-805a-b1e2a337fb33
mitre_attack_url: https://attack.mitre.org/techniques/T1070/009
name: Clear Persistence
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Clear Persistence
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Deletion, User Account: User Account Deletion, File: File Modification, Windows Registry: Windows Registry Key Modification, Process: Process Creation, Windows Registry: Windows Registry Key Deletion, Scheduled Job: Scheduled Job Modification, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1070/009](https://attack.mitre.org/techniques/T1070/009) |

# Clear Persistence (attack-pattern--d2c4e5ea-dbdf-4113-805a-b1e2a337fb33)

## Description
Adversaries may clear artifacts associated with previously established persistence on a host system to remove evidence of their activity. This may involve various actions, such as removing services, deleting executables, [Modify Registry](https://attack.mitre.org/techniques/T1112), [Plist File Modification](https://attack.mitre.org/techniques/T1647), or other methods of cleanup to prevent defenders from collecting evidence of their persistent presence.(Citation: Cylance Dust Storm) Adversaries may also delete accounts previously created to maintain persistence (i.e. [Create Account](https://attack.mitre.org/techniques/T1136)).(Citation: Talos - Cisco Attack 2022)

In some instances, artifacts of persistence may also be removed once an adversary’s persistence is executed in order to prevent errors with the new instance of the malware.(Citation: NCC Group Team9 June 2020)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1070/009)
- [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Talos - Cisco Attack 2022](https://blog.talosintelligence.com/recent-cyber-attack/)
- [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
