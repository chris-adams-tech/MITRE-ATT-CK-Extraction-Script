---
data_sources:
- 'Process: OS API Execution'
id: attack-pattern--a4657bc9-d22f-47d2-a7b7-dd6ec33f3dde
mitre_attack_url: https://attack.mitre.org/techniques/T1574/013
name: KernelCallbackTable
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - KernelCallbackTable
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/013](https://attack.mitre.org/techniques/T1574/013) |

# KernelCallbackTable (attack-pattern--a4657bc9-d22f-47d2-a7b7-dd6ec33f3dde)

## Description
Adversaries may abuse the <code>KernelCallbackTable</code> of a process to hijack its execution flow in order to run their own payloads.(Citation: Lazarus APT January 2022)(Citation: FinFisher exposed ) The <code>KernelCallbackTable</code> can be found in the Process Environment Block (PEB) and is initialized to an array of graphic functions available to a GUI process once <code>user32.dll</code> is loaded.(Citation: Windows Process Injection KernelCallbackTable)

An adversary may hijack the execution flow of a process using the <code>KernelCallbackTable</code> by replacing an original callback function with a malicious payload. Modifying callback functions can be achieved in various ways involving related behaviors such as [Reflective Code Loading](https://attack.mitre.org/techniques/T1620) or [Process Injection](https://attack.mitre.org/techniques/T1055) into another process.

A pointer to the memory address of the <code>KernelCallbackTable</code> can be obtained by locating the PEB (ex: via a call to the <code>NtQueryInformationProcess()</code> [Native API](https://attack.mitre.org/techniques/T1106) function).(Citation: NtQueryInformationProcess) Once the pointer is located, the <code>KernelCallbackTable</code> can be duplicated, and a function in the table (e.g., <code>fnCOPYDATA</code>) set to the address of a malicious payload (ex: via <code>WriteProcessMemory()</code>). The PEB is then updated with the new address of the table. Once the tampered function is invoked, the malicious payload will be triggered.(Citation: Lazarus APT January 2022)

The tampered function is typically invoked using a Windows message. After the process is hijacked and malicious code is executed, the <code>KernelCallbackTable</code> may also be restored to its original state by the rest of the malicious payload.(Citation: Lazarus APT January 2022) Use of the <code>KernelCallbackTable</code> to hijack execution flow may evade detection from security products since the execution can be masked under a legitimate process.

## Detection
Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious behaviors that could relate to post-compromise behavior.

Monitoring Windows API calls indicative of the various types of code injection may generate a significant amount of data and may not be directly useful for defense unless collected under specific circumstances. for known bad sequence of calls, since benign use of API functions may be common and difficult to distinguish from malicious behavior. Windows API calls such as <code>WriteProcessMemory()</code> and <code>NtQueryInformationProcess()</code> with the parameter set to <code>ProcessBasicInformation</code> may be used for this technique.(Citation: Lazarus APT January 2022)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/013)
- [Lazarus APT January 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [FinFisher exposed ](https://www.microsoft.com/security/blog/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
- [Windows Process Injection KernelCallbackTable](https://modexp.wordpress.com/2019/05/25/windows-injection-finspy/)
- [NtQueryInformationProcess](https://docs.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntqueryinformationprocess)
