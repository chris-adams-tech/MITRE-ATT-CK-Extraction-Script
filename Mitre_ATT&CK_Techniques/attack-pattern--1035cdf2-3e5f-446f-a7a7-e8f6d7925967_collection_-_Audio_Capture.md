---
data_sources:
- 'Process: OS API Execution'
- 'Command: Command Execution'
id: attack-pattern--1035cdf2-3e5f-446f-a7a7-e8f6d7925967
mitre_attack_url: https://attack.mitre.org/techniques/T1123
name: Audio Capture
platforms:
- Linux
- macOS
- Windows
tactics:
- collection
title: collection - Audio Capture
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: OS API Execution, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1123](https://attack.mitre.org/techniques/T1123) |

# Audio Capture (attack-pattern--1035cdf2-3e5f-446f-a7a7-e8f6d7925967)

## Description
An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.(Citation: ESET Attor Oct 2019)

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

## Detection
Detection of this technique may be difficult due to the various APIs that may be used. Telemetry data regarding API use may not be useful depending on how a system is normally used, but may provide context to other potentially malicious activity occurring on a system.

Behavior that could indicate technique use include an unknown or unusual process accessing APIs associated with devices or software that interact with the microphone, recording devices, or recording software, and a process periodically writing files to disk that contain audio data.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1123)
- [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
