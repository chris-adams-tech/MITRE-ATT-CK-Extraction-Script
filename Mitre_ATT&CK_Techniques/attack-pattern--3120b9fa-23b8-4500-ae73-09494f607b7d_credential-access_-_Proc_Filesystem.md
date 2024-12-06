---
contributors:
- Tim (Wadhwa-)Brown
data_sources:
- 'Command: Command Execution'
- 'File: File Access'
id: attack-pattern--3120b9fa-23b8-4500-ae73-09494f607b7d
mitre_attack_url: https://attack.mitre.org/techniques/T1003/007
name: Proc Filesystem
platforms:
- Linux
tactics:
- credential-access
title: credential-access - Proc Filesystem
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux |
| **Data Sources** | Command: Command Execution, File: File Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1003/007](https://attack.mitre.org/techniques/T1003/007) |

# Proc Filesystem (attack-pattern--3120b9fa-23b8-4500-ae73-09494f607b7d)

## Description
Adversaries may gather credentials from the proc filesystem or `/proc`. The proc filesystem is a pseudo-filesystem used as an interface to kernel data structures for Linux based systems managing virtual memory. For each process, the `/proc/<PID>/maps` file shows how memory is mapped within the process’s virtual address space. And `/proc/<PID>/mem`, exposed for debugging purposes, provides access to the process’s virtual address space.(Citation: Picus Labs Proc cump 2022)(Citation: baeldung Linux proc map 2022)

When executing with root privileges, adversaries can search these memory locations for all processes on a system that contain patterns indicative of credentials. Adversaries may use regex patterns, such as <code>grep -E "^[0-9a-f-]* r" /proc/"$pid"/maps | cut -d' ' -f 1</code>, to look for fixed strings in memory structures or cached hashes.(Citation: atomic-red proc file system) When running without privileged access, processes can still view their own virtual memory locations. Some services or programs may save credentials in clear text inside the process’s memory.(Citation: MimiPenguin GitHub May 2017)(Citation: Polop Linux PrivEsc Gitbook)

If running as or with the permissions of a web browser, a process can search the `/maps` & `/mem` locations for common website credential patterns (that can also be used to find adjacent memory within the same structure) in which hashes or cleartext credentials may be located.

## Detection
To obtain the passwords and hashes stored in memory, processes must open a maps file in the `/proc` filesystem for the process being analyzed. This file is stored under the path `/proc/PID/maps`, where the `PID` directory is the unique pid of the program being interrogated for such authentication data. The AuditD monitoring tool, which ships stock in many Linux distributions, can be used to watch for hostile processes opening this file in the proc file system, alerting on the pid, process name, and arguments of such programs.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1003/007)
- [atomic-red proc file system](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.007/T1003.007.md)
- [baeldung Linux proc map 2022](https://www.baeldung.com/linux/proc-id-maps)
- [Polop Linux PrivEsc Gitbook](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#proc-usdpid-maps-and-proc-usdpid-mem)
- [MimiPenguin GitHub May 2017](https://github.com/huntergregal/mimipenguin)
- [Picus Labs Proc cump 2022](https://www.picussecurity.com/resource/the-mitre-attck-t1003-os-credential-dumping-technique-and-its-adversary-use)
