---
contributors:
- Matthew Demaske, Adaptforward
- Pedro Harrison
- Mayuresh Dani, Qualys
- Wietze Beukema, @wietze
- Akshat Pradhan, Qualys
- Wirapong Petshagun
data_sources:
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Creation'
- 'Network Traffic: Network Traffic Flow'
- 'Service: Service Creation'
- 'Command: Command Execution'
- 'File: File Metadata'
- 'Windows Registry: Windows Registry Key Creation'
- 'Driver: Driver Load'
- 'Service: Service Modification'
- 'Process: OS API Execution'
id: attack-pattern--2959d63f-73fd-46a1-abd2-109d7dcede32
mitre_attack_url: https://attack.mitre.org/techniques/T1543/003
name: Windows Service
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Windows Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Modification, Process: Process Creation, Network Traffic: Network Traffic Flow, Service: Service Creation, Command: Command Execution, File: File Metadata, Windows Registry: Windows Registry Key Creation, Driver: Driver Load, Service: Service Modification, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1543/003](https://attack.mitre.org/techniques/T1543/003) |

# Windows Service (attack-pattern--2959d63f-73fd-46a1-abd2-109d7dcede32)

## Description
Adversaries may create or modify Windows services to repeatedly execute malicious payloads as part of persistence. When Windows boots up, it starts programs or applications called services that perform background system functions.(Citation: TechNet Services) Windows service configuration information, including the file path to the service's executable or recovery programs/commands, is stored in the Windows Registry.

Adversaries may install a new service or modify an existing service to execute at startup in order to persist on a system. Service configurations can be set or modified using system utilities (such as sc.exe), by directly modifying the Registry, or by interacting directly with the Windows API. 

Adversaries may also use services to install and execute malicious drivers. For example, after dropping a driver file (ex: `.sys`) to disk, the payload can be loaded and registered via [Native API](https://attack.mitre.org/techniques/T1106) functions such as `CreateServiceW()` (or manually via functions such as `ZwLoadDriver()` and `ZwSetValueKey()`), by creating the required service Registry values (i.e. [Modify Registry](https://attack.mitre.org/techniques/T1112)), or by using command-line utilities such as `PnPUtil.exe`.(Citation: Symantec W.32 Stuxnet Dossier)(Citation: Crowdstrike DriveSlayer February 2022)(Citation: Unit42 AcidBox June 2020) Adversaries may leverage these drivers as [Rootkit](https://attack.mitre.org/techniques/T1014)s to hide the presence of malicious activity on a system. Adversaries may also load a signed yet vulnerable driver onto a compromised machine (known as "Bring Your Own Vulnerable Driver" (BYOVD)) as part of [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).(Citation: ESET InvisiMole June 2020)(Citation: Unit42 AcidBox June 2020)

Services may be created with administrator privileges but are executed under SYSTEM privileges, so an adversary may also use a service to escalate privileges. Adversaries may also directly start services through [Service Execution](https://attack.mitre.org/techniques/T1569/002).

To make detection analysis more challenging, malicious services may also incorporate [Masquerade Task or Service](https://attack.mitre.org/techniques/T1036/004) (ex: using a service and/or payload name related to a legitimate OS or benign software component). Adversaries may also create ‘hidden’ services (i.e., [Hide Artifacts](https://attack.mitre.org/techniques/T1564)), for example by using the `sc sdset` command to set service permissions via the Service Descriptor Definition Language (SDDL). This may hide a Windows service from the view of standard service enumeration methods such as `Get-Service`, `sc query`, and `services.exe`.(Citation: SANS 1)(Citation: SANS 2)

## Detection
Monitor processes and command-line arguments for actions that could create or modify services. Command-line invocation of tools capable of adding or modifying services may be unusual, depending on how systems are typically used in a particular environment. Services may also be modified through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001), so additional logging may need to be configured to gather the appropriate data. Remote access tools with built-in features may also interact directly with the Windows API to perform these functions outside of typical system utilities. Collect service utility execution and service binary path arguments used for analysis. Service binary paths may even be changed to execute commands or scripts.  

Look for changes to service Registry entries that do not correlate with known software, patch cycles, etc. Service information is stored in the Registry at <code>HKLM\SYSTEM\CurrentControlSet\Services</code>. Changes to the binary path and the service startup type changed from manual or disabled to automatic, if it does not typically do so, may be suspicious. Tools such as Sysinternals Autoruns may also be used to detect system service changes that could be attempts at persistence.(Citation: TechNet Autoruns)  

Creation of new services may generate an alterable event (ex: Event ID 4697 and/or 7045 (Citation: Microsoft 4697 APR 2017)(Citation: Microsoft Windows Event Forwarding FEB 2018)). New, benign services may be created during installation of new software.

Suspicious program execution through services may show up as outlier processes that have not been seen before when compared against historical data. Look for abnormal process call trees from known services and for execution of other commands that could relate to Discovery or other adversary techniques. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1543/003)
- [Microsoft Windows Event Forwarding FEB 2018](https://docs.microsoft.com/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection)
- [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [SANS 1](https://www.sans.org/blog/red-team-tactics-hiding-windows-services/)
- [SANS 2](https://www.sans.org/blog/defense-spotlight-finding-hidden-windows-services/)
- [TechNet Services](https://technet.microsoft.com/en-us/library/cc772408.aspx)
- [Microsoft 4697 APR 2017](https://docs.microsoft.com/windows/security/threat-protection/auditing/event-4697)
- [Symantec W.32 Stuxnet Dossier](https://www.wired.com/images_blogs/threatlevel/2010/11/w32_stuxnet_dossier.pdf)
- [Unit42 AcidBox June 2020](https://unit42.paloaltonetworks.com/acidbox-rare-malware/)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
- [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
