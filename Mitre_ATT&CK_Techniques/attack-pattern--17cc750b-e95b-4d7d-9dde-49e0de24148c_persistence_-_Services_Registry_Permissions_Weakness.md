---
contributors:
- Travis Smith, Tripwire
- Matthew Demaske, Adaptforward
data_sources:
- 'Windows Registry: Windows Registry Key Modification'
- 'Service: Service Modification'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--17cc750b-e95b-4d7d-9dde-49e0de24148c
mitre_attack_url: https://attack.mitre.org/techniques/T1574/011
name: Services Registry Permissions Weakness
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - Services Registry Permissions Weakness
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Modification, Service: Service Modification, Command: Command Execution, Process: Process Creation |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/011](https://attack.mitre.org/techniques/T1574/011) |

# Services Registry Permissions Weakness (attack-pattern--17cc750b-e95b-4d7d-9dde-49e0de24148c)

## Description
Adversaries may execute their own malicious payloads by hijacking the Registry entries used by services. Adversaries may use flaws in the permissions for Registry keys related to services to redirect from the originally specified executable to one that they control, in order to launch their own code when a service starts. Windows stores local service configuration information in the Registry under <code>HKLM\SYSTEM\CurrentControlSet\Services</code>. The information stored under a service's Registry keys can be manipulated to modify a service's execution parameters through tools such as the service controller, sc.exe,  [PowerShell](https://attack.mitre.org/techniques/T1059/001), or [Reg](https://attack.mitre.org/software/S0075). Access to Registry keys is controlled through access control lists and user permissions. (Citation: Registry Key Security)(Citation: malware_hides_service)

If the permissions for users and groups are not properly set and allow access to the Registry keys for a service, adversaries may change the service's binPath/ImagePath to point to a different executable under their control. When the service starts or is restarted, then the adversary-controlled program will execute, allowing the adversary to establish persistence and/or privilege escalation to the account context the service is set to execute under (local/domain account, SYSTEM, LocalService, or NetworkService).

Adversaries may also alter other Registry keys in the service’s Registry tree. For example, the <code>FailureCommand</code> key may be changed so that the service is executed in an elevated context anytime the service fails or is intentionally corrupted.(Citation: Kansa Service related collectors)(Citation: Tweet Registry Perms Weakness)

The <code>Performance</code> key contains the name of a driver service's performance DLL and the names of several exported functions in the DLL.(Citation: microsoft_services_registry_tree) If the <code>Performance</code> key is not already present and if an adversary-controlled user has the <code>Create Subkey</code> permission, adversaries may create the <code>Performance</code> key in the service’s Registry tree to point to a malicious DLL.(Citation: insecure_reg_perms)

Adversaries may also add the <code>Parameters</code> key, which stores driver-specific data, or other custom subkeys for their malicious services to establish persistence or enable other malicious activities.(Citation: microsoft_services_registry_tree)(Citation: troj_zegost) Additionally, If adversaries launch their malicious services using svchost.exe, the service’s file may be identified using <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\servicename\Parameters\ServiceDll</code>.(Citation: malware_hides_service)

## Detection
Service changes are reflected in the Registry. Modification to existing services should not occur frequently. If a service binary path or failure parameters are changed to values that are not typical for that service and does not correlate with software updates, then it may be due to malicious activity. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

Tools such as Sysinternals Autoruns may also be used to detect system changes that could be attempts at persistence, including listing current service information. (Citation: Autoruns for Windows) Look for changes to services that do not correlate with known software, patch cycles, etc. Suspicious program execution through services may show up as outlier processes that have not been seen before when compared against historical data.

Monitor processes and command-line arguments for actions that could be done to modify services. Remote access tools with built-in features may interact directly with the Windows API to perform these functions outside of typical system utilities. Services may also be changed through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001), so additional logging may need to be configured to gather the appropriate data.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/011)
- [Tweet Registry Perms Weakness](https://x.com/r0wdy_/status/936365549553991680)
- [insecure_reg_perms](https://itm4n.github.io/windows-registry-rpceptmapper-eop/)
- [Kansa Service related collectors](https://trustedsignal.blogspot.com/2014/05/kansa-service-related-collectors-and.html)
- [malware_hides_service](https://www.bleepingcomputer.com/tutorials/how-malware-hides-as-a-service/)
- [Autoruns for Windows](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [Registry Key Security](https://docs.microsoft.com/en-us/windows/win32/sysinfo/registry-key-security-and-access-rights?redirectedfrom=MSDN)
- [microsoft_services_registry_tree](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree)
- [troj_zegost](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/troj_zegost)
