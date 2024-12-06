---
contributors:
- Wayne Silva, F-Secure Countercept
data_sources:
- 'Process: Process Creation'
- 'Process: OS API Execution'
- 'Process: Process Metadata'
id: attack-pattern--93591901-3172-4e94-abf8-6034ab26f44a
mitre_attack_url: https://attack.mitre.org/techniques/T1134/004
name: Parent PID Spoofing
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Parent PID Spoofing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Process: OS API Execution, Process: Process Metadata |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1134/004](https://attack.mitre.org/techniques/T1134/004) |

# Parent PID Spoofing (attack-pattern--93591901-3172-4e94-abf8-6034ab26f44a)

## Description
Adversaries may spoof the parent process identifier (PPID) of a new process to evade process-monitoring defenses or to elevate privileges. New processes are typically spawned directly from their parent, or calling, process unless explicitly specified. One way of explicitly assigning the PPID of a new process is via the <code>CreateProcess</code> API call, which supports a parameter that defines the PPID to use.(Citation: DidierStevens SelectMyParent Nov 2009) This functionality is used by Windows features such as User Account Control (UAC) to correctly set the PPID after a requested elevated process is spawned by SYSTEM (typically via <code>svchost.exe</code> or <code>consent.exe</code>) rather than the current user context.(Citation: Microsoft UAC Nov 2018)

Adversaries may abuse these mechanisms to evade defenses, such as those blocking processes spawning directly from Office documents, and analysis targeting unusual/potentially malicious parent-child process relationships, such as spoofing the PPID of [PowerShell](https://attack.mitre.org/techniques/T1059/001)/[Rundll32](https://attack.mitre.org/techniques/T1218/011) to be <code>explorer.exe</code> rather than an Office document delivered as part of [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001).(Citation: CounterCept PPID Spoofing Dec 2018) This spoofing could be executed via [Visual Basic](https://attack.mitre.org/techniques/T1059/005) within a malicious Office document or any code that can perform [Native API](https://attack.mitre.org/techniques/T1106).(Citation: CTD PPID Spoofing Macro Mar 2019)(Citation: CounterCept PPID Spoofing Dec 2018)

Explicitly assigning the PPID may also enable elevated privileges given appropriate access rights to the parent process. For example, an adversary in a privileged user context (i.e. administrator) may spawn a new process and assign the parent as a process running as SYSTEM (such as <code>lsass.exe</code>), causing the new process to be elevated via the inherited access token.(Citation: XPNSec PPID Nov 2017)

## Detection
Look for inconsistencies between the various fields that store PPID information, such as the EventHeader ProcessId from data collected via Event Tracing for Windows (ETW), Creator Process ID/Name from Windows event logs, and the ProcessID and ParentProcessID (which are also produced from ETW and other utilities such as Task Manager and Process Explorer). The ETW provided EventHeader ProcessId identifies the actual parent process.(Citation: CounterCept PPID Spoofing Dec 2018)

Monitor and analyze API calls to <code>CreateProcess</code>/<code>CreateProcessA</code>, specifically those from user/potentially malicious processes and with parameters explicitly assigning PPIDs (ex: the Process Creation Flags of 0x8XXX, indicating that the process is being created with extended startup information(Citation: Microsoft Process Creation Flags May 2018)). Malicious use of <code>CreateProcess</code>/<code>CreateProcessA</code> may also be proceeded by a call to <code>UpdateProcThreadAttribute</code>, which may be necessary to update process creation attributes.(Citation: Secuirtyinbits Ataware3 May 2019) This may generate false positives from normal UAC elevation behavior, so compare to a system baseline/understanding of normal system activity if possible.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1134/004)
- [XPNSec PPID Nov 2017](https://blog.xpnsec.com/becoming-system/)
- [CounterCept PPID Spoofing Dec 2018](https://www.countercept.com/blog/detecting-parent-pid-spoofing/)
- [Microsoft UAC Nov 2018](https://docs.microsoft.com/windows/security/identity-protection/user-account-control/how-user-account-control-works)
- [Microsoft Process Creation Flags May 2018](https://docs.microsoft.com/windows/desktop/ProcThread/process-creation-flags)
- [Secuirtyinbits Ataware3 May 2019](https://www.securityinbits.com/malware-analysis/parent-pid-spoofing-stage-2-ataware-ransomware-part-3)
- [DidierStevens SelectMyParent Nov 2009](https://blog.didierstevens.com/2009/11/22/quickpost-selectmyparent-or-playing-with-the-windows-process-tree/)
- [CTD PPID Spoofing Macro Mar 2019](https://blog.christophetd.fr/building-an-office-macro-to-spoof-process-parent-and-command-line/)
