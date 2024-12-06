---
data_sources:
- 'Module: Module Load'
- 'WMI: WMI Creation'
- 'File: File Metadata'
- 'File: File Creation'
- 'File: File Modification'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
- 'Cloud Service: Cloud Service Modification'
- 'Process: Process Creation'
id: attack-pattern--b6301b64-ef57-4cce-bb0b-77026f14a8db
mitre_attack_url: https://attack.mitre.org/techniques/T1546
name: Event Triggered Execution
platforms:
- Linux
- macOS
- Windows
- SaaS
- IaaS
- Office Suite
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Event Triggered Execution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Linux, macOS, Windows, SaaS, IaaS, Office Suite |
| **Data Sources** | Module: Module Load, WMI: WMI Creation, File: File Metadata, File: File Creation, File: File Modification, Windows Registry: Windows Registry Key Modification, Command: Command Execution, Cloud Service: Cloud Service Modification, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546](https://attack.mitre.org/techniques/T1546) |

# Event Triggered Execution (attack-pattern--b6301b64-ef57-4cce-bb0b-77026f14a8db)

## Description
Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other user activity such as running specific applications/binaries. Cloud environments may also support various functions and services that monitor and can be invoked in response to specific cloud events.(Citation: Backdooring an AWS account)(Citation: Varonis Power Automate Data Exfiltration)(Citation: Microsoft DART Case Report 001)

Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing malicious code. After gaining access to a victim system, adversaries may create/modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.(Citation: FireEye WMI 2015)(Citation: Malware Persistence on OS X)(Citation: amnesia malware)

Since the execution can be proxied by an account with higher permissions, such as SYSTEM or service accounts, an adversary may be able to abuse these triggered execution mechanisms to escalate their privileges. 

## Detection
Monitoring for additions or modifications of mechanisms that could be used to trigger event-based execution, especially the addition of abnormal commands such as execution of unknown programs, opening network sockets, or reaching out across the network. Also look for changes that do not line up with updates, patches, or other planned administrative activity. 

These mechanisms may vary by OS, but are typically stored in central repositories that store configuration information such as the Windows Registry, Common Information Model (CIM), and/or specific named files, the last of which can be hashed and compared to known good values. 

Monitor for processes, API/System calls, and other common ways of manipulating these event repositories. 

Tools such as Sysinternals Autoruns can be used to detect changes to execution triggers that could be attempts at persistence. Also look for abnormal process call trees for execution of other commands that could relate to Discovery actions or other techniques.  

Monitor DLL loads by processes, specifically looking for DLLs that are not recognized or not normally loaded into a process. Look for abnormal process behavior that may be due to a process loading a malicious DLL. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as making network connections for Command and Control, learning details about the environment through Discovery, and conducting Lateral Movement. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546)
- [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)
- [Microsoft DART Case Report 001](https://www.microsoft.com/security/blog/2020/03/09/real-life-cybercrime-stories-dart-microsoft-detection-and-response-team)
- [amnesia malware](https://researchcenter.paloaltonetworks.com/2017/04/unit42-new-iotlinux-malware-targets-dvrs-forms-botnet/)
- [Backdooring an AWS account](https://medium.com/daniel-grzelak/backdooring-an-aws-account-da007d36f8f9)
- [Varonis Power Automate Data Exfiltration](https://www.varonis.com/blog/power-automate-data-exfiltration)
- [Malware Persistence on OS X](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
