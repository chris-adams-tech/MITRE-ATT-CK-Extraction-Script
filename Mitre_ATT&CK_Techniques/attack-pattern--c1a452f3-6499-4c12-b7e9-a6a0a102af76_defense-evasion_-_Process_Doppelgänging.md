---
id: attack-pattern--c1a452f3-6499-4c12-b7e9-a6a0a102af76
mitre_attack_url: https://attack.mitre.org/techniques/T1186
name: "Process Doppelg\xE4nging"
platforms:
- Windows
tactics:
- defense-evasion
title: "defense-evasion - Process Doppelg\xE4nging"
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1186](https://attack.mitre.org/techniques/T1186) |

# Process Doppelgänging (attack-pattern--c1a452f3-6499-4c12-b7e9-a6a0a102af76)

## Description
Windows Transactional NTFS (TxF) was introduced in Vista as a method to perform safe file operations. (Citation: Microsoft TxF) To ensure data integrity, TxF enables only one transacted handle to write to a file at a given time. Until the write handle transaction is terminated, all other handles are isolated from the writer and may only read the committed version of the file that existed at the time the handle was opened. (Citation: Microsoft Basic TxF Concepts) To avoid corruption, TxF performs an automatic rollback if the system or application fails during a write transaction. (Citation: Microsoft Where to use TxF)

Although deprecated, the TxF application programming interface (API) is still enabled as of Windows 10. (Citation: BlackHat Process Doppelgänging Dec 2017)

Adversaries may leverage TxF to a perform a file-less variation of [Process Injection](https://attack.mitre.org/techniques/T1055) called Process Doppelgänging. Similar to [Process Hollowing](https://attack.mitre.org/techniques/T1093), Process Doppelgänging involves replacing the memory of a legitimate process, enabling the veiled execution of malicious code that may evade defenses and detection. Process Doppelgänging's use of TxF also avoids the use of highly-monitored API functions such as NtUnmapViewOfSection, VirtualProtectEx, and SetThreadContext. (Citation: BlackHat Process Doppelgänging Dec 2017)

Process Doppelgänging is implemented in 4 steps (Citation: BlackHat Process Doppelgänging Dec 2017):

* Transact – Create a TxF transaction using a legitimate executable then overwrite the file with malicious code. These changes will be isolated and only visible within the context of the transaction.
* Load – Create a shared section of memory and load the malicious executable.
* Rollback – Undo changes to original executable, effectively removing malicious code from the file system.
* Animate – Create a process from the tainted section of memory and initiate execution.

## Detection
Monitor and analyze calls to CreateTransaction, CreateFileTransacted, RollbackTransaction, and other rarely used functions indicative of TxF activity. Process Doppelgänging also invokes an outdated and undocumented implementation of the Windows process loader via calls to NtCreateProcessEx and NtCreateThreadEx as well as API calls used to modify memory within another process, such as WriteProcessMemory. (Citation: BlackHat Process Doppelgänging Dec 2017) (Citation: hasherezade Process Doppelgänging Dec 2017)

Scan file objects reported during the PsSetCreateProcessNotifyRoutine, (Citation: Microsoft PsSetCreateProcessNotifyRoutine routine) which triggers a callback whenever a process is created or deleted, specifically looking for file objects with enabled write access. (Citation: BlackHat Process Doppelgänging Dec 2017) Also consider comparing file objects loaded in memory to the corresponding file on disk. (Citation: hasherezade Process Doppelgänging Dec 2017)

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1186)
- [Microsoft TxF](https://msdn.microsoft.com/library/windows/desktop/bb968806.aspx)
- [Microsoft Basic TxF Concepts](https://msdn.microsoft.com/library/windows/desktop/dd979526.aspx)
- [Microsoft Where to use TxF](https://msdn.microsoft.com/library/windows/desktop/aa365738.aspx)
- [BlackHat Process Doppelgänging Dec 2017](https://www.blackhat.com/docs/eu-17/materials/eu-17-Liberman-Lost-In-Transaction-Process-Doppelganging.pdf)
- [hasherezade Process Doppelgänging Dec 2017](https://hshrzd.wordpress.com/2017/12/18/process-doppelganging-a-new-way-to-impersonate-a-process/)
- [Microsoft PsSetCreateProcessNotifyRoutine routine](https://msdn.microsoft.com/library/windows/hardware/ff559951.aspx)
