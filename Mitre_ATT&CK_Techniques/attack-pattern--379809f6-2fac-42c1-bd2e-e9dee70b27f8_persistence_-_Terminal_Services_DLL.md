---
data_sources:
- 'Module: Module Load'
- 'Command: Command Execution'
- 'File: File Modification'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Creation'
id: attack-pattern--379809f6-2fac-42c1-bd2e-e9dee70b27f8
mitre_attack_url: https://attack.mitre.org/techniques/T1505/005
name: Terminal Services DLL
platforms:
- Windows
tactics:
- persistence
title: persistence - Terminal Services DLL
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Data Sources** | Module: Module Load, Command: Command Execution, File: File Modification, Windows Registry: Windows Registry Key Modification, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1505/005](https://attack.mitre.org/techniques/T1505/005) |

# Terminal Services DLL (attack-pattern--379809f6-2fac-42c1-bd2e-e9dee70b27f8)

## Description
Adversaries may abuse components of Terminal Services to enable persistent access to systems. Microsoft Terminal Services, renamed to Remote Desktop Services in some Windows Server OSs as of 2022, enable remote terminal connections to hosts. Terminal Services allows servers to transmit a full, interactive, graphical user interface to clients via RDP.(Citation: Microsoft Remote Desktop Services)

[Windows Service](https://attack.mitre.org/techniques/T1543/003)s that are run as a "generic" process (ex: <code>svchost.exe</code>) load the service's DLL file, the location of which is stored in a Registry entry named <code>ServiceDll</code>.(Citation: Microsoft System Services Fundamentals) The <code>termsrv.dll</code> file, typically stored in `%SystemRoot%\System32\`, is the default <code>ServiceDll</code> value for Terminal Services in `HKLM\System\CurrentControlSet\services\TermService\Parameters\`.

Adversaries may modify and/or replace the Terminal Services DLL to enable persistent access to victimized hosts.(Citation: James TermServ DLL) Modifications to this DLL could be done to execute arbitrary payloads (while also potentially preserving normal <code>termsrv.dll</code> functionality) as well as to simply enable abusable features of Terminal Services. For example, an adversary may enable features such as concurrent [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001) sessions by either patching the <code>termsrv.dll</code> file or modifying the <code>ServiceDll</code> value to point to a DLL that provides increased RDP functionality.(Citation: Windows OS Hub RDP)(Citation: RDPWrap Github) On a non-server Windows OS this increased functionality may also enable an adversary to avoid Terminal Services prompts that warn/log out users of a system when a new RDP session is created.

## Detection
Monitor for changes to Registry keys associated with <code>ServiceDll</code> and other subkey values under <code>HKLM\System\CurrentControlSet\services\TermService\Parameters\</code>.

Monitor unexpected changes and/or interactions with <code>termsrv.dll</code>, which is typically stored in <code>%SystemRoot%\System32\</code>.

Monitor commands as well as  processes and arguments for potential adversary actions to modify Registry values (ex: <code>reg.exe</code>) or modify/replace the legitimate <code>termsrv.dll</code>.

Monitor module loads by the Terminal Services process (ex: <code>svchost.exe -k termsvcs</code>) for unexpected DLLs (the default is <code>%SystemRoot%\System32\termsrv.dll</code>, though an adversary could also use [Match Legitimate Name or Location](https://attack.mitre.org/techniques/T1036/005) on a malicious payload).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1505/005)
- [James TermServ DLL](https://x.com/james_inthe_box/status/1150495335812177920)
- [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)
- [Microsoft Remote Desktop Services](https://docs.microsoft.com/windows/win32/termserv/about-terminal-services)
- [RDPWrap Github](https://github.com/stascorp/rdpwrap)
- [Windows OS Hub RDP](http://woshub.com/how-to-allow-multiple-rdp-sessions-in-windows-10/)
