---
data_sources:
- 'Process: OS API Execution'
- 'Module: Module Load'
- 'Command: Command Execution'
- 'File: File Creation'
- 'Windows Registry: Windows Registry Key Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'File: File Modification'
- 'Kernel: Kernel Module Load'
- 'Process: Process Creation'
- 'Driver: Driver Load'
id: attack-pattern--1ecb2399-e8ba-4f6b-8ba7-5c27d49405cf
mitre_attack_url: https://attack.mitre.org/techniques/T1547
name: Boot or Logon Autostart Execution
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- persistence
- privilege-escalation
title: persistence - Boot or Logon Autostart Execution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Process: OS API Execution, Module: Module Load, Command: Command Execution, File: File Creation, Windows Registry: Windows Registry Key Creation, Windows Registry: Windows Registry Key Modification, File: File Modification, Kernel: Kernel Module Load, Process: Process Creation, Driver: Driver Load |
| **Permissions Required** | User, Administrator, root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547](https://attack.mitre.org/techniques/T1547) |

# Boot or Logon Autostart Execution (attack-pattern--1ecb2399-e8ba-4f6b-8ba7-5c27d49405cf)

## Description
Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon.(Citation: Microsoft Run Key)(Citation: MSDN Authentication Packages)(Citation: Microsoft TimeProvider)(Citation: Cylance Reg Persistence Sept 2013)(Citation: Linux Kernel Programming) These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel.

Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.

## Detection
Monitor for additions or modifications of mechanisms that could be used to trigger autostart execution, such as relevant additions to the Registry. Look for changes that are not correlated with known updates, patches, or other planned administrative activity. Tools such as Sysinternals Autoruns may also be used to detect system autostart configuration changes that could be attempts at persistence.(Citation: TechNet Autoruns)  Changes to some autostart configuration settings may happen under normal conditions when legitimate software is installed. 

Suspicious program execution as autostart programs may show up as outlier processes that have not been seen before when compared against historical data.To increase confidence of malicious activity, data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

Monitor DLL loads by processes, specifically looking for DLLs that are not recognized or not normally loaded into a process. Look for abnormal process behavior that may be due to a process loading a malicious DLL.

Monitor for abnormal usage of utilities and command-line parameters involved in kernel modification or driver installation.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547)
- [Cylance Reg Persistence Sept 2013](https://blog.cylance.com/windows-registry-persistence-part-2-the-run-keys-and-search-order)
- [MSDN Authentication Packages](https://msdn.microsoft.com/library/windows/desktop/aa374733.aspx)
- [Microsoft Run Key](https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys)
- [Microsoft TimeProvider](https://msdn.microsoft.com/library/windows/desktop/ms725475.aspx)
- [Linux Kernel Programming](https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
