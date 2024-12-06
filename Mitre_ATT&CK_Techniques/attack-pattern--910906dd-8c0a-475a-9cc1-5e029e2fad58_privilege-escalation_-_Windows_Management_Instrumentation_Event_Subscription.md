---
contributors:
- Brent Murphy, Elastic
- David French, Elastic
- Viren Chaudhari, Qualys
data_sources:
- 'File: File Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'WMI: WMI Creation'
id: attack-pattern--910906dd-8c0a-475a-9cc1-5e029e2fad58
mitre_attack_url: https://attack.mitre.org/techniques/T1546/003
name: Windows Management Instrumentation Event Subscription
platforms:
- Windows
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Windows Management Instrumentation Event Subscription
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Windows |
| **Data Sources** | File: File Creation, Process: Process Creation, Command: Command Execution, WMI: WMI Creation |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/003](https://attack.mitre.org/techniques/T1546/003) |

# Windows Management Instrumentation Event Subscription (attack-pattern--910906dd-8c0a-475a-9cc1-5e029e2fad58)

## Description
Adversaries may establish persistence and elevate privileges by executing malicious content triggered by a Windows Management Instrumentation (WMI) event subscription. WMI can be used to install event filters, providers, consumers, and bindings that execute code when a defined event occurs. Examples of events that may be subscribed to are the wall clock time, user login, or the computer's uptime.(Citation: Mandiant M-Trends 2015)

Adversaries may use the capabilities of WMI to subscribe to an event and execute arbitrary code when that event occurs, providing persistence on a system.(Citation: FireEye WMI SANS 2015)(Citation: FireEye WMI 2015) Adversaries may also compile WMI scripts – using `mofcomp.exe`  –into Windows Management Object (MOF) files (.mof extension) that can be used to create a malicious subscription.(Citation: Dell WMI Persistence)(Citation: Microsoft MOF May 2018)

WMI subscription execution is proxied by the WMI Provider Host process (WmiPrvSe.exe) and thus may result in elevated SYSTEM privileges.

## Detection
Monitor WMI event subscription entries, comparing current WMI event subscriptions to known good subscriptions for each host. Tools such as Sysinternals Autoruns may also be used to detect WMI changes that could be attempts at persistence.(Citation: TechNet Autoruns)(Citation: Medium Detecting WMI Persistence) Monitor for the creation of new WMI <code>EventFilter</code>, <code>EventConsumer</code>, and <code>FilterToConsumerBinding</code> events. Event ID 5861 is logged on Windows 10 systems when new <code>EventFilterToConsumerBinding</code> events are created.(Citation: Elastic - Hunting for Persistence Part 1)

Monitor processes and command-line arguments that can be used to register WMI persistence, such as the <code> Register-WmiEvent</code> [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlet, as well as those that result from the execution of subscriptions (i.e. spawning from the WmiPrvSe.exe WMI Provider Host process).(Citation: Microsoft Register-WmiEvent)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/003)
- [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)
- [Dell WMI Persistence](https://www.secureworks.com/blog/wmi-persistence)
- [FireEye WMI SANS 2015](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/sans-dfir-2015.pdf)
- [Medium Detecting WMI Persistence](https://medium.com/threatpunter/detecting-removing-wmi-persistence-60ccbb7dff96)
- [Elastic - Hunting for Persistence Part 1](https://www.elastic.co/blog/hunting-for-persistence-using-elastic-security-part-1)
- [Mandiant M-Trends 2015](https://www2.fireeye.com/rs/fireye/images/rpt-m-trends-2015.pdf)
- [Microsoft Register-WmiEvent](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/register-wmievent?view=powershell-5.1)
- [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
- [Microsoft MOF May 2018](https://docs.microsoft.com/en-us/windows/win32/wmisdk/managed-object-format--mof-)
