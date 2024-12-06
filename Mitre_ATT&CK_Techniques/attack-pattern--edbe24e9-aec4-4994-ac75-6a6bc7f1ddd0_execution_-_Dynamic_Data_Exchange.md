---
id: attack-pattern--edbe24e9-aec4-4994-ac75-6a6bc7f1ddd0
mitre_attack_url: https://attack.mitre.org/techniques/T1173
name: Dynamic Data Exchange
platforms:
- Windows
tactics:
- execution
title: execution - Dynamic Data Exchange
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1173](https://attack.mitre.org/techniques/T1173) |

# Dynamic Data Exchange (attack-pattern--edbe24e9-aec4-4994-ac75-6a6bc7f1ddd0)

## Description
Windows Dynamic Data Exchange (DDE) is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links (duplications of changes to a data item), and requests for command execution.

Object Linking and Embedding (OLE), or the ability to link data between documents, was originally implemented through DDE. Despite being superseded by COM, DDE may be enabled in Windows 10 and most of Microsoft Office 2016 via Registry keys. (Citation: BleepingComputer DDE Disabled in Word Dec 2017) (Citation: Microsoft ADV170021 Dec 2017) (Citation: Microsoft DDE Advisory Nov 2017)

Adversaries may use DDE to execute arbitrary commands. Microsoft Office documents can be poisoned with DDE commands (Citation: SensePost PS DDE May 2016) (Citation: Kettle CSV DDE Aug 2014), directly or through embedded files (Citation: Enigma Reviving DDE Jan 2018), and used to deliver execution via phishing campaigns or hosted Web content, avoiding the use of Visual Basic for Applications (VBA) macros. (Citation: SensePost MacroLess DDE Oct 2017) DDE could also be leveraged by an adversary operating on a compromised machine who does not have direct access to command line execution.

## Detection
OLE and Office Open XML files can be scanned for ‘DDEAUTO', ‘DDE’, and other strings indicative of DDE execution. (Citation: NVisio Labs DDE Detection Oct 2017)

Monitor for Microsoft Office applications loading DLLs and other modules not typically associated with the application.

Monitor for spawning of unusual processes (such as cmd.exe) from Microsoft Office applications.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1173)
- [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)
- [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)
- [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)
- [SensePost PS DDE May 2016](https://sensepost.com/blog/2016/powershell-c-sharp-and-dde-the-power-within/)
- [Kettle CSV DDE Aug 2014](https://www.contextis.com/blog/comma-separated-vulnerabilities)
- [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)
- [SensePost MacroLess DDE Oct 2017](https://sensepost.com/blog/2017/macro-less-code-exec-in-msword/)
- [NVisio Labs DDE Detection Oct 2017](https://blog.nviso.be/2017/10/11/detecting-dde-in-ms-office-documents/)
