---
id: attack-pattern--772bc7a8-a157-42cc-8728-d648e25c7fe7
mitre_attack_url: https://attack.mitre.org/techniques/T1175
name: Component Object Model and Distributed COM
platforms:
- Windows
tactics:
- lateral-movement
- execution
title: lateral-movement - Component Object Model and Distributed COM
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement, execution |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1175](https://attack.mitre.org/techniques/T1175) |

# Component Object Model and Distributed COM (attack-pattern--772bc7a8-a157-42cc-8728-d648e25c7fe7)

## Description
**This technique has been deprecated. Please use [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) and [Component Object Model](https://attack.mitre.org/techniques/T1559/001).**

Adversaries may use the Windows Component Object Model (COM) and Distributed Component Object Model (DCOM) for local code execution or to execute on remote systems as part of lateral movement. 

COM is a component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more interfaces.(Citation: Fireeye Hunting COM June 2019) Through COM, a client object can call methods of server objects, which are typically Dynamic Link Libraries (DLL) or executables (EXE).(Citation: Microsoft COM) DCOM is transparent middleware that extends the functionality of Component Object Model (COM) (Citation: Microsoft COM) beyond a local computer using remote procedure call (RPC) technology.(Citation: Fireeye Hunting COM June 2019)

Permissions to interact with local and remote server COM objects are specified by access control lists (ACL) in the Registry. (Citation: Microsoft COM ACL)(Citation: Microsoft Process Wide Com Keys)(Citation: Microsoft System Wide Com Keys) By default, only Administrators may remotely activate and launch COM objects through DCOM.

Adversaries may abuse COM for local command and/or payload execution. Various COM interfaces are exposed that can be abused to invoke arbitrary execution via a variety of programming languages such as C, C++, Java, and VBScript.(Citation: Microsoft COM) Specific COM objects also exists to directly perform functions beyond code execution, such as creating a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), fileless download/execution, and other adversary behaviors such as Privilege Escalation and Persistence.(Citation: Fireeye Hunting COM June 2019)(Citation: ProjectZero File Write EoP Apr 2018)

Adversaries may use DCOM for lateral movement. Through DCOM, adversaries operating in the context of an appropriately privileged user can remotely obtain arbitrary and even direct shellcode execution through Office applications (Citation: Enigma Outlook DCOM Lateral Movement Nov 2017) as well as other Windows objects that contain insecure methods.(Citation: Enigma MMC20 COM Jan 2017)(Citation: Enigma DCOM Lateral Movement Jan 2017) DCOM can also execute macros in existing documents (Citation: Enigma Excel DCOM Sept 2017) and may also invoke [Dynamic Data Exchange](https://attack.mitre.org/techniques/T1173) (DDE) execution directly through a COM created instance of a Microsoft Office application (Citation: Cyberreason DCOM DDE Lateral Movement Nov 2017), bypassing the need for a malicious document.

## Detection
Monitor for COM objects loading DLLs and other modules not typically associated with the application.(Citation: Enigma Outlook DCOM Lateral Movement Nov 2017) Enumeration of COM objects, via [Query Registry](https://attack.mitre.org/techniques/T1012) or [PowerShell](https://attack.mitre.org/techniques/T1086), may also proceed malicious use.(Citation: Fireeye Hunting COM June 2019)(Citation: Enigma MMC20 COM Jan 2017)

Monitor for spawning of processes associated with COM objects, especially those invoked by a user different than the one currently logged on.

Monitor for any influxes or abnormal increases in Distributed Computing Environment/Remote Procedure Call (DCE/RPC) traffic.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1175)
- [Fireeye Hunting COM June 2019](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)
- [Microsoft COM](https://msdn.microsoft.com/library/windows/desktop/ms680573.aspx)
- [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)
- [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)
- [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)
- [ProjectZero File Write EoP Apr 2018](https://googleprojectzero.blogspot.com/2018/04/windows-exploitation-tricks-exploiting.html)
- [Enigma Outlook DCOM Lateral Movement Nov 2017](https://enigma0x3.net/2017/11/16/lateral-movement-using-outlooks-createobject-method-and-dotnettojscript/)
- [Enigma MMC20 COM Jan 2017](https://enigma0x3.net/2017/01/05/lateral-movement-using-the-mmc20-application-com-object/)
- [Enigma DCOM Lateral Movement Jan 2017](https://enigma0x3.net/2017/01/23/lateral-movement-via-dcom-round-2/)
- [Enigma Excel DCOM Sept 2017](https://enigma0x3.net/2017/09/11/lateral-movement-using-excel-application-and-dcom/)
- [Cyberreason DCOM DDE Lateral Movement Nov 2017](https://www.cybereason.com/blog/leveraging-excel-dde-for-lateral-movement-via-dcom)
