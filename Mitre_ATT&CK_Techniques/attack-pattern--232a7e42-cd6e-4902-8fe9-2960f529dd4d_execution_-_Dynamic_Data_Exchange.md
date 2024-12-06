---
data_sources:
- 'Process: Process Creation'
- 'Module: Module Load'
- 'Script: Script Execution'
id: attack-pattern--232a7e42-cd6e-4902-8fe9-2960f529dd4d
mitre_attack_url: https://attack.mitre.org/techniques/T1559/002
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
| **Data Sources** | Process: Process Creation, Module: Module Load, Script: Script Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1559/002](https://attack.mitre.org/techniques/T1559/002) |

# Dynamic Data Exchange (attack-pattern--232a7e42-cd6e-4902-8fe9-2960f529dd4d)

## Description
Adversaries may use Windows Dynamic Data Exchange (DDE) to execute arbitrary commands. DDE is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links (duplications of changes to a data item), and requests for command execution.

Object Linking and Embedding (OLE), or the ability to link data between documents, was originally implemented through DDE. Despite being superseded by [Component Object Model](https://attack.mitre.org/techniques/T1559/001), DDE may be enabled in Windows 10 and most of Microsoft Office 2016 via Registry keys.(Citation: BleepingComputer DDE Disabled in Word Dec 2017)(Citation: Microsoft ADV170021 Dec 2017)(Citation: Microsoft DDE Advisory Nov 2017)

Microsoft Office documents can be poisoned with DDE commands, directly or through embedded files, and used to deliver execution via [Phishing](https://attack.mitre.org/techniques/T1566) campaigns or hosted Web content, avoiding the use of Visual Basic for Applications (VBA) macros.(Citation: SensePost PS DDE May 2016)(Citation: Kettle CSV DDE Aug 2014)(Citation: Enigma Reviving DDE Jan 2018)(Citation: SensePost MacroLess DDE Oct 2017) Similarly, adversaries may infect payloads to execute applications and/or commands on a victim device by way of embedding DDE formulas within a CSV file intended to be opened through a Windows spreadsheet program.(Citation: OWASP CSV Injection)(Citation: CSV Excel Macro Injection )

DDE could also be leveraged by an adversary operating on a compromised machine who does not have direct access to a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059). DDE execution can be invoked remotely via [Remote Services](https://attack.mitre.org/techniques/T1021) such as [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) (DCOM).(Citation: Fireeye Hunting COM June 2019)

## Detection
Monitor processes for abnormal behavior indicative of DDE abuse, such as Microsoft Office applications loading DLLs and other modules not typically associated with the application or these applications spawning unusual processes (such as cmd.exe).

OLE, Office Open XML, CSV, and other files can be scanned for ‘DDEAUTO', ‘DDE’, and other strings indicative of DDE execution.(Citation: NVisio Labs DDE Detection Oct 2017)(Citation: OWASP CSV Injection)(Citation: CSV Excel Macro Injection )

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1559/002)
- [OWASP CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection)
- [CSV Excel Macro Injection ](https://blog.securelayer7.net/how-to-perform-csv-excel-macro-injection/)
- [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)
- [SensePost PS DDE May 2016](https://sensepost.com/blog/2016/powershell-c-sharp-and-dde-the-power-within/)
- [Fireeye Hunting COM June 2019](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)
- [Kettle CSV DDE Aug 2014](https://www.contextis.com/blog/comma-separated-vulnerabilities)
- [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)
- [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)
- [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)
- [NVisio Labs DDE Detection Oct 2017](https://blog.nviso.be/2017/10/11/detecting-dde-in-ms-office-documents/)
- [SensePost MacroLess DDE Oct 2017](https://sensepost.com/blog/2017/macro-less-code-exec-in-msword/)
