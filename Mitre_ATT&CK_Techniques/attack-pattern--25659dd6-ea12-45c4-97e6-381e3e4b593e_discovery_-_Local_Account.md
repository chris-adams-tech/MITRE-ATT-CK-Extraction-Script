---
contributors:
- Daniel Stepanic, Elastic
- Miriam Wiesner, @miriamxyra, Microsoft Security
data_sources:
- 'Process: OS API Execution'
- 'Group: Group Enumeration'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'File: File Access'
id: attack-pattern--25659dd6-ea12-45c4-97e6-381e3e4b593e
mitre_attack_url: https://attack.mitre.org/techniques/T1087/001
name: Local Account
platforms:
- Linux
- macOS
- Windows
tactics:
- discovery
title: discovery - Local Account
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: OS API Execution, Group: Group Enumeration, Process: Process Creation, Command: Command Execution, File: File Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1087/001](https://attack.mitre.org/techniques/T1087/001) |

# Local Account (attack-pattern--25659dd6-ea12-45c4-97e6-381e3e4b593e)

## Description
Adversaries may attempt to get a listing of local system accounts. This information can help adversaries determine which local accounts exist on a system to aid in follow-on behavior.

Commands such as <code>net user</code> and <code>net localgroup</code> of the [Net](https://attack.mitre.org/software/S0039) utility and <code>id</code> and <code>groups</code> on macOS and Linux can list local users and groups.(Citation: Mandiant APT1)(Citation: id man page)(Citation: groups man page) On Linux, local users can also be enumerated through the use of the <code>/etc/passwd</code> file. On macOS the <code>dscl . list /Users</code> command can be used to enumerate local accounts.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

Monitor for processes that can be used to enumerate user accounts, such as <code>net.exe</code> and <code>net1.exe</code>, especially when executed in quick succession.(Citation: Elastic - Koadiac Detection with EQL)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1087/001)
- [id man page](https://linux.die.net/man/1/id)
- [groups man page](https://linux.die.net/man/1/groups)
- [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Elastic - Koadiac Detection with EQL](https://www.elastic.co/blog/embracing-offensive-tooling-building-detections-against-koadic-using-eql)
