---
contributors:
- TruKno
data_sources:
- 'Process: Process Creation'
- 'Process: OS API Execution'
- 'Application Log: Application Log Content'
- 'Command: Command Execution'
id: attack-pattern--e4dc8c01-417f-458d-9ee0-bb0617c1b391
mitre_attack_url: https://attack.mitre.org/techniques/T1622
name: Debugger Evasion
platforms:
- Windows
- Linux
- macOS
tactics:
- defense-evasion
- discovery
title: defense-evasion - Debugger Evasion
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, discovery |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Process: Process Creation, Process: OS API Execution, Application Log: Application Log Content, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1622](https://attack.mitre.org/techniques/T1622) |

# Debugger Evasion (attack-pattern--e4dc8c01-417f-458d-9ee0-bb0617c1b391)

## Description
Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders to trace and/or analyze the execution of potential malware payloads.(Citation: ProcessHacker Github)

Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative of a debugged environment. Similar to [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497), if the adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for debugger artifacts before dropping secondary or additional payloads.

Specific checks will vary based on the target and/or adversary, but may involve [Native API](https://attack.mitre.org/techniques/T1106) function calls such as <code>IsDebuggerPresent()</code> and <code> NtQueryInformationProcess()</code>, or manually checking the <code>BeingDebugged</code> flag of the Process Environment Block (PEB). Other checks for debugging artifacts may also seek to enumerate hardware breakpoints, interrupt assembly opcodes, time checks, or measurements if exceptions are raised in the current process (assuming a present debugger would “swallow” or handle the potential error).(Citation: hasherezade debug)(Citation: AlKhaser Debug)(Citation: vxunderground debug)

Adversaries may use the information learned from these debugger checks during automated discovery to shape follow-on behaviors. Debuggers can also be evaded by detaching the process or flooding debug logs with meaningless data via messages produced by looping [Native API](https://attack.mitre.org/techniques/T1106) function calls such as <code>OutputDebugStringW()</code>.(Citation: wardle evilquest partii)(Citation: Checkpoint Dridex Jan 2021)

## Detection
Debugger related system checks will likely occur in the first steps of an operation but may also occur throughout as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained. Detecting actions related to debugger identification may be difficult depending on the adversary's implementation and monitoring required. Monitoring for suspicious [Native API](https://attack.mitre.org/techniques/T1106) function calls as well as processes being spawned that gather a variety of system information or perform other forms of Discovery, especially in a short period of time, may aid in detection.

Monitor debugger logs for signs of abnormal and potentially malicious activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1622)
- [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
- [hasherezade debug](https://github.com/hasherezade/malware_training_vol1/blob/main/slides/module3/Module3_2_fingerprinting.pdf)
- [AlKhaser Debug](https://github.com/LordNoteworthy/al-khaser/tree/master/al-khaser/AntiDebug)
- [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)
- [ProcessHacker Github](https://github.com/processhacker/processhacker)
- [vxunderground debug](https://github.com/vxunderground/VX-API/tree/main/Anti%20Debug)
