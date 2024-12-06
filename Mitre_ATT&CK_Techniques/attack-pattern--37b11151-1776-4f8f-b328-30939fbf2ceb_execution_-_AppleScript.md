---
contributors:
- Phil Stokes, SentinelOne
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Process: OS API Execution'
id: attack-pattern--37b11151-1776-4f8f-b328-30939fbf2ceb
mitre_attack_url: https://attack.mitre.org/techniques/T1059/002
name: AppleScript
platforms:
- macOS
tactics:
- execution
title: execution - AppleScript
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | macOS |
| **Data Sources** | Command: Command Execution, Process: Process Creation, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/002](https://attack.mitre.org/techniques/T1059/002) |

# AppleScript (attack-pattern--37b11151-1776-4f8f-b328-30939fbf2ceb)

## Description
Adversaries may abuse AppleScript for execution. AppleScript is a macOS scripting language designed to control applications and parts of the OS via inter-application messages called AppleEvents.(Citation: Apple AppleScript) These AppleEvent messages can be sent independently or easily scripted with AppleScript. These events can locate open windows, send keystrokes, and interact with almost any open application locally or remotely.

Scripts can be run from the command-line via <code>osascript /path/to/script</code> or <code>osascript -e "script here"</code>. Aside from the command line, scripts can be executed in numerous ways including Mail rules, Calendar.app alarms, and Automator workflows. AppleScripts can also be executed as plain text shell scripts by adding <code>#!/usr/bin/osascript</code> to the start of the script file.(Citation: SentinelOne AppleScript)

AppleScripts do not need to call <code>osascript</code> to execute. However, they may be executed from within mach-O binaries by using the macOS [Native API](https://attack.mitre.org/techniques/T1106)s <code>NSAppleScript</code> or <code>OSAScript</code>, both of which execute code independent of the <code>/usr/bin/osascript</code> command line utility.

Adversaries may abuse AppleScript to execute various behaviors, such as interacting with an open SSH connection, moving to remote machines, and even presenting users with fake dialog boxes. These events cannot start applications remotely (they can start them locally), but they can interact with applications if they're already running remotely. On macOS 10.10 Yosemite and higher, AppleScript has the ability to execute [Native API](https://attack.mitre.org/techniques/T1106)s, which otherwise would require compilation and execution in a mach-O binary file format.(Citation: SentinelOne macOS Red Team) Since this is a scripting language, it can be used to launch more common techniques as well such as a reverse shell via [Python](https://attack.mitre.org/techniques/T1059/006).(Citation: Macro Malware Targets Macs)

## Detection
Monitor for execution of AppleScript through <code>osascript</code> and usage of the <code>NSAppleScript</code> and <code>OSAScript</code> APIs that may be related to other suspicious behavior occurring on the system. Scripts are likely to perform actions with various effects on a system that may generate events, depending on the types of monitoring used. Monitor processes and command-line arguments for script execution and subsequent behavior. Actions may be related to network and system information [Discovery](https://attack.mitre.org/tactics/TA0007), [Collection](https://attack.mitre.org/tactics/TA0009), or other scriptable post-compromise behaviors and could be used as indicators of detection leading back to the source script.

Understanding standard usage patterns is important to avoid a high number of false positives. If scripting is restricted for normal users, then any attempts to enable scripts running on a system would be considered suspicious. If scripts are not commonly used on a system, but enabled, scripts running out of cycle from patching or other administrator functions are suspicious. Scripts should be captured from the file system when possible to determine their actions and intent.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/002)
- [Apple AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [SentinelOne macOS Red Team](https://www.sentinelone.com/blog/macos-red-team-calling-apple-apis-without-building-binaries/)
- [SentinelOne AppleScript](https://www.sentinelone.com/blog/how-offensive-actors-use-applescript-for-attacking-macos/)
- [Macro Malware Targets Macs](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/macro-malware-targets-macs/)
