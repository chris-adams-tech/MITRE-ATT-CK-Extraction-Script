---
data_sources:
- 'File: File Creation'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--ef67e13e-5598-4adc-bdb2-998225874fa9
mitre_attack_url: https://attack.mitre.org/techniques/T1204/001
name: Malicious Link
platforms:
- Linux
- macOS
- Windows
tactics:
- execution
title: execution - Malicious Link
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | File: File Creation, Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1204/001](https://attack.mitre.org/techniques/T1204/001) |

# Malicious Link (attack-pattern--ef67e13e-5598-4adc-bdb2-998225874fa9)

## Description
An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected to social engineering to get them to click on a link that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002). Clicking on a link may also lead to other execution techniques such as exploitation of a browser or application vulnerability via [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203). Links may also lead users to download files that require execution via [Malicious File](https://attack.mitre.org/techniques/T1204/002).

## Detection
Inspect network traffic for indications that a user visited a malicious site, such as links included in phishing campaigns directed at your organization.

Anti-virus can potentially detect malicious documents and files that are downloaded from a link and executed on the user's computer.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1204/001)
