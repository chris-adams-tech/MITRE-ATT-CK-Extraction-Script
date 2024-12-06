---
contributors:
- "Jo\xE3o Paulo de A. Filho, @Hug1nN__"
- Shlomi Salem, SentinelOne
- Lior Ribak, SentinelOne
- Rex Guo, @Xiaofei_REX, Confluera
- Joas Antonio dos Santos, @C0d3Cr4zy, Inmetrics
- Jiraput Thamsongkrah
data_sources:
- 'Module: Module Load'
- 'Script: Script Execution'
- 'Process: OS API Execution'
id: attack-pattern--4933e63b-9b77-476e-ab29-761bc5b7d15a
mitre_attack_url: https://attack.mitre.org/techniques/T1620
name: Reflective Code Loading
platforms:
- macOS
- Linux
- Windows
tactics:
- defense-evasion
title: defense-evasion - Reflective Code Loading
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Linux, Windows |
| **Data Sources** | Module: Module Load, Script: Script Execution, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1620](https://attack.mitre.org/techniques/T1620) |

# Reflective Code Loading (attack-pattern--4933e63b-9b77-476e-ab29-761bc5b7d15a)

## Description
Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads. Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating a thread or process backed by a file path on disk (e.g., [Shared Modules](https://attack.mitre.org/techniques/T1129)).

Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless executable code (ex: position-independent shellcode).(Citation: Introducing Donut)(Citation: S1 Custom Shellcode Tool)(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Mandiant BYOL) For example, the `Assembly.Load()` method executed by [PowerShell](https://attack.mitre.org/techniques/T1059/001) may be abused to load raw code into the running process.(Citation: Microsoft AssemblyLoad)

Reflective code injection is very similar to [Process Injection](https://attack.mitre.org/techniques/T1055) except that the “injection” loads code into the processes’ own memory instead of that of a separate process. Reflective loading may evade process-based detections since the execution of the arbitrary code may be masked within a legitimate or otherwise benign process. Reflectively loading payloads directly into memory may also avoid creating files or other artifacts on disk, while also enabling malware to keep these payloads encrypted (or otherwise obfuscated) until execution.(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Intezer ACBackdoor)(Citation: S1 Old Rat New Tricks)

## Detection
Monitor for code artifacts associated with reflectively loading code, such as the abuse of .NET functions such as <code>Assembly.Load()</code> and [Native API](https://attack.mitre.org/techniques/T1106) functions such as <code>CreateThread()</code>, <code>memfd_create()</code>, <code>execve()</code>, and/or <code>execveat()</code>.(Citation: 00sec Droppers)(Citation: S1 Old Rat New Tricks)

Monitor for artifacts of abnormal process execution. For example, a common signature related to reflective code loading on Windows is mechanisms related to the .NET Common Language Runtime (CLR) -- such as mscor.dll, mscoree.dll, and clr.dll -- loading into abnormal processes (such as notepad.exe). Similarly, AMSI / ETW traces can be used to identify signs of arbitrary code execution from within the memory of potentially compromised processes.(Citation: MDSec Detecting DOTNET)(Citation: Introducing Donut)

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1620)
- [00sec Droppers](https://0x00sec.org/t/super-stealthy-droppers/3715)
- [S1 Custom Shellcode Tool](https://www.sentinelone.com/blog/building-a-custom-tool-for-shellcode-analysis/)
- [Mandiant BYOL](https://www.mandiant.com/resources/bring-your-own-land-novel-red-teaming-technique)
- [S1 Old Rat New Tricks](https://www.sentinelone.com/blog/teaching-an-old-rat-new-tricks/)
- [MDSec Detecting DOTNET](https://www.mdsec.co.uk/2020/06/detecting-and-advancing-in-memory-net-tradecraft/)
- [Microsoft AssemblyLoad](https://learn.microsoft.com/dotnet/api/system.reflection.assembly.load)
- [Intezer ACBackdoor](https://www.intezer.com/blog/research/acbackdoor-analysis-of-a-new-multiplatform-backdoor/)
- [Stuart ELF Memory](https://magisterquis.github.io/2018/03/31/in-memory-only-elf-execution.html)
- [Introducing Donut](https://thewover.github.io/Introducing-Donut/)
