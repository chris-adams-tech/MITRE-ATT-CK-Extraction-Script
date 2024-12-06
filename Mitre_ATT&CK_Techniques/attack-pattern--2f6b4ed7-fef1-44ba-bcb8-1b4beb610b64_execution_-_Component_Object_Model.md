---
data_sources:
- 'Module: Module Load'
- 'Script: Script Execution'
- 'Process: Process Creation'
id: attack-pattern--2f6b4ed7-fef1-44ba-bcb8-1b4beb610b64
mitre_attack_url: https://attack.mitre.org/techniques/T1559/001
name: Component Object Model
platforms:
- Windows
tactics:
- execution
title: execution - Component Object Model
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows |
| **Data Sources** | Module: Module Load, Script: Script Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1559/001](https://attack.mitre.org/techniques/T1559/001) |

# Component Object Model (attack-pattern--2f6b4ed7-fef1-44ba-bcb8-1b4beb610b64)

## Description
Adversaries may use the Windows Component Object Model (COM) for local code execution. COM is an inter-process communication (IPC) component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more interfaces.(Citation: Fireeye Hunting COM June 2019) Through COM, a client object can call methods of server objects, which are typically binary Dynamic Link Libraries (DLL) or executables (EXE).(Citation: Microsoft COM) Remote COM execution is facilitated by [Remote Services](https://attack.mitre.org/techniques/T1021) such as  [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) (DCOM).(Citation: Fireeye Hunting COM June 2019)

Various COM interfaces are exposed that can be abused to invoke arbitrary execution via a variety of programming languages such as C, C++, Java, and [Visual Basic](https://attack.mitre.org/techniques/T1059/005).(Citation: Microsoft COM) Specific COM objects also exist to directly perform functions beyond code execution, such as creating a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), fileless download/execution, and other adversary behaviors related to privilege escalation and persistence.(Citation: Fireeye Hunting COM June 2019)(Citation: ProjectZero File Write EoP Apr 2018)

## Detection
Monitor for COM objects loading DLLs and other modules not typically associated with the application.(Citation: Enigma Outlook DCOM Lateral Movement Nov 2017) Enumeration of COM objects, via [Query Registry](https://attack.mitre.org/techniques/T1012) or [PowerShell](https://attack.mitre.org/techniques/T1059/001), may also proceed malicious use.(Citation: Fireeye Hunting COM June 2019)(Citation: Enigma MMC20 COM Jan 2017)

Monitor for spawning of processes associated with COM objects, especially those invoked by a user different than the one currently logged on. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1559/001)
- [Fireeye Hunting COM June 2019](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)
- [Microsoft COM](https://msdn.microsoft.com/library/windows/desktop/ms680573.aspx)
- [ProjectZero File Write EoP Apr 2018](https://googleprojectzero.blogspot.com/2018/04/windows-exploitation-tricks-exploiting.html)
- [Enigma Outlook DCOM Lateral Movement Nov 2017](https://enigma0x3.net/2017/11/16/lateral-movement-using-outlooks-createobject-method-and-dotnettojscript/)
- [Enigma MMC20 COM Jan 2017](https://enigma0x3.net/2017/01/05/lateral-movement-using-the-mmc20-application-com-object/)
