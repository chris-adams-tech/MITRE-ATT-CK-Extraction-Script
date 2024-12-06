---
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Access'
- 'Process: Process Modification'
id: attack-pattern--7c0f17c9-1af6-4628-9cbd-9e45482dd605
mitre_attack_url: https://attack.mitre.org/techniques/T1055/004
name: Asynchronous Procedure Call
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Asynchronous Procedure Call
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Process: OS API Execution, Process: Process Access, Process: Process Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1055/004](https://attack.mitre.org/techniques/T1055/004) |

# Asynchronous Procedure Call (attack-pattern--7c0f17c9-1af6-4628-9cbd-9e45482dd605)

## Description
Adversaries may inject malicious code into processes via the asynchronous procedure call (APC) queue in order to evade process-based defenses as well as possibly elevate privileges. APC injection is a method of executing arbitrary code in the address space of a separate live process. 

APC injection is commonly performed by attaching malicious code to the APC Queue (Citation: Microsoft APC) of a process's thread. Queued APC functions are executed when the thread enters an alterable state.(Citation: Microsoft APC) A handle to an existing victim process is first created with native Windows API calls such as <code>OpenThread</code>. At this point <code>QueueUserAPC</code> can be used to invoke a function (such as <code>LoadLibrayA</code> pointing to a malicious DLL). 

A variation of APC injection, dubbed "Early Bird injection", involves creating a suspended process in which malicious code can be written and executed before the process' entry point (and potentially subsequent anti-malware hooks) via an APC. (Citation: CyberBit Early Bird Apr 2018) AtomBombing (Citation: ENSIL AtomBombing Oct 2016) is another variation that utilizes APCs to invoke malicious code previously written to the global atom table.(Citation: Microsoft Atom Table)

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via APC injection may also evade detection from security products since the execution is masked under a legitimate process. 

## Detection
Monitoring Windows API calls indicative of the various types of code injection may generate a significant amount of data and may not be directly useful for defense unless collected under specific circumstances for known bad sequences of calls, since benign use of API functions may be common and difficult to distinguish from malicious behavior. Windows API calls such as <code>SuspendThread</code>/<code>SetThreadContext</code>/<code>ResumeThread</code>, <code>QueueUserAPC</code>/<code>NtQueueApcThread</code>, and those that can be used to modify memory within another process, such as <code>VirtualAllocEx</code>/<code>WriteProcessMemory</code>, may be used for this technique.(Citation: Elastic Process Injection July 2017)

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1055/004)
- [Microsoft APC](https://msdn.microsoft.com/library/windows/desktop/ms681951.aspx)
- [CyberBit Early Bird Apr 2018](https://www.cyberbit.com/blog/endpoint-security/new-early-bird-code-injection-technique-discovered/)
- [ENSIL AtomBombing Oct 2016](https://blog.ensilo.com/atombombing-brand-new-code-injection-for-windows)
- [Microsoft Atom Table](https://msdn.microsoft.com/library/windows/desktop/ms649053.aspx)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
