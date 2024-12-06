---
contributors:
- Veeral Patel
data_sources:
- 'Sensor Health: Host Status'
- 'File: File Metadata'
id: attack-pattern--3f18edba-28f4-4bb9-82c3-8aa60dcac5f7
mitre_attack_url: https://attack.mitre.org/techniques/T1195
name: Supply Chain Compromise
platforms:
- Linux
- Windows
- macOS
tactics:
- initial-access
title: initial-access - Supply Chain Compromise
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Sensor Health: Host Status, File: File Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1195](https://attack.mitre.org/techniques/T1195) |

# Supply Chain Compromise (attack-pattern--3f18edba-28f4-4bb9-82c3-8aa60dcac5f7)

## Description
Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for the purpose of data or system compromise.

Supply chain compromise can take place at any stage of the supply chain including:

* Manipulation of development tools
* Manipulation of a development environment
* Manipulation of source code repositories (public or private)
* Manipulation of source code in open-source dependencies
* Manipulation of software update/distribution mechanisms
* Compromised/infected system images (multiple cases of removable media infected at the factory)(Citation: IBM Storwize)(Citation: Schneider Electric USB Malware) 
* Replacement of legitimate software with modified versions
* Sales of modified/counterfeit products to legitimate distributors
* Shipment interdiction

While supply chain compromise can impact any component of hardware or software, adversaries looking to gain execution have often focused on malicious additions to legitimate software in software distribution or update channels.(Citation: Avast CCleaner3 2018)(Citation: Microsoft Dofoil 2018)(Citation: Command Five SK 2011) Targeting may be specific to a desired victim set or malicious software may be distributed to a broad set of consumers but only move on to additional tactics on specific victims.(Citation: Symantec Elderwood Sept 2012)(Citation: Avast CCleaner3 2018)(Citation: Command Five SK 2011) Popular open source projects that are used as dependencies in many applications may also be targeted as a means to add malicious code to users of the dependency.(Citation: Trendmicro NPM Compromise)

## Detection
Use verification of distributed binaries through hash checking or other integrity checking mechanisms. Scan downloads for malicious signatures and attempt to test software and updates prior to deployment while taking note of potential suspicious activity. Perform physical inspection of hardware to look for potential tampering.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1195)
- [Avast CCleaner3 2018](https://blog.avast.com/new-investigations-in-ccleaner-incident-point-to-a-possible-third-stage-that-had-keylogger-capacities)
- [Command Five SK 2011](https://www.commandfive.com/papers/C5_APT_SKHack.pdf)
- [IBM Storwize](https://www-01.ibm.com/support/docview.wss?uid=ssg1S1010146&myns=s028&mynp=OCSTHGUJ&mynp=OCSTLM5A&mynp=OCSTLM6B&mynp=OCHW206&mync=E&cm_sp=s028-_-OCSTHGUJ-OCSTLM5A-OCSTLM6B-OCHW206-_-E)
- [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)
- [Schneider Electric USB Malware](https://www.se.com/us/en/download/document/SESN-2018-236-01/)
- [Trendmicro NPM Compromise](https://www.trendmicro.com/vinfo/dk/security/news/cybercrime-and-digital-threats/hacker-infects-node-js-package-to-steal-from-bitcoin-wallets)
- [Microsoft Dofoil 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/07/behavior-monitoring-combined-with-machine-learning-spoils-a-massive-dofoil-coin-mining-campaign/)
