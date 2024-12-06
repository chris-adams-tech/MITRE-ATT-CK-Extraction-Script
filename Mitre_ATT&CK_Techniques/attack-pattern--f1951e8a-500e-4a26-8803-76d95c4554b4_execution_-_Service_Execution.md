---
data_sources:
- 'Windows Registry: Windows Registry Key Modification'
- 'Network Traffic: Network Traffic Flow'
- 'Service: Service Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--f1951e8a-500e-4a26-8803-76d95c4554b4
mitre_attack_url: https://attack.mitre.org/techniques/T1569/002
name: Service Execution
platforms:
- Windows
tactics:
- execution
title: execution - Service Execution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Modification, Network Traffic: Network Traffic Flow, Service: Service Creation, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1569/002](https://attack.mitre.org/techniques/T1569/002) |

# Service Execution (attack-pattern--f1951e8a-500e-4a26-8803-76d95c4554b4)

## Description
Adversaries may abuse the Windows service control manager to execute malicious commands or payloads. The Windows service control manager (<code>services.exe</code>) is an interface to manage and manipulate services.(Citation: Microsoft Service Control Manager) The service control manager is accessible to users via GUI components as well as system utilities such as <code>sc.exe</code> and [Net](https://attack.mitre.org/software/S0039).

[PsExec](https://attack.mitre.org/software/S0029) can also be used to execute commands or payloads via a temporary Windows service created through the service control manager API.(Citation: Russinovich Sysinternals) Tools such as [PsExec](https://attack.mitre.org/software/S0029) and <code>sc.exe</code> can accept remote servers as arguments and may be used to conduct remote execution.

Adversaries may leverage these mechanisms to execute malicious content. This can be done by either executing a new or modified service. This technique is the execution used in conjunction with [Windows Service](https://attack.mitre.org/techniques/T1543/003) during service persistence or privilege escalation.

## Detection
Changes to service Registry entries and command line invocation of tools capable of modifying services that do not correlate with known software, patch cycles, etc., may be suspicious. If a service is used only to execute a binary or script and not to persist, then it will likely be changed back to its original form shortly after the service is restarted so the service is not left broken, as is the case with the common administrator tool [PsExec](https://attack.mitre.org/software/S0029).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1569/002)
- [Microsoft Service Control Manager](https://docs.microsoft.com/windows/win32/services/service-control-manager)
- [Russinovich Sysinternals](https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx)
