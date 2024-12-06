---
contributors:
- Travis Smith, Tripwire
- Mark Tsipershtein
data_sources:
- 'File: File Modification'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Script: Script Execution'
id: attack-pattern--cbb66055-0325-4111-aca0-40547b6ad5b0
mitre_attack_url: https://attack.mitre.org/techniques/T1564/003
name: Hidden Window
platforms:
- macOS
- Windows
- Linux
tactics:
- defense-evasion
title: defense-evasion - Hidden Window
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Windows, Linux |
| **Data Sources** | File: File Modification, Command: Command Execution, Process: Process Creation, Script: Script Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1564/003](https://attack.mitre.org/techniques/T1564/003) |

# Hidden Window (attack-pattern--cbb66055-0325-4111-aca0-40547b6ad5b0)

## Description
Adversaries may use hidden windows to conceal malicious activity from the plain sight of users. In some cases, windows that would typically be displayed when an application carries out an operation can be hidden. This may be utilized by system administrators to avoid disrupting user work environments when carrying out administrative tasks. 

Adversaries may abuse these functionalities to hide otherwise visible windows from users so as not to alert the user to adversary activity on the system.(Citation: Antiquated Mac Malware)

On macOS, the configurations for how applications run are listed in property list (plist) files. One of the tags in these files can be <code>apple.awt.UIElement</code>, which allows for Java applications to prevent the application's icon from appearing in the Dock. A common use for this is when applications run in the system tray, but don't also want to show up in the Dock.

Similarly, on Windows there are a variety of features in scripting languages, such as [PowerShell](https://attack.mitre.org/techniques/T1059/001), Jscript, and [Visual Basic](https://attack.mitre.org/techniques/T1059/005) to make windows hidden. One example of this is <code>powershell.exe -WindowStyle Hidden</code>.(Citation: PowerShell About 2019)

In addition, Windows supports the `CreateDesktop()` API that can create a hidden desktop window with its own corresponding <code>explorer.exe</code> process.(Citation: Hidden VNC)(Citation: Anatomy of an hVNC Attack)  All applications running on the hidden desktop window, such as a hidden VNC (hVNC) session,(Citation: Hidden VNC) will be invisible to other desktops windows.

## Detection
Monitor processes and command-line arguments for actions indicative of hidden windows. In Windows, enable and configure event logging and PowerShell logging to check for the hidden window style. In MacOS, plist files are ASCII text files with a specific format, so they're relatively easy to parse. File monitoring can check for the <code>apple.awt.UIElement</code> or any other suspicious plist tag in plist files and flag them.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1564/003)
- [Hidden VNC](https://www.malwaretech.com/2015/09/hidden-vnc-for-beginners.html)
- [Anatomy of an hVNC Attack](https://securityintelligence.com/anatomy-of-an-hvnc-attack/)
- [Antiquated Mac Malware](https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/)
- [PowerShell About 2019](https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Core/About/about_PowerShell_exe?view=powershell-5.1)
