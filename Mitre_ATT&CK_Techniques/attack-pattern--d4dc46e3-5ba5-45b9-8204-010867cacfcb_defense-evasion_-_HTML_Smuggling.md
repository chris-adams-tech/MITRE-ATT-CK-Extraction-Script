---
contributors:
- Stan Hegt, Outflank
- Jonathan Boucher, @crash_wave, Bank of Canada
- Krishnan Subramanian, @krish203
- Vinay Pidathala
data_sources:
- 'File: File Creation'
id: attack-pattern--d4dc46e3-5ba5-45b9-8204-010867cacfcb
mitre_attack_url: https://attack.mitre.org/techniques/T1027/006
name: HTML Smuggling
platforms:
- Windows
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - HTML Smuggling
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/006](https://attack.mitre.org/techniques/T1027/006) |

# HTML Smuggling (attack-pattern--d4dc46e3-5ba5-45b9-8204-010867cacfcb)

## Description
Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign HTML files. HTML documents can store large binary objects known as JavaScript Blobs (immutable data that represents raw bytes) that can later be constructed into file-like objects. Data may also be stored in Data URLs, which enable embedding media type or MIME files inline of HTML documents. HTML5 also introduced a download attribute that may be used to initiate file downloads.(Citation: HTML Smuggling Menlo Security 2020)(Citation: Outlflank HTML Smuggling 2018)

Adversaries may deliver payloads to victims that bypass security controls through HTML Smuggling by abusing JavaScript Blobs and/or HTML5 download attributes. Security controls such as web content filters may not identify smuggled malicious files inside of HTML/JS files, as the content may be based on typically benign MIME types such as <code>text/plain</code> and/or <code>text/html</code>. Malicious files or data can be obfuscated and hidden inside of HTML files through Data URLs and/or JavaScript Blobs and can be deobfuscated when they reach the victim (i.e. [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140)), potentially bypassing content filters.

For example, JavaScript Blobs can be abused to dynamically generate malicious files in the victim machine and may be dropped to disk by abusing JavaScript functions such as <code>msSaveBlob</code>.(Citation: HTML Smuggling Menlo Security 2020)(Citation: MSTIC NOBELIUM May 2021)(Citation: Outlflank HTML Smuggling 2018)(Citation: nccgroup Smuggling HTA 2017)

## Detection
Detection of HTML Smuggling is difficult as HTML5 and JavaScript attributes are used by legitimate services and applications. HTML Smuggling can be performed in many ways via JavaScript, developing rules for the different variants, with a combination of different encoding and/or encryption schemes, may be very challenging.(Citation: Outlflank HTML Smuggling 2018) Detecting specific JavaScript and/or HTML5 attribute strings such as <code>Blob</code>, <code>msSaveOrOpenBlob</code>, and/or <code>download</code> may be a good indicator of HTML Smuggling. These strings may also be used by legitimate services therefore it is possible to raise false positives.

Consider monitoring files downloaded from the Internet, possibly by HTML Smuggling, for suspicious activities. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/006)
- [Outlflank HTML Smuggling 2018](https://outflank.nl/blog/2018/08/14/html-smuggling-explained/)
- [MSTIC NOBELIUM May 2021](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/)
- [HTML Smuggling Menlo Security 2020](https://www.menlosecurity.com/blog/new-attack-alert-duri)
- [nccgroup Smuggling HTA 2017](https://www.nccgroup.com/us/research-blog/smuggling-hta-files-in-internet-exploreredge/)
