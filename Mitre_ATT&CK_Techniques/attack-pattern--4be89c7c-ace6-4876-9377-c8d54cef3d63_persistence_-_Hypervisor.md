---
id: attack-pattern--4be89c7c-ace6-4876-9377-c8d54cef3d63
mitre_attack_url: https://attack.mitre.org/techniques/T1062
name: Hypervisor
platforms:
- Windows
tactics:
- persistence
title: persistence - Hypervisor
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1062](https://attack.mitre.org/techniques/T1062) |

# Hypervisor (attack-pattern--4be89c7c-ace6-4876-9377-c8d54cef3d63)

## Description
**This technique has been deprecated and should no longer be used.**

A type-1 hypervisor is a software layer that sits between the guest operating systems and system's hardware. (Citation: Wikipedia Hypervisor) It presents a virtual running environment to an operating system. An example of a common hypervisor is Xen. (Citation: Wikipedia Xen) A type-1 hypervisor operates at a level below the operating system and could be designed with [Rootkit](https://attack.mitre.org/techniques/T1014) functionality to hide its existence from the guest operating system. (Citation: Myers 2007) A malicious hypervisor of this nature could be used to persist on systems through interruption.

## Detection
Type-1 hypervisors may be detected by performing timing analysis. Hypervisors emulate certain CPU instructions that would normally be executed by the hardware. If an instruction takes orders of magnitude longer to execute than normal on a system that should not contain a hypervisor, one may be present. (Citation: virtualization.info 2006)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1062)
- [capec](https://capec.mitre.org/data/definitions/552.html)
- [Wikipedia Hypervisor](https://en.wikipedia.org/wiki/Hypervisor)
- [Wikipedia Xen](http://en.wikipedia.org/wiki/Xen)
- [Myers 2007](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.90.8832&rep=rep1&type=pdf)
- [virtualization.info 2006](http://virtualization.info/en/news/2006/08/debunking-blue-pill-myth.html)
