---
contributors:
- Sam Seabrook, Duke Energy
data_sources:
- 'Internet Scan: Response Content'
id: attack-pattern--09312b1a-c3c6-4b45-9844-3ccc78e5d82f
mitre_attack_url: https://attack.mitre.org/techniques/T1592
name: Gather Victim Host Information
platforms:
- PRE
tactics:
- reconnaissance
title: reconnaissance - Gather Victim Host Information
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | reconnaissance |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1592](https://attack.mitre.org/techniques/T1592) |

# Gather Victim Host Information (attack-pattern--09312b1a-c3c6-4b45-9844-3ccc78e5d82f)

## Description
Adversaries may gather information about the victim's hosts that can be used during targeting. Information about hosts may include a variety of details, including administrative data (ex: name, assigned IP, functionality, etc.) as well as specifics regarding its configuration (ex: operating system, language, etc.).

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Adversaries may also compromise sites then include malicious content designed to collect host information from visitors.(Citation: ATT ScanBox) Information about hosts may also be exposed to adversaries via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195) or [External Remote Services](https://attack.mitre.org/techniques/T1133)).

Adversaries may also gather victim host information via User-Agent HTTP headers, which are sent to a server to identify the application, operating system, vendor, and/or version of the requesting user agent. This can be used to inform the adversary’s follow-on action. For example, adversaries may check user agents for the requesting operating system, then only serve malware for target operating systems while ignoring others.(Citation: TrellixQakbot)

## Detection
Internet scanners may be used to look for patterns associated with malicious content designed to collect host information from visitors.(Citation: ThreatConnect Infrastructure Dec 2020)(Citation: ATT ScanBox)

Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1592)
- [ATT ScanBox](https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks)
- [TrellixQakbot](https://www.trellix.com/blogs/research/qakbot-evolves-to-onenote-malware-distribution/)
- [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
