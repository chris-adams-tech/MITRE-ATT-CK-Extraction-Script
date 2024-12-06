---
contributors:
- Travis Smith, Tripwire
- Stefan Kanthak
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Modification'
id: attack-pattern--98034fef-d9fb-4667-8dc4-2eab6231724c
mitre_attack_url: https://attack.mitre.org/techniques/T1546/001
name: Change Default File Association
platforms:
- Windows
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Change Default File Association
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution, Windows Registry: Windows Registry Key Modification |
| **Permissions Required** | Administrator, SYSTEM, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/001](https://attack.mitre.org/techniques/T1546/001) |

# Change Default File Association (attack-pattern--98034fef-d9fb-4667-8dc4-2eab6231724c)

## Description
Adversaries may establish persistence by executing malicious content triggered by a file type association. When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility.(Citation: Microsoft Change Default Programs)(Citation: Microsoft File Handlers)(Citation: Microsoft Assoc Oct 2017) Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.

System file associations are listed under <code>HKEY_CLASSES_ROOT\.[extension]</code>, for example <code>HKEY_CLASSES_ROOT\.txt</code>. The entries point to a handler for that extension located at <code>HKEY_CLASSES_ROOT\\[handler]</code>. The various commands are then listed as subkeys underneath the shell key at <code>HKEY_CLASSES_ROOT\\[handler]\shell\\[action]\command</code>. For example: 

* <code>HKEY_CLASSES_ROOT\txtfile\shell\open\command</code>
* <code>HKEY_CLASSES_ROOT\txtfile\shell\print\command</code>
* <code>HKEY_CLASSES_ROOT\txtfile\shell\printto\command</code>

The values of the keys listed are commands that are executed when the handler opens the file extension. Adversaries can modify these values to continually execute arbitrary commands.(Citation: TrendMicro TROJ-FAKEAV OCT 2012)

## Detection
Collect and analyze changes to Registry keys that associate file extensions to default applications for execution and correlate with unknown process launch activity or unusual file types for that process.

User file association preferences are stored under <code> [HKEY_CURRENT_USER]\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts</code> and override associations configured under <code>[HKEY_CLASSES_ROOT]</code>. Changes to a user's preference will occur under this entry's subkeys.

Also look for abnormal process call trees for execution of other commands that could relate to Discovery actions or other techniques.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/001)
- [Microsoft Change Default Programs](https://support.microsoft.com/en-us/help/18539/windows-7-change-default-programs)
- [Microsoft File Handlers](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/extensibility/specifying-file-handlers-for-file-name-extensions?view=vs-2015)
- [Microsoft Assoc Oct 2017](https://docs.microsoft.com/windows-server/administration/windows-commands/assoc)
- [TrendMicro TROJ-FAKEAV OCT 2012](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/troj_fakeav.gzd)
