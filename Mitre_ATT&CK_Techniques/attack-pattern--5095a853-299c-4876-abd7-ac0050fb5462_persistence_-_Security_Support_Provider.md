---
data_sources:
- 'Command: Command Execution'
- 'Module: Module Load'
- 'Windows Registry: Windows Registry Key Modification'
id: attack-pattern--5095a853-299c-4876-abd7-ac0050fb5462
mitre_attack_url: https://attack.mitre.org/techniques/T1547/005
name: Security Support Provider
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Security Support Provider
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Module: Module Load, Windows Registry: Windows Registry Key Modification |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/005](https://attack.mitre.org/techniques/T1547/005) |

# Security Support Provider (attack-pattern--5095a853-299c-4876-abd7-ac0050fb5462)

## Description
Adversaries may abuse security support providers (SSPs) to execute DLLs when the system boots. Windows SSP DLLs are loaded into the Local Security Authority (LSA) process at system start. Once loaded into the LSA, SSP DLLs have access to encrypted and plaintext passwords that are stored in Windows, such as any logged-on user's Domain password or smart card PINs.

The SSP configuration is stored in two Registry keys: <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages</code> and <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages</code>. An adversary may modify these Registry keys to add new SSPs, which will be loaded the next time the system boots, or when the AddSecurityPackage Windows API function is called.(Citation: Graeber 2014)

## Detection
Monitor the Registry for changes to the SSP Registry keys. Monitor the LSA process for DLL loads. Windows 8.1 and Windows Server 2012 R2 may generate events when unsigned SSP DLLs try to load into the LSA by setting the Registry key <code>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\LSASS.exe</code> with AuditLevel = 8. (Citation: Graeber 2014) (Citation: Microsoft Configure LSA)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/005)
- [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)
- [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)
