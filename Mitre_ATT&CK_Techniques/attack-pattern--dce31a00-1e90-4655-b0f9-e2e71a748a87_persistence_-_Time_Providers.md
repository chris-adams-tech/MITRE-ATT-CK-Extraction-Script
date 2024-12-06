---
contributors:
- Scott Lundgren, @5twenty9, Carbon Black
id: attack-pattern--dce31a00-1e90-4655-b0f9-e2e71a748a87
mitre_attack_url: https://attack.mitre.org/techniques/T1209
name: Time Providers
platforms:
- Windows
tactics:
- persistence
title: persistence - Time Providers
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1209](https://attack.mitre.org/techniques/T1209) |

# Time Providers (attack-pattern--dce31a00-1e90-4655-b0f9-e2e71a748a87)

## Description
The Windows Time service (W32Time) enables time synchronization across and within domains. (Citation: Microsoft W32Time Feb 2018) W32Time time providers are responsible for retrieving time stamps from hardware/network resources and outputting these values to other network clients. (Citation: Microsoft TimeProvider)

Time providers are implemented as dynamic-link libraries (DLLs) that are registered in the subkeys of  <code>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\W32Time\TimeProviders\</code>. (Citation: Microsoft TimeProvider) The time provider manager, directed by the service control manager, loads and starts time providers listed and enabled under this key at system startup and/or whenever parameters are changed. (Citation: Microsoft TimeProvider)

Adversaries may abuse this architecture to establish Persistence, specifically by registering and enabling a malicious DLL as a time provider. Administrator privileges are required for time provider registration, though execution will run in context of the Local Service account. (Citation: Github W32Time Oct 2017)

## Detection
Baseline values and monitor/analyze activity related to modifying W32Time information in the Registry, including application programming interface (API) calls such as RegCreateKeyEx and RegSetValueEx as well as execution of the W32tm.exe utility. (Citation: Microsoft W32Time May 2017) There is no restriction on the number of custom time providers registrations, though each may require a DLL payload written to disk. (Citation: Github W32Time Oct 2017)

The Sysinternals Autoruns tool may also be used to analyze auto-starting locations, including DLLs listed as time providers. (Citation: TechNet Autoruns)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1209)
- [Microsoft W32Time Feb 2018](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-top)
- [Microsoft TimeProvider](https://msdn.microsoft.com/library/windows/desktop/ms725475.aspx)
- [Github W32Time Oct 2017](https://github.com/scottlundgren/w32time)
- [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
