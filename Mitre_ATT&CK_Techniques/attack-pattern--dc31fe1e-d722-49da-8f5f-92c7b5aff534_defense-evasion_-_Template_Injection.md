---
contributors:
- Michael Raggi @aRtAGGI
- Brian Wiltse @evalstrings
- Patrick Campbell, @pjcampbe11
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Process: Process Creation'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--dc31fe1e-d722-49da-8f5f-92c7b5aff534
mitre_attack_url: https://attack.mitre.org/techniques/T1221
name: Template Injection
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Template Injection
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Network Traffic: Network Connection Creation, Process: Process Creation, Network Traffic: Network Traffic Content |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1221](https://attack.mitre.org/techniques/T1221) |

# Template Injection (attack-pattern--dc31fe1e-d722-49da-8f5f-92c7b5aff534)

## Description
Adversaries may create or modify references in user document templates to conceal malicious code or force authentication attempts. For example, Microsoft’s Office Open XML (OOXML) specification defines an XML-based format for Office documents (.docx, xlsx, .pptx) to replace older binary formats (.doc, .xls, .ppt). OOXML files are packed together ZIP archives compromised of various XML files, referred to as parts, containing properties that collectively define how a document is rendered.(Citation: Microsoft Open XML July 2017)

Properties within parts may reference shared public resources accessed via online URLs. For example, template properties may reference a file, serving as a pre-formatted document blueprint, that is fetched when the document is loaded.

Adversaries may abuse these templates to initially conceal malicious code to be executed via user documents. Template references injected into a document may enable malicious payloads to be fetched and executed when the document is loaded.(Citation: SANS Brian Wiltse Template Injection) These documents can be delivered via other techniques such as [Phishing](https://attack.mitre.org/techniques/T1566) and/or [Taint Shared Content](https://attack.mitre.org/techniques/T1080) and may evade static detections since no typical indicators (VBA macro, script, etc.) are present until after the malicious payload is fetched.(Citation: Redxorblue Remote Template Injection) Examples have been seen in the wild where template injection was used to load malicious code containing an exploit.(Citation: MalwareBytes Template Injection OCT 2017)

Adversaries may also modify the <code>*\template</code> control word within an .rtf file to similarly conceal then download malicious code. This legitimate control word value is intended to be a file destination of a template file resource that is retrieved and loaded when an .rtf file is opened. However, adversaries may alter the bytes of an existing .rtf file to insert a template control word field to include a URL resource of a malicious payload.(Citation: Proofpoint RTF Injection)(Citation: Ciberseguridad Decoding malicious RTF files)

This technique may also enable [Forced Authentication](https://attack.mitre.org/techniques/T1187) by injecting a SMB/HTTPS (or other credential prompting) URL and triggering an authentication attempt.(Citation: Anomali Template Injection MAR 2018)(Citation: Talos Template Injection July 2017)(Citation: ryhanson phishery SEPT 2016)

## Detection
Analyze process behavior to determine if user document applications (such as Office) are performing actions, such as opening network connections, reading files, spawning abnormal child processes (ex: [PowerShell](https://attack.mitre.org/techniques/T1059/001)), or other suspicious actions that could relate to post-compromise behavior.

Monitor .rtf files for strings indicating the <code>&#42;\template</code> control word has been modified to retrieve a URL resource, such as <code>&#42;\template http</code> or <code>&#42;\template \u-</code>.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1221)
- [Microsoft Open XML July 2017](https://docs.microsoft.com/previous-versions/office/developer/office-2007/aa338205(v=office.12))
- [SANS Brian Wiltse Template Injection](https://www.sans.org/reading-room/whitepapers/testing/template-injection-attacks-bypassing-security-controls-living-land-38780)
- [Redxorblue Remote Template Injection](http://blog.redxorblue.com/2018/07/executing-macros-from-docx-with-remote.html)
- [MalwareBytes Template Injection OCT 2017](https://blog.malwarebytes.com/threat-analysis/2017/10/decoy-microsoft-word-document-delivers-malware-through-rat/)
- [Proofpoint RTF Injection](https://www.proofpoint.com/us/blog/threat-insight/injection-new-black-novel-rtf-template-inject-technique-poised-widespread)
- [Ciberseguridad Decoding malicious RTF files](https://ciberseguridad.blog/decodificando-ficheros-rtf-maliciosos/)
- [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)
- [Talos Template Injection July 2017](https://blog.talosintelligence.com/2017/07/template-injection.html)
- [ryhanson phishery SEPT 2016](https://github.com/ryhanson/phishery)
