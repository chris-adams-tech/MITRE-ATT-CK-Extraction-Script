---
contributors:
- ESET
- "Christoffer Str\xF6mblad"
data_sources:
- 'File: File Creation'
- 'Application Log: Application Log Content'
id: attack-pattern--35187df2-31ed-43b6-a1f5-2f1d3d58d3f1
mitre_attack_url: https://attack.mitre.org/techniques/T1505/002
name: Transport Agent
platforms:
- Linux
- Windows
tactics:
- persistence
title: persistence - Transport Agent
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Linux, Windows |
| **Data Sources** | File: File Creation, Application Log: Application Log Content |
| **Permissions Required** | SYSTEM, Administrator, root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1505/002](https://attack.mitre.org/techniques/T1505/002) |

# Transport Agent (attack-pattern--35187df2-31ed-43b6-a1f5-2f1d3d58d3f1)

## Description
Adversaries may abuse Microsoft transport agents to establish persistent access to systems. Microsoft Exchange transport agents can operate on email messages passing through the transport pipeline to perform various tasks such as filtering spam, filtering malicious attachments, journaling, or adding a corporate signature to the end of all outgoing emails.(Citation: Microsoft TransportAgent Jun 2016)(Citation: ESET LightNeuron May 2019) Transport agents can be written by application developers and then compiled to .NET assemblies that are subsequently registered with the Exchange server. Transport agents will be invoked during a specified stage of email processing and carry out developer defined tasks. 

Adversaries may register a malicious transport agent to provide a persistence mechanism in Exchange Server that can be triggered by adversary-specified email events.(Citation: ESET LightNeuron May 2019) Though a malicious transport agent may be invoked for all emails passing through the Exchange transport pipeline, the agent can be configured to only carry out specific tasks in response to adversary defined criteria. For example, the transport agent may only carry out an action like copying in-transit attachments and saving them for later exfiltration if the recipient email address matches an entry on a list provided by the adversary. 

## Detection
Consider monitoring application logs for abnormal behavior that may indicate suspicious installation of application software components. Consider monitoring file locations associated with the installation of new application software components such as paths from which applications typically load such extensible components.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1505/002)
- [Microsoft TransportAgent Jun 2016](https://docs.microsoft.com/en-us/exchange/transport-agents-exchange-2013-help)
- [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
