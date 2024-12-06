---
contributors:
- TruKno
data_sources:
- 'Driver: Driver Load'
- 'Process: OS API Execution'
- 'Windows Registry: Windows Registry Key Modification'
id: attack-pattern--09a60ea3-a8d1-4ae5-976e-5783248b72a4
mitre_attack_url: https://attack.mitre.org/techniques/T1056/001
name: Keylogging
platforms:
- Windows
- macOS
- Linux
- Network
tactics:
- collection
- credential-access
title: collection - Keylogging
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection, credential-access |
| **Platforms** | Windows, macOS, Linux, Network |
| **Data Sources** | Driver: Driver Load, Process: OS API Execution, Windows Registry: Windows Registry Key Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1056/001](https://attack.mitre.org/techniques/T1056/001) |

# Keylogging (attack-pattern--09a60ea3-a8d1-4ae5-976e-5783248b72a4)

## Description
Adversaries may log user keystrokes to intercept credentials as the user types them. Keylogging is likely to be used to acquire credentials for new access opportunities when [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) efforts are not effective, and may require an adversary to intercept keystrokes on a system for a substantial period of time before credentials can be successfully captured. In order to increase the likelihood of capturing credentials quickly, an adversary may also perform actions such as clearing browser cookies to force users to reauthenticate to systems.(Citation: Talos Kimsuky Nov 2021)

Keylogging is the most prevalent type of input capture, with many different ways of intercepting keystrokes.(Citation: Adventures of a Keystroke) Some methods include:

* Hooking API callbacks used for processing keystrokes. Unlike [Credential API Hooking](https://attack.mitre.org/techniques/T1056/004), this focuses solely on API functions intended for processing keystroke data.
* Reading raw keystroke data from the hardware buffer.
* Windows Registry modifications.
* Custom drivers.
* [Modify System Image](https://attack.mitre.org/techniques/T1601) may provide adversaries with hooks into the operating system of network devices to read raw keystrokes for login sessions.(Citation: Cisco Blog Legacy Device Attacks) 

## Detection
Keyloggers may take many forms, possibly involving modification to the Registry and installation of a driver, setting a hook, or polling to intercept keystrokes. Commonly used API calls include `SetWindowsHook`, `GetKeyState`, and `GetAsyncKeyState`.(Citation: Adventures of a Keystroke) Monitor the Registry and file system for such changes, monitor driver installs, and look for common keylogging API calls. API calls alone are not an indicator of keylogging, but may provide behavioral data that is useful when combined with other information such as new files written to disk and unusual processes.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1056/001)
- [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
- [Adventures of a Keystroke](http://opensecuritytraining.info/Keylogging_files/The%20Adventures%20of%20a%20Keystroke.pdf)
