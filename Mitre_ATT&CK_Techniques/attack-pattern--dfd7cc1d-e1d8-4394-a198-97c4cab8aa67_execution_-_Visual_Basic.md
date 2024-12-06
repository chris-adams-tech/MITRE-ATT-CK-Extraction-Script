---
data_sources:
- 'Module: Module Load'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Script: Script Execution'
id: attack-pattern--dfd7cc1d-e1d8-4394-a198-97c4cab8aa67
mitre_attack_url: https://attack.mitre.org/techniques/T1059/005
name: Visual Basic
platforms:
- Windows
- macOS
- Linux
tactics:
- execution
title: execution - Visual Basic
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Module: Module Load, Command: Command Execution, Process: Process Creation, Script: Script Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/005](https://attack.mitre.org/techniques/T1059/005) |

# Visual Basic (attack-pattern--dfd7cc1d-e1d8-4394-a198-97c4cab8aa67)

## Description
Adversaries may abuse Visual Basic (VB) for execution. VB is a programming language created by Microsoft with interoperability with many Windows technologies such as [Component Object Model](https://attack.mitre.org/techniques/T1559/001) and the [Native API](https://attack.mitre.org/techniques/T1106) through the Windows API. Although tagged as legacy with no planned future evolutions, VB is integrated and supported in the .NET Framework and cross-platform .NET Core.(Citation: VB .NET Mar 2020)(Citation: VB Microsoft)

Derivative languages based on VB have also been created, such as Visual Basic for Applications (VBA) and VBScript. VBA is an event-driven programming language built into Microsoft Office, as well as several third-party applications.(Citation: Microsoft VBA)(Citation: Wikipedia VBA) VBA enables documents to contain macros used to automate the execution of tasks and other functionality on the host. VBScript is a default scripting language on Windows hosts and can also be used in place of [JavaScript](https://attack.mitre.org/techniques/T1059/007) on HTML Application (HTA) webpages served to Internet Explorer (though most modern browsers do not come with VBScript support).(Citation: Microsoft VBScript)

Adversaries may use VB payloads to execute malicious commands. Common malicious usage includes automating execution of behaviors with VBScript or embedding VBA content into [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001) payloads (which may also involve [Mark-of-the-Web Bypass](https://attack.mitre.org/techniques/T1553/005) to enable execution).(Citation: Default VBS macros Blocking )

## Detection
Monitor for events associated with VB execution, such as Office applications spawning processes, usage of the Windows Script Host (typically cscript.exe or wscript.exe), file activity involving VB payloads or scripts, or loading of modules associated with VB languages (ex: vbscript.dll). VB execution is likely to perform actions with various effects on a system that may generate events, depending on the types of monitoring used. Monitor processes and command-line arguments for execution and subsequent behavior. Actions may be related to network and system information [Discovery](https://attack.mitre.org/tactics/TA0007), [Collection](https://attack.mitre.org/tactics/TA0009), or other programable post-compromise behaviors and could be used as indicators of detection leading back to the source.

Understanding standard usage patterns is important to avoid a high number of false positives. If VB execution is restricted for normal users, then any attempts to enable related components running on a system would be considered suspicious. If VB execution is not commonly used on a system, but enabled, execution running out of cycle from patching or other administrator functions is suspicious. Payloads and scripts should be captured from the file system when possible to determine their actions and intent.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/005)
- [VB .NET Mar 2020](https://devblogs.microsoft.com/vbteam/visual-basic-support-planned-for-net-5-0/)
- [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)
- [Microsoft VBScript](https://docs.microsoft.com/previous-versions//1kw29xwf(v=vs.85))
- [Microsoft VBA](https://docs.microsoft.com/office/vba/api/overview/)
- [VB Microsoft](https://docs.microsoft.com/dotnet/visual-basic/)
- [Wikipedia VBA](https://en.wikipedia.org/wiki/Visual_Basic_for_Applications)
