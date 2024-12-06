---
contributors:
- Oddvar Moe, @oddvarmoe
id: attack-pattern--62166220-e498-410f-a90a-19d4339d4e99
mitre_attack_url: https://attack.mitre.org/techniques/T1183
name: Image File Execution Options Injection
platforms:
- Windows
tactics:
- privilege-escalation
- persistence
- defense-evasion
title: privilege-escalation - Image File Execution Options Injection
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence, defense-evasion |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1183](https://attack.mitre.org/techniques/T1183) |

# Image File Execution Options Injection (attack-pattern--62166220-e498-410f-a90a-19d4339d4e99)

## Description
Image File Execution Options (IFEO) enable a developer to attach a debugger to an application. When a process is created, a debugger present in an application’s IFEO will be prepended to the application’s name, effectively launching the new process under the debugger (e.g., “C:\dbg\ntsd.exe -g  notepad.exe”). (Citation: Microsoft Dev Blog IFEO Mar 2010)

IFEOs can be set directly via the Registry or in Global Flags via the GFlags tool. (Citation: Microsoft GFlags Mar 2017) IFEOs are represented as <code>Debugger</code> values in the Registry under <code>HKLM\SOFTWARE{\Wow6432Node}\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<executable></code> where <code><executable></code> is the binary on which the debugger is attached. (Citation: Microsoft Dev Blog IFEO Mar 2010)

IFEOs can also enable an arbitrary monitor program to be launched when a specified program silently exits (i.e. is prematurely terminated by itself or a second, non kernel-mode process). (Citation: Microsoft Silent Process Exit NOV 2017) (Citation: Oddvar Moe IFEO APR 2018) Similar to debuggers, silent exit monitoring can be enabled through GFlags and/or by directly modifying IEFO and silent process exit Registry values in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\</code>. (Citation: Microsoft Silent Process Exit NOV 2017) (Citation: Oddvar Moe IFEO APR 2018)

An example where the evil.exe process is started when notepad.exe exits: (Citation: Oddvar Moe IFEO APR 2018)

* <code>reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512</code>
* <code>reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v ReportingMode /t REG_DWORD /d 1</code>
* <code>reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v MonitorProcess /d "C:\temp\evil.exe"</code>

Similar to [Process Injection](https://attack.mitre.org/techniques/T1055), these values may be abused to obtain persistence and privilege escalation by causing a malicious executable to be loaded and run in the context of separate processes on the computer. (Citation: Elastic Process Injection July 2017) Installing IFEO mechanisms may also provide Persistence via continuous invocation.

Malware may also use IFEO for Defense Evasion by registering invalid debuggers that redirect and effectively disable various system and security applications. (Citation: FSecure Hupigon) (Citation: Symantec Ushedix June 2008)

## Detection
Monitor for common processes spawned under abnormal parents and/or with creation flags indicative of debugging such as <code>DEBUG_PROCESS</code> and <code>DEBUG_ONLY_THIS_PROCESS</code>. (Citation: Microsoft Dev Blog IFEO Mar 2010)

Monitor Registry values associated with IFEOs, as well as silent process exit monitoring, for modifications that do not correlate with known software, patch cycles, etc. Monitor and analyze application programming interface (API) calls that are indicative of Registry edits such as RegCreateKeyEx and RegSetValueEx. (Citation: Elastic Process Injection July 2017)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1183)
- [Microsoft Dev Blog IFEO Mar 2010](https://blogs.msdn.microsoft.com/mithuns/2010/03/24/image-file-execution-options-ifeo/)
- [Microsoft GFlags Mar 2017](https://docs.microsoft.com/windows-hardware/drivers/debugger/gflags-overview)
- [Microsoft Silent Process Exit NOV 2017](https://docs.microsoft.com/windows-hardware/drivers/debugger/registry-entries-for-silent-process-exit)
- [Oddvar Moe IFEO APR 2018](https://oddvar.moe/2018/04/10/persistence-using-globalflags-in-image-file-execution-options-hidden-from-autoruns-exe/)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [FSecure Hupigon](https://www.f-secure.com/v-descs/backdoor_w32_hupigon_emv.shtml)
- [Symantec Ushedix June 2008](https://www.symantec.com/security_response/writeup.jsp?docid=2008-062807-2501-99&tabid=2)
