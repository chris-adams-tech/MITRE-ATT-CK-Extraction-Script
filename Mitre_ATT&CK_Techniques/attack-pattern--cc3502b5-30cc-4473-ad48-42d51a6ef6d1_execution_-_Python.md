---
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--cc3502b5-30cc-4473-ad48-42d51a6ef6d1
mitre_attack_url: https://attack.mitre.org/techniques/T1059/006
name: Python
platforms:
- Linux
- Windows
- macOS
tactics:
- execution
title: execution - Python
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Process: Process Creation, Command: Command Execution |
| **System Requirements** | Python is installed. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/006](https://attack.mitre.org/techniques/T1059/006) |

# Python (attack-pattern--cc3502b5-30cc-4473-ad48-42d51a6ef6d1)

## Description
Adversaries may abuse Python commands and scripts for execution. Python is a very popular scripting/programming language, with capabilities to perform many functions. Python can be executed interactively from the command-line (via the <code>python.exe</code> interpreter) or via scripts (.py) that can be written and distributed to different systems. Python code can also be compiled into binary executables.(Citation: Zscaler APT31 Covid-19 October 2020)

Python comes with many built-in packages to interact with the underlying system, such as file operations and device I/O. Adversaries can use these libraries to download and execute commands or other scripts as well as perform various malicious behaviors.

## Detection
Monitor systems for abnormal Python usage and python.exe behavior, which could be an indicator of malicious activity. Understanding standard usage patterns is important to avoid a high number of false positives. If scripting is restricted for normal users, then any attempts to enable scripts running on a system would be considered suspicious. If scripts are not commonly used on a system, but enabled, scripts running out of cycle from patching or other administrator functions are suspicious. Scripts should be captured from the file system when possible to determine their actions and intent.

Scripts are likely to perform actions with various effects on a system that may generate events, depending on the types of monitoring used. Monitor processes and command-line arguments for script execution and subsequent behavior. Actions may be related to network and system information Discovery, Collection, or other scriptable post-compromise behaviors and could be used as indicators of detection leading back to the source script.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/006)
- [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)
