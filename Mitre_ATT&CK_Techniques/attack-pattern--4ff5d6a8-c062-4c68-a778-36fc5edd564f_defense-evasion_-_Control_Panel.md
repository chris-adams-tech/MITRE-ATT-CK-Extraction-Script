---
contributors:
- ESET
data_sources:
- 'File: File Creation'
- 'Module: Module Load'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
- 'Process: OS API Execution'
- 'Process: Process Creation'
id: attack-pattern--4ff5d6a8-c062-4c68-a778-36fc5edd564f
mitre_attack_url: https://attack.mitre.org/techniques/T1218/002
name: Control Panel
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Control Panel
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | File: File Creation, Module: Module Load, Windows Registry: Windows Registry Key Modification, Command: Command Execution, Process: OS API Execution, Process: Process Creation |
| **Permissions Required** | User, Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/002](https://attack.mitre.org/techniques/T1218/002) |

# Control Panel (attack-pattern--4ff5d6a8-c062-4c68-a778-36fc5edd564f)

## Description
Adversaries may abuse control.exe to proxy execution of malicious payloads. The Windows Control Panel process binary (control.exe) handles execution of Control Panel items, which are utilities that allow users to view and adjust computer settings.

Control Panel items are registered executable (.exe) or Control Panel (.cpl) files, the latter are actually renamed dynamic-link library (.dll) files that export a <code>CPlApplet</code> function.(Citation: Microsoft Implementing CPL)(Citation: TrendMicro CPL Malware Jan 2014) For ease of use, Control Panel items typically include graphical menus available to users after being registered and loaded into the Control Panel.(Citation: Microsoft Implementing CPL) Control Panel items can be executed directly from the command line, programmatically via an application programming interface (API) call, or by simply double-clicking the file.(Citation: Microsoft Implementing CPL) (Citation: TrendMicro CPL Malware Jan 2014)(Citation: TrendMicro CPL Malware Dec 2013)

Malicious Control Panel items can be delivered via [Phishing](https://attack.mitre.org/techniques/T1566) campaigns(Citation: TrendMicro CPL Malware Jan 2014)(Citation: TrendMicro CPL Malware Dec 2013) or executed as part of multi-stage malware.(Citation: Palo Alto Reaver Nov 2017) Control Panel items, specifically CPL files, may also bypass application and/or file extension allow lists.

Adversaries may also rename malicious DLL files (.dll) with Control Panel file extensions (.cpl) and register them to <code>HKCU\Software\Microsoft\Windows\CurrentVersion\Control Panel\Cpls</code>. Even when these registered DLLs do not comply with the CPL file specification and do not export <code>CPlApplet</code> functions, they are loaded and executed through its <code>DllEntryPoint</code> when Control Panel is executed. CPL files not exporting <code>CPlApplet</code> are not directly executable.(Citation: ESET InvisiMole June 2020)

## Detection
Monitor and analyze activity related to items associated with CPL files, such as the control.exe and the <code>Control_RunDLL</code> and <code>ControlRunDLLAsUser</code> API functions in shell32.dll. When executed from the command line or clicked, control.exe will execute the CPL file (ex: <code>control.exe file.cpl</code>) before [Rundll32](https://attack.mitre.org/techniques/T1218/011) is used to call the CPL's API functions (ex: <code>rundll32.exe shell32.dll,Control_RunDLL file.cpl</code>). CPL files can be executed directly via the CPL API function with just the latter [Rundll32](https://attack.mitre.org/techniques/T1218/011) command, which may bypass detections and/or execution filters for control.exe.(Citation: TrendMicro CPL Malware Jan 2014)

Inventory Control Panel items to locate unregistered and potentially malicious files present on systems:

* Executable format registered Control Panel items will have a globally unique identifier (GUID) and registration Registry entries in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel\NameSpace</code> and <code>HKEY_CLASSES_ROOT\CLSID\{GUID}</code>. These entries may contain information about the Control Panel item such as its display name, path to the local file, and the command executed when opened in the Control Panel. (Citation: Microsoft Implementing CPL)
* CPL format registered Control Panel items stored in the System32 directory are automatically shown in the Control Panel. Other Control Panel items will have registration entries in the <code>CPLs</code> and <code>Extended Properties</code> Registry keys of <code>HKEY_LOCAL_MACHINE or HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Control Panel</code>. These entries may include information such as a GUID, path to the local file, and a canonical name used to launch the file programmatically (<code> WinExec("c:\windows\system32\control.exe {Canonical_Name}", SW_NORMAL);</code>) or from a command line (<code>control.exe /name {Canonical_Name}</code>).(Citation: Microsoft Implementing CPL)
* Some Control Panel items are extensible via Shell extensions registered in <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Controls Folder\{name}\Shellex\PropertySheetHandlers</code> where {name} is the predefined name of the system item.(Citation: Microsoft Implementing CPL)

Analyze new Control Panel items as well as those present on disk for malicious content. Both executable and CPL formats are compliant Portable Executable (PE) images and can be examined using traditional tools and methods, pending anti-reverse-engineering techniques.(Citation: TrendMicro CPL Malware Jan 2014)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/002)
- [Microsoft Implementing CPL](https://msdn.microsoft.com/library/windows/desktop/cc144185.aspx)
- [TrendMicro CPL Malware Jan 2014](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp-cpl-malware.pdf)
- [TrendMicro CPL Malware Dec 2013](https://blog.trendmicro.com/trendlabs-security-intelligence/control-panel-files-used-as-malicious-attachments/)
- [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
- [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
