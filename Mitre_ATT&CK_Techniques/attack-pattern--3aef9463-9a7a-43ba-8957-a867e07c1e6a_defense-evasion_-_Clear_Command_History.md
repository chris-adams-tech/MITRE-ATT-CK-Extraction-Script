---
contributors:
- Vikas Singh, Sophos
- Emile Kenning, Sophos
- Austin Clark, @c2defense
data_sources:
- 'Process: Process Creation'
- 'File: File Deletion'
- 'File: File Modification'
- 'Command: Command Execution'
- 'User Account: User Account Authentication'
id: attack-pattern--3aef9463-9a7a-43ba-8957-a867e07c1e6a
mitre_attack_url: https://attack.mitre.org/techniques/T1070/003
name: Clear Command History
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- defense-evasion
title: defense-evasion - Clear Command History
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Process: Process Creation, File: File Deletion, File: File Modification, Command: Command Execution, User Account: User Account Authentication |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1070/003](https://attack.mitre.org/techniques/T1070/003) |

# Clear Command History (attack-pattern--3aef9463-9a7a-43ba-8957-a867e07c1e6a)

## Description
In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done.

On Linux and macOS, these command histories can be accessed in a few different ways. While logged in, this command history is tracked in a file pointed to by the environment variable <code>HISTFILE</code>. When a user logs off a system, this information is flushed to a file in the user's home directory called <code>~/.bash_history</code>. The benefit of this is that it allows users to go back to commands they've used before in different sessions.

Adversaries may delete their commands from these logs by manually clearing the history (<code>history -c</code>) or deleting the bash history file <code>rm ~/.bash_history</code>.  

Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to clear command history data (<code>clear logging</code> and/or <code>clear history</code>).(Citation: US-CERT-TA18-106A)

On Windows hosts, PowerShell has two different command history providers: the built-in history and the command history managed by the <code>PSReadLine</code> module. The built-in history only tracks the commands used in the current session. This command history is not available to other sessions and is deleted when the session ends.

The <code>PSReadLine</code> command history tracks the commands used in all PowerShell sessions and writes them to a file (<code>$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt</code> by default). This history file is available to all sessions and contains all past history since the file is not deleted when the session ends.(Citation: Microsoft PowerShell Command History)

Adversaries may run the PowerShell command <code>Clear-History</code> to flush the entire command history from a current PowerShell session. This, however, will not delete/flush the <code>ConsoleHost_history.txt</code> file. Adversaries may also delete the <code>ConsoleHost_history.txt</code> file or edit its contents to hide PowerShell commands they have run.(Citation: Sophos PowerShell command audit)(Citation: Sophos PowerShell Command History Forensics)

## Detection
User authentication, especially via remote terminal services like SSH, without new entries in that user's <code>~/.bash_history</code> is suspicious. Additionally, the removal/clearing of the <code>~/.bash_history</code> file can be an indicator of suspicious activity.

Monitor for suspicious modifications or deletion of <code>ConsoleHost_history.txt</code> and use of the <code>Clear-History</code> command.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1070/003)
- [Sophos PowerShell command audit](https://community.sophos.com/products/intercept/early-access-program/f/live-discover-response-queries/121529/live-discover---powershell-command-audit)
- [Microsoft PowerShell Command History](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_history?view=powershell-7)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [Sophos PowerShell Command History Forensics](https://community.sophos.com/products/malware/b/blog/posts/powershell-command-history-forensics)
