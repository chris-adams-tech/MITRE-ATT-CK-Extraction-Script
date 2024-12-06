---
contributors:
- Sylvain Gil, Exabeam
- Barry Shteiman, Exabeam
- Ryan Benson, Exabeam
id: attack-pattern--54456690-84de-4538-9101-643e26437e09
mitre_attack_url: https://attack.mitre.org/techniques/T1483
name: Domain Generation Algorithms
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Domain Generation Algorithms
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1483](https://attack.mitre.org/techniques/T1483) |

# Domain Generation Algorithms (attack-pattern--54456690-84de-4538-9101-643e26437e09)

## Description
Adversaries may make use of Domain Generation Algorithms (DGAs) to dynamically identify a destination for command and control traffic rather than relying on a list of static IP addresses or domains. This has the advantage of making it much harder for defenders block, track, or take over the command and control channel, as there potentially could be thousands of domains that malware can check for instructions.(Citation: Cybereason Dissecting DGAs)(Citation: Cisco Umbrella DGA)(Citation: Unit 42 DGA Feb 2019)

DGAs can take the form of apparently random or “gibberish” strings (ex: istgmxdejdnxuyla.ru) when they construct domain names by generating each letter. Alternatively, some DGAs employ whole words as the unit by concatenating words together instead of letters (ex: cityjulydish.net). Many DGAs are time-based, generating a different domain for each time period (hourly, daily, monthly, etc). Others incorporate a seed value as well to make predicting future domains more difficult for defenders.(Citation: Cybereason Dissecting DGAs)(Citation: Cisco Umbrella DGA)(Citation: Talos CCleanup 2017)(Citation: Akamai DGA Mitigation)

Adversaries may use DGAs for the purpose of [Fallback Channels](https://attack.mitre.org/techniques/T1008). When contact is lost with the primary command and control server malware may employ a DGA as a means to reestablishing command and control.(Citation: Talos CCleanup 2017)(Citation: FireEye POSHSPY April 2017)(Citation: ESET Sednit 2017 Activity)

## Detection
Detecting dynamically generated domains can be challenging due to the number of different DGA algorithms, constantly evolving malware families, and the increasing complexity of the algorithms. There is a myriad of approaches for detecting a pseudo-randomly generated domain name, including using frequency analysis, Markov chains, entropy, proportion of dictionary words, ratio of vowels to other characters, and more.(Citation: Data Driven Security DGA) CDN domains may trigger these detections due to the format of their domain names. In addition to detecting a DGA domain based on the name, another more general approach for detecting a suspicious domain is to check for recently registered names or for rarely visited domains.

Machine learning approaches to detecting DGA domains have been developed and have seen success in applications. One approach is to use N-Gram methods to determine a randomness score for strings used in the domain name. If the randomness score is high, and the domains are not whitelisted (CDN, etc), then it may be determined if a domain or related to a legitimate host or DGA.(Citation: Pace University Detecting DGA May 2017) Another approach is to use deep learning to classify domains as DGA-generated.(Citation: Elastic Predicting DGA)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1483)
- [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)
- [Cisco Umbrella DGA](https://umbrella.cisco.com/blog/2016/10/10/domain-generation-algorithms-effective/)
- [Unit 42 DGA Feb 2019](https://unit42.paloaltonetworks.com/threat-brief-understanding-domain-generation-algorithms-dga/)
- [Talos CCleanup 2017](http://blog.talosintelligence.com/2017/09/avast-distributes-malware.html)
- [Akamai DGA Mitigation](https://blogs.akamai.com/2018/01/a-death-match-of-domain-generation-algorithms.html)
- [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
- [ESET Sednit 2017 Activity](https://www.welivesecurity.com/2017/12/21/sednit-update-fancy-bear-spent-year/)
- [Data Driven Security DGA](https://datadrivensecurity.info/blog/posts/2014/Oct/dga-part2/)
- [Pace University Detecting DGA May 2017](http://csis.pace.edu/~ctappert/srd2017/2017PDF/d4.pdf)
- [Elastic Predicting DGA](https://arxiv.org/pdf/1611.00791.pdf)
