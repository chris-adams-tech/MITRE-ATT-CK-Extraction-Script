---
contributors:
- Cody Thomas, SpecterOps
data_sources:
- 'Module: Module Load'
- 'Process: Process Creation'
- 'Script: Script Execution'
- 'Command: Command Execution'
id: attack-pattern--0f4a0c76-ab2d-4cb0-85d3-3f0efb8cba0d
mitre_attack_url: https://attack.mitre.org/techniques/T1059/007
name: JavaScript
platforms:
- Windows
- macOS
- Linux
tactics:
- execution
title: execution - JavaScript
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Module: Module Load, Process: Process Creation, Script: Script Execution, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/007](https://attack.mitre.org/techniques/T1059/007) |

# JavaScript (attack-pattern--0f4a0c76-ab2d-4cb0-85d3-3f0efb8cba0d)

## Description
Adversaries may abuse various implementations of JavaScript for execution. JavaScript (JS) is a platform-independent scripting language (compiled just-in-time at runtime) commonly associated with scripts in webpages, though JS can be executed in runtime environments outside the browser.(Citation: NodeJS)

JScript is the Microsoft implementation of the same scripting standard. JScript is interpreted via the Windows Script engine and thus integrated with many components of Windows such as the [Component Object Model](https://attack.mitre.org/techniques/T1559/001) and Internet Explorer HTML Application (HTA) pages.(Citation: JScrip May 2018)(Citation: Microsoft JScript 2007)(Citation: Microsoft Windows Scripts)

JavaScript for Automation (JXA) is a macOS scripting language based on JavaScript, included as part of Apple’s Open Scripting Architecture (OSA), that was introduced in OSX 10.10. Apple’s OSA provides scripting capabilities to control applications, interface with the operating system, and bridge access into the rest of Apple’s internal APIs. As of OSX 10.10, OSA only supports two languages, JXA and [AppleScript](https://attack.mitre.org/techniques/T1059/002). Scripts can be executed via the command line utility <code>osascript</code>, they can be compiled into applications or script files via <code>osacompile</code>, and they can be compiled and executed in memory of other programs by leveraging the OSAKit Framework.(Citation: Apple About Mac Scripting 2016)(Citation: SpecterOps JXA 2020)(Citation: SentinelOne macOS Red Team)(Citation: Red Canary Silver Sparrow Feb2021)(Citation: MDSec macOS JXA and VSCode)

Adversaries may abuse various implementations of JavaScript to execute various behaviors. Common uses include hosting malicious scripts on websites as part of a [Drive-by Compromise](https://attack.mitre.org/techniques/T1189) or downloading and executing these script files as secondary payloads. Since these payloads are text-based, it is also very common for adversaries to obfuscate their content as part of [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027).

## Detection
Monitor for events associated with scripting execution, such as process activity, usage of the Windows Script Host (typically cscript.exe or wscript.exe), file activity involving scripts, or loading of modules associated with scripting languages (ex: JScript.dll). Scripting execution is likely to perform actions with various effects on a system that may generate events, depending on the types of monitoring used. Monitor processes and command-line arguments for execution and subsequent behavior. Actions may be related to network and system information [Discovery](https://attack.mitre.org/tactics/TA0007), [Collection](https://attack.mitre.org/tactics/TA0009), or other programmable post-compromise behaviors and could be used as indicators of detection leading back to the source.

Monitor for execution of JXA through <code>osascript</code> and usage of <code>OSAScript</code> API that may be related to other suspicious behavior occurring on the system.

Understanding standard usage patterns is important to avoid a high number of false positives. If scripting is restricted for normal users, then any attempts to enable related components running on a system would be considered suspicious. If scripting is not commonly used on a system, but enabled, execution running out of cycle from patching or other administrator functions is suspicious. Scripts should be captured from the file system when possible to determine their actions and intent.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/007)
- [Apple About Mac Scripting 2016](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/index.html)
- [MDSec macOS JXA and VSCode](https://www.mdsec.co.uk/2021/01/macos-post-exploitation-shenanigans-with-vscode-extensions/)
- [Microsoft JScript 2007](https://docs.microsoft.com/archive/blogs/gauravseth/the-world-of-jscript-javascript-ecmascript)
- [Microsoft Windows Scripts](https://docs.microsoft.com/scripting/winscript/windows-script-interfaces)
- [JScrip May 2018](https://docs.microsoft.com/windows/win32/com/translating-to-jscript)
- [NodeJS](https://nodejs.org/)
- [SentinelOne macOS Red Team](https://www.sentinelone.com/blog/macos-red-team-calling-apple-apis-without-building-binaries/)
- [SpecterOps JXA 2020](https://posts.specterops.io/persistent-jxa-66e1c3cd1cf5)
- [Red Canary Silver Sparrow Feb2021](https://redcanary.com/blog/clipping-silver-sparrows-wings/)
