---
data_sources:
- 'Windows Registry: Windows Registry Key Creation'
- 'Command: Command Execution'
- 'File: File Modification'
- 'Windows Registry: Windows Registry Key Modification'
- 'File: File Creation'
- 'Process: Process Creation'
- 'Module: Module Load'
id: attack-pattern--ed7efd4d-ce28-4a19-a8e6-c58011eb2c7a
mitre_attack_url: https://attack.mitre.org/techniques/T1137/002
name: Office Test
platforms:
- Windows
- Office Suite
tactics:
- persistence
title: persistence - Office Test
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, Office Suite |
| **Data Sources** | Windows Registry: Windows Registry Key Creation, Command: Command Execution, File: File Modification, Windows Registry: Windows Registry Key Modification, File: File Creation, Process: Process Creation, Module: Module Load |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1137/002](https://attack.mitre.org/techniques/T1137/002) |

# Office Test (attack-pattern--ed7efd4d-ce28-4a19-a8e6-c58011eb2c7a)

## Description
Adversaries may abuse the Microsoft Office "Office Test" Registry key to obtain persistence on a compromised system. An Office Test Registry location exists that allows a user to specify an arbitrary DLL that will be executed every time an Office application is started. This Registry key is thought to be used by Microsoft to load DLLs for testing and debugging purposes while developing Office applications. This Registry key is not created by default during an Office installation.(Citation: Hexacorn Office Test)(Citation: Palo Alto Office Test Sofacy)

There exist user and global Registry keys for the Office Test feature, such as:

* <code>HKEY_CURRENT_USER\Software\Microsoft\Office test\Special\Perf</code>
* <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Office test\Special\Perf</code>

Adversaries may add this Registry key and specify a malicious DLL that will be executed whenever an Office application, such as Word or Excel, is started.

## Detection
Monitor for the creation of the Office Test Registry key. Many Office-related persistence mechanisms require changes to the Registry and for binaries, files, or scripts to be written to disk or existing files modified to include malicious scripts. Collect events related to Registry key creation and modification for keys that could be used for Office-based persistence. Since v13.52, Autoruns can detect tasks set up using the Office Test Registry key.(Citation: Palo Alto Office Test Sofacy)

Consider monitoring Office processes for anomalous DLL loads.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1137/002)
- [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)
- [Hexacorn Office Test](http://www.hexacorn.com/blog/2014/04/16/beyond-good-ol-run-key-part-10/)
