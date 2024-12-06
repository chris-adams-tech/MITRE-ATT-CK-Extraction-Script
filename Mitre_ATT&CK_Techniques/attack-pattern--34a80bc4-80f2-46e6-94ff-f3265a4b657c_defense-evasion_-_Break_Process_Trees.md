---
contributors:
- Tim (Wadhwa-)Brown
data_sources:
- 'Process: OS API Execution'
- 'Process: Process Creation'
id: attack-pattern--34a80bc4-80f2-46e6-94ff-f3265a4b657c
mitre_attack_url: https://attack.mitre.org/techniques/T1036/009
name: Break Process Trees
platforms:
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - Break Process Trees
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS |
| **Data Sources** | Process: OS API Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/009](https://attack.mitre.org/techniques/T1036/009) |

# Break Process Trees (attack-pattern--34a80bc4-80f2-46e6-94ff-f3265a4b657c)

## Description
An adversary may attempt to evade process tree-based analysis by modifying executed malware's parent process ID (PPID). If endpoint protection software leverages the “parent-child" relationship for detection, breaking this relationship could result in the adversary’s behavior not being associated with previous process tree activity. On Unix-based systems breaking this process tree is common practice for administrators to execute software using scripts and programs.(Citation: 3OHA double-fork 2022) 

On Linux systems, adversaries may execute a series of [Native API](https://attack.mitre.org/techniques/T1106) calls to alter malware's process tree. For example, adversaries can execute their payload without any arguments, call the `fork()` API call twice, then have the parent process exit. This creates a grandchild process with no parent process that is immediately adopted by the `init` system process (PID 1), which successfully disconnects the execution of the adversary's payload from its previous process tree.

Another example is using the “daemon” syscall to detach from the current parent process and run in the background.(Citation: Sandfly BPFDoor 2022)(Citation: Microsoft XorDdos Linux Stealth 2022) 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/009)
- [3OHA double-fork 2022](https://0xjet.github.io/3OHA/2022/04/11/post.html)
- [Microsoft XorDdos Linux Stealth 2022](https://www.microsoft.com/en-us/security/blog/2022/05/19/rise-in-xorddos-a-deeper-look-at-the-stealthy-ddos-malware-targeting-linux-devices/)
- [Sandfly BPFDoor 2022](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
