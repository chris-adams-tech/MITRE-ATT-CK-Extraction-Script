---
contributors:
- Thomas B
- Ivy Drexel
data_sources:
- 'Module: Module Load'
- 'File: File Creation'
- 'Process: Process Creation'
id: attack-pattern--356662f7-e315-4759-86c9-6214e2a50ff8
mitre_attack_url: https://attack.mitre.org/techniques/T1574/014
name: AppDomainManager
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- defense-evasion
title: persistence - AppDomainManager
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Module: Module Load, File: File Creation, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1574/014](https://attack.mitre.org/techniques/T1574/014) |

# AppDomainManager (attack-pattern--356662f7-e315-4759-86c9-6214e2a50ff8)

## Description
Adversaries may execute their own malicious payloads by hijacking how the .NET `AppDomainManager` loads assemblies. The .NET framework uses the `AppDomainManager` class to create and manage one or more isolated runtime environments (called application domains) inside a process to host the execution of .NET applications. Assemblies (`.exe` or `.dll` binaries compiled to run as .NET code) may be loaded into an application domain as executable code.(Citation: Microsoft App Domains) 

Known as "AppDomainManager injection," adversaries may execute arbitrary code by hijacking how .NET applications load assemblies. For example, malware may create a custom application domain inside a target process to load and execute an arbitrary assembly. Alternatively, configuration files (`.config`) or process environment variables that define .NET runtime settings may be tampered with to instruct otherwise benign .NET applications to load a malicious assembly (identified by name) into the target process.(Citation: PenTestLabs AppDomainManagerInject)(Citation: PwC Yellow Liderc)(Citation: Rapid7 AppDomain Manager Injection)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1574/014)
- [PenTestLabs AppDomainManagerInject](https://pentestlaboratories.com/2020/05/26/appdomainmanager-injection-and-detection/)
- [Microsoft App Domains](https://learn.microsoft.com/dotnet/framework/app-domains/application-domains)
- [PwC Yellow Liderc](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
- [Rapid7 AppDomain Manager Injection](https://www.rapid7.com/blog/post/2023/05/05/appdomain-manager-injection-new-techniques-for-red-teams/)
