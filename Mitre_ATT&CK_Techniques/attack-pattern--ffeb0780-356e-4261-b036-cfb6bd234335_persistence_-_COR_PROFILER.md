---
contributors:
- Jesse Brown, Red Canary
data_sources:
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Module: Module Load'
- 'Command: Command Execution'
id: attack-pattern--ffeb0780-356e-4261-b036-cfb6bd234335
mitre_attack_url: https://attack.mitre.org/techniques/T1574/012
name: COR_PROFILER
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - COR_PROFILER
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Windows Registry: Windows Registry Key Modification, Module: Module Load, Command: Command Execution |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/012](https://attack.mitre.org/techniques/T1574/012) |

# COR_PROFILER (attack-pattern--ffeb0780-356e-4261-b036-cfb6bd234335)

## Description
Adversaries may leverage the COR_PROFILER environment variable to hijack the execution flow of programs that load the .NET CLR. The COR_PROFILER is a .NET Framework feature which allows developers to specify an unmanaged (or external of .NET) profiling DLL to be loaded into each .NET process that loads the Common Language Runtime (CLR). These profilers are designed to monitor, troubleshoot, and debug managed code executed by the .NET CLR.(Citation: Microsoft Profiling Mar 2017)(Citation: Microsoft COR_PROFILER Feb 2013)

The COR_PROFILER environment variable can be set at various scopes (system, user, or process) resulting in different levels of influence. System and user-wide environment variable scopes are specified in the Registry, where a [Component Object Model](https://attack.mitre.org/techniques/T1559/001) (COM) object can be registered as a profiler DLL. A process scope COR_PROFILER can also be created in-memory without modifying the Registry. Starting with .NET Framework 4, the profiling DLL does not need to be registered as long as the location of the DLL is specified in the COR_PROFILER_PATH environment variable.(Citation: Microsoft COR_PROFILER Feb 2013)

Adversaries may abuse COR_PROFILER to establish persistence that executes a malicious DLL in the context of all .NET processes every time the CLR is invoked. The COR_PROFILER can also be used to elevate privileges (ex: [Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002)) if the victim .NET process executes at a higher permission level, as well as to hook and [Impair Defenses](https://attack.mitre.org/techniques/T1562) provided by .NET processes.(Citation: RedCanary Mockingbird May 2020)(Citation: Red Canary COR_PROFILER May 2020)(Citation: Almond COR_PROFILER Apr 2019)(Citation: GitHub OmerYa Invisi-Shell)(Citation: subTee .NET Profilers May 2017)

## Detection
For detecting system and user scope abuse of the COR_PROFILER, monitor the Registry for changes to COR_ENABLE_PROFILING, COR_PROFILER, and COR_PROFILER_PATH that correspond to system and user environment variables that do not correlate to known developer tools. Extra scrutiny should be placed on suspicious modification of these Registry keys by command line tools like wmic.exe, setx.exe, and [Reg](https://attack.mitre.org/software/S0075), monitoring for command-line arguments indicating a change to COR_PROFILER variables may aid in detection. For system, user, and process scope abuse of the COR_PROFILER, monitor for new suspicious unmanaged profiling DLLs loading into .NET processes shortly after the CLR causing abnormal process behavior.(Citation: Red Canary COR_PROFILER May 2020) Consider monitoring for DLL files that are associated with COR_PROFILER environment variables.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/012)
- [Microsoft Profiling Mar 2017](https://docs.microsoft.com/en-us/dotnet/framework/unmanaged-api/profiling/profiling-overview)
- [Microsoft COR_PROFILER Feb 2013](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ee471451(v=vs.100))
- [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)
- [Red Canary COR_PROFILER May 2020](https://redcanary.com/blog/cor_profiler-for-persistence/)
- [Almond COR_PROFILER Apr 2019](https://offsec.almond.consulting/UAC-bypass-dotnet.html)
- [GitHub OmerYa Invisi-Shell](https://github.com/OmerYa/Invisi-Shell)
- [subTee .NET Profilers May 2017](https://web.archive.org/web/20170720041203/http://subt0x10.blogspot.com/2017/05/subvert-clr-process-listing-with-net.html)
