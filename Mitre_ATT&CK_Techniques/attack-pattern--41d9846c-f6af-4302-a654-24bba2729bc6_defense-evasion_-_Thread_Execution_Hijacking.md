---
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Modification'
- 'Process: Process Access'
id: attack-pattern--41d9846c-f6af-4302-a654-24bba2729bc6
mitre_attack_url: https://attack.mitre.org/techniques/T1055/003
name: Thread Execution Hijacking
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Thread Execution Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Process: OS API Execution, Process: Process Modification, Process: Process Access |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1055/003](https://attack.mitre.org/techniques/T1055/003) |

# Thread Execution Hijacking (attack-pattern--41d9846c-f6af-4302-a654-24bba2729bc6)

## Description
Adversaries may inject malicious code into hijacked processes in order to evade process-based defenses as well as possibly elevate privileges. Thread Execution Hijacking is a method of executing arbitrary code in the address space of a separate live process. 

Thread Execution Hijacking is commonly performed by suspending an existing process then unmapping/hollowing its memory, which can then be replaced with malicious code or the path to a DLL. A handle to an existing victim process is first created with native Windows API calls such as <code>OpenThread</code>. At this point the process can be suspended then written to, realigned to the injected code, and resumed via <code>SuspendThread </code>, <code>VirtualAllocEx</code>, <code>WriteProcessMemory</code>, <code>SetThreadContext</code>, then <code>ResumeThread</code> respectively.(Citation: Elastic Process Injection July 2017)

This is very similar to [Process Hollowing](https://attack.mitre.org/techniques/T1055/012) but targets an existing process rather than creating a process in a suspended state.  

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via Thread Execution Hijacking may also evade detection from security products since the execution is masked under a legitimate process. 

## Detection
Monitoring Windows API calls indicative of the various types of code injection may generate a significant amount of data and may not be directly useful for defense unless collected under specific circumstances for known bad sequences of calls, since benign use of API functions may be common and difficult to distinguish from malicious behavior. Windows API calls such as <code>CreateRemoteThread</code>, <code>SuspendThread</code>/<code>SetThreadContext</code>/<code>ResumeThread</code>, and those that can be used to modify memory within another process, such as <code>VirtualAllocEx</code>/<code>WriteProcessMemory</code>, may be used for this technique.(Citation: Elastic Process Injection July 2017)

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1055/003)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
