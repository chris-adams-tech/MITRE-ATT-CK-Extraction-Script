---
contributors:
- Travis Smith, Tripwire
id: attack-pattern--04ee0cb7-dac3-4c6c-9387-4c6aa096f4cf
mitre_attack_url: https://attack.mitre.org/techniques/T1143
name: Hidden Window
platforms:
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Hidden Window
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1143](https://attack.mitre.org/techniques/T1143) |

# Hidden Window (attack-pattern--04ee0cb7-dac3-4c6c-9387-4c6aa096f4cf)

## Description
Adversaries may implement hidden windows to conceal malicious activity from the plain sight of users. In some cases, windows that would typically be displayed when an application carries out an operation can be hidden. This may be utilized by system administrators to avoid disrupting user work environments when carrying out administrative tasks. Adversaries may abuse operating system functionality to hide otherwise visible windows from users so as not to alert the user to adversary activity on the system.

### Windows
There are a variety of features in scripting languages in Windows, such as [PowerShell](https://attack.mitre.org/techniques/T1086), Jscript, and VBScript to make windows hidden. One example of this is <code>powershell.exe -WindowStyle Hidden</code>.  (Citation: PowerShell About 2019)

### Mac
The configurations for how applications run on macOS are listed in property list (plist) files. One of the tags in these files can be <code>apple.awt.UIElement</code>, which allows for Java applications to prevent the application's icon from appearing in the Dock. A common use for this is when applications run in the system tray, but don't also want to show up in the Dock. However, adversaries can abuse this feature and hide their running window.(Citation: Antiquated Mac Malware)


## Detection
Monitor processes and command-line arguments for actions indicative of hidden windows. In Windows, enable and configure event logging and PowerShell logging to check for the hidden window style. In MacOS, plist files are ASCII text files with a specific format, so they're relatively easy to parse. File monitoring can check for the <code>apple.awt.UIElement</code> or any other suspicious plist tag in plist files and flag them.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1143)
- [PowerShell About 2019](https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Core/About/about_PowerShell_exe?view=powershell-5.1)
- [Antiquated Mac Malware](https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/)
