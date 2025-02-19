---
contributors:
- Praetorian
- ExtraHop
- "Jannie Li, Microsoft Threat Intelligence\u202FCenter\u202F(MSTIC)"
data_sources:
- 'Logon Session: Logon Session Creation'
- 'Logon Session: Logon Session Metadata'
- 'Network Traffic: Network Traffic Content'
- 'Application Log: Application Log Content'
id: attack-pattern--9fa07bef-9c81-421e-a8e5-ad4366c5a925
mitre_attack_url: https://attack.mitre.org/techniques/T1199
name: Trusted Relationship
platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Identity Provider
- Office Suite
tactics:
- initial-access
title: initial-access - Trusted Relationship
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Identity Provider, Office Suite |
| **Data Sources** | Logon Session: Logon Session Creation, Logon Session: Logon Session Metadata, Network Traffic: Network Traffic Content, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1199](https://attack.mitre.org/techniques/T1199) |

# Trusted Relationship (attack-pattern--9fa07bef-9c81-421e-a8e5-ad4366c5a925)

## Description
Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network.

Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider's access may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the enterprise. As such, [Valid Accounts](https://attack.mitre.org/techniques/T1078) used by the other party for access to internal network systems may be compromised and used.(Citation: CISA IT Service Providers)

In Office 365 environments, organizations may grant Microsoft partners or resellers delegated administrator permissions. By compromising a partner or reseller account, an adversary may be able to leverage existing delegated administrator relationships or send new delegated administrator offers to clients in order to gain administrative control over the victim tenant.(Citation: Office 365 Delegated Administration)

## Detection
Establish monitoring for activity conducted by second and third party providers and other trusted entities that may be leveraged as a means to gain access to the network. Depending on the type of relationship, an adversary may have access to significant amounts of information about the target before conducting an operation, especially if the trusted relationship is based on IT services. Adversaries may be able to act quickly towards an objective, so proper monitoring for behavior related to Credential Access, Lateral Movement, and Collection will be important to detect the intrusion.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1199)
- [CISA IT Service Providers](https://us-cert.cisa.gov/APTs-Targeting-IT-Service-Provider-Customers)
- [Office 365 Delegated Administration](https://support.microsoft.com/en-us/topic/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e?ui=en-us&rs=en-us&ad=us)
