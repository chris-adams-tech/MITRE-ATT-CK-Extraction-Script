---
contributors:
- Stefan Kanthak
- Travis Smith, Tripwire
- "Harun K\xFC\xDFner"
data_sources:
- 'Windows Registry: Windows Registry Key Modification'
- 'File: File Creation'
- 'Module: Module Load'
- 'Process: OS API Execution'
id: attack-pattern--43881e51-ac74-445b-b4c6-f9f9e9bf23fe
mitre_attack_url: https://attack.mitre.org/techniques/T1547/010
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
| **Data Sources** | Windows Registry: Windows Registry Key Modification, File: File Creation, Module: Module Load, Process: OS API Execution |
| **Permissions Required** | SYSTEM, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/010](https://attack.mitre.org/techniques/T1547/010) |

# Port Monitors (attack-pattern--43881e51-ac74-445b-b4c6-f9f9e9bf23fe)

## Description
Adversaries may use port monitors to run an adversary supplied DLL during system boot for persistence or privilege escalation. A port monitor can be set through the <code>AddMonitor</code> API call to set a DLL to be loaded at startup.(Citation: AddMonitor) This DLL can be located in <code>C:\Windows\System32</code> and will be loaded and run by the print spooler service, `spoolsv.exe`, under SYSTEM level permissions on boot.(Citation: Bloxham) 

Alternatively, an arbitrary DLL can be loaded if permissions allow writing a fully-qualified pathname for that DLL to the `Driver` value of an existing or new arbitrarily named subkey of <code>HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors</code>. The Registry key contains entries for the following:

* Local Port
* Standard TCP/IP Port
* USB Monitor
* WSD Port


## Detection
Monitor process API calls to <code>AddMonitor</code>.(Citation: AddMonitor) Monitor DLLs that are loaded by spoolsv.exe for DLLs that are abnormal. New DLLs written to the System32 directory that do not correlate with known good software or patching may be suspicious. 

Monitor Registry writes to <code>HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors</code>, paying particular attention to changes in the "Driver" subkey. Run the Autoruns utility, which checks for this Registry key as a persistence mechanism.(Citation: TechNet Autoruns)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/010)
- [Bloxham](https://www.defcon.org/images/defcon-22/dc-22-presentations/Bloxham/DEFCON-22-Brady-Bloxham-Windows-API-Abuse-UPDATED.pdf)
- [AddMonitor](https://learn.microsoft.com/en-us/windows/win32/printdocs/addmonitor)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
