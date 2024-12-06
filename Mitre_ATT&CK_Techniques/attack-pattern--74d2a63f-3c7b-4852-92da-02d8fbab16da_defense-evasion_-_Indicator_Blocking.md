---
contributors:
- Rob Smith
- Lucas Heiligenstein
data_sources:
- 'Command: Command Execution'
- 'Sensor Health: Host Status'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Creation'
id: attack-pattern--74d2a63f-3c7b-4852-92da-02d8fbab16da
mitre_attack_url: https://attack.mitre.org/techniques/T1562/006
name: Indicator Blocking
platforms:
- Windows
- macOS
- Linux
tactics:
- defense-evasion
title: defense-evasion - Indicator Blocking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Command: Command Execution, Sensor Health: Host Status, Windows Registry: Windows Registry Key Modification, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/006](https://attack.mitre.org/techniques/T1562/006) |

# Indicator Blocking (attack-pattern--74d2a63f-3c7b-4852-92da-02d8fbab16da)

## Description
An adversary may attempt to block indicators or events typically captured by sensors from being gathered and analyzed. This could include maliciously redirecting(Citation: Microsoft Lamin Sept 2017) or even disabling host-based sensors, such as Event Tracing for Windows (ETW)(Citation: Microsoft About Event Tracing 2018), by tampering settings that control the collection and flow of event telemetry.(Citation: Medium Event Tracing Tampering 2018) These settings may be stored on the system in configuration files and/or in the Registry as well as being accessible via administrative utilities such as [PowerShell](https://attack.mitre.org/techniques/T1059/001) or [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047).

For example, adversaries may modify the `File` value in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Security</code> to hide their malicious actions in a new or different .evtx log file. This action does not require a system reboot and takes effect immediately.(Citation: disable_win_evt_logging) 

ETW interruption can be achieved multiple ways, however most directly by defining conditions using the [PowerShell](https://attack.mitre.org/techniques/T1059/001) <code>Set-EtwTraceProvider</code> cmdlet or by interfacing directly with the Registry to make alterations.

In the case of network-based reporting of indicators, an adversary may block traffic associated with reporting to prevent central analysis. This may be accomplished by many means, such as stopping a local process responsible for forwarding telemetry and/or creating a host-based firewall rule to block traffic to specific hosts responsible for aggregating events, such as security information and event management (SIEM) products.

In Linux environments, adversaries may disable or reconfigure log processing tools such as syslog or nxlog to inhibit detection and monitoring capabilities to facilitate follow on behaviors (Citation: LemonDuck).

## Detection
Detect lack of reported activity from a host sensor. Different methods of blocking may cause different disruptions in reporting. Systems may suddenly stop reporting all data or only certain kinds of data.

Depending on the types of host information collected, an analyst may be able to detect the event that triggered a process to stop or connection to be blocked. For example, Sysmon will log when its configuration state has changed (Event ID 16) and Windows Management Instrumentation (WMI) may be used to subscribe ETW providers that log any provider removal from a specific trace session. (Citation: Medium Event Tracing Tampering 2018) To detect changes in ETW you can also monitor the registry key which contains configurations for all ETW event providers: <code>HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\AUTOLOGGER_NAME\{PROVIDER_GUID}</code>

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/006)
- [disable_win_evt_logging](https://ptylu.github.io/content/report/report.html?report=25)
- [LemonDuck](https://www.crowdstrike.com/blog/lemonduck-botnet-targets-docker-for-cryptomining-operations/)
- [Microsoft Lamin Sept 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?name=Backdoor:Win32/Lamin.A)
- [Microsoft About Event Tracing 2018](https://docs.microsoft.com/en-us/windows/desktop/etw/consuming-events)
- [Medium Event Tracing Tampering 2018](https://medium.com/palantir/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63)
