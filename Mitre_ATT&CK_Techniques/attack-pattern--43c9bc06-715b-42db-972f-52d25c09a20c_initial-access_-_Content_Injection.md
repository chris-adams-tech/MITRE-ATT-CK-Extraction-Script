---
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Process: Process Creation'
- 'File: File Creation'
id: attack-pattern--43c9bc06-715b-42db-972f-52d25c09a20c
mitre_attack_url: https://attack.mitre.org/techniques/T1659
name: Content Injection
platforms:
- Linux
- macOS
- Windows
tactics:
- initial-access
- command-and-control
title: initial-access - Content Injection
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access, command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content, Process: Process Creation, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1659](https://attack.mitre.org/techniques/T1659) |

# Content Injection (attack-pattern--43c9bc06-715b-42db-972f-52d25c09a20c)

## Description
Adversaries may gain access and continuously communicate with victims by injecting malicious content into systems through online network traffic. Rather than luring victims to malicious payloads hosted on a compromised website (i.e., [Drive-by Target](https://attack.mitre.org/techniques/T1608/004) followed by [Drive-by Compromise](https://attack.mitre.org/techniques/T1189)), adversaries may initially access victims through compromised data-transfer channels where they can manipulate traffic and/or inject their own content. These compromised online network channels may also be used to deliver additional payloads (i.e., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) and other data to already compromised systems.(Citation: ESET MoustachedBouncer)

Adversaries may inject content to victim systems in various ways, including:

* From the middle, where the adversary is in-between legitimate online client-server communications (**Note:** this is similar but distinct from [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557), which describes AiTM activity solely within an enterprise environment) (Citation: Kaspersky Encyclopedia MiTM)
* From the side, where malicious content is injected and races to the client as a fake response to requests of a legitimate online server (Citation: Kaspersky ManOnTheSide)

Content injection is often the result of compromised upstream communication channels, for example at the level of an internet service provider (ISP) as is the case with "lawful interception."(Citation: Kaspersky ManOnTheSide)(Citation: ESET MoustachedBouncer)(Citation: EFF China GitHub Attack)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1659)
- [EFF China GitHub Attack](https://www.eff.org/deeplinks/2015/04/china-uses-unencrypted-websites-to-hijack-browsers-in-github-attack)
- [ESET MoustachedBouncer](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Kaspersky Encyclopedia MiTM](https://encyclopedia.kaspersky.com/glossary/man-in-the-middle-attack/)
- [Kaspersky ManOnTheSide](https://usa.kaspersky.com/blog/man-on-the-side/27854/)
