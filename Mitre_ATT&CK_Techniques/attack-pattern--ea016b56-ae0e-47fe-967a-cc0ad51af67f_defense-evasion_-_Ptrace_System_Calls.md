---
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Access'
- 'Process: Process Modification'
id: attack-pattern--ea016b56-ae0e-47fe-967a-cc0ad51af67f
mitre_attack_url: https://attack.mitre.org/techniques/T1055/008
name: Ptrace System Calls
platforms:
- Linux
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Ptrace System Calls
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Linux |
| **Data Sources** | Process: OS API Execution, Process: Process Access, Process: Process Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1055/008](https://attack.mitre.org/techniques/T1055/008) |

# Ptrace System Calls (attack-pattern--ea016b56-ae0e-47fe-967a-cc0ad51af67f)

## Description
Adversaries may inject malicious code into processes via ptrace (process trace) system calls in order to evade process-based defenses as well as possibly elevate privileges. Ptrace system call injection is a method of executing arbitrary code in the address space of a separate live process. 

Ptrace system call injection involves attaching to and modifying a running process. The ptrace system call enables a debugging process to observe and control another process (and each individual thread), including changing memory and register values.(Citation: PTRACE man) Ptrace system call injection is commonly performed by writing arbitrary code into a running process (ex: <code>malloc</code>) then invoking that memory with <code>PTRACE_SETREGS</code> to set the register containing the next instruction to execute. Ptrace system call injection can also be done with <code>PTRACE_POKETEXT</code>/<code>PTRACE_POKEDATA</code>, which copy data to a specific address in the target processes’ memory (ex: the current address of the next instruction). (Citation: PTRACE man)(Citation: Medium Ptrace JUL 2018) 

Ptrace system call injection may not be possible targeting processes that are non-child processes and/or have higher-privileges.(Citation: BH Linux Inject) 

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via ptrace system call injection may also evade detection from security products since the execution is masked under a legitimate process. 

## Detection
Monitoring for Linux specific calls such as the ptrace system call should not generate large amounts of data due to their specialized nature, and can be a very effective method to detect some of the common process injection methods.(Citation: ArtOfMemoryForensics)  (Citation: GNU Acct)  (Citation: RHEL auditd)  (Citation: Chokepoint preload rootkits) 

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1055/008)
- [PTRACE man](http://man7.org/linux/man-pages/man2/ptrace.2.html)
- [Medium Ptrace JUL 2018](https://medium.com/@jain.sm/code-injection-in-running-process-using-ptrace-d3ea7191a4be)
- [BH Linux Inject](https://github.com/gaffe23/linux-inject/blob/master/slides_BHArsenal2015.pdf)
- [GNU Acct](https://www.gnu.org/software/acct/)
- [RHEL auditd](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/chap-system_auditing)
- [Chokepoint preload rootkits](http://www.chokepoint.net/2014/02/detecting-userland-preload-rootkits.html)
