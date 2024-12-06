---
data_sources:
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Modification'
- 'Module: Module Load'
id: attack-pattern--b8cfed42-6a8a-4989-ad72-541af74475ec
mitre_attack_url: https://attack.mitre.org/techniques/T1547/002
name: Authentication Package
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Authentication Package
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Windows Registry: Windows Registry Key Modification, Module: Module Load |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/002](https://attack.mitre.org/techniques/T1547/002) |

# Authentication Package (attack-pattern--b8cfed42-6a8a-4989-ad72-541af74475ec)

## Description
Adversaries may abuse authentication packages to execute DLLs when the system boots. Windows authentication package DLLs are loaded by the Local Security Authority (LSA) process at system start. They provide support for multiple logon processes and multiple security protocols to the operating system.(Citation: MSDN Authentication Packages)

Adversaries can use the autostart mechanism provided by LSA authentication packages for persistence by placing a reference to a binary in the Windows Registry location <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\</code> with the key value of <code>"Authentication Packages"=&lt;target binary&gt;</code>. The binary will then be executed by the system when the authentication packages are loaded.

## Detection
Monitor the Registry for changes to the LSA Registry keys. Monitor the LSA process for DLL loads. Windows 8.1 and Windows Server 2012 R2 may generate events when unsigned DLLs try to load into the LSA by setting the Registry key <code>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\LSASS.exe</code> with AuditLevel = 8. (Citation: Graeber 2014) (Citation: Microsoft Configure LSA)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/002)
- [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)
- [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)
- [MSDN Authentication Packages](https://msdn.microsoft.com/library/windows/desktop/aa374733.aspx)
