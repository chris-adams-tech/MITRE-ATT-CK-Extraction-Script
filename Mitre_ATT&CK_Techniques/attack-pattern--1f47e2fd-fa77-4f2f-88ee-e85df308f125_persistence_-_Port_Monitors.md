---
contributors:
- Stefan Kanthak
- Travis Smith, Tripwire
id: attack-pattern--1f47e2fd-fa77-4f2f-88ee-e85df308f125
mitre_attack_url: https://attack.mitre.org/techniques/T1013
name: Port Monitors
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Port Monitors
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1013](https://attack.mitre.org/techniques/T1013) |

# Port Monitors (attack-pattern--1f47e2fd-fa77-4f2f-88ee-e85df308f125)

## Description
A port monitor can be set through the  (Citation: AddMonitor) API call to set a DLL to be loaded at startup. (Citation: AddMonitor) This DLL can be located in <code>C:\Windows\System32</code> and will be loaded by the print spooler service, spoolsv.exe, on boot. The spoolsv.exe process also runs under SYSTEM level permissions. (Citation: Bloxham) Alternatively, an arbitrary DLL can be loaded if permissions allow writing a fully-qualified pathname for that DLL to <code>HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors</code>. 

The Registry key contains entries for the following:

* Local Port
* Standard TCP/IP Port
* USB Monitor
* WSD Port

Adversaries can use this technique to load malicious code at startup that will persist on system reboot and execute as SYSTEM.

## Detection
* Monitor process API calls to  (Citation: AddMonitor).
* Monitor DLLs that are loaded by spoolsv.exe for DLLs that are abnormal.
* New DLLs written to the System32 directory that do not correlate with known good software or patching may be suspicious.
* Monitor Registry writes to <code>HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors</code>.
* Run the Autoruns utility, which checks for this Registry key as a persistence mechanism (Citation: TechNet Autoruns)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1013)
- [AddMonitor](http://msdn.microsoft.com/en-us/library/dd183341)
- [Bloxham](https://www.defcon.org/images/defcon-22/dc-22-presentations/Bloxham/DEFCON-22-Brady-Bloxham-Windows-API-Abuse-UPDATED.pdf)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
