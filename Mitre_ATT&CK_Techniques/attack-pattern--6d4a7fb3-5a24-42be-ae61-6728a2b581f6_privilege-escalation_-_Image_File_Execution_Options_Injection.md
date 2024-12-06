---
contributors:
- Oddvar Moe, @oddvarmoe
data_sources:
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Creation'
id: attack-pattern--6d4a7fb3-5a24-42be-ae61-6728a2b581f6
mitre_attack_url: https://attack.mitre.org/techniques/T1546/012
name: Image File Execution Options Injection
platforms:
- Windows
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Image File Execution Options Injection
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Windows Registry: Windows Registry Key Modification, Process: Process Creation |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/012](https://attack.mitre.org/techniques/T1546/012) |

# Image File Execution Options Injection (attack-pattern--6d4a7fb3-5a24-42be-ae61-6728a2b581f6)

## Description
Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by Image File Execution Options (IFEO) debuggers. IFEOs enable a developer to attach a debugger to an application. When a process is created, a debugger present in an application’s IFEO will be prepended to the application’s name, effectively launching the new process under the debugger (e.g., <code>C:\dbg\ntsd.exe -g  notepad.exe</code>). (Citation: Microsoft Dev Blog IFEO Mar 2010)

IFEOs can be set directly via the Registry or in Global Flags via the GFlags tool. (Citation: Microsoft GFlags Mar 2017) IFEOs are represented as <code>Debugger</code> values in the Registry under <code>HKLM\SOFTWARE{\Wow6432Node}\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<executable></code> where <code>&lt;executable&gt;</code> is the binary on which the debugger is attached. (Citation: Microsoft Dev Blog IFEO Mar 2010)

IFEOs can also enable an arbitrary monitor program to be launched when a specified program silently exits (i.e. is prematurely terminated by itself or a second, non kernel-mode process). (Citation: Microsoft Silent Process Exit NOV 2017) (Citation: Oddvar Moe IFEO APR 2018) Similar to debuggers, silent exit monitoring can be enabled through GFlags and/or by directly modifying IFEO and silent process exit Registry values in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\</code>. (Citation: Microsoft Silent Process Exit NOV 2017) (Citation: Oddvar Moe IFEO APR 2018)

Similar to [Accessibility Features](https://attack.mitre.org/techniques/T1546/008), on Windows Vista and later as well as Windows Server 2008 and later, a Registry key may be modified that configures "cmd.exe," or another program that provides backdoor access, as a "debugger" for an accessibility program (ex: utilman.exe). After the Registry is modified, pressing the appropriate key combination at the login screen while at the keyboard or when connected with [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001) will cause the "debugger" program to be executed with SYSTEM privileges. (Citation: Tilbury 2014)

Similar to [Process Injection](https://attack.mitre.org/techniques/T1055), these values may also be abused to obtain privilege escalation by causing a malicious executable to be loaded and run in the context of separate processes on the computer. (Citation: Elastic Process Injection July 2017) Installing IFEO mechanisms may also provide Persistence via continuous triggered invocation.

Malware may also use IFEO to [Impair Defenses](https://attack.mitre.org/techniques/T1562) by registering invalid debuggers that redirect and effectively disable various system and security applications. (Citation: FSecure Hupigon) (Citation: Symantec Ushedix June 2008)

## Detection
Monitor for abnormal usage of the GFlags tool as well as common processes spawned under abnormal parents and/or with creation flags indicative of debugging such as <code>DEBUG_PROCESS</code> and <code>DEBUG_ONLY_THIS_PROCESS</code>. (Citation: Microsoft Dev Blog IFEO Mar 2010)

Monitor Registry values associated with IFEOs, as well as silent process exit monitoring, for modifications that do not correlate with known software, patch cycles, etc. Monitor and analyze application programming interface (API) calls that are indicative of Registry edits such as <code>RegCreateKeyEx</code> and <code>RegSetValueEx</code>. (Citation: Elastic Process Injection July 2017)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/012)
- [Microsoft Dev Blog IFEO Mar 2010](https://blogs.msdn.microsoft.com/mithuns/2010/03/24/image-file-execution-options-ifeo/)
- [Microsoft GFlags Mar 2017](https://docs.microsoft.com/windows-hardware/drivers/debugger/gflags-overview)
- [Microsoft Silent Process Exit NOV 2017](https://docs.microsoft.com/windows-hardware/drivers/debugger/registry-entries-for-silent-process-exit)
- [Oddvar Moe IFEO APR 2018](https://oddvar.moe/2018/04/10/persistence-using-globalflags-in-image-file-execution-options-hidden-from-autoruns-exe/)
- [Tilbury 2014](http://blog.crowdstrike.com/registry-analysis-with-crowdresponse/)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [FSecure Hupigon](https://www.f-secure.com/v-descs/backdoor_w32_hupigon_emv.shtml)
- [Symantec Ushedix June 2008](https://www.symantec.com/security_response/writeup.jsp?docid=2008-062807-2501-99&tabid=2)
