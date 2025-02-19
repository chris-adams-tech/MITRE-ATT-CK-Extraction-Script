---
id: attack-pattern--7fd87010-3a00-4da3-b905-410525e8ec44
mitre_attack_url: https://attack.mitre.org/techniques/T1064
name: Scripting
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
- execution
title: defense-evasion - Scripting
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, execution |
| **Platforms** | Linux, macOS, Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1064](https://attack.mitre.org/techniques/T1064) |

# Scripting (attack-pattern--7fd87010-3a00-4da3-b905-410525e8ec44)

## Description
**This technique has been deprecated. Please use [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) where appropriate.**

Adversaries may use scripts to aid in operations and perform multiple actions that would otherwise be manual. Scripting is useful for speeding up operational tasks and reducing the time required to gain access to critical resources. Some scripting languages may be used to bypass process monitoring mechanisms by directly interacting with the operating system at an API level instead of calling other programs. Common scripting languages for Windows include VBScript and [PowerShell](https://attack.mitre.org/techniques/T1086) but could also be in the form of command-line batch scripts.

Scripts can be embedded inside Office documents as macros that can be set to execute when files used in [Spearphishing Attachment](https://attack.mitre.org/techniques/T1193) and other types of spearphishing are opened. Malicious embedded macros are an alternative means of execution than software exploitation through [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203), where adversaries will rely on macros being allowed or that the user will accept to activate them.

Many popular offensive frameworks exist which use forms of scripting for security testers and adversaries alike. Metasploit (Citation: Metasploit_Ref), Veil (Citation: Veil_Ref), and PowerSploit (Citation: Powersploit) are three examples that are popular among penetration testers for exploit and post-compromise operations and include many features for evading defenses. Some adversaries are known to use PowerShell. (Citation: Alperovitch 2014)

## Detection
Scripting may be common on admin, developer, or power user systems, depending on job function. If scripting is restricted for normal users, then any attempts to enable scripts running on a system would be considered suspicious. If scripts are not commonly used on a system, but enabled, scripts running out of cycle from patching or other administrator functions are suspicious. Scripts should be captured from the file system when possible to determine their actions and intent.

Scripts are likely to perform actions with various effects on a system that may generate events, depending on the types of monitoring used. Monitor processes and command-line arguments for script execution and subsequent behavior. Actions may be related to network and system information Discovery, Collection, or other scriptable post-compromise behaviors and could be used as indicators of detection leading back to the source script.

Analyze Office file attachments for potentially malicious macros. Execution of macros may create suspicious process trees depending on what the macro is designed to do. Office processes, such as winword.exe, spawning instances of cmd.exe, script application like wscript.exe or powershell.exe, or other suspicious processes may indicate malicious activity. (Citation: Uperesia Malicious Office Documents)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1064)
- [Metasploit_Ref](http://www.metasploit.com)
- [Veil_Ref](https://www.veil-framework.com/framework/)
- [Powersploit](https://github.com/mattifestation/PowerSploit)
- [Alperovitch 2014](https://blog.crowdstrike.com/deep-thought-chinese-targeting-national-security-think-tanks/)
- [Uperesia Malicious Office Documents](https://www.uperesia.com/analyzing-malicious-office-documents)
