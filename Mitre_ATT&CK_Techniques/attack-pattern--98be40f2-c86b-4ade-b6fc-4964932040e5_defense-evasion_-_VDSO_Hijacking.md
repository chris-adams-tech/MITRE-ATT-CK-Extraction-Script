---
data_sources:
- 'Process: OS API Execution'
- 'Module: Module Load'
id: attack-pattern--98be40f2-c86b-4ade-b6fc-4964932040e5
mitre_attack_url: https://attack.mitre.org/techniques/T1055/014
name: VDSO Hijacking
platforms:
- Linux
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - VDSO Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Linux |
| **Data Sources** | Process: OS API Execution, Module: Module Load |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1055/014](https://attack.mitre.org/techniques/T1055/014) |

# VDSO Hijacking (attack-pattern--98be40f2-c86b-4ade-b6fc-4964932040e5)

## Description
Adversaries may inject malicious code into processes via VDSO hijacking in order to evade process-based defenses as well as possibly elevate privileges. Virtual dynamic shared object (vdso) hijacking is a method of executing arbitrary code in the address space of a separate live process. 

VDSO hijacking involves redirecting calls to dynamically linked shared libraries. Memory protections may prevent writing executable code to a process via [Ptrace System Calls](https://attack.mitre.org/techniques/T1055/008). However, an adversary may hijack the syscall interface code stubs mapped into a process from the vdso shared object to execute syscalls to open and map a malicious shared object. This code can then be invoked by redirecting the execution flow of the process via patched memory address references stored in a process' global offset table (which store absolute addresses of mapped library functions).(Citation: ELF Injection May 2009)(Citation: Backtrace VDSO)(Citation: VDSO Aug 2005)(Citation: Syscall 2014)

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via VDSO hijacking may also evade detection from security products since the execution is masked under a legitimate process.  

## Detection
Monitor for malicious usage of system calls, such as ptrace and mmap, that can be used to attach to, manipulate memory, then redirect a processes' execution path. Monitoring for Linux specific calls such as the ptrace system call should not generate large amounts of data due to their specialized nature, and can be a very effective method to detect some of the common process injection methods.(Citation: ArtOfMemoryForensics)(Citation: GNU Acct)(Citation: RHEL auditd)(Citation: Chokepoint preload rootkits) 

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1055/014)
- [Backtrace VDSO](https://backtrace.io/blog/backtrace/elf-shared-library-injection-forensics/)
- [Syscall 2014](https://lwn.net/Articles/604515/)
- [GNU Acct](https://www.gnu.org/software/acct/)
- [RHEL auditd](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/chap-system_auditing)
- [ELF Injection May 2009](https://web.archive.org/web/20150711051625/http://vxer.org/lib/vrn00.html)
- [VDSO Aug 2005](https://web.archive.org/web/20051013084246/http://www.trilithium.com/johan/2005/08/linux-gate/)
- [Chokepoint preload rootkits](http://www.chokepoint.net/2014/02/detecting-userland-preload-rootkits.html)
