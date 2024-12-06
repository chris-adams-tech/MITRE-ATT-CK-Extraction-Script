---
data_sources:
- 'Command: Command Execution'
- 'Process: OS API Execution'
id: attack-pattern--0259baeb-9f63-4c69-bf10-eb038c390688
mitre_attack_url: https://attack.mitre.org/techniques/T1113
name: Screen Capture
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
title: collection - Screen Capture
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Command: Command Execution, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1113](https://attack.mitre.org/techniques/T1113) |

# Screen Capture (attack-pattern--0259baeb-9f63-4c69-bf10-eb038c390688)

## Description
Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as <code>CopyFromScreen</code>, <code>xwd</code>, or <code>screencapture</code>.(Citation: CopyFromScreen .NET)(Citation: Antiquated Mac Malware)


## Detection
Monitoring for screen capture behavior will depend on the method used to obtain data from the operating system and write output files. Detection methods could include collecting information from unusual processes using API calls used to obtain image data, and monitoring for image files written to disk. The sensor data may need to be correlated with other events to identify malicious activity, depending on the legitimacy of this behavior within a given network environment.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1113)
- [CopyFromScreen .NET](https://docs.microsoft.com/en-us/dotnet/api/system.drawing.graphics.copyfromscreen?view=netframework-4.8)
- [Antiquated Mac Malware](https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/)
