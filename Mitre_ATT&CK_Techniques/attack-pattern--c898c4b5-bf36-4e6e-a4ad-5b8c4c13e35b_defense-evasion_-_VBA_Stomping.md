---
contributors:
- Rick Cole, Mandiant
data_sources:
- 'File: File Metadata'
- 'Script: Script Execution'
id: attack-pattern--c898c4b5-bf36-4e6e-a4ad-5b8c4c13e35b
mitre_attack_url: https://attack.mitre.org/techniques/T1564/007
name: VBA Stomping
platforms:
- Linux
- Windows
- macOS
tactics:
- defense-evasion
title: defense-evasion - VBA Stomping
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | File: File Metadata, Script: Script Execution |
| **Permissions Required** | User |
| **System Requirements** | MS Office version specified in <code>_VBA_PROJECT</code> stream must match host |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1564/007](https://attack.mitre.org/techniques/T1564/007) |

# VBA Stomping (attack-pattern--c898c4b5-bf36-4e6e-a4ad-5b8c4c13e35b)

## Description
Adversaries may hide malicious Visual Basic for Applications (VBA) payloads embedded within MS Office documents by replacing the VBA source code with benign data.(Citation: FireEye VBA stomp Feb 2020)

MS Office documents with embedded VBA content store source code inside of module streams. Each module stream has a <code>PerformanceCache</code> that stores a separate compiled version of the VBA source code known as p-code. The p-code is executed when the MS Office version specified in the <code>_VBA_PROJECT</code> stream (which contains the version-dependent description of the VBA project) matches the version of the host MS Office application.(Citation: Evil Clippy May 2019)(Citation: Microsoft _VBA_PROJECT Stream)

An adversary may hide malicious VBA code by overwriting the VBA source code location with zero’s, benign code, or random bytes while leaving the previously compiled malicious p-code. Tools that scan for malicious VBA source code may be bypassed as the unwanted code is hidden in the compiled p-code. If the VBA source code is removed, some tools might even think that there are no macros present. If there is a version match between the <code>_VBA_PROJECT</code> stream and host MS Office application, the p-code will be executed, otherwise the benign VBA source code will be decompressed and recompiled to p-code, thus removing malicious p-code and potentially bypassing dynamic analysis.(Citation: Walmart Roberts Oct 2018)(Citation: FireEye VBA stomp Feb 2020)(Citation: pcodedmp Bontchev)

## Detection
Detection efforts should be placed finding differences between VBA source code and p-code.(Citation: Walmart Roberts Oct 2018) VBA code can be extracted from p-code before execution with tools such as the pcodedmp disassembler. The oletools toolkit leverages the pcodedmp disassembler to detect VBA stomping by comparing keywords present in the VBA source code and p-code.(Citation: pcodedmp Bontchev)(Citation: oletools toolkit)

If the document is opened with a Graphical User Interface (GUI) the malicious p-code is decompiled and may be viewed. However, if the <code>PROJECT</code> stream, which specifies the project properties, is modified in a specific way the decompiled VBA code will not be displayed. For example, adding a module name that is undefined to the <code>PROJECT</code> stream will inhibit attempts of reading the VBA source code through the GUI.(Citation: FireEye VBA stomp Feb 2020)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1564/007)
- [FireEye VBA stomp Feb 2020](https://www.fireeye.com/blog/threat-research/2020/01/stomp-2-dis-brilliance-in-the-visual-basics.html)
- [Evil Clippy May 2019](https://outflank.nl/blog/2019/05/05/evil-clippy-ms-office-maldoc-assistant/)
- [Microsoft _VBA_PROJECT Stream](https://docs.microsoft.com/en-us/openspecs/office_file_formats/ms-ovba/ef7087ac-3974-4452-aab2-7dba2214d239)
- [Walmart Roberts Oct 2018](https://medium.com/walmartglobaltech/vba-stomping-advanced-maldoc-techniques-612c484ab278)
- [pcodedmp Bontchev](https://github.com/bontchev/pcodedmp)
- [oletools toolkit](https://github.com/decalage2/oletools)
