---
data_sources:
- 'File: File Metadata'
id: attack-pattern--77eae145-55db-4519-8ae5-77b0c7215d69
mitre_attack_url: https://attack.mitre.org/techniques/T1036/002
name: Right-to-Left Override
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
title: defense-evasion - Right-to-Left Override
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1036/002](https://attack.mitre.org/techniques/T1036/002) |

# Right-to-Left Override (attack-pattern--77eae145-55db-4519-8ae5-77b0c7215d69)

## Description
Adversaries may abuse the right-to-left override (RTLO or RLO) character (U+202E) to disguise a string and/or file name to make it appear benign. RTLO is a non-printing Unicode character that causes the text that follows it to be displayed in reverse. For example, a Windows screensaver executable named <code>March 25 \u202Excod.scr</code> will display as <code>March 25 rcs.docx</code>. A JavaScript file named <code>photo_high_re\u202Egnp.js</code> will be displayed as <code>photo_high_resj.png</code>.(Citation: Infosecinstitute RTLO Technique)

Adversaries may abuse the RTLO character as a means of tricking a user into executing what they think is a benign file type. A common use of this technique is with [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001)/[Malicious File](https://attack.mitre.org/techniques/T1204/002) since it can trick both end users and defenders if they are not aware of how their tools display and render the RTLO character. Use of the RTLO character has been seen in many targeted intrusion attempts and criminal activity.(Citation: Trend Micro PLEAD RTLO)(Citation: Kaspersky RTLO Cyber Crime) RTLO can be used in the Windows Registry as well, where regedit.exe displays the reversed characters but the command line tool reg.exe does not by default.

## Detection
Detection methods should include looking for common formats of RTLO characters within filenames such as <code>\u202E</code>, <code>[U+202E]</code>, and <code>%E2%80%AE</code>. Defenders should also check their analysis tools to ensure they do not interpret the RTLO character and instead print the true name of the file containing it.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1036/002)
- [Infosecinstitute RTLO Technique](https://resources.infosecinstitute.com/spoof-using-right-to-left-override-rtlo-technique-2/)
- [Trend Micro PLEAD RTLO](https://blog.trendmicro.com/trendlabs-security-intelligence/plead-targeted-attacks-against-taiwanese-government-agencies-2/)
- [Kaspersky RTLO Cyber Crime](https://securelist.com/zero-day-vulnerability-in-telegram/83800/)
