---
contributors:
- Scott Lundgren, @5twenty9, Carbon Black
- "Harun K\xFC\xDFner"
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Modification'
- 'Module: Module Load'
id: attack-pattern--61afc315-860c-4364-825d-0d62b2e91edc
mitre_attack_url: https://attack.mitre.org/techniques/T1547/003
name: Time Providers
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Time Providers
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution, Windows Registry: Windows Registry Key Modification, Module: Module Load |
| **Permissions Required** | SYSTEM, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/003](https://attack.mitre.org/techniques/T1547/003) |

# Time Providers (attack-pattern--61afc315-860c-4364-825d-0d62b2e91edc)

## Description
Adversaries may abuse time providers to execute DLLs when the system boots. The Windows Time service (W32Time) enables time synchronization across and within domains.(Citation: Microsoft W32Time Feb 2018) W32Time time providers are responsible for retrieving time stamps from hardware/network resources and outputting these values to other network clients.(Citation: Microsoft TimeProvider)

Time providers are implemented as dynamic-link libraries (DLLs) that are registered in the subkeys of `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\W32Time\TimeProviders\`.(Citation: Microsoft TimeProvider) The time provider manager, directed by the service control manager, loads and starts time providers listed and enabled under this key at system startup and/or whenever parameters are changed.(Citation: Microsoft TimeProvider)

Adversaries may abuse this architecture to establish persistence, specifically by creating a new arbitrarily named subkey  pointing to a malicious DLL in the `DllName` value. Administrator privileges are required for time provider registration, though execution will run in context of the Local Service account.(Citation: Github W32Time Oct 2017)

## Detection
Baseline values and monitor/analyze activity related to modifying W32Time information in the Registry, including application programming interface (API) calls such as <code>RegCreateKeyEx</code> and <code>RegSetValueEx</code> as well as execution of the W32tm.exe utility.(Citation: Microsoft W32Time May 2017) There is no restriction on the number of custom time providers registrations, though each may require a DLL payload written to disk.(Citation: Github W32Time Oct 2017)

The Sysinternals Autoruns tool may also be used to analyze auto-starting locations, including DLLs listed as time providers.(Citation: TechNet Autoruns)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/003)
- [Github W32Time Oct 2017](https://github.com/scottlundgren/w32time)
- [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [Microsoft W32Time Feb 2018](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-top)
- [Microsoft TimeProvider](https://msdn.microsoft.com/library/windows/desktop/ms725475.aspx)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
