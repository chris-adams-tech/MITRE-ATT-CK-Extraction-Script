---
data_sources:
- 'Process: Process Creation'
- 'Process: Process Modification'
- 'Process: OS API Execution'
- 'Process: Process Access'
id: attack-pattern--b200542e-e877-4395-875b-cf1a44537ca4
mitre_attack_url: https://attack.mitre.org/techniques/T1055/012
name: Process Hollowing
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Process Hollowing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Process: Process Modification, Process: OS API Execution, Process: Process Access |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1055/012](https://attack.mitre.org/techniques/T1055/012) |

# Process Hollowing (attack-pattern--b200542e-e877-4395-875b-cf1a44537ca4)

## Description
Adversaries may inject malicious code into suspended and hollowed processes in order to evade process-based defenses. Process hollowing is a method of executing arbitrary code in the address space of a separate live process.  

Process hollowing is commonly performed by creating a process in a suspended state then unmapping/hollowing its memory, which can then be replaced with malicious code. A victim process can be created with native Windows API calls such as <code>CreateProcess</code>, which includes a flag to suspend the processes primary thread. At this point the process can be unmapped using APIs calls such as <code>ZwUnmapViewOfSection</code> or <code>NtUnmapViewOfSection</code>  before being written to, realigned to the injected code, and resumed via <code>VirtualAllocEx</code>, <code>WriteProcessMemory</code>, <code>SetThreadContext</code>, then <code>ResumeThread</code> respectively.(Citation: Leitch Hollowing)(Citation: Elastic Process Injection July 2017)

This is very similar to [Thread Local Storage](https://attack.mitre.org/techniques/T1055/005) but creates a new process rather than targeting an existing process. This behavior will likely not result in elevated privileges since the injected process was spawned from (and thus inherits the security context) of the injecting process. However, execution via process hollowing may also evade detection from security products since the execution is masked under a legitimate process. 

## Detection
Monitoring Windows API calls indicative of the various types of code injection may generate a significant amount of data and may not be directly useful for defense unless collected under specific circumstances for known bad sequences of calls, since benign use of API functions may be common and difficult to distinguish from malicious behavior. Windows API calls such as <code>CreateRemoteThread</code>, <code>SuspendThread</code>/<code>SetThreadContext</code>/<code>ResumeThread</code>, and those that can be used to modify memory within another process, such as <code>VirtualAllocEx</code>/<code>WriteProcessMemory</code>, may be used for this technique.(Citation: Elastic Process Injection July 2017)

Processing hollowing commonly involves spawning an otherwise benign victim process. Consider correlating detections of processes created in a suspended state (ex: through API flags or process’ thread metadata) with other malicious activity such as attempts to modify a process' memory, especially by its parent process, or other abnormal process behavior.(Citation: Nviso Spoof Command Line 2020)(Citation: Mandiant Endpoint Evading 2019)

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1055/012)
- [Nviso Spoof Command Line 2020](https://blog.nviso.eu/2020/02/04/the-return-of-the-spoof-part-2-command-line-spoofing/)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [Leitch Hollowing](https://new.dc414.org/wp-content/uploads/2011/01/Process-Hollowing.pdf)
- [Mandiant Endpoint Evading 2019](https://www.mandiant.com/resources/staying-hidden-on-the-endpoint-evading-detection-with-shellcode)
