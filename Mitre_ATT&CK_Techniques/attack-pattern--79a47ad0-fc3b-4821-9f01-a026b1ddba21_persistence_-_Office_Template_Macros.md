---
data_sources:
- 'File: File Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Creation'
- 'File: File Modification'
id: attack-pattern--79a47ad0-fc3b-4821-9f01-a026b1ddba21
mitre_attack_url: https://attack.mitre.org/techniques/T1137/001
name: Office Template Macros
platforms:
- Windows
- Office Suite
tactics:
- persistence
title: persistence - Office Template Macros
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | File: File Creation, Windows Registry: Windows Registry Key Modification, Command: Command Execution, Process: Process Creation, Windows Registry: Windows Registry Key Creation, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1137/001](https://attack.mitre.org/techniques/T1137/001) |

# Office Template Macros (attack-pattern--79a47ad0-fc3b-4821-9f01-a026b1ddba21)

## Description
Adversaries may abuse Microsoft Office templates to obtain persistence on a compromised system. Microsoft Office contains templates that are part of common Office applications and are used to customize styles. The base templates within the application are used each time an application starts. (Citation: Microsoft Change Normal Template)

Office Visual Basic for Applications (VBA) macros (Citation: MSDN VBA in Office) can be inserted into the base template and used to execute code when the respective Office application starts in order to obtain persistence. Examples for both Word and Excel have been discovered and published. By default, Word has a Normal.dotm template created that can be modified to include a malicious macro. Excel does not have a template file created by default, but one can be added that will automatically be loaded.(Citation: enigma0x3 normal.dotm)(Citation: Hexacorn Office Template Macros) Shared templates may also be stored and pulled from remote locations.(Citation: GlobalDotName Jun 2019) 

Word Normal.dotm location:<br>
<code>C:\Users\&lt;username&gt;\AppData\Roaming\Microsoft\Templates\Normal.dotm</code>

Excel Personal.xlsb location:<br>
<code>C:\Users\&lt;username&gt;\AppData\Roaming\Microsoft\Excel\XLSTART\PERSONAL.XLSB</code>

Adversaries may also change the location of the base template to point to their own by hijacking the application's search order, e.g. Word 2016 will first look for Normal.dotm under <code>C:\Program Files (x86)\Microsoft Office\root\Office16\</code>, or by modifying the GlobalDotName registry key. By modifying the GlobalDotName registry key an adversary can specify an arbitrary location, file name, and file extension to use for the template that will be loaded on application startup. To abuse GlobalDotName, adversaries may first need to register the template as a trusted document or place it in a trusted location.(Citation: GlobalDotName Jun 2019) 

An adversary may need to enable macros to execute unrestricted depending on the system or enterprise security policy on use of macros.

## Detection
Many Office-related persistence mechanisms require changes to the Registry and for binaries, files, or scripts to be written to disk or existing files modified to include malicious scripts. Collect events related to Registry key creation and modification for keys that could be used for Office-based persistence.(Citation: CrowdStrike Outlook Forms)(Citation: Outlook Today Home Page) Modification to base templates, like Normal.dotm, should also be investigated since the base templates should likely not contain VBA macros. Changes to the Office macro security settings should also be investigated.(Citation: GlobalDotName Jun 2019)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1137/001)
- [MSDN VBA in Office](https://msdn.microsoft.com/en-us/vba/office-shared-vba/articles/getting-started-with-vba-in-office)
- [Hexacorn Office Template Macros](http://www.hexacorn.com/blog/2017/04/19/beyond-good-ol-run-key-part-62/)
- [Microsoft Change Normal Template](https://support.office.com/article/Change-the-Normal-template-Normal-dotm-06de294b-d216-47f6-ab77-ccb5166f98ea)
- [enigma0x3 normal.dotm](https://enigma0x3.net/2014/01/23/maintaining-access-with-normal-dotm/comment-page-1/)
- [CrowdStrike Outlook Forms](https://malware.news/t/using-outlook-forms-for-lateral-movement-and-persistence/13746)
- [GlobalDotName Jun 2019](https://www.221bluestreet.com/post/office-templates-and-globaldotname-a-stealthy-office-persistence-technique)
- [Outlook Today Home Page](https://medium.com/@bwtech789/outlook-today-homepage-persistence-33ea9b505943)
