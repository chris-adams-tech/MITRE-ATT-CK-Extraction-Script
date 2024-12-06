---
contributors:
- Praetorian
data_sources:
- 'Process: OS API Execution'
- 'Command: Command Execution'
id: attack-pattern--6faf650d-bf31-4eb4-802d-1000cf38efaf
mitre_attack_url: https://attack.mitre.org/techniques/T1125
name: Video Capture
platforms:
- Windows
- macOS
- Linux
tactics:
- collection
title: collection - Video Capture
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Process: OS API Execution, Command: Command Execution |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1125](https://attack.mitre.org/techniques/T1125) |

# Video Capture (attack-pattern--6faf650d-bf31-4eb4-802d-1000cf38efaf)

## Description
An adversary can leverage a computer's peripheral devices (e.g., integrated cameras or webcams) or applications (e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured from devices or applications, potentially in specified intervals, in lieu of video files.

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique differs from [Screen Capture](https://attack.mitre.org/techniques/T1113) due to use of specific devices or applications for video recording rather than capturing the victim's screen.

In macOS, there are a few different malware samples that record the user's webcam such as FruitFly and Proton. (Citation: objective-see 2017 review)

## Detection
Detection of this technique may be difficult due to the various APIs that may be used. Telemetry data regarding API use may not be useful depending on how a system is normally used, but may provide context to other potentially malicious activity occurring on a system.

Behavior that could indicate technique use include an unknown or unusual process accessing APIs associated with devices or software that interact with the video camera, recording devices, or recording software, and a process periodically writing files to disk that contain video or camera image data.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1125)
- [objective-see 2017 review](https://objective-see.com/blog/blog_0x25.html)
