---
contributors:
- Tim (Wadhwa-)Brown
data_sources:
- 'Process: OS API Execution'
- 'File: File Modification'
- 'Command: Command Execution'
- 'File: File Deletion'
- 'Process: Process Modification'
id: attack-pattern--562e9b64-7239-493d-80f4-2bff900d9054
mitre_attack_url: https://attack.mitre.org/techniques/T1562/012
name: Disable or Modify Linux Audit System
platforms:
- Linux
tactics:
- defense-evasion
title: defense-evasion - Disable or Modify Linux Audit System
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux |
| **Data Sources** | Process: OS API Execution, File: File Modification, Command: Command Execution, File: File Deletion, Process: Process Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/012](https://attack.mitre.org/techniques/T1562/012) |

# Disable or Modify Linux Audit System (attack-pattern--562e9b64-7239-493d-80f4-2bff900d9054)

## Description
Adversaries may disable or modify the Linux audit system to hide malicious activity and avoid detection. Linux admins use the Linux Audit system to track security-relevant information on a system. The Linux Audit system operates at the kernel-level and maintains event logs on application and system activity such as process, network, file, and login events based on pre-configured rules.

Often referred to as `auditd`, this is the name of the daemon used to write events to disk and is governed by the parameters set in the `audit.conf` configuration file. Two primary ways to configure the log generation rules are through the command line `auditctl` utility and the file `/etc/audit/audit.rules`,  containing a sequence of `auditctl` commands loaded at boot time.(Citation: Red Hat System Auditing)(Citation: IzyKnows auditd threat detection 2022)

With root privileges, adversaries may be able to ensure their activity is not logged through disabling the Audit system service, editing the configuration/rule files, or by hooking the Audit system library functions. Using the command line, adversaries can disable the Audit system service through killing processes associated with `auditd` daemon or use `systemctl` to stop the Audit service. Adversaries can also hook Audit system functions to disable logging or modify the rules contained in the `/etc/audit/audit.rules` or `audit.conf` files to ignore malicious activity.(Citation: Trustwave Honeypot SkidMap 2023)(Citation: ESET Ebury Feb 2014)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/012)
- [IzyKnows auditd threat detection 2022](https://izyknows.medium.com/linux-auditd-for-threat-detection-d06c8b941505)
- [Red Hat System Auditing](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/chap-system_auditing)
- [ESET Ebury Feb 2014](https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/)
- [Trustwave Honeypot SkidMap 2023](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/honeypot-recon-new-variant-of-skidmap-targeting-redis/)
