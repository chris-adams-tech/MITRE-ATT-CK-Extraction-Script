---
id: attack-pattern--197ef1b9-e764-46c3-b96c-23f77985dc81
mitre_attack_url: https://attack.mitre.org/techniques/T1583/002
name: DNS Server
platforms:
- PRE
tactics:
- resource-development
title: resource-development - DNS Server
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1583/002](https://attack.mitre.org/techniques/T1583/002) |

# DNS Server (attack-pattern--197ef1b9-e764-46c3-b96c-23f77985dc81)

## Description
Adversaries may set up their own Domain Name System (DNS) servers that can be used during targeting. During post-compromise activity, adversaries may utilize DNS traffic for various tasks, including for Command and Control (ex: [Application Layer Protocol](https://attack.mitre.org/techniques/T1071)). Instead of hijacking existing DNS servers, adversaries may opt to configure and run their own DNS servers in support of operations.

By running their own DNS servers, adversaries can have more control over how they administer server-side DNS C2 traffic ([DNS](https://attack.mitre.org/techniques/T1071/004)). With control over a DNS server, adversaries can configure DNS applications to provide conditional responses to malware and, generally, have more flexibility in the structure of the DNS-based C2 channel.(Citation: Unit42 DNS Mar 2019)

## Detection
Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1583/002)
- [Unit42 DNS Mar 2019](https://unit42.paloaltonetworks.com/dns-tunneling-how-dns-can-be-abused-by-malicious-actors/)
