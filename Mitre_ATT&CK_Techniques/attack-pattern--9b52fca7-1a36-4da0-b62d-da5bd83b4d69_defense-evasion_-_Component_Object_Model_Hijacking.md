---
contributors:
- ENDGAME
id: attack-pattern--9b52fca7-1a36-4da0-b62d-da5bd83b4d69
mitre_attack_url: https://attack.mitre.org/techniques/T1122
name: Component Object Model Hijacking
platforms:
- Windows
tactics:
- defense-evasion
- persistence
title: defense-evasion - Component Object Model Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence |
| **Platforms** | Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1122](https://attack.mitre.org/techniques/T1122) |

# Component Object Model Hijacking (attack-pattern--9b52fca7-1a36-4da0-b62d-da5bd83b4d69)

## Description
The Component Object Model (COM) is a system within Windows to enable interaction between software components through the operating system. (Citation: Microsoft Component Object Model) Adversaries can use this system to insert malicious code that can be executed in place of legitimate software through hijacking the COM references and relationships as a means for persistence. Hijacking a COM object requires a change in the Windows Registry to replace a reference to a legitimate system component which may cause that component to not work when executed. When that system component is executed through normal system operation the adversary's code will be executed instead. (Citation: GDATA COM Hijacking) An adversary is likely to hijack objects that are used frequently enough to maintain a consistent level of persistence, but are unlikely to break noticeable functionality within the system as to avoid system instability that could lead to detection.

## Detection
There are opportunities to detect COM hijacking by searching for Registry references that have been replaced and through Registry operations replacing know binary paths with unknown paths. Even though some third party applications define user COM objects, the presence of objects within <code>HKEY_CURRENT_USER\Software\Classes\CLSID\</code> may be anomalous and should be investigated since user objects will be loaded prior to machine objects in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\</code>. (Citation: Elastic COM Hijacking) Registry entries for existing COM objects may change infrequently. When an entry with a known good path and binary is replaced or changed to an unusual value to point to an unknown binary in a new location, then it may indicate suspicious behavior and should be investigated. Likewise, if software DLL loads are collected and analyzed, any unusual DLL load that can be correlated with a COM object Registry modification may indicate COM hijacking has been performed.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1122)
- [Microsoft Component Object Model](https://msdn.microsoft.com/library/ms694363.aspx)
- [GDATA COM Hijacking](https://blog.gdatasoftware.com/2014/10/23941-com-object-hijacking-the-discreet-way-of-persistence)
- [Elastic COM Hijacking](https://www.elastic.co/blog/how-hunt-detecting-persistence-evasion-com)
