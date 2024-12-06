---
contributors:
- Stefan Kanthak
- Travis Smith, Tripwire
id: attack-pattern--68c96494-1a50-403e-8844-69a6af278c68
mitre_attack_url: https://attack.mitre.org/techniques/T1042
name: Change Default File Association
platforms:
- Windows
tactics:
- persistence
title: persistence - Change Default File Association
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows |
| **Permissions Required** | User, Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1042](https://attack.mitre.org/techniques/T1042) |

# Change Default File Association (attack-pattern--68c96494-1a50-403e-8844-69a6af278c68)

## Description
When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access (Citation: Microsoft Change Default Programs) (Citation: Microsoft File Handlers) or by administrators using the built-in assoc utility. (Citation: Microsoft Assoc Oct 2017) Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.

System file associations are listed under <code>HKEY_CLASSES_ROOT\.[extension]</code>, for example <code>HKEY_CLASSES_ROOT\.txt</code>. The entries point to a handler for that extension located at <code>HKEY_CLASSES_ROOT\[handler]</code>. The various commands are then listed as subkeys underneath the shell key at <code>HKEY_CLASSES_ROOT\[handler]\shell\[action]\command</code>. For example:
* <code>HKEY_CLASSES_ROOT\txtfile\shell\open\command</code>
* <code>HKEY_CLASSES_ROOT\txtfile\shell\print\command</code>
* <code>HKEY_CLASSES_ROOT\txtfile\shell\printto\command</code>

The values of the keys listed are commands that are executed when the handler opens the file extension. Adversaries can modify these values to continually execute arbitrary commands. (Citation: TrendMicro TROJ-FAKEAV OCT 2012)

## Detection
Collect and analyze changes to Registry keys that associate file extensions to default applications for execution and correlate with unknown process launch activity or unusual file types for that process. 

User file association preferences are stored under <code> [HKEY_CURRENT_USER]\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts</code> and override associations configured under <code>[HKEY_CLASSES_ROOT]</code>. Changes to a user's preference will occur under this entry's subkeys.

Also look for abnormal process call trees for execution of other commands that could relate to Discovery actions or other techniques.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1042)
- [capec](https://capec.mitre.org/data/definitions/556.html)
- [Microsoft Change Default Programs](https://support.microsoft.com/en-us/help/18539/windows-7-change-default-programs)
- [Microsoft File Handlers](http://msdn.microsoft.com/en-us/library/bb166549.aspx)
- [Microsoft Assoc Oct 2017](https://docs.microsoft.com/windows-server/administration/windows-commands/assoc)
- [TrendMicro TROJ-FAKEAV OCT 2012](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/troj_fakeav.gzd)
