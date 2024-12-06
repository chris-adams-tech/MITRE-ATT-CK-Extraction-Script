---
id: attack-pattern--e906ae4d-1d3a-4675-be23-22f7311c0da4
mitre_attack_url: https://attack.mitre.org/techniques/T1084
name: Windows Management Instrumentation Event Subscription
platforms:
- Windows
tactics:
- persistence
title: persistence - Windows Management Instrumentation Event Subscription
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1084](https://attack.mitre.org/techniques/T1084) |

# Windows Management Instrumentation Event Subscription (attack-pattern--e906ae4d-1d3a-4675-be23-22f7311c0da4)

## Description
Windows Management Instrumentation (WMI) can be used to install event filters, providers, consumers, and bindings that execute code when a defined event occurs. Adversaries may use the capabilities of WMI to subscribe to an event and execute arbitrary code when that event occurs, providing persistence on a system. Adversaries may attempt to evade detection of this technique by compiling WMI scripts into Windows Management Object (MOF) files (.mof extension). (Citation: Dell WMI Persistence) Examples of events that may be subscribed to are the wall clock time or the computer's uptime. (Citation: Kazanciyan 2014) Several threat groups have reportedly used this technique to maintain persistence. (Citation: Mandiant M-Trends 2015)

## Detection
Monitor WMI event subscription entries, comparing current WMI event subscriptions to known good subscriptions for each host. Tools such as Sysinternals Autoruns may also be used to detect WMI changes that could be attempts at persistence. (Citation: TechNet Autoruns) (Citation: Medium Detecting WMI Persistence)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1084)
- [Dell WMI Persistence](https://www.secureworks.com/blog/wmi-persistence)
- [Kazanciyan 2014](https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf)
- [Mandiant M-Trends 2015](https://www2.fireeye.com/rs/fireye/images/rpt-m-trends-2015.pdf)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
- [Medium Detecting WMI Persistence](https://medium.com/threatpunter/detecting-removing-wmi-persistence-60ccbb7dff96)
