---
contributors:
- Vikas Singh, Sophos
- Emile Kenning, Sophos
- Austin Clark, @c2defense
data_sources:
- 'Sensor Health: Host Status'
- 'Command: Command Execution'
id: attack-pattern--8f504411-cb96-4dac-a537-8d2bb7679c59
mitre_attack_url: https://attack.mitre.org/techniques/T1562/003
name: Impair Command History Logging
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- defense-evasion
title: defense-evasion - Impair Command History Logging
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Sensor Health: Host Status, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/003](https://attack.mitre.org/techniques/T1562/003) |

# Impair Command History Logging (attack-pattern--8f504411-cb96-4dac-a537-8d2bb7679c59)

## Description
Adversaries may impair command history logging to hide commands they run on a compromised system. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done. 

On Linux and macOS, command history is tracked in a file pointed to by the environment variable <code>HISTFILE</code>. When a user logs off a system, this information is flushed to a file in the user's home directory called <code>~/.bash_history</code>. The <code>HISTCONTROL</code> environment variable keeps track of what should be saved by the <code>history</code> command and eventually into the <code>~/.bash_history</code> file when a user logs out. <code>HISTCONTROL</code> does not exist by default on macOS, but can be set by the user and will be respected.

Adversaries may clear the history environment variable (<code>unset HISTFILE</code>) or set the command history size to zero (<code>export HISTFILESIZE=0</code>) to prevent logging of commands. Additionally, <code>HISTCONTROL</code> can be configured to ignore commands that start with a space by simply setting it to "ignorespace". <code>HISTCONTROL</code> can also be set to ignore duplicate commands by setting it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples. This means that “ ls” will not be saved, but “ls” would be saved by history. Adversaries can abuse this to operate without leaving traces by simply prepending a space to all of their terminal commands. 

On Windows systems, the <code>PSReadLine</code> module tracks commands used in all PowerShell sessions and writes them to a file (<code>$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt</code> by default). Adversaries may change where these logs are saved using <code>Set-PSReadLineOption -HistorySavePath {File Path}</code>. This will cause <code>ConsoleHost_history.txt</code> to stop receiving logs. Additionally, it is possible to turn off logging to this file using the PowerShell command <code>Set-PSReadlineOption -HistorySaveStyle SaveNothing</code>.(Citation: Microsoft PowerShell Command History)(Citation: Sophos PowerShell command audit)(Citation: Sophos PowerShell Command History Forensics)

Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to disable historical command logging (e.g. <code>no logging</code>).

## Detection
Correlating a user session with a distinct lack of new commands in their <code>.bash_history</code> can be a clue to suspicious behavior. Additionally, users checking or changing their <code>HISTCONTROL</code>, <code>HISTFILE</code>, or <code>HISTFILESIZE</code> environment variables may be suspicious.

Monitor for modification of PowerShell command history settings through processes being created with <code>-HistorySaveStyle SaveNothing</code> command-line arguments and use of the PowerShell commands <code>Set-PSReadlineOption -HistorySaveStyle SaveNothing</code> and <code>Set-PSReadLineOption -HistorySavePath {File Path}</code>. Further, [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands may also be used to clear or disable historical log data with built-in features native to the network device platform.  Monitor such command activity for unexpected or unauthorized use of commands being run by non-standard users from non-standard locations.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/003)
- [Sophos PowerShell command audit](https://community.sophos.com/products/intercept/early-access-program/f/live-discover-response-queries/121529/live-discover---powershell-command-audit)
- [Microsoft PowerShell Command History](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_history?view=powershell-7)
- [Sophos PowerShell Command History Forensics](https://community.sophos.com/products/malware/b/blog/posts/powershell-command-history-forensics)
