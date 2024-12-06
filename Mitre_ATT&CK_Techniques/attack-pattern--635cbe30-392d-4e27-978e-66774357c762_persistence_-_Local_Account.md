---
contributors:
- Austin Clark, @c2defense
data_sources:
- 'User Account: User Account Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--635cbe30-392d-4e27-978e-66774357c762
mitre_attack_url: https://attack.mitre.org/techniques/T1136/001
name: Local Account
platforms:
- Linux
- macOS
- Windows
- Network
- Containers
tactics:
- persistence
title: persistence - Local Account
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Linux, macOS, Windows, Network, Containers |
| **Data Sources** | User Account: User Account Creation, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1136/001](https://attack.mitre.org/techniques/T1136/001) |

# Local Account (attack-pattern--635cbe30-392d-4e27-978e-66774357c762)

## Description
Adversaries may create a local account to maintain access to victim systems. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. 

For example, with a sufficient level of access, the Windows <code>net user /add</code> command can be used to create a local account. On macOS systems the <code>dscl -create</code> command can be used to create a local account. Local accounts may also be added to network devices, often via common [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as <code>username</code>, or to Kubernetes clusters using the `kubectl` utility.(Citation: cisco_username_cmd)(Citation: Kubernetes Service Accounts Security)

Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

## Detection
Monitor for processes and command-line parameters associated with local account creation, such as <code>net user /add</code> , <code>useradd</code> , and <code>dscl -create</code> . Collect data on account creation within a network. Event ID 4720 is generated when a user account is created on a Windows system. (Citation: Microsoft User Creation Event) Perform regular audits of local system accounts to detect suspicious accounts that may have been created by an adversary. For network infrastructure devices, collect AAA logging to monitor for account creations.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1136/001)
- [cisco_username_cmd](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-t2.html#wp1047035630)
- [Kubernetes Service Accounts Security](https://kubernetes.io/docs/concepts/security/service-accounts/)
- [Microsoft User Creation Event](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720)
