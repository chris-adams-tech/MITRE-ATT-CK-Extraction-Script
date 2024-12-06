---
id: attack-pattern--c3bce4f4-9795-46c6-976e-8676300bbc39
mitre_attack_url: https://attack.mitre.org/techniques/T1028
name: Windows Remote Management
platforms:
- Windows
tactics:
- execution
- lateral-movement
title: execution - Windows Remote Management
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, lateral-movement |
| **Platforms** | Windows |
| **Permissions Required** | User, Administrator |
| **System Requirements** | WinRM listener turned on and configured on remote system |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1028](https://attack.mitre.org/techniques/T1028) |

# Windows Remote Management (attack-pattern--c3bce4f4-9795-46c6-976e-8676300bbc39)

## Description
Windows Remote Management (WinRM) is the name of both a Windows service and a protocol that allows a user to interact with a remote system (e.g., run an executable, modify the Registry, modify services). (Citation: Microsoft WinRM) It may be called with the <code>winrm</code> command or by any number of programs such as PowerShell. (Citation: Jacobsen 2014)

## Detection
Monitor use of WinRM within an environment by tracking service execution. If it is not normally used or is disabled, then this may be an indicator of suspicious behavior. Monitor processes created and actions taken by the WinRM process or a WinRM invoked script to correlate it with other related events. (Citation: Medium Detecting Lateral Movement)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1028)
- [capec](https://capec.mitre.org/data/definitions/555.html)
- [Microsoft WinRM](http://msdn.microsoft.com/en-us/library/aa384426)
- [Jacobsen 2014](https://www.slideshare.net/kieranjacobsen/lateral-movement-with-power-shell-2)
- [Medium Detecting Lateral Movement](https://medium.com/threatpunter/detecting-lateral-movement-using-sysmon-and-splunk-318d3be141bc)
