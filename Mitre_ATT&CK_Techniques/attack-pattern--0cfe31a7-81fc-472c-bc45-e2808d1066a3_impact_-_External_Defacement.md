---
data_sources:
  - "Application Log: Application Log Content"
  - "File: File Modification"
  - "File: File Creation"
  - "Network Traffic: Network Traffic Content"
id: attack-pattern--0cfe31a7-81fc-472c-bc45-e2808d1066a3
mitre_attack_url: https://attack.mitre.org/techniques/T1491/002
name: External Defacement
platforms:
  - Windows
  - IaaS
  - Linux
  - macOS
tactics:
  - impact
title: T1491.002 - impact - External Defacement
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Data Sources** | Application Log: Application Log Content, File: File Modification, File: File Creation, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1491/002](https://attack.mitre.org/techniques/T1491/002) |

# External Defacement (attack-pattern--0cfe31a7-81fc-472c-bc45-e2808d1066a3)

## Description
An adversary may deface systems external to an organization in an attempt to deliver messaging, intimidate, or otherwise mislead an organization or users. [External Defacement](https://attack.mitre.org/techniques/T1491/002) may ultimately cause users to distrust the systems and to question/discredit the system’s integrity. Externally-facing websites are a common victim of defacement; often targeted by adversary and hacktivist groups in order to push a political message or spread propaganda.(Citation: FireEye Cyber Threats to Media Industries)(Citation: Kevin Mandia Statement to US Senate Committee on Intelligence)(Citation: Anonymous Hackers Deface Russian Govt Site) [External Defacement](https://attack.mitre.org/techniques/T1491/002) may be used as a catalyst to trigger events, or as a response to actions taken by an organization or government. Similarly, website defacement may also be used as setup, or a precursor, for future attacks such as [Drive-by Compromise](https://attack.mitre.org/techniques/T1189).(Citation: Trend Micro Deep Dive Into Defacement)

## Detection
Monitor external websites for unplanned content changes. Monitor application logs for abnormal behavior that may indicate attempted or successful exploitation. Use deep packet inspection to look for artifacts of common exploit traffic, such as SQL injection. Web Application Firewalls may detect improper inputs attempting exploitation.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1491/002)
- [FireEye Cyber Threats to Media Industries](https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/ib-entertainment.pdf)
- [Kevin Mandia Statement to US Senate Committee on Intelligence](https://www.intelligence.senate.gov/sites/default/files/documents/os-kmandia-033017.pdf)
- [Anonymous Hackers Deface Russian Govt Site](https://torrentfreak.com/anonymous-hackers-deface-russian-govt-site-to-protest-web-blocking-nsfw-180512/)
- [Trend Micro Deep Dive Into Defacement](https://documents.trendmicro.com/assets/white_papers/wp-a-deep-dive-into-defacement.pdf)
