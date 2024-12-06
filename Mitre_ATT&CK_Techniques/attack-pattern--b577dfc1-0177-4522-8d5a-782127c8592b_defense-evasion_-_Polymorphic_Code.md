---
contributors:
- Ye Yint Min Thu Htut, Active Defense Team, DBS Bank
- TruKno
data_sources:
- 'Application Log: Application Log Content'
- 'File: File Creation'
- 'File: File Metadata'
id: attack-pattern--b577dfc1-0177-4522-8d5a-782127c8592b
mitre_attack_url: https://attack.mitre.org/techniques/T1027/014
name: Polymorphic Code
platforms:
- Windows
- macOS
- Linux
tactics:
- defense-evasion
title: defense-evasion - Polymorphic Code
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, macOS, Linux |
| **Data Sources** | Application Log: Application Log Content, File: File Creation, File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1027/014](https://attack.mitre.org/techniques/T1027/014) |

# Polymorphic Code (attack-pattern--b577dfc1-0177-4522-8d5a-782127c8592b)

## Description
Adversaries may utilize polymorphic code (also known as metamorphic or mutating code) to evade detection. Polymorphic code is a type of software capable of changing its runtime footprint during code execution.(Citation: polymorphic-blackberry) With each execution of the software, the code is mutated into a different version of itself that achieves the same purpose or objective as the original. This functionality enables the malware to evade traditional signature-based defenses, such as antivirus and antimalware tools.(Citation: polymorphic-sentinelone) 
Other obfuscation techniques can be used in conjunction with polymorphic code to accomplish the intended effects, including using mutation engines to conduct actions such as [Software Packing](https://attack.mitre.org/techniques/T1027/002), [Command Obfuscation](https://attack.mitre.org/techniques/T1027/010), or [Encrypted/Encoded File](https://attack.mitre.org/techniques/T1027/013).(Citation: polymorphic-linkedin)(Citation: polymorphic-medium)


## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1027/014)
- [polymorphic-blackberry](https://www.blackberry.com/us/en/solutions/endpoint-security/ransomware-protection/polymorphic-malware)
- [polymorphic-sentinelone](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/what-is-polymorphic-malware)
- [polymorphic-medium](https://medium.com/@shellseekerscyber/explainer-packed-malware-16f09cc75035)
- [polymorphic-linkedin](https://www.linkedin.com/pulse/techniques-concealing-malware-hindering-analysis-packing-akshay-unijc)
