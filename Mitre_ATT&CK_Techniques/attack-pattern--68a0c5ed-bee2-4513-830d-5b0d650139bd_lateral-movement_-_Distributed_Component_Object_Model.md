---
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Module: Module Load'
- 'Process: Process Creation'
id: attack-pattern--68a0c5ed-bee2-4513-830d-5b0d650139bd
mitre_attack_url: https://attack.mitre.org/techniques/T1021/003
name: Distributed Component Object Model
platforms:
- Windows
tactics:
- lateral-movement
title: lateral-movement - Distributed Component Object Model
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows |
| **Data Sources** | Network Traffic: Network Connection Creation, Module: Module Load, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1021/003](https://attack.mitre.org/techniques/T1021/003) |

# Distributed Component Object Model (attack-pattern--68a0c5ed-bee2-4513-830d-5b0d650139bd)

## Description
Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with remote machines by taking advantage of Distributed Component Object Model (DCOM). The adversary may then perform actions as the logged-on user.

The Windows Component Object Model (COM) is a component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more interfaces. Through COM, a client object can call methods of server objects, which are typically Dynamic Link Libraries (DLL) or executables (EXE). Distributed COM (DCOM) is transparent middleware that extends the functionality of COM beyond a local computer using remote procedure call (RPC) technology.(Citation: Fireeye Hunting COM June 2019)(Citation: Microsoft COM)

Permissions to interact with local and remote server COM objects are specified by access control lists (ACL) in the Registry.(Citation: Microsoft Process Wide Com Keys) By default, only Administrators may remotely activate and launch COM objects through DCOM.(Citation: Microsoft COM ACL)

Through DCOM, adversaries operating in the context of an appropriately privileged user can remotely obtain arbitrary and even direct shellcode execution through Office applications(Citation: Enigma Outlook DCOM Lateral Movement Nov 2017) as well as other Windows objects that contain insecure methods.(Citation: Enigma MMC20 COM Jan 2017)(Citation: Enigma DCOM Lateral Movement Jan 2017) DCOM can also execute macros in existing documents(Citation: Enigma Excel DCOM Sept 2017) and may also invoke [Dynamic Data Exchange](https://attack.mitre.org/techniques/T1559/002) (DDE) execution directly through a COM created instance of a Microsoft Office application(Citation: Cyberreason DCOM DDE Lateral Movement Nov 2017), bypassing the need for a malicious document. DCOM can be used as a method of remotely interacting with [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047). (Citation: MSDN WMI)

## Detection
Monitor for COM objects loading DLLs and other modules not typically associated with the application.(Citation: Enigma Outlook DCOM Lateral Movement Nov 2017) Enumeration of COM objects, via [Query Registry](https://attack.mitre.org/techniques/T1012) or [PowerShell](https://attack.mitre.org/techniques/T1059/001), may also proceed malicious use.(Citation: Fireeye Hunting COM June 2019)(Citation: Enigma MMC20 COM Jan 2017) Monitor for spawning of processes associated with COM objects, especially those invoked by a user different than the one currently logged on.

Monitor for any influxes or abnormal increases in DCOM related Distributed Computing Environment/Remote Procedure Call (DCE/RPC) traffic (typically over port 135).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1021/003)
- [Fireeye Hunting COM June 2019](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)
- [Microsoft COM](https://msdn.microsoft.com/library/windows/desktop/ms680573.aspx)
- [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)
- [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)
- [MSDN WMI](https://msdn.microsoft.com/en-us/library/aa394582.aspx)
- [Enigma DCOM Lateral Movement Jan 2017](https://enigma0x3.net/2017/01/23/lateral-movement-via-dcom-round-2/)
- [Enigma MMC20 COM Jan 2017](https://enigma0x3.net/2017/01/05/lateral-movement-using-the-mmc20-application-com-object/)
- [Enigma Outlook DCOM Lateral Movement Nov 2017](https://enigma0x3.net/2017/11/16/lateral-movement-using-outlooks-createobject-method-and-dotnettojscript/)
- [Enigma Excel DCOM Sept 2017](https://enigma0x3.net/2017/09/11/lateral-movement-using-excel-application-and-dcom/)
- [Cyberreason DCOM DDE Lateral Movement Nov 2017](https://www.cybereason.com/blog/leveraging-excel-dde-for-lateral-movement-via-dcom)
