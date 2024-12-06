---
contributors:
- Gordon Long, Box, Inc., @ethicalhax
- Stefan Kanthak
- Tristan Madani (Cybereason)
data_sources:
- 'Process: OS API Execution'
- 'Module: Module Load'
id: attack-pattern--391d824f-0ef1-47a0-b0ee-c59a75e27670
mitre_attack_url: https://attack.mitre.org/techniques/T1106
name: Native API
platforms:
- Windows
- macOS
- Linux
tactics:
- execution
title: execution - Native API
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Process: OS API Execution, Module: Module Load |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1106](https://attack.mitre.org/techniques/T1106) |

# Native API (attack-pattern--391d824f-0ef1-47a0-b0ee-c59a75e27670)

## Description
Adversaries may interact with the native OS application programming interface (API) to execute behaviors. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes.(Citation: NT API Windows)(Citation: Linux Kernel API) These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations.

Adversaries may abuse these OS API functions as a means of executing behaviors. Similar to [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), the native API and its hierarchy of interfaces provide mechanisms to interact with and utilize various components of a victimized system.

Native API functions (such as <code>NtCreateProcess</code>) may be directed invoked via system calls / syscalls, but these features are also often exposed to user-mode applications via interfaces and libraries.(Citation: OutFlank System Calls)(Citation: CyberBit System Calls)(Citation: MDSec System Calls) For example, functions such as the Windows API <code>CreateProcess()</code> or GNU <code>fork()</code> will allow programs and scripts to start other processes.(Citation: Microsoft CreateProcess)(Citation: GNU Fork) This may allow API callers to execute a binary, run a CLI command, load modules, etc. as thousands of similar API functions exist for various system operations.(Citation: Microsoft Win32)(Citation: LIBC)(Citation: GLIBC)

Higher level software frameworks, such as Microsoft .NET and macOS Cocoa, are also available to interact with native APIs. These frameworks typically provide language wrappers/abstractions to API functionalities and are designed for ease-of-use/portability of code.(Citation: Microsoft NET)(Citation: Apple Core Services)(Citation: MACOS Cocoa)(Citation: macOS Foundation)

Adversaries may use assembly to directly or in-directly invoke syscalls in an attempt to subvert defensive sensors and detection signatures such as user mode API-hooks.(Citation: Redops Syscalls) Adversaries may also attempt to tamper with sensors and defensive tools associated with API monitoring, such as unhooking monitored functions via [Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001).

## Detection
Monitoring API calls may generate a significant amount of data and may not be useful for defense unless collected under specific circumstances, since benign use of API functions are common and may be difficult to distinguish from malicious behavior. Correlation of other events with behavior surrounding API function calls using API monitoring will provide additional context to an event that may assist in determining if it is due to malicious behavior. Correlation of activity by process lineage by process ID may be sufficient. 

Utilization of the Windows APIs may involve processes loading/accessing system DLLs associated with providing called functions (ex: ntdll.dll, kernel32.dll, advapi32.dll, user32.dll, and gdi32.dll). Monitoring for DLL loads, especially to abnormal/unusual or potentially malicious processes, may indicate abuse of the Windows API. Though noisy, this data can be combined with other indicators to identify adversary activity. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1106)
- [MACOS Cocoa](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/CocoaApplicationLayer/CocoaApplicationLayer.html#//apple_ref/doc/uid/TP40001067-CH274-SW1)
- [Apple Core Services](https://developer.apple.com/documentation/coreservices)
- [macOS Foundation](https://developer.apple.com/documentation/foundation)
- [OutFlank System Calls](https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/)
- [Redops Syscalls](https://redops.at/en/blog/direct-syscalls-vs-indirect-syscalls)
- [GNU Fork](https://www.gnu.org/software/libc/manual/html_node/Creating-a-Process.html)
- [CyberBit System Calls](https://www.cyberbit.com/blog/endpoint-security/malware-mitigation-when-direct-system-calls-are-used/)
- [GLIBC](https://www.gnu.org/software/libc/)
- [LIBC](https://man7.org/linux/man-pages//man7/libc.7.html)
- [Linux Kernel API](https://www.kernel.org/doc/html/v4.12/core-api/kernel-api.html)
- [MDSec System Calls](https://www.mdsec.co.uk/2020/12/bypassing-user-mode-hooks-and-direct-invocation-of-system-calls-for-red-teams/)
- [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)
- [Microsoft Win32](https://docs.microsoft.com/en-us/windows/win32/api/)
- [Microsoft NET](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet-framework)
- [NT API Windows](https://undocumented.ntinternals.net/)
